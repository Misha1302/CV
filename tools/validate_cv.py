from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "cv-print-profiles.json").read_text(encoding="utf-8"))
TARGET = list(DATA["profiles"])

STALE = ["1 358", "1,358", "23.07.2026", "July 23, 2026", "секционная премия", "section prize"]

def validate_html() -> None:
    for filename in TARGET + ["ru.html", "en.html"]:
        text = (ROOT / filename).read_text(encoding="utf-8")
        for marker in STALE:
            if marker in text:
                raise RuntimeError(f"{filename}: stale marker {marker}")
        expected_education = "Студент программы «Программная инженерия» НИУ ВШЭ" if filename.startswith("ru") else "Software Engineering student at HSE University"
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
    titles = [x.get_text(" ", strip=True) for x in selector.select(".selector-card h2")]
    expected = ["Compiler / Language Platforms", "Compiler Testing / Developer Tools", "C++ Systems / Program Analysis"]
    if titles[:3] != expected:
        raise RuntimeError(f"Selector main order mismatch: {titles[:3]}")

def validate_pdfs(pdf_dir: Path) -> list[dict]:
    results = []
    for profile in DATA["profiles"].values():
        path = pdf_dir / profile["pdf"]
        if not path.exists() or path.stat().st_size == 0:
            raise RuntimeError(f"Missing PDF {path}")
        doc = fitz.open(path)
        if doc.page_count != 1:
            raise RuntimeError(f"{path.name}: {doc.page_count} pages")
        page = doc[0]
        text = page.get_text("text")
        if len(text.strip()) < 1200:
            raise RuntimeError(f"{path.name}: weak text layer")
        sizes = [span["size"] for block in page.get_text("dict")["blocks"] if "lines" in block for line in block["lines"] for span in line["spans"] if span.get("text", "").strip()]
        if min(sizes) < 8.4:
            raise RuntimeError(f"{path.name}: min font {min(sizes):.2f}")
        if len(page.get_links()) < 3:
            raise RuntimeError(f"{path.name}: too few links")
        results.append({"file": path.name, "text": len(text), "min_font": round(min(sizes), 2), "links": len(page.get_links())})
    return results

def validate_manifest() -> None:
    manifest = ROOT / "MANIFEST.sha256"
    expected = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        expected[rel.removeprefix("./")] = digest
    actual = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == manifest or ".git" in path.parts or path.relative_to(ROOT).as_posix() == ".github/workflows/cv-v31-release.yml":
            continue
        rel = path.relative_to(ROOT).as_posix()
        actual[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    if expected != actual:
        missing = sorted(set(actual) - set(expected))[:10]
        extra = sorted(set(expected) - set(actual))[:10]
        changed = sorted(k for k in actual.keys() & expected.keys() if actual[k] != expected[k])[:10]
        raise RuntimeError(f"Manifest mismatch missing={missing} extra={extra} changed={changed}")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--skip-manifest", action="store_true")
    args = parser.parse_args()
    validate_html()
    results = validate_pdfs(args.pdf_dir)
    if not args.skip_manifest:
        validate_manifest()
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
