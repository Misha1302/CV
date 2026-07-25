from __future__ import annotations

import hashlib
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
PLANFUZZ_URL = "https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md"
PAGES = (
    "ru-compiler.html",
    "en-compiler.html",
    "ru-devtools.html",
    "en-devtools.html",
)


def add_link(filename: str) -> None:
    path = ROOT / filename
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    card = next(
        (
            article
            for article in soup.select("article.project-card")
            if (heading := article.find("h3")) is not None
            and heading.get_text(" ", strip=True) == "PlanFuzz"
        ),
        None,
    )
    if card is None:
        raise RuntimeError(f"{filename}: PlanFuzz project card not found")

    existing = card.select_one(f'a[href="{PLANFUZZ_URL}"]')
    if existing is None:
        links = card.select_one(".project-links")
        if links is None:
            links = soup.new_tag("div")
            links["class"] = ["project-links"]
            card.append(links)

        anchor = soup.new_tag("a", href=PLANFUZZ_URL)
        anchor["target"] = "_blank"
        anchor["rel"] = "noopener noreferrer"
        anchor.string = "PlanFuzz в Wist2 ↗" if filename.startswith("ru-") else "PlanFuzz in Wist2 ↗"
        links.append(anchor)

    path.write_text(str(soup), encoding="utf-8")


def add_regression_check() -> None:
    path = ROOT / "tools/validate_cv.py"
    source = path.read_text(encoding="utf-8")
    anchor = "    compiler = (ROOT / 'ru-compiler.html').read_text(encoding='utf-8')\n"
    check = '''    planfuzz_url = 'https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md'\n    for filename in ['ru-compiler.html', 'en-compiler.html', 'ru-devtools.html', 'en-devtools.html']:\n        page = BeautifulSoup((ROOT / filename).read_text(encoding='utf-8'), 'html.parser')\n        card = next((article for article in page.select('article.project-card') if article.find('h3') and article.find('h3').get_text(' ', strip=True) == 'PlanFuzz'), None)\n        if card is None:\n            raise RuntimeError(f'{filename}: missing PlanFuzz project card')\n        link = card.select_one(f'a[href="{planfuzz_url}"]')\n        if link is None or not link.get_text(' ', strip=True):\n            raise RuntimeError(f'{filename}: PlanFuzz card has no visible canonical link')\n'''
    if check not in source:
        if anchor not in source:
            raise RuntimeError("validate_cv.py insertion anchor not found")
        source = source.replace(anchor, check + anchor)
        path.write_text(source, encoding="utf-8")


def rebuild_manifest() -> None:
    lines: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.sha256" or ".git" in path.parts:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  ./{path.relative_to(ROOT).as_posix()}")
    (ROOT / "MANIFEST.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    for filename in PAGES:
        add_link(filename)
    add_regression_check()
    (ROOT / "tools/add_planfuzz_links.py").unlink()
    rebuild_manifest()


if __name__ == "__main__":
    main()
