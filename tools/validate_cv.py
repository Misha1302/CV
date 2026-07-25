from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data' / 'cv-print-profiles.json').read_text(encoding='utf-8'))
TARGET = list(DATA['profiles'])
FACTS = DATA.get('facts', {})
PROJECT_URLS = DATA.get('project_urls', {})
STALE = ['1 358', '1,358', '1 459', '1,459', '23.07.2026', 'July 23, 2026', 'секционная премия', 'section prize']
A4_WIDTH = 595.28
A4_HEIGHT = 841.89
A4_TOLERANCE = 3.0
MIN_FONT_SIZE = 8.4
FLAGSHIP = {'ru-compiler.html', 'en-compiler.html', 'ru-devtools.html', 'en-devtools.html', 'ru-cpp-systems.html', 'en-cpp-systems.html'}


def normalized(value: str) -> str:
    return re.sub(r'\s+', ' ', value).strip()


def pdf_link_targets(page: fitz.Page) -> list[str]:
    return sorted(link.get('uri', '') for link in page.get_links() if link.get('uri'))


def validate_data() -> None:
    if DATA.get('version') != 32:
        raise RuntimeError(f'Expected data version 32, got {DATA.get("version")}')
    if FACTS.get('wist2_tests_passed') != 1465:
        raise RuntimeError(f'Unexpected Wist2 test fact: {FACTS}')
    if FACTS.get('wist2_packages') != 9 or not FACTS.get('wist2_source_commit'):
        raise RuntimeError(f'Incomplete Wist2 fact source: {FACTS}')
    for filename in FLAGSHIP:
        profile = DATA['profiles'][filename]
        if profile.get('density') not in {'roomy', 'spacious'} or float(profile.get('min_fill', 0)) < 0.78:
            raise RuntimeError(f'{filename}: flagship print-density contract missing')
        if int(profile.get('min_links', 0)) < 6:
            raise RuntimeError(f'{filename}: direct-link contract missing')
        if not profile.get('ats_order'):
            raise RuntimeError(f'{filename}: ATS order contract missing')
    for title in ['PlanFuzz', 'PS-form Analyzer', 'PS-form Harness', 'x86-64 Codegen Lab', 'AdvancedAlgorithms Verification', 'UniversalToolchain/Wist2']:
        if title not in PROJECT_URLS:
            raise RuntimeError(f'Missing project URL: {title}')
    for filename in ['ru-devtools.html', 'en-devtools.html']:
        if 'reduction' not in DATA['profiles'][filename]['proofs'][2][0].lower() and 'сокращение' not in DATA['profiles'][filename]['proofs'][2][0].lower():
            raise RuntimeError(f'{filename}: test-count proof was not replaced by reduction evidence')
    for filename in ['ru-cpp-systems.html', 'en-cpp-systems.html']:
        if '500' not in DATA['profiles'][filename]['proofs'][2][0]:
            raise RuntimeError(f'{filename}: weak toolchain proof remains')


def validate_html() -> None:
    for filename in TARGET + ['ru.html', 'en.html']:
        text = (ROOT / filename).read_text(encoding='utf-8')
        for marker in STALE:
            if marker in text:
                raise RuntimeError(f'{filename}: stale marker {marker}')
        expected_education = 'Студент программы «Программная инженерия» НИУ ВШЭ' if filename.startswith('ru') else 'Software Engineering student at HSE University'
        if expected_education not in text:
            raise RuntimeError(f'{filename}: missing canonical education')
        if 'style.css?v=32' not in text:
            raise RuntimeError(f'{filename}: stale stylesheet version')
    compiler = (ROOT / 'ru-compiler.html').read_text(encoding='utf-8')
    for marker in ['Callable-first SSA', 'экспериментальный PlanFuzz', '1 465 / 1 465']:
        if marker not in compiler:
            raise RuntimeError(f'ru-compiler.html: missing {marker}')
    if 'Typed composition plans' not in compiler and 'Планы типизированной композиции' not in compiler:
        raise RuntimeError('ru-compiler.html: missing typed-composition proof')
    devtools = (ROOT / 'ru-devtools.html').read_text(encoding='utf-8')
    for marker in ['экспериментальный PlanFuzz', 'exact fingerprints', 'program/plan reduction']:
        if marker.lower() not in devtools.lower():
            raise RuntimeError(f'ru-devtools.html: missing {marker}')
    if 'ограниченный Wist Int32 adapter' not in devtools and 'ограниченный адаптер Wist для Int32' not in devtools:
        raise RuntimeError('ru-devtools.html: missing restricted Wist adapter scope')
    selector = BeautifulSoup((ROOT / 'index.html').read_text(encoding='utf-8'), 'html.parser')
    titles = [item.get_text(' ', strip=True) for item in selector.select('.selector-card h2')]
    expected = ['Compiler / Language Platforms', 'Compiler Testing / Developer Tools', 'C++ Systems / Program Analysis']
    if titles[:3] != expected:
        raise RuntimeError(f'Selector main order mismatch: {titles[:3]}')


