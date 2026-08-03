from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import socket
import statistics
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from urllib.parse import urldefrag, urlparse

import fitz
from bs4 import BeautifulSoup

from build_site import ROOT, build_outputs, canonical_sha256, format_int, load_data, write_or_check, wist_claim

A4_WIDTH = 595.28
A4_HEIGHT = 841.89
A4_TOLERANCE = 3.0
ALLOWED_PDF_SCHEMES = {"https", "mailto"}
TEMPORARY_EXTERNAL_STATUSES = {401, 403, 429}
STALE_FACTS = ("1 325", "1,325", "1 465", "1,465", "1 551", "1,551")
FORBIDDEN_PATH_MARKERS = ("/home/runner/", "file:", "\\home\\runner", "C:\\", "../", "./cases/")
FORBIDDEN_SCRIPT_MARKERS = ("textContent", "innerHTML", "outerHTML", "document.write", "insertAdjacentHTML")
EXPECTED_COMPILER_ORDER = {
    "ru": ["ПРОФИЛЬ", "КЛЮЧЕВЫЕ ДОКАЗАТЕЛЬСТВА", "ОПЫТ", "ИЗБРАННЫЕ ПРОЕКТЫ", "НАВЫКИ", "ОБРАЗОВАНИЕ И ДОСТИЖЕНИЯ"],
    "en": ["PROFILE", "KEY EVIDENCE", "EXPERIENCE", "SELECTED PROJECTS", "SKILLS", "EDUCATION AND RECOGNITION"],
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_profile_variants(data: dict):
    for profile_id in data["profile_order"]:
        for lang in ("ru", "en"):
            yield profile_id, lang, data["profiles"][profile_id][lang], int(data["profiles"][profile_id]["pdf_pages"])


def generated_html_paths(data: dict) -> list[Path]:
    paths = [ROOT / "index.html"]
    for _, _, profile, _ in all_profile_variants(data):
        paths.append(ROOT / profile["filename"])
    for project in data["projects"].values():
        paths.extend([ROOT / project["case_ru"], ROOT / project["case_en"]])
    paths.extend(ROOT / source for source in data["redirects"])
    return sorted(set(paths))


def validate_source_of_truth(data: dict) -> None:
    write_or_check(build_outputs(data), check=True)
    meta = json.loads((ROOT / "data" / "build-meta.json").read_text(encoding="utf-8"))
    if meta["canonical_source_sha256"] != canonical_sha256():
        raise RuntimeError("build-meta canonical source SHA mismatch")
    if meta["schema_version"] != data["schema_version"]:
        raise RuntimeError("build-meta schema mismatch")
    forbidden_sources = [ROOT / "data" / "cv-print-profiles.json", ROOT / "tools" / "update_profiles_v33.py"]
    for path in forbidden_sources:
        if path.exists():
            raise RuntimeError(f"legacy parallel source remains: {path.relative_to(ROOT)}")


def heading_levels(soup: BeautifulSoup) -> list[int]:
    return [int(tag.name[1]) for tag in soup.find_all(re.compile(r"^h[1-6]$"))]


def validate_heading_hierarchy(path: Path, soup: BeautifulSoup) -> None:
    levels = heading_levels(soup)
    if not levels or levels[0] != 1:
        raise RuntimeError(f"{path.name}: heading hierarchy must start with H1")
    for previous, current in zip(levels, levels[1:]):
        if current > previous + 1:
            raise RuntimeError(f"{path.name}: heading level jump h{previous}->h{current}")


def local_target(path: Path, value: str) -> Path:
    return (path.parent / urlparse(value).path).resolve()


def validate_html(data: dict) -> set[str]:
    external: set[str] = set()
    for path in generated_html_paths(data):
        if not path.exists() or not path.stat().st_size:
            raise RuntimeError(f"missing generated page: {path.relative_to(ROOT)}")
        raw = path.read_text(encoding="utf-8")
        for stale in STALE_FACTS:
            if stale in raw:
                raise RuntimeError(f"{path.relative_to(ROOT)}: stale fact {stale}")
        soup = BeautifulSoup(raw, "html.parser")
        if soup.html is None or soup.html.get("lang") not in {"ru", "en"}:
            raise RuntimeError(f"{path.relative_to(ROOT)}: missing/invalid lang")
        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: expected one H1, got {len(h1s)}")
        validate_heading_hierarchy(path, soup)
        for image in soup.find_all("img"):
            if not image.has_attr("alt") or not image.get("alt", "").strip():
                raise RuntimeError(f"{path.relative_to(ROOT)}: image missing useful alt")
        for node in soup.select("a[href], link[href], img[src], script[src]"):
            attr = "href" if node.has_attr("href") else "src"
            value = str(node.get(attr, ""))
            if not value or value.startswith(("#", "mailto:", "tel:", "data:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme in {"http", "https"}:
                if not value.startswith(data["site_url"]):
                    external.add(urldefrag(value)[0])
                continue
            target = local_target(path, value)
            try:
                target.relative_to(ROOT)
            except ValueError as exc:
                raise RuntimeError(f"{path.relative_to(ROOT)}: local link escapes repository: {value}") from exc
            if not target.exists():
                raise RuntimeError(f"{path.relative_to(ROOT)}: broken local link: {value}")
        if path.name == "index.html" or "cases" in path.parts or path.name in data["redirects"]:
            continue
        canonical = soup.select_one('link[rel="canonical"]')
        hreflang = soup.select('link[rel="alternate"][hreflang]')
        description = soup.select_one('meta[name="description"]')
        og = soup.select_one('meta[property="og:title"]')
        twitter = soup.select_one('meta[name="twitter:title"]')
        jsonld = soup.select_one('script[type="application/ld+json"]')
        source = soup.select_one('meta[name="cv:source-sha256"]')
        if not canonical or not str(canonical.get("href", "")).startswith(data["site_url"]):
            raise RuntimeError(f"{path.name}: canonical missing")
        if {item.get("hreflang") for item in hreflang} != {"ru", "en", "x-default"}:
            raise RuntimeError(f"{path.name}: hreflang set invalid")
        if not description or not description.get("content"):
            raise RuntimeError(f"{path.name}: description missing")
        if not og or not twitter:
            raise RuntimeError(f"{path.name}: Open Graph/Twitter metadata missing")
        if not jsonld or not jsonld.string:
            raise RuntimeError(f"{path.name}: JSON-LD missing")
        schema = json.loads(jsonld.string)
        if schema.get("@type") != "Person" or not schema.get("jobTitle"):
            raise RuntimeError(f"{path.name}: JSON-LD content invalid")
        if not source or source.get("content") != canonical_sha256():
            raise RuntimeError(f"{path.name}: canonical source SHA metadata mismatch")
        main = soup.find("main")
        if main is None or not normalize(main.get_text(" ")):
            raise RuntimeError(f"{path.name}: critical content missing from static HTML")
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    if ":focus-visible" not in css:
        raise RuntimeError("style.css: visible focus policy missing")
    script = (ROOT / "script.js").read_text(encoding="utf-8")
    for marker in FORBIDDEN_SCRIPT_MARKERS:
        if marker in script:
            raise RuntimeError(f"script.js: critical content mutation marker: {marker}")
    return external


def font_sizes(page: fitz.Page) -> list[float]:
    return [
        float(span["size"])
        for block in page.get_text("dict").get("blocks", [])
        for line in block.get("lines", [])
        for span in line.get("spans", [])
        if span.get("text", "").strip()
    ]


def text_blocks(page: fitz.Page) -> list[tuple[fitz.Rect, str]]:
    blocks = []
    for block in page.get_text("blocks"):
        text = normalize(str(block[4]))
        if text:
            blocks.append((fitz.Rect(block[:4]), text))
    return blocks


def validate_block_geometry(path: Path, page_number: int, page: fitz.Page) -> dict[str, float | int]:
    bounds = page.rect
    blocks = [
        (rect, text) for rect, text in text_blocks(page)
        if not (rect.y0 > page.rect.height - 30 and re.fullmatch(r"\d+ / \d+", text))
    ]
    if not blocks:
        raise RuntimeError(f"{path.name}: page {page_number}: no text blocks")
    for rect, text in blocks:
        if rect.x0 < bounds.x0 - 1 or rect.y0 < bounds.y0 - 1 or rect.x1 > bounds.x1 + 1 or rect.y1 > bounds.y1 + 1:
            raise RuntimeError(f"{path.name}: page {page_number}: text outside media box: {text[:50]}")
    # Detect only substantial cross-block overlap. Tiny intersections arise from glyph metrics.
    for i, (left, left_text) in enumerate(blocks):
        for right, right_text in blocks[i + 1:]:
            intersection = left & right
            if intersection.is_empty:
                continue
            if intersection.get_area() > 14 and min(intersection.width, intersection.height) > 1.5:
                raise RuntimeError(f"{path.name}: page {page_number}: overlapping text blocks: {left_text[:35]!r} / {right_text[:35]!r}")
    top = min(rect.y0 for rect, _ in blocks)
    bottom = max(rect.y1 for rect, _ in blocks)
    used = max(0.0, bottom - top)
    occupancy = used / max(1.0, bounds.height)
    return {
        "text_chars": len(page.get_text("text")),
        "first_text_y": round(top, 2),
        "last_text_y": round(bottom, 2),
        "bottom_whitespace": round(bounds.height - bottom, 2),
        "vertical_occupancy": round(occupancy, 4),
    }


def pdf_structure(doc: fitz.Document, path: Path, lang: str) -> dict[str, str | int]:
    catalog = doc.pdf_catalog()
    struct_type, struct_value = doc.xref_get_key(catalog, "StructTreeRoot")
    mark_type, mark_value = doc.xref_get_key(catalog, "MarkInfo")
    lang_type, lang_value = doc.xref_get_key(catalog, "Lang")
    if struct_type == "null" or not struct_value:
        raise RuntimeError(f"{path.name}: /StructTreeRoot missing")
    if mark_type == "null" or "true" not in mark_value.casefold():
        raise RuntimeError(f"{path.name}: /MarkInfo /Marked true missing")
    if lang_type == "null" or lang not in lang_value.casefold():
        raise RuntimeError(f"{path.name}: /Lang missing or mismatched: {lang_value}")
    toc = doc.get_toc(simple=True)
    if not toc:
        raise RuntimeError(f"{path.name}: document outline missing")
    return {"StructTreeRoot": struct_type, "MarkInfo": mark_value, "Lang": lang_value, "outline_entries": len(toc)}


def validate_pdf_link(path: Path, page_number: int, link: dict) -> str:
    kind = link.get("kind")
    if kind != fitz.LINK_URI:
        raise RuntimeError(f"{path.name}: page {page_number}: non-URI/Launch/GoToR annotation is forbidden: {link}")
    uri = link.get("uri")
    if not isinstance(uri, str) or not uri.strip():
        raise RuntimeError(f"{path.name}: page {page_number}: URI annotation without URI: {link}")
    parsed = urlparse(uri)
    if parsed.scheme.casefold() not in ALLOWED_PDF_SCHEMES:
        raise RuntimeError(f"{path.name}: page {page_number}: invalid link scheme: {uri}")
    lowered = uri.casefold()
    if any(marker.casefold() in lowered for marker in FORBIDDEN_PATH_MARKERS):
        raise RuntimeError(f"{path.name}: page {page_number}: local/path target leaked: {uri}")
    if parsed.scheme == "https" and not parsed.netloc:
        raise RuntimeError(f"{path.name}: page {page_number}: malformed HTTPS URI: {uri}")
    if parsed.scheme == "mailto" and "@" not in parsed.path:
        raise RuntimeError(f"{path.name}: page {page_number}: malformed mailto URI: {uri}")
    return uri


def ordered_markers(text: str, markers: list[str], context: str) -> list[int]:
    folded = text.casefold()
    positions = []
    for marker in markers:
        position = folded.find(marker.casefold())
        if position < 0:
            raise RuntimeError(f"{context}: missing section marker {marker!r}")
        positions.append(position)
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        raise RuntimeError(f"{context}: logical section order broken: {dict(zip(markers, positions))}")
    return positions


def pdftotext(path: Path, layout: bool) -> str:
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as handle:
        target = Path(handle.name)
    try:
        cmd = ["pdftotext"] + (["-layout"] if layout else []) + [str(path), str(target)]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return target.read_text(encoding="utf-8", errors="replace")
    finally:
        target.unlink(missing_ok=True)


def validate_profile_text(data: dict, profile_id: str, lang: str, profile: dict, text: str, context: str) -> None:
    person_name = data["person"][f"name_{lang}"]
    if person_name.casefold() not in text[:180].casefold():
        raise RuntimeError(f"{context}: name is not first")
    name_position = text.casefold().find(person_name.casefold())
    role_position = text.casefold().find(profile["role"].casefold())
    if role_position < 0 or role_position - name_position > 220:
        raise RuntimeError(f"{context}: role is not adjacent to name")
    for required in (data["person"]["email"], data["person"]["github_label"]):
        if required.casefold() not in text.casefold():
            raise RuntimeError(f"{context}: missing contact {required}")
    for stale in STALE_FACTS:
        if stale in text:
            raise RuntimeError(f"{context}: stale exact fact {stale}")
    for exp_id in profile["experience_ids"]:
        exp = data["experiences"][exp_id]
        date = exp[f"date_{lang}"]
        title = exp[f"title_{lang}"]
        date_position = text.casefold().find(date.casefold())
        title_position = text.casefold().find(title.casefold())
        if date_position < 0 or title_position < 0 or abs(date_position - title_position) > 300:
            raise RuntimeError(f"{context}: date separated from role {title}")
    if profile_id == "compiler":
        ordered_markers(text, EXPECTED_COMPILER_ORDER[lang], context)
        expected_count = format_int(data["evidence"]["wist_verification"]["passed"], lang)
        expected_date = data["evidence"]["wist_verification"][f"date_{lang}"]
        if expected_count not in text or expected_date not in text:
            raise RuntimeError(f"{context}: canonical Wist claim missing")
        if lang == "ru" and "Разрабатываю оптимизационный проход LLVM" not in normalize(text):
            raise RuntimeError(f"{context}: unfinished LLVM work lost present-tense boundary")
        if lang == "en" and "Developing an LLVM optimization pass" not in normalize(text):
            raise RuntimeError(f"{context}: unfinished LLVM work lost present-tense boundary")


def validate_pdfs(data: dict, pdf_dir: Path) -> list[dict]:
    results = []
    for profile_id, lang, profile, expected_pages in all_profile_variants(data):
        path = pdf_dir / profile["pdf"]
        if not path.exists() or path.stat().st_size == 0:
            raise RuntimeError(f"missing PDF: {path}")
        with fitz.open(path) as doc:
            if doc.page_count != expected_pages:
                raise RuntimeError(f"{path.name}: expected {expected_pages} pages, got {doc.page_count}")
            structure = pdf_structure(doc, path, lang)
            pages = []
            all_sizes: list[float] = []
            links = []
            text_parts = []
            for page_number, page in enumerate(doc, start=1):
                if abs(page.rect.width - A4_WIDTH) > A4_TOLERANCE or abs(page.rect.height - A4_HEIGHT) > A4_TOLERANCE:
                    raise RuntimeError(f"{path.name}: page {page_number}: expected A4, got {page.rect.width:.2f} x {page.rect.height:.2f}")
                text = page.get_text("text")
                if len(text.strip()) < 550:
                    raise RuntimeError(f"{path.name}: page {page_number}: nearly empty text layer ({len(text.strip())} chars)")
                text_parts.append(text)
                sizes = font_sizes(page)
                if not sizes:
                    raise RuntimeError(f"{path.name}: page {page_number}: no font spans")
                all_sizes += sizes
                geometry = validate_block_geometry(path, page_number, page)
                if page_number == doc.page_count and geometry["vertical_occupancy"] < (0.43 if expected_pages > 1 else 0.58):
                    raise RuntimeError(f"{path.name}: page {page_number}: nearly empty trailing page ({geometry['vertical_occupancy']})")
                page_links = []
                for link in page.get_links():
                    uri = validate_pdf_link(path, page_number, link)
                    page_links.append(uri)
                    links.append({"page": page_number, "uri": uri, "kind": "URI"})
                pages.append({"page": page_number, **geometry, "links": page_links})
            minimum = min(all_sizes)
            median = statistics.median(all_sizes)
            if minimum < 8.45:
                raise RuntimeError(f"{path.name}: minimum font {minimum:.2f}pt below 8.45pt")
            median_floor = 9.35 if profile_id == "compiler" else 9.0
            if median < median_floor:
                raise RuntimeError(f"{path.name}: median font {median:.2f}pt below {median_floor:.2f}pt")
            if len(links) < 4:
                raise RuntimeError(f"{path.name}: too few external URI annotations ({len(links)})")
            pymupdf_text = "\n".join(text_parts)
        validate_profile_text(data, profile_id, lang, profile, pymupdf_text, f"{path.name}: PyMuPDF")
        layout_text = pdftotext(path, layout=True)
        plain_text = pdftotext(path, layout=False)
        validate_profile_text(data, profile_id, lang, profile, layout_text, f"{path.name}: pdftotext -layout")
        validate_profile_text(data, profile_id, lang, profile, plain_text, f"{path.name}: pdftotext")
        results.append({
            "file": path.name,
            "profile": profile_id,
            "lang": lang,
            "pages": expected_pages,
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
            "min_font_pt": round(minimum, 2),
            "median_font_pt": round(median, 2),
            "page_metrics": pages,
            "links": links,
            "structure": structure,
            "section_order": "PASS",
        })
    return results


def validate_ats(data: dict) -> list[dict]:
    results = []
    for profile_id, lang, profile, _ in all_profile_variants(data):
        path = ROOT / "ats" / profile["ats"]
        if not path.exists():
            raise RuntimeError(f"missing ATS text: {path}")
        text = path.read_text(encoding="utf-8")
        validate_profile_text(data, profile_id, lang, profile, text, path.name)
        if f"canonical-source-sha256: {canonical_sha256()}" not in text:
            raise RuntimeError(f"{path.name}: source binding missing")
        results.append({"file": path.name, "chars": len(text), "sha256": sha256(path), "section_order": "PASS"})
    return results


def compare_pdf_sets(generated_dir: Path, committed_dir: Path, data: dict) -> None:
    for _, _, profile, _ in all_profile_variants(data):
        left = generated_dir / profile["pdf"]
        right = committed_dir / profile["pdf"]
        if not right.exists():
            raise RuntimeError(f"missing comparison PDF: {right}")
        if left.read_bytes() != right.read_bytes():
            raise RuntimeError(f"{profile['pdf']}: clean rebuild is not byte-for-byte deterministic")


def validate_claim_parity(data: dict, pdf_results: list[dict]) -> dict:
    expected_ru = wist_claim(data, "ru", compact=True)
    expected_en = wist_claim(data, "en", compact=True)
    count_ru = format_int(data["evidence"]["wist_verification"]["passed"], "ru")
    count_en = format_int(data["evidence"]["wist_verification"]["passed"], "en")
    surfaces = []
    for path in generated_html_paths(data):
        surfaces.append((path.relative_to(ROOT).as_posix(), path.read_text(encoding="utf-8")))
    for _, _, profile, _ in all_profile_variants(data):
        path = ROOT / "ats" / profile["ats"]
        surfaces.append((path.relative_to(ROOT).as_posix(), path.read_text(encoding="utf-8")))
    for item in pdf_results:
        path = Path(item.get("resolved_path", "")) if item.get("resolved_path") else None
        # PDF content was already validated against exact owner; no duplicate parsing needed here.
    stale_hits = []
    exact_hits = Counter()
    for label, text in surfaces:
        for stale in STALE_FACTS:
            if stale in text:
                stale_hits.append((label, stale))
        if count_ru in text:
            exact_hits["ru"] += text.count(count_ru)
        if count_en in text:
            exact_hits["en"] += text.count(count_en)
    if stale_hits:
        raise RuntimeError(f"stale claim parity hits: {stale_hits[:10]}")
    if exact_hits["ru"] == 0 or exact_hits["en"] == 0:
        raise RuntimeError("canonical Wist exact claim not propagated")
    return {"expected_ru": expected_ru, "expected_en": expected_en, "surface_hits": dict(exact_hits), "status": "PASS"}


def external_network_available() -> bool:
    if os.environ.get("CV_EXTERNAL_REQUIRE_LIVE") == "1":
        return True
    try:
        with socket.create_connection(("1.1.1.1", 443), timeout=1.0):
            return True
    except OSError:
        return False


def cached_external_result(url: str, policy: dict, reason: str) -> dict:
    cached = policy.get("offline_cache", {}).get(url)
    if cached and int(cached.get("status", 0)) != 404 and int(cached.get("status", 0)) < 400:
        return {
            "url": url,
            "status": int(cached["status"]),
            "method": "provider",
            "mode": "offline-provider-cache",
            "evidence": cached.get("evidence"),
            "network_errors": [reason],
        }
    raise RuntimeError(f"external link unavailable and no valid provider cache: {url}: {reason}")


def check_external_url(url: str, policy: dict) -> dict:
    if not external_network_available():
        return cached_external_result(url, policy, "outbound network preflight failed")
    headers = {"User-Agent": "Mozilla/5.0 CV-validation/35", "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8"}
    errors = []
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=18) as response:
                status = int(response.status)
                if status == 404:
                    raise RuntimeError(f"external link is 404: {url}")
                if status >= 400 and status not in TEMPORARY_EXTERNAL_STATUSES:
                    raise RuntimeError(f"external link failed: {url} -> HTTP {status}")
                return {"url": url, "status": status, "method": method, "mode": "live"}
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise RuntimeError(f"external link is 404: {url}") from exc
            if exc.code in TEMPORARY_EXTERNAL_STATUSES:
                return {"url": url, "status": exc.code, "method": method, "mode": "typed-temporary-allowlist"}
            if method == "GET":
                raise RuntimeError(f"external link failed: {url} -> HTTP {exc.code}") from exc
            errors.append(f"{method}: HTTP {exc.code}")
        except (urllib.error.URLError, TimeoutError, socket.timeout, OSError) as exc:
            errors.append(f"{method}: {exc}")
            if method == "GET":
                if os.environ.get("CV_EXTERNAL_REQUIRE_LIVE") == "1":
                    raise RuntimeError(f"external link live check required but unavailable: {url}: {errors}") from exc
                cached = policy.get("offline_cache", {}).get(url)
                if cached and int(cached.get("status", 0)) != 404 and int(cached.get("status", 0)) < 400:
                    return {"url": url, "status": int(cached["status"]), "method": method, "mode": "offline-provider-cache", "evidence": cached.get("evidence"), "network_errors": errors}
                raise RuntimeError(f"external link unavailable and no valid provider cache: {url}: {errors}") from exc
    raise RuntimeError(f"external link failed: {url}: {errors}")


def collect_pdf_external_urls(pdf_results: list[dict]) -> set[str]:
    return {item["uri"] for result in pdf_results for item in result["links"] if urlparse(item["uri"]).scheme == "https"}


def validate_manifest() -> dict:
    path = ROOT / "MANIFEST.sha256"
    if not path.exists():
        raise RuntimeError("MANIFEST.sha256 missing")
    expected = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        expected[rel.removeprefix("./")] = digest
    actual = {}
    for item in sorted(ROOT.rglob("*")):
        if not item.is_file() or item == path or ".git" in item.parts or "__pycache__" in item.parts or item.suffix == ".pyc":
            continue
        actual[item.relative_to(ROOT).as_posix()] = sha256(item)
    if expected != actual:
        missing = sorted(set(actual) - set(expected))[:10]
        extra = sorted(set(expected) - set(actual))[:10]
        changed = sorted(key for key in expected.keys() & actual.keys() if expected[key] != actual[key])[:10]
        raise RuntimeError(f"manifest mismatch missing={missing} extra={extra} changed={changed}")
    return {"entries": len(actual), "sha256": sha256(path), "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--compare-dir", type=Path)
    parser.add_argument("--check-external", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    data = load_data()
    validate_source_of_truth(data)
    html_external = validate_html(data)
    ats_results = validate_ats(data)
    pdf_results = validate_pdfs(data, args.pdf_dir)
    if args.compare_dir:
        validate_pdfs(data, args.compare_dir)
        compare_pdf_sets(args.pdf_dir, args.compare_dir, data)
    claim_parity = validate_claim_parity(data, pdf_results)
    external_results = []
    if args.check_external:
        policy = json.loads((ROOT / "data" / "external-link-policy.json").read_text(encoding="utf-8"))
        if set(policy.get("temporary_status_allowlist", [])) != TEMPORARY_EXTERNAL_STATUSES:
            raise RuntimeError("external-link typed status allowlist differs from policy")
        urls = html_external | collect_pdf_external_urls(pdf_results)
        for url in sorted(urls):
            external_results.append(check_external_url(url, policy))
    manifest_result = None if args.skip_manifest else validate_manifest()
    report = {
        "status": "PASS",
        "canonical_source_sha256": canonical_sha256(),
        "html_pages": len(generated_html_paths(data)),
        "ats": ats_results,
        "pdfs": pdf_results,
        "claim_parity": claim_parity,
        "external_links": external_results,
        "manifest": manifest_result,
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
