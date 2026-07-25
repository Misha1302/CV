from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "cv-print-profiles.json").read_text(encoding="utf-8"))
TARGET = list(DATA["profiles"])

STALE = ["1 358", "1,358", "23.07.2026", "July 23, 2026", "секционная премия", "section prize"]
A4_WIDTH = 595.28
A4_HEIGHT = 841.89
A4_TOLERANCE = 3.0
MIN_FONT_SIZE = 8.4


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def pdf_link_targets(page: fitz.Page) -> list[str]:
    return sorted(link.get("uri", "") for link in page.get_links() if link.get("uri"))


def validate_html() -> None:
    for filename in TARGET + ["ru.html", "en.html"]:
        text = (ROOT / filename).read_text(encoding="utf-8")
        for marker in STALE:
            if marker in text:
                raise RuntimeError(f"{filename}: stale marker {marker}")
        expected_education = (
            "Студент программы «Программная инженерия» НИУ ВШЭ"
            if filename.startswith("ru")
            else "Software Engineering student at HSE University"
        )
        if expected_education not in text:
            raise RuntimeError(f"{filename}: missing canonical education")
        if "style.css?v=31" not in text:
            raise RuntimeError(f"{filename}: stale stylesheet version")

    compiler = (ROOT / "ru-compiler.html").read_text(encoding="utf-8")
    for marker in ["Typed language plans", "Callable-first SSA", "PlanFuzz", "1 459 / 1 459"]:
        if marker not in compiler:
            raise RuntimeError(f"ru-compiler.html: missing {marker}")

    devtools = (ROOT / "ru-devtools.html").read_text(encoding="utf-8")
    for marker in ["7 oracle families", "Fresh-process", "exact fingerprints", "program/plan reduction"]:
        if marker.lower() not in devtools.lower():
            raise RuntimeError(f"ru-devtools.html: missing {marker}")

    selector = BeautifulSoup((ROOT / "index.html").read_text(encoding="utf-8"), "html.parser")
    titles = [item.get_text(" ", strip=True) for item in selector.select(".selector-card h2")]
    expected = [
        "Compiler / Language Platforms",
        "Compiler Testing / Developer Tools",
        "C++ Systems / Program Analysis",
    ]
    if titles[:3] != expected:
        raise RuntimeError(f"Selector main order mismatch: {titles[:3]}")


def validate_pdf(path: Path, profile: dict) -> dict:
    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f"Missing PDF {path}")

    doc = fitz.open(path)
    if doc.page_count != 1:
        raise RuntimeError(f"{path.name}: {doc.page_count} pages")

    page = doc[0]
    rect = page.rect
    if abs(rect.width - A4_WIDTH) > A4_TOLERANCE or abs(rect.height - A4_HEIGHT) > A4_TOLERANCE:
        raise RuntimeError(f"{path.name}: expected A4, got {rect.width:.2f} x {rect.height:.2f}")

    text = page.get_text("text")
    normalized_text = normalized(text)
    if len(normalized_text) < 1200:
        raise RuntimeError(f"{path.name}: weak text layer ({len(normalized_text)} chars)")

    for marker in STALE:
        if marker in text:
            raise RuntimeError(f"{path.name}: stale marker {marker}")

    required_markers = [profile["name"], profile["role"], profile["education"]]
    required_markers.extend(proof[0] for proof in profile["proofs"])
    for marker in required_markers:
        if normalized(marker) not in normalized_text:
            raise RuntimeError(f"{path.name}: missing canonical marker {marker!r}")

    sizes = [
        span["size"]
        for block in page.get_text("dict")["blocks"]
        if "lines" in block
        for line in block["lines"]
        for span in line["spans"]
        if span.get("text", "").strip()
    ]
    if not sizes:
        raise RuntimeError(f"{path.name}: no extractable text spans")
    if min(sizes) < MIN_FONT_SIZE:
        raise RuntimeError(f"{path.name}: min font {min(sizes):.2f}")

    links = pdf_link_targets(page)
    if len(links) < 3:
        raise RuntimeError(f"{path.name}: too few links ({len(links)})")

    return {
        "file": path.name,
        "pages": 1,
        "text": len(text),
        "min_font": round(min(sizes), 2),
        "links": len(links),
    }


def validate_pdfs(pdf_dir: Path) -> list[dict]:
    return [validate_pdf(pdf_dir / profile["pdf"], profile) for profile in DATA["profiles"].values()]


def compare_pdf_sets(generated_dir: Path, committed_dir: Path) -> None:
    for profile in DATA["profiles"].values():
        generated_path = generated_dir / profile["pdf"]
        committed_path = committed_dir / profile["pdf"]
        with fitz.open(generated_path) as generated, fitz.open(committed_path) as committed:
            generated_page = generated[0]
            committed_page = committed[0]
            generated_text = normalized(generated_page.get_text("text"))
            committed_text = normalized(committed_page.get_text("text"))
            if generated_text != committed_text:
                raise RuntimeError(f"{profile['pdf']}: committed text differs from clean rebuild")
            if pdf_link_targets(generated_page) != pdf_link_targets(committed_page):
                raise RuntimeError(f"{profile['pdf']}: committed links differ from clean rebuild")


def validate_manifest() -> None:
    manifest = ROOT / "MANIFEST.sha256"
    expected: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        expected[rel.removeprefix("./")] = digest

    actual: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == manifest or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        actual[rel] = hashlib.sha256(path.read_bytes()).hexdigest()

    if expected != actual:
        missing = sorted(set(actual) - set(expected))[:10]
        extra = sorted(set(expected) - set(actual))[:10]
        changed = sorted(key for key in actual.keys() & expected.keys() if actual[key] != expected[key])[:10]
        raise RuntimeError(f"Manifest mismatch missing={missing} extra={extra} changed={changed}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--compare-dir", type=Path)
    parser.add_argument("--skip-manifest", action="store_true")
    args = parser.parse_args()

    validate_html()
    results = validate_pdfs(args.pdf_dir)
    if args.compare_dir:
        validate_pdfs(args.compare_dir)
        compare_pdf_sets(args.pdf_dir, args.compare_dir)
    if not args.skip_manifest:
        validate_manifest()
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