def validate_pdf(path: Path, profile: dict) -> dict:
    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f'Missing PDF {path}')
    doc = fitz.open(path)
    if doc.page_count != 1:
        raise RuntimeError(f'{path.name}: {doc.page_count} pages')
    page = doc[0]
    rect = page.rect
    if abs(rect.width - A4_WIDTH) > A4_TOLERANCE or abs(rect.height - A4_HEIGHT) > A4_TOLERANCE:
        raise RuntimeError(f'{path.name}: expected A4, got {rect.width:.2f} x {rect.height:.2f}')
    text = page.get_text('text')
    normalized_text = normalized(text)
    folded = normalized_text.casefold()
    if len(normalized_text) < 1200:
        raise RuntimeError(f'{path.name}: weak text layer ({len(normalized_text)} chars)')
    for marker in STALE:
        if marker in text:
            raise RuntimeError(f'{path.name}: stale marker {marker}')
    required = [profile['name'], profile['role'], profile['education']]
    required.extend(proof[0] for proof in profile['proofs'])
    for marker in required:
        if normalized(marker).casefold() not in folded:
            raise RuntimeError(f'{path.name}: missing canonical marker {marker!r}')
    cursor = -1
    for marker in profile.get('ats_order', []):
        position = folded.find(normalized(marker).casefold(), cursor + 1)
        if position < 0:
            raise RuntimeError(f'{path.name}: ATS marker missing or out of order: {marker!r}')
        cursor = position
    sizes = [span['size'] for block in page.get_text('dict')['blocks'] if 'lines' in block for line in block['lines'] for span in line['spans'] if span.get('text', '').strip()]
    if not sizes or min(sizes) < MIN_FONT_SIZE:
        raise RuntimeError(f'{path.name}: min font {min(sizes) if sizes else "none"}')
    links = pdf_link_targets(page)
    min_links = int(profile.get('min_links', 3))
    if len(links) < min_links:
        raise RuntimeError(f'{path.name}: too few links ({len(links)} < {min_links})')
    for title, _ in profile['projects']:
        url = PROJECT_URLS.get(title)
        if url and url not in links:
            raise RuntimeError(f'{path.name}: missing direct project link for {title}')
    return {'file': path.name, 'pages': 1, 'text': len(text), 'min_font': round(min(sizes), 2), 'links': len(links)}


def validate_pdfs(pdf_dir: Path) -> list[dict]:
    return [validate_pdf(pdf_dir / profile['pdf'], profile) for profile in DATA['profiles'].values()]


def compare_pdf_sets(generated_dir: Path, committed_dir: Path) -> None:
    for profile in DATA['profiles'].values():
        with fitz.open(generated_dir / profile['pdf']) as generated, fitz.open(committed_dir / profile['pdf']) as committed:
            generated_page = generated[0]
            committed_page = committed[0]
            if normalized(generated_page.get_text('text')) != normalized(committed_page.get_text('text')):
                raise RuntimeError(f'{profile["pdf"]}: committed text differs from clean rebuild')
            if pdf_link_targets(generated_page) != pdf_link_targets(committed_page):
                raise RuntimeError(f'{profile["pdf"]}: committed links differ from clean rebuild')


def validate_manifest() -> None:
    manifest = ROOT / 'MANIFEST.sha256'
    expected = {}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if line.strip():
            digest, rel = line.split('  ', 1)
            expected[rel.removeprefix('./')] = digest
    actual = {}
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or path == manifest or '.git' in path.parts:
            continue
        actual[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if expected != actual:
        missing = sorted(set(actual) - set(expected))[:10]
        extra = sorted(set(expected) - set(actual))[:10]
        changed = sorted(key for key in actual.keys() & expected.keys() if actual[key] != expected[key])[:10]
        raise RuntimeError(f'Manifest mismatch missing={missing} extra={extra} changed={changed}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf-dir', type=Path, default=ROOT / 'pdf')
    parser.add_argument('--compare-dir', type=Path)
    parser.add_argument('--skip-manifest', action='store_true')
    args = parser.parse_args()
    validate_data()
    validate_html()
    results = validate_pdfs(args.pdf_dir)
    if args.compare_dir:
        validate_pdfs(args.compare_dir)
        compare_pdf_sets(args.pdf_dir, args.compare_dir)
    if not args.skip_manifest:
        validate_manifest()
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
