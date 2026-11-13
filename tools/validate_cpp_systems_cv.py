"""Semantic and rendered-form checks for the isolated C++ / Systems CV."""
from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

import fitz
from docx import Document
from build_cpp_systems_cv import markdown, snapshot


def require(value: object, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def validate(data: dict, output_dir: Path) -> list[dict]:
    summaries = []
    for lang, labels in (
        ("ru", ("ПРОФИЛЬ", "ТЕХНОЛОГИИ", "ОПЫТ", "ИНЖЕНЕРНЫЕ ПРОЕКТЫ", "ОБРАЗОВАНИЕ", "ДОСТИЖЕНИЯ")),
        ("en", ("PROFILE", "TECHNICAL SKILLS", "EXPERIENCE", "ENGINEERING PROJECTS", "EDUCATION", "RECOGNITION")),
    ):
        info = snapshot(data, lang)
        profile = info["profile"]
        stem = Path(profile["pdf"]).stem
        pdf_path, docx_path, md_path = (output_dir / (stem + ext) for ext in (".pdf", ".docx", ".md"))
        require(all(p.is_file() for p in (pdf_path, docx_path, md_path)),
                f"Missing C++ Systems document forms: {stem}")
        require(md_path.read_text(encoding="utf-8") == markdown(data, lang),
                f"Stale C++ Systems Markdown: {stem}")
        text_md = md_path.read_text(encoding="utf-8")
        require("907/912" not in text_md and "104/104" in text_md and "29/29" in text_md and "14/14" in text_md,
                f"Broken bounded statistics or overly detailed smoke outcome in the CV: {stem}")
        pdf = fitz.open(pdf_path)
        require(pdf.page_count == 1, f"ATS C++ PDF is not one page: {stem}")
        page = pdf[0]
        require(abs(page.rect.width - 595.28) < 3 and abs(page.rect.height - 841.89) < 3,
                f"ATS C++ PDF is not A4: {stem}")
        text = page.get_text("text")
        folded = text.upper()
        positions = [folded.find(label) for label in labels]
        require(all(pos >= 0 for pos in positions) and positions == sorted(positions),
                f"Out-of-order ATS PDF sections: {stem}; {dict(zip(labels, positions))}")
        # Ensure paragraphs are not clipped. PDF font sizes use pt; contact can be smaller.
        spans = [
            s for b in page.get_text("dict")["blocks"] if "lines" in b
            for line in b["lines"] for s in line["spans"] if s["text"].strip()
        ]
        require(spans and min(s["size"] for s in spans) >= 8.5,
                f"Unreadable font in C++ PDF: {stem}")
        require(any(9.5 <= s["size"] <= 9.8 for s in spans),
                f"Missing minimum 9.5 pt body size: {stem}")
        require(max(s["bbox"][3] for s in spans) < page.rect.height - 25,
                f"Possible clipped PDF after bottom margin: {stem}")
        urls = {link.get("uri") for link in page.get_links() if link.get("uri")}
        expected_urls = {
            info["person"]["telegram"], info["person"]["github"], "mailto:" + info["person"]["email"],
            "https://youtu.be/2jqmw-1c7kE",
            *(p["source_url"] for p in info["projects"]),
        }
        require(expected_urls <= urls, f"Broken/missing PDF hyperlinks: {stem}")
        require(all(p["name"] in text for p in info["projects"]),
                f"Project omitted from PDF text layer: {stem}")
        with ZipFile(docx_path) as z:
            require(z.testzip() is None, f"Damaged DOCX: {stem}")
            rel = z.read("word/_rels/document.xml.rels").decode("utf-8")
            xml = z.read("word/document.xml").decode("utf-8")
            require(all(url in rel.replace("&amp;", "&") for url in expected_urls),
                    f"Missing DOCX hyperlinks: {stem}")
            require(all(p["name"] in xml.replace("&amp;", "&") for p in info["projects"]),
                    f"Project omitted from DOCX: {stem}")
        doc = Document(docx_path)
        require(len(doc.sections) == 1 and len(doc.paragraphs) >= 18,
                f"Invalid C++ DOCX document structure: {stem}")
        require("SharpChecker" in text and "104/104" in text and "14/14" in text
                and "29/29" in text, f"Key bounded achievements missing: {stem}")
        # No unverified C++ years-of-industry claim, false performance claims or
        # claiming the entire Rust backend was authored in C++.
        unsupported = ("99.9%", "100% safe", "высоконагруженном продакшене",
                       "guaranteed speedup", "4 years commercial C++")
        require(not any(x.casefold() in text.casefold() for x in unsupported),
                f"Unsupported systems claim: {stem}")
        summaries.append({
            "stem": stem,
            "lang": lang,
            "pages": pdf.page_count,
            "body_font_pt": 9.65,
            "minimum_font_pt": round(min(s["size"] for s in spans), 2),
            "text_chars": len(text),
            "links": len(urls),
            "ats_reading_order": "PASS",
            "md": "synced",
            "docx": "valid",
        })
        pdf.close()
    return summaries
