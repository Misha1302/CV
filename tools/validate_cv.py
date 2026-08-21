from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urldefrag, urlparse

import fitz
from bs4 import BeautifulSoup

from build_site import ROOT, build_outputs, load_data, write_or_check

STALE_MARKERS = [
    "до 20 часов в неделю",
    "up to 20 hours/week",
    "с сентября 2026",
    "from September 2026",
    "С сентября 2026",
]
FORBIDDEN_SCRIPT_MARKERS = ["textContent =", "innerHTML =", "createTreeWalker", "availabilityReplacements"]
TECH_WORDS = {
    "asp.net", "core", "rest", "openapi", "postgresql", "sqlite", "docker", "compose", "nginx", "systemd",
    "webhooks", "backend", "runtime", "compiler", "ssa", "cfg", "llvm", "c++", "c17", "rust", "python", "linux",
    "manifest", "manifests", "lock", "lifecycle", "ownership", "fail-closed", "recovery", "backup", "restore",
    "rollback", "audit", "reconciliation", "idempotency", "interpreter", "cil", "parity", "clean-consumer",
    "differential", "metamorphic", "testing", "exact", "oracles", "replay", "reducers", "codegen", "x86-64",
    "linear", "scan", "iced-x86", "sanitizers", "health", "gates", "state", "machines", "payments", "payment",
    "software", "engineer", "program", "analysis", "platform", "platforms", "typed", "contracts", "routes", "passes",
}


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def html_files(data: dict) -> list[Path]:
    files = [ROOT / "index.html"]
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            files.append(ROOT / data["profiles"][key][lang]["filename"])
    for project in data["projects"].values():
        files.append(ROOT / project["case_ru"])
        files.append(ROOT / project["case_en"])
    for source in data["redirects"]:
        files.append(ROOT / source)
    return files


def validate_source_of_truth(data: dict) -> None:
    write_or_check(build_outputs(data), check=True)
    old_data = ROOT / "data" / "cv-print-profiles.json"
    if old_data.exists():
        raise RuntimeError("Legacy data/cv-print-profiles.json still exists")
    old_updater = ROOT / "tools" / "update_profiles_v33.py"
    if old_updater.exists():
        raise RuntimeError("Legacy tools/update_profiles_v33.py still exists")
    legacy_patterns = [
        "QA-report-targeted-cv-v*.md",
        "pdf/Mikhail_Razakov_DevTools_*.pdf",
        "pdf/Mikhail_Razakov_Algorithms_*.pdf",
        "pdf/Mikhail_Razakov_EdTech_*.pdf",
        "pdf/Mikhail_Razakov_Reliability_*.pdf",
    ]
    for pattern in legacy_patterns:
        matches = list(ROOT.glob(pattern))
        if matches:
            raise RuntimeError(f"Legacy generated artifacts remain for {pattern}: {[p.name for p in matches]}")


def validate_script() -> None:
    script = (ROOT / "script.js").read_text(encoding="utf-8")
    for marker in FORBIDDEN_SCRIPT_MARKERS:
        if marker in script:
            raise RuntimeError(f"script.js mutates document content: {marker}")
    if "mobile-menu" not in script:
        raise RuntimeError("script.js lost mobile-menu behavior")


def page_role(profile: dict, soup: BeautifulSoup) -> None:
    title = soup.title.get_text(strip=True) if soup.title else ""
    description = soup.select_one('meta[name="description"]')
    og_title = soup.select_one('meta[property="og:title"]')
    twitter_title = soup.select_one('meta[name="twitter:title"]')
    canonical = soup.select_one('link[rel="canonical"]')
    jsonld = soup.select_one('script[type="application/ld+json"]')
    h1 = soup.select_one("main h1")
    role = soup.select_one(".hero-role")
    print_role = soup.select_one(".print-cv .pcv-header h2")
    required = [title, profile["description"], profile["role"]]
    if any(not item for item in required):
        raise RuntimeError(f"Incomplete profile metadata for {profile['filename']}")
    if not description or description.get("content") != profile["description"]:
        raise RuntimeError(f"{profile['filename']}: description mismatch")
    if not og_title or og_title.get("content") != profile["title"]:
        raise RuntimeError(f"{profile['filename']}: og:title mismatch")
    if not twitter_title or twitter_title.get("content") != profile["title"]:
        raise RuntimeError(f"{profile['filename']}: twitter:title mismatch")
    if title != profile["title"]:
        raise RuntimeError(f"{profile['filename']}: <title> mismatch")
    if not canonical or not canonical.get("href", "").endswith(profile["filename"]):
        raise RuntimeError(f"{profile['filename']}: canonical mismatch")
    if not h1 or not normalized(h1.get_text(" ")):
        raise RuntimeError(f"{profile['filename']}: missing H1")
    if not role or normalized(role.get_text(" ")) != profile["role"]:
        raise RuntimeError(f"{profile['filename']}: visible role mismatch")
    if not print_role or normalized(print_role.get_text(" ")) != profile["role"]:
        raise RuntimeError(f"{profile['filename']}: print role mismatch")
    if jsonld is None or jsonld.string is None:
        raise RuntimeError(f"{profile['filename']}: missing JSON-LD")
    schema = json.loads(jsonld.string)
    if schema.get("jobTitle") != profile["role"]:
        raise RuntimeError(f"{profile['filename']}: JSON-LD role mismatch")


