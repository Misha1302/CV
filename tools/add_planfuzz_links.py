from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANFUZZ_URL = "https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md"
PAGES = (
    "ru-compiler.html",
    "en-compiler.html",
    "ru-devtools.html",
    "en-devtools.html",
)
PROJECT_CARD = re.compile(
    r'(<article class="project-card">(?:(?!</article>).)*?<h3>PlanFuzz</h3>(?:(?!</article>).)*?)(</article>)',
    re.DOTALL,
)
FEATURED_HEADER = re.compile(
    r'(<article class="project-featured"><div>(?:(?!</div>).)*?<h3>PlanFuzz</h3>(?:(?!</div>).)*?)(</div>)',
    re.DOTALL,
)


def link_markup(filename: str) -> str:
    label = "PlanFuzz в Wist2 ↗" if filename.startswith("ru-") else "PlanFuzz in Wist2 ↗"
    return (
        '<div class="project-links"><a href="'
        + PLANFUZZ_URL
        + '" rel="noopener noreferrer" target="_blank">'
        + label
        + "</a></div>"
    )


def add_link(filename: str) -> None:
    path = ROOT / filename
    source = path.read_text(encoding="utf-8")
    pattern = PROJECT_CARD if "compiler" in filename else FEATURED_HEADER
    match = pattern.search(source)
    if match is None:
        raise RuntimeError(f"{filename}: visible PlanFuzz card not found")
    if PLANFUZZ_URL in match.group(0):
        return

    source = source[: match.start(2)] + link_markup(filename) + source[match.start(2) :]
    path.write_text(source, encoding="utf-8")


def add_regression_check() -> None:
    path = ROOT / "tools/validate_cv.py"
    source = path.read_text(encoding="utf-8")
    anchor = "    compiler = (ROOT / 'ru-compiler.html').read_text(encoding='utf-8')\n"
    check = '''    planfuzz_url = 'https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md'\n    for filename in ['ru-compiler.html', 'en-compiler.html', 'ru-devtools.html', 'en-devtools.html']:\n        page = BeautifulSoup((ROOT / filename).read_text(encoding='utf-8'), 'html.parser')\n        cards = page.select('article.project-card, article.project-featured')\n        card = next((article for article in cards if article.find('h3') and article.find('h3').get_text(' ', strip=True) == 'PlanFuzz'), None)\n        if card is None:\n            raise RuntimeError(f'{filename}: missing visible PlanFuzz card')\n        link = card.select_one(f'a[href="{planfuzz_url}"]')\n        if link is None or not link.get_text(' ', strip=True):\n            raise RuntimeError(f'{filename}: PlanFuzz card has no visible canonical link')\n'''
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
