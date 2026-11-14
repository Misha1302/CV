"""Semantic and rendered checks for specialized one-column ATS exports."""
from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

import fitz
from docx import Document
from build_cpp_systems_cv import markdown, snapshot


def require(value: object, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def validate(data: dict, output_dir: Path, profile_key: str = "systems") -> list[dict]:
    summaries = []
    for lang, labels in (
        ("ru", ("ПРОФИЛЬ", "ТЕХНОЛОГИИ", "ОПЫТ", "ИНЖЕНЕРНЫЕ ПРОЕКТЫ", "ОБРАЗОВАНИЕ", "ДОСТИЖЕНИЯ")),
        ("en", ("PROFILE", "TECHNICAL SKILLS", "EXPERIENCE", "ENGINEERING PROJECTS", "EDUCATION", "RECOGNITION")),
    ):
        info = snapshot(data, lang, profile_key)
        profile = info["profile"]
        stem = Path(profile["pdf"]).stem
        pdf_path, docx_path, md_path = (output_dir / (stem + ext) for ext in (".pdf", ".docx", ".md"))
        require(all(p.is_file() for p in (pdf_path, docx_path, md_path)),
                f"Missing C++ Systems document forms: {stem}")
        require(md_path.read_text(encoding="utf-8") == markdown(data, lang, profile_key),
                f"Stale C++ Systems Markdown: {stem}")
        text_md = md_path.read_text(encoding="utf-8")
        counts = {
            "systems": ("104/104", "29/29", "14/14"),
            "program_analysis": ("104/104", "29/29", "18/18"),
            "general": ("104/104", "29/29"),
            "compiler_backend": ("104/104", "29/29", "42/42"),
            "quantdev": ("104/104", "29/29", "14/14", "31", "20", "8"),
            "quant": ("104/104", "14/14", "31", "20"),
        }[profile_key]
        require("907/912" not in text_md and all(count in text_md for count in counts),
                f"Broken bounded statistics or overly detailed smoke outcome in the CV: {stem}")
        if profile_key == "quant":
            require(text_md.index("Simple Parallel Channel Tracker") <
                    text_md.index("UniversalToolchain / Wist2") <
                    text_md.index("PS-form Memory Dependence Analyzer"),
                    f"Quant Research project order incorrect: {stem}")
            require("XAGUSD" in text_md and "31" in text_md and "10" in text_md
                    and "20" in text_md and "8" in text_md,
                    f"Quant Research needs bounded market-data artifacts: {stem}")
            require(("gold set" in text_md.lower()) and
                    (("прибыльност" in text_md.lower()) if lang == "ru"
                     else "profitability" in text_md.lower()),
                    f"Quant Research needs explicit missing gold labels and profitability: {stem}")
            require("four" in text_md.lower() if lang == "en" else "четырёх" in text_md.lower(),
                    f"Quant Research study must identify comparison of four policies: {stem}")
            require("not a financial" in text_md.lower() if lang == "en" else
                    "не эксперимент на финансовых" in text_md.lower(),
                    f"Compiler-controlled research must not be presented as financial experiment: {stem}")
            private = [p for p in info["projects"] if p.get("privacy_status") == "private_unpublished"]
            require(len(private) == 1 and private[0]["id"] == "parallel_channel_tracker"
                    and not private[0].get("source_url"),
                    f"Private Quant Research project must not publish its source: {stem}")
        if profile_key == "quantdev":
            require(text_md.index("PS-form Memory Dependence Analyzer")
                    < text_md.index("Simple Parallel Channel Tracker")
                    < text_md.index("LLVM Interprocedural Global IV Optimization"),
                    f"Quant Developer project order incorrect: {stem}")
            require("XAGUSD" in text_md and "31" in text_md and "10" in text_md
                    and "20" in text_md and "8" in text_md,
                    f"Missing scoped financial research data evidence: {stem}")
            require(("gold set" in text_md.lower() or "gold-разметка" in text_md.lower())
                    and ("не подтвержд" in text_md.lower() if lang == "ru" else
                         "not been established" in text_md.lower()),
                    f"Quant Developer must not imply expert truth or trading accuracy: {stem}")
            private = [p for p in info["projects"] if p.get("privacy_status") == "private_unpublished"]
            require(len(private) == 1 and private[0]["id"] == "parallel_channel_tracker"
                    and not private[0].get("source_url"),
                    f"Private financial case must not publish a source link: {stem}")
        if profile_key == "compiler_backend":
            require(text_md.index("x86-64 Compiler Backend & Register Allocation")
                    < text_md.index("LLVM Interprocedural Global IV Optimization")
                    < text_md.index("UniversalToolchain / Wist2"),
                    f"Compiler Backend project priority incorrect: {stem}")
            require("dd0693c" in text_md and "42/42" in text_md,
                    f"Missing pinned Rust backend regression count: {stem}")
            require(("не заверш" in text_md.lower() if lang == "ru" else "blocked by disk quota" in text_md.lower()),
                    f"Release-test limitation must be explicit: {stem}")
            require("iced-x86" in text_md and "simulated annealing" in text_md.lower(),
                    f"Rust x86 backend skills/evidence missing: {stem}")
            require("манифест" in text_md.lower() if lang == "ru" else "manifest" in text_md.lower(),
                    f"1324 tests must be attributed to manifest: {stem}")
        if profile_key == "general":
            require(text_md.index("UniversalToolchain / Wist2") < text_md.index("LLVM Interprocedural Global IV Optimization")
                    < text_md.index("x86-64 Compiler Backend & Register Allocation"),
                    f"Compiler Infrastructure priority order incorrect: {stem}")
            require("PlanFuzz" in text_md and "1324" in text_md.replace(",", "").replace(" ", ""),
                    f"Missing test-manifest/PlanFuzz boundary: {stem}")
            require("manifest" in text_md.lower() or "манифест" in text_md.lower(),
                    f"Unattributed 1324-test claim: {stem}")
        if profile_key == "program_analysis":
            require(text_md.index("DerefAfterNullAnalyzer") < text_md.index("LLVM Interprocedural Global IV Optimization")
                    < text_md.index("PS-form Memory Dependence Analyzer"),
                    f"Wrong Program Analysis priority order: {stem}")
        pdf = fitz.open(pdf_path)
        require(pdf.page_count == 1, f"ATS C++ PDF is not one page: {stem}")
        page = pdf[0]
        require(abs(page.rect.width - 595.28) < 3 and abs(page.rect.height - 841.89) < 3,
                f"ATS C++ PDF is not A4: {stem}")
        text = page.get_text("text")
        # Section titles are exact lines: substrings such as the Russian
        # "преобразование" must not be mistaken for the heading "Образование".
        extracted_lines = [line.strip().upper() for line in text.splitlines()]
        positions = [extracted_lines.index(label) if label in extracted_lines else -1
                     for label in labels]
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
            *(p["source_url"] for p in info["projects"] if p.get("source_url")),
        }
        require(expected_urls <= urls, f"Broken/missing PDF hyperlinks: {stem}")
        if profile_key == "quant":
            require(len(urls) == 6 and not any("file://" in url or
                    "Parallel Channel Tracker" in url for url in urls),
                    f"Private Quant Research source was exposed: {stem}")
        if profile_key == "quantdev":
            require(len(urls) == 6 and not any("file://" in url or
                    "Parallel Channel Tracker" in url for url in urls),
                    f"Private quant source was exposed as PDF hyperlink: {stem}")
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
        require("SharpChecker" in text and all(count in text for count in counts),
                f"Key bounded achievements missing: {stem}")
        if profile_key == "quant":
            require("XAGUSD" in text and "31" in text and "104/104" in text
                    and ("8" in text if lang == "ru" else "eight" in text.lower()),
                    f"Quant Research data and bounded selection evidence missing: {stem}")
            require("LangDev" in text and "PS-form" in text,
                    f"Quant Research project/recognition missing: {stem}")
        if profile_key == "quantdev":
            require("XAGUSD" in text and "31" in text and "29/29" in text
                    and "104/104" in text and "14/14" in text,
                    f"Quant Developer test evidence missing: {stem}")
        if profile_key == "compiler_backend":
            require("42/42" in text and "29/29" in text and "Rust" in text,
                    f"Compiler Backend measured evidence missing: {stem}")
            require("dd0693c" in text and "iced-x86" in text,
                    f"Compiler Backend pinned Rust source absent: {stem}")
        if profile_key == "general":
            require("LanguagePlan" in text and "PlanFuzz" in text and "LLVM",
                    f"Compiler Infrastructure architectural evidence missing: {stem}")
            require("1324" in "".join(c for c in text if c.isdigit()) or "1324" in text.replace(",", "").replace(" ", ""),
                    f"Missing bounded 1324-manifest claim: {stem}")
        if profile_key == "program_analysis":
            require("Roslyn" in text and "fixed-point" in text.lower()
                    and "18/18" in text and "29/29" in text,
                    f"Program Analysis evidence missing: {stem}")
        # No unverified C++ years-of-industry claim, false performance claims or
        # claiming the entire Rust backend was authored in C++.
        unsupported = ("99.9%", "100% safe", "высоконагруженном продакшене",
                       "guaranteed speedup", "4 years commercial C++")
        require(not any(x.casefold() in text.casefold() for x in unsupported),
                f"Unsupported systems claim: {stem}")
        summaries.append({
            "stem": stem,
            "specialization": profile_key,
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
