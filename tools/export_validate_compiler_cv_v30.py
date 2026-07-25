from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse
import json

import fitz
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


MAPPINGS = {
    "ru-compiler.html": "pdf/Mikhail_Razakov_Compiler_RU.pdf",
    "en-compiler.html": "pdf/Mikhail_Razakov_Compiler_EN.pdf",
}
CHANGED = {Path(path).name for path in MAPPINGS.values()}
EVIDENCE = Path("v30-evidence")


def export_pdfs() -> dict[str, dict[str, float | int]]:
    metrics: dict[str, dict[str, float | int]] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        try:
            for html, output in MAPPINGS.items():
                page = browser.new_page(
                    viewport={"width": 1440, "height": 900},
                    device_scale_factor=1,
                    color_scheme="light",
                    reduced_motion="reduce",
                )
                page.set_default_timeout(60000)
                page.emulate_media(media="print", color_scheme="light", reduced_motion="reduce")
                page.goto(Path(html).resolve().as_uri(), wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                page.wait_for_timeout(250)
                layout = page.evaluate(
                    """() => {
                      const cv = document.querySelector('.print-cv');
                      if (!cv) throw new Error('print-cv missing');
                      const rect = cv.getBoundingClientRect();
                      const all = Array.from(cv.querySelectorAll('*'));
                      const sizes = all.map(el => parseFloat(getComputedStyle(el).fontSize)).filter(Number.isFinite);
                      let bottom = rect.top;
                      for (const el of all) bottom = Math.max(bottom, el.getBoundingClientRect().bottom);
                      return {
                        clientHeight: cv.clientHeight,
                        scrollHeight: cv.scrollHeight,
                        clientWidth: cv.clientWidth,
                        scrollWidth: cv.scrollWidth,
                        minCssFontPx: Math.min(...sizes),
                        usedRatio: (bottom - rect.top) / rect.height,
                      };
                    }"""
                )
                if layout["scrollHeight"] > layout["clientHeight"] + 2 or layout["scrollWidth"] > layout["clientWidth"] + 2:
                    raise RuntimeError(f"{html}: print overflow: {layout}")
                if layout["minCssFontPx"] < 11.3:
                    raise RuntimeError(f"{html}: CSS font below 8.45 pt gate: {layout}")
                if not 0.78 <= layout["usedRatio"] <= 0.97:
                    raise RuntimeError(f"{html}: implausible page utilization: {layout}")
                page.pdf(
                    path=output,
                    format="A4",
                    print_background=True,
                    display_header_footer=False,
                    prefer_css_page_size=True,
                    scale=1.0,
                    margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                    tagged=True,
                    outline=True,
                )
                metrics[html] = layout
                page.close()
        finally:
            browser.close()
    Path("v30-layout-metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    return metrics


def validate_html() -> None:
    html_files = sorted(Path(".").glob("*.html"))
    if len(html_files) != 17:
        raise RuntimeError(f"Expected 17 HTML files, found {len(html_files)}")

    ids_by_file: dict[str, set[str]] = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "style.css?v=30" not in text:
            raise RuntimeError(f"{path}: stale CSS cache key")
        if "script.js" in text and "script.js?v=30" not in text:
            raise RuntimeError(f"{path}: stale JS cache key")
        soup = BeautifulSoup(text, "html.parser")
        ids = [node.get("id") for node in soup.find_all(attrs={"id": True})]
        if len(ids) != len(set(ids)):
            raise RuntimeError(f"{path}: duplicate IDs")
        ids_by_file[path.name] = set(ids)
        for anchor in soup.select('a[target="_blank"]'):
            if not {"noopener", "noreferrer"} <= set(anchor.get("rel") or []):
                raise RuntimeError(f"{path}: unsafe target=_blank")

    for path in html_files:
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        for node in soup.select("[href], [src]"):
            raw = node.get("href") or node.get("src")
            if not raw or raw.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
                continue
            parsed = urlparse(raw)
            target = (path.parent / (unquote(parsed.path) or path.name)).resolve()
            if not target.exists():
                raise RuntimeError(f"{path}: missing local target {raw}")
            if parsed.fragment:
                html_name = target.name if target.suffix == ".html" else path.name
                if parsed.fragment not in ids_by_file.get(html_name, set()):
                    raise RuntimeError(f"{path}: missing fragment {raw}")

    ru = Path("ru-compiler.html").read_text(encoding="utf-8")
    en = Path("en-compiler.html").read_text(encoding="utf-8")
    both = ru + "\n" + en
    for stale in (
        "baseline от 14.07.2026",
        "verified baseline dated July 14, 2026",
        "Студент НИУ ВШЭ.",
        "HSE University student.",
        "<strong>Конвейер</strong>Лексер",
    ):
        if stale in both:
            raise RuntimeError(f"Stale compiler wording remains: {stale}")
    for stale in ("<strong>Compiler / IR</strong>", "<strong>Low-level</strong>", ">Преподавание</h2>"):
        if stale in ru:
            raise RuntimeError(f"Stale Russian compiler wording remains: {stale}")
    if ">Teaching</h2>" in en:
        raise RuntimeError("Stale English teaching heading remains")
    for required in (
        "Студент программы «Программная инженерия» НИУ ВШЭ",
        "Software Engineering student at HSE University",
        "LLVM-направление",
        "LLVM track",
        "полный прогон 23.07.2026: 0 сбоев, сборка успешна",
        "full run on July 23, 2026: 0 failures, build succeeded",
        "IR-преобразования, interpreter/CIL parity и контракты",
        "IR transforms, interpreter/CIL parity and contracts",
        "Техническая коммуникация",
        "Technical communication",
        "<strong>Конвейер:</strong> лексер",
    ):
        if required not in both:
            raise RuntimeError(f"Required compiler wording missing: {required}")

    metadata = Path("RELEASE-METADATA.md").read_text(encoding="utf-8")
    if "- Version: v30" not in metadata or "v29, commit `fae03e5adb4152bd1aaa43e56f49d383dc8f9e6d`" not in metadata:
        raise RuntimeError("Release metadata mismatch")


def render_before() -> None:
    (EVIDENCE / "before").mkdir(parents=True, exist_ok=True)
    for before in sorted((EVIDENCE / "before-pdf").glob("*.pdf")):
        with fitz.open(before) as doc:
            if len(doc) != 1:
                raise RuntimeError(f"{before}: pre-change PDF not one page")
            doc[0].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(EVIDENCE / "before" / f"{before.stem}.png")


def validate_pdfs() -> dict[str, dict[str, float | int]]:
    pdfs = sorted(Path("pdf").glob("*.pdf"))
    if len(pdfs) != 14:
        raise RuntimeError(f"Expected 14 PDFs, found {len(pdfs)}")
    (EVIDENCE / "after").mkdir(parents=True, exist_ok=True)
    metrics: dict[str, dict[str, float | int]] = {}

    for path in pdfs:
        doc = fitz.open(path)
        if len(doc) != 1:
            raise RuntimeError(f"{path}: expected one page, found {len(doc)}")
        page = doc[0]
        if abs(page.rect.width - 595.28) > 3 or abs(page.rect.height - 841.89) > 3:
            raise RuntimeError(f"{path}: expected A4, got {page.rect}")
        text = page.get_text("text")
        normalized = " ".join(text.split())
        links = [link.get("uri") for link in page.get_links() if link.get("uri")]
        spans = [
            span
            for block in page.get_text("dict").get("blocks", [])
            for line in block.get("lines", [])
            for span in line.get("spans", [])
            if span.get("text", "").strip()
        ]
        if not spans or not links:
            raise RuntimeError(f"{path}: missing text layer or links")
        min_font = min(float(span["size"]) for span in spans)

        if path.name in CHANGED:
            if min_font < 8.45:
                raise RuntimeError(f"{path}: minimum font below gate: {min_font}")
            if path.name.endswith("_RU.pdf"):
                required = (
                    "Программная инженерия",
                    "LLVM-направление",
                    "Техническая коммуникация",
                    "лучший итоговый балл",
                    "IR-преобразования",
                )
                stale = ("Compiler / IR", "Low-level", "Преподавание")
                ordered = ("Михаил Разаков", "UniversalToolchain", "МЦСТ", "PS-form")
                education = "Программная инженерия"
            else:
                required = (
                    "Software Engineering student",
                    "LLVM track",
                    "Technical communication",
                    "top MEPhI Junior score",
                    "IR transforms",
                )
                stale = ("Teaching",)
                ordered = ("Mikhail Razakov", "UniversalToolchain", "MCST", "PS-form")
                education = "Software Engineering"
            missing = [token for token in required if token not in normalized]
            bad = [token for token in stale if token in normalized]
            if missing or bad:
                raise RuntimeError(f"{path}: wording check failed: missing={missing}, stale={bad}")
            positions = [normalized.find(token) for token in ordered]
            if any(pos < 0 for pos in positions) or positions != sorted(positions):
                raise RuntimeError(f"{path}: ATS main-flow order failed: {dict(zip(ordered, positions))}")
            if education not in normalized:
                raise RuntimeError(f"{path}: education marker missing")
            page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(EVIDENCE / "after" / f"{path.stem}.png")

        metrics[path.name] = {
            "pages": len(doc),
            "min_font_pt": round(min_font, 2),
            "text_chars": len(text.strip()),
            "links": len(links),
        }
        doc.close()

    Path("v30-pdf-metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    return metrics


def write_qa(layout: dict[str, dict[str, float | int]], metrics: dict[str, dict[str, float | int]]) -> None:
    focused = {key: metrics[key] for key in sorted(CHANGED)}
    Path("QA-report-targeted-cv-v30.md").write_text(
        "# QA report - targeted CV v30\n\n"
        "## Scope\n\n"
        "- Compiler RU/EN were reviewed against v29 and rebuilt at scale=1.0.\n"
        "- Education, Wist2 qualifiers, LLVM-track positioning, Russian terminology, typography and technical communication were checked.\n"
        "- All 17 HTML files parse; local links/fragments resolve and IDs are unique.\n"
        "- All 14 PDFs remain one-page A4 documents with text layers and clickable links.\n"
        "- ATS validation checks the main reading flow separately from the side-column education marker.\n"
        "- MANIFEST.sha256 is regenerated after temporary files are removed.\n\n"
        "## Layout result\n\n```json\n"
        + json.dumps(layout, ensure_ascii=False, indent=2)
        + "\n```\n\n## Focused PDF result\n\n```json\n"
        + json.dumps(focused, ensure_ascii=False, indent=2)
        + "\n```\n\n## Automated verdict\n\n**PASS.** Human before/after render review required before merge.\n",
        encoding="utf-8",
    )


def main() -> None:
    layout = export_pdfs()
    validate_html()
    render_before()
    metrics = validate_pdfs()
    write_qa(layout, metrics)
    print(json.dumps({key: metrics[key] for key in sorted(CHANGED)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
