from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

BANNED_PATTERNS = [
    re.compile(pattern, re.IGNORECASE | re.DOTALL)
    for pattern in [
        r"без потери технических деталей",
        r"полная карта проектов",
        r"главные доказательства",
        r"ключевые доказательства",
        r"проверяемая практика",
        r"широкая инженерная база",
        r"сильнее всего проявля",
        r"позиционирован(?:ие|ия)",
        r"целостн(?:ый|ого|ому|ым|ом|ая|ой|ую|ые|ых)\s+(?:результат|процесс|профиль|опыт|взаимодействие)",
        r"не только.{0,100}но и",
        r"broader engineering base",
        r"strongest when",
        r"complete user (?:and engineering )?workflow",
        r"holistic (?:result|profile|workflow|experience)",
        r"positioning is",
        r"not only.{0,100}but also",
    ]
]

PDFS = [
    "Mikhail_Razakov_Compiler_RU.pdf",
    "Mikhail_Razakov_Compiler_EN.pdf",
    "Mikhail_Razakov_Backend_RU.pdf",
    "Mikhail_Razakov_Backend_EN.pdf",
    "Mikhail_Razakov_EdTech_RU.pdf",
    "Mikhail_Razakov_EdTech_EN.pdf",
]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link"}:
            return
        values = dict(attrs)
        href = values.get("href")
        if href:
            self.links.append(href)


def plain_text(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def check_banned(text: str, source: str, errors: list[str]) -> None:
    for pattern in BANNED_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(f"{source}: banned phrase matched {pattern.pattern!r}: {match.group(0)!r}")


def check_html(errors: list[str]) -> None:
    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        errors.append("No top-level HTML files found")
        return

    for path in html_files:
        raw = path.read_text(encoding="utf-8")
        check_banned(plain_text(raw), path.name, errors)
        parser = LinkParser()
        parser.feed(raw)
        for href in parser.links:
            split = urlsplit(href)
            if split.scheme or href.startswith(("#", "mailto:", "tel:")):
                continue
            target_text = unquote(split.path)
            if not target_text:
                continue
            target = (path.parent / target_text).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.name}: local link escapes repository root: {href}")
                continue
            if not target.exists():
                errors.append(f"{path.name}: missing local link target: {href}")


def check_pdfs(errors: list[str]) -> None:
    for name in PDFS:
        path = ROOT / "pdf" / name
        if not path.exists():
            errors.append(f"Missing PDF: pdf/{name}")
            continue
        reader = PdfReader(str(path))
        if len(reader.pages) != 1:
            errors.append(f"pdf/{name}: expected one page, found {len(reader.pages)}")
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        if len(text.strip()) < 300:
            errors.append(f"pdf/{name}: extracted text is unexpectedly short")
        check_banned(text, f"pdf/{name}", errors)


def main() -> int:
    errors: list[str] = []
    check_html(errors)
    check_pdfs(errors)
    if errors:
        print("CV validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("CV validation passed: copy, local links and PDFs are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
