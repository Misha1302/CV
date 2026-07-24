from pathlib import Path
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup
import fitz

pages = sorted(Path('.').glob('*.html'))
if len(pages) != 17:
    raise RuntimeError(f'Expected 17 HTML files, found {len(pages)}')

all_ids: dict[str, set[str]] = {}
for path in pages:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    ids = [node.get('id') for node in soup.find_all(attrs={'id': True})]
    if len(ids) != len(set(ids)):
        raise RuntimeError(f'{path}: duplicate IDs')
    all_ids[path.name] = set(ids)
    for anchor in soup.select('a[target="_blank"]'):
        if not {'noopener', 'noreferrer'} <= set(anchor.get('rel') or []):
            raise RuntimeError(f'{path}: unsafe target=_blank')

for path in pages:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    for node in soup.select('[href], [src]'):
        raw = node.get('href') or node.get('src')
        if not raw or raw.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        parsed = urlparse(raw)
        target = (path.parent / (unquote(parsed.path) or path.name)).resolve()
        if not target.exists():
            raise RuntimeError(f'{path}: missing local target {raw}')
        if parsed.fragment:
            target_name = target.name if target.suffix == '.html' else path.name
            if parsed.fragment not in all_ids.get(target_name, set()):
                raise RuntimeError(f'{path}: missing fragment {raw}')

pdfs = sorted(Path('pdf').glob('*.pdf'))
if len(pdfs) != 14:
    raise RuntimeError(f'Expected 14 role PDFs, found {len(pdfs)}')

focused = {
    'Mikhail_Razakov_Compiler_RU.pdf', 'Mikhail_Razakov_Compiler_EN.pdf',
    'Mikhail_Razakov_CPP_Systems_RU.pdf', 'Mikhail_Razakov_CPP_Systems_EN.pdf',
}
required_links = {
    'https://github.com/Misha1302/Nasm-X86-Course',
    'https://github.com/Misha1302/x86-64-codegen-ra-playground',
}
for path in pdfs:
    doc = fitz.open(path)
    if len(doc) != 1:
        raise RuntimeError(f'{path}: expected one page')
    if path.name in focused:
        page = doc[0]
        spans = [
            span
            for block in page.get_text('dict').get('blocks', [])
            for line in block.get('lines', [])
            for span in line.get('spans', [])
            if span.get('text', '').strip()
        ]
        min_font = min(float(span['size']) for span in spans)
        if min_font < 7.45:
            raise RuntimeError(f'{path}: unreadable font {min_font:.2f}pt')
        links = {link.get('uri') for link in page.get_links() if link.get('uri')}
        if not required_links <= links:
            raise RuntimeError(f'{path}: missing evidence links {required_links - links}')
    doc.close()

print('Validated 17 HTML files and 14 one-page role PDFs')
