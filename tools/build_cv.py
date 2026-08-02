from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz
from weasyprint import HTML

from build_site import ROOT, build_outputs, load_data, write_or_check


def validate_pdf(path: Path, expected_role: str) -> dict[str, object]:
    doc = fitz.open(path)
    if doc.page_count != 1:
        raise RuntimeError(f"{path.name}: expected one page, got {doc.page_count}")
    page = doc[0]
    rect = page.rect
    if abs(rect.width - 595.28) > 3 or abs(rect.height - 841.89) > 3:
        raise RuntimeError(f"{path.name}: expected A4, got {rect.width:.2f} x {rect.height:.2f}")
    text = page.get_text("text")
    if expected_role.casefold() not in text.casefold():
        raise RuntimeError(f"{path.name}: role missing from text layer")
    if len(text.strip()) < 1100:
        raise RuntimeError(f"{path.name}: weak text layer ({len(text)})")
    sizes = [
        span["size"]
        for block in page.get_text("dict")["blocks"] if "lines" in block
        for line in block["lines"]
        for span in line["spans"]
        if span.get("text", "").strip()
    ]
    if not sizes or min(sizes) < 6.8:
        raise RuntimeError(f"{path.name}: font too small ({min(sizes) if sizes else 'none'})")
    links = [link.get("uri") for link in page.get_links() if link.get("uri")]
    if len(links) < 3:
        raise RuntimeError(f"{path.name}: too few links ({len(links)})")
    return {
        "file": path.name,
        "pages": 1,
        "text_chars": len(text),
        "min_font": round(min(sizes), 2),
        "links": len(links),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--evidence-dir", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    data = load_data()
    write_or_check(build_outputs(data), check=False)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.evidence_dir:
        args.evidence_dir.mkdir(parents=True, exist_ok=True)

    report = []
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            profile = data["profiles"][key][lang]
            html_path = ROOT / profile["filename"]
            pdf_path = args.output_dir / profile["pdf"]
            HTML(filename=str(html_path), base_url=str(ROOT)).write_pdf(str(pdf_path))
            result = validate_pdf(pdf_path, profile["role"])
            if args.evidence_dir:
                doc = fitz.open(pdf_path)
                pix = doc[0].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
                pix.save(args.evidence_dir / f"{pdf_path.stem}.png")
            report.append(result | {"html": html_path.name})

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