def validate_languages(path: Path, soup: BeautifulSoup) -> None:
    lang = soup.html.get("lang") if soup.html else None
    text = normalized(soup.get_text(" "))
    if lang == "en" and re.search(r"[А-Яа-яЁё]", text):
        raise RuntimeError(f"{path.relative_to(ROOT)}: Cyrillic text on English page")
    if lang == "ru":
        # Detect an untranslated English sentence rather than accepted technical terms.
        for sentence in re.split(r"[.!?]\s+", text):
            tokens = re.findall(r"[A-Za-z][A-Za-z0-9+./-]*", sentence)
            if len(tokens) < 7:
                continue
            unknown = [token for token in tokens if token.casefold() not in TECH_WORDS and not token.isupper()]
            if len(unknown) >= 5 and not re.search(r"[А-Яа-яЁё]", sentence):
                raise RuntimeError(f"{path.relative_to(ROOT)}: probable untranslated sentence: {sentence[:140]}")


def validate_html(data: dict) -> set[str]:
    external: set[str] = set()
    existing = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_file()}
    for path in html_files(data):
        if not path.exists():
            raise RuntimeError(f"Missing generated page: {path.relative_to(ROOT)}")
        raw = path.read_text(encoding="utf-8")
        for marker in STALE_MARKERS:
            if marker.casefold() in raw.casefold():
                raise RuntimeError(f"{path.relative_to(ROOT)}: stale marker {marker!r}")
        if "avatars.githubusercontent.com" in raw:
            raise RuntimeError(f"{path.relative_to(ROOT)}: remote avatar dependency remains")
        soup = BeautifulSoup(raw, "html.parser")
        validate_languages(path, soup)
        for link in soup.select("a[href], link[href], img[src], script[src]"):
            attr = "href" if link.has_attr("href") else "src"
            value = link.get(attr, "")
            if not value or value.startswith(("mailto:", "tel:", "javascript:", "data:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme in {"http", "https"}:
                if not value.startswith(data["site_url"]):
                    external.add(urldefrag(value)[0])
                continue
            if value.startswith("#"):
                target_id = value[1:]
                if target_id and not soup.find(id=target_id):
                    raise RuntimeError(f"{path.relative_to(ROOT)}: missing fragment {value}")
                continue
            relative_path = urlparse(value).path
            relative = (path.parent / relative_path).resolve()
            try:
                rel = relative.relative_to(ROOT).as_posix()
            except ValueError as exc:
                raise RuntimeError(f"{path.relative_to(ROOT)}: link escapes repository: {value}") from exc
            if rel not in existing:
                raise RuntimeError(f"{path.relative_to(ROOT)}: broken internal link {value}")
        img = soup.select_one(".identity-card img.identity-mark")
        profile_match = next(
            (data["profiles"][key][lang] for key in data["profile_order"] for lang in ("ru", "en")
             if data["profiles"][key][lang]["filename"] == path.name),
            None,
        )
        if profile_match:
            show_portrait = profile_match.get("show_portrait", True)
            portrait_asset = profile_match.get("portrait_asset", "assets/portrait.svg")
            if show_portrait and (not img or img.get("src") != portrait_asset or not img.get("alt")):
                raise RuntimeError(f"{path.relative_to(ROOT)}: local accessible portrait missing")
            if not show_portrait and img:
                raise RuntimeError(f"{path.relative_to(ROOT)}: portrait present despite show_portrait=false")
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            profile = data["profiles"][key][lang]
            soup = BeautifulSoup((ROOT / profile["filename"]).read_text(encoding="utf-8"), "html.parser")
            page_role(profile, soup)
    return external


def check_external_url(url: str) -> tuple[str, int]:
    headers = {"User-Agent": "Mozilla/5.0 CV-link-validator/1.0"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                return url, int(response.status)
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403, 405, 429, 999}:
                return url, exc.code
            if method == "GET":
                raise RuntimeError(f"External link failed: {url} -> HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            if method == "GET":
                raise RuntimeError(f"External link failed: {url} -> {exc}") from exc
    raise RuntimeError(f"External link failed: {url}")


def validate_pdfs(data: dict, pdf_dir: Path) -> list[dict[str, object]]:
    results = []
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            profile = data["profiles"][key][lang]
            path = pdf_dir / profile["pdf"]
            if not path.exists() or not path.stat().st_size:
                raise RuntimeError(f"Missing PDF {path}")
            doc = fitz.open(path)
            if doc.page_count != 1:
                raise RuntimeError(f"{path.name}: expected one page")
            page = doc[0]
            text = normalized(page.get_text("text"))
            if profile["role"].casefold() not in text.casefold():
                raise RuntimeError(f"{path.name}: role mismatch")
            for marker in STALE_MARKERS:
                if marker.casefold() in text.casefold():
                    raise RuntimeError(f"{path.name}: stale marker {marker}")
            links = [link.get("uri") for link in page.get_links() if link.get("uri")]
            if len(links) < 3:
                raise RuntimeError(f"{path.name}: too few links")
            results.append({"file": path.name, "text_chars": len(text), "links": len(links)})
    return results



def compare_pdf_sets(generated_dir: Path, committed_dir: Path, data: dict) -> None:
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            profile = data["profiles"][key][lang]
            generated_path = generated_dir / profile["pdf"]
            committed_path = committed_dir / profile["pdf"]
            if not committed_path.exists():
                raise RuntimeError(f"Missing committed PDF {committed_path}")
            with fitz.open(generated_path) as generated, fitz.open(committed_path) as committed:
                generated_text = normalized(generated[0].get_text("text"))
                committed_text = normalized(committed[0].get_text("text"))
                if generated_text != committed_text:
                    raise RuntimeError(f"{profile['pdf']}: committed PDF text differs from clean rebuild")
                generated_links = sorted(link.get("uri", "") for link in generated[0].get_links() if link.get("uri"))
                committed_links = sorted(link.get("uri", "") for link in committed[0].get_links() if link.get("uri"))
                if generated_links != committed_links:
                    raise RuntimeError(f"{profile['pdf']}: committed PDF links differ from clean rebuild")


def validate_manifest() -> None:
    manifest = ROOT / "MANIFEST.sha256"
    if not manifest.exists():
        raise RuntimeError("MANIFEST.sha256 missing")
    expected: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            expected[rel.removeprefix("./")] = digest
    actual: dict[str, str] = {}
    import hashlib
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == manifest or ".git" in path.parts or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        actual[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if expected != actual:
        missing = sorted(set(actual) - set(expected))[:8]
        extra = sorted(set(expected) - set(actual))[:8]
        changed = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])[:8]
        raise RuntimeError(f"Manifest mismatch missing={missing} extra={extra} changed={changed}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--check-external", action="store_true")
    parser.add_argument("--compare-dir", type=Path)
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    data = load_data()
    validate_source_of_truth(data)
    validate_script()
    external = validate_html(data)
    link_results = []
    if args.check_external:
        for url in sorted(external):
            link_results.append(check_external_url(url))
    pdf_results = validate_pdfs(data, args.pdf_dir)
    if args.compare_dir:
        validate_pdfs(data, args.compare_dir)
        compare_pdf_sets(args.pdf_dir, args.compare_dir, data)
    if not args.skip_manifest:
        validate_manifest()
    report = {
        "profiles": len(data["profile_order"]) * 2,
        "pages": len(html_files(data)),
        "external_links": [{"url": url, "status": status} for url, status in link_results],
        "pdfs": pdf_results,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"VALIDATION_ERROR: {exc}", file=sys.stderr)
        raise
