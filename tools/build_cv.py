from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / 'data' / 'cv-print-profiles.json'


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def normalized(value: str) -> str:
    return re.sub(r'\s+', ' ', value).strip()


def build_block(profile: dict, project_urls: dict[str, str]) -> str:
    contact_values = profile['contact']
    contact_links = [
        f'<a href="mailto:{esc(contact_values[0])}">{esc(contact_values[0])}</a>',
        f'<a href="https://{esc(contact_values[1])}">{esc(contact_values[1])}</a>',
        f'<a href="https://{esc(contact_values[2])}">{esc(contact_values[2])}</a>',
    ]
    contact = '<br>'.join(contact_links)
    ru = profile.get('lang') == 'ru'
    labels = {
        'experience': 'Опыт' if ru else 'Experience',
        'projects': 'Избранные проекты' if ru else 'Selected projects',
        'skills': 'Компетенции' if ru else 'Skills',
        'education': 'Образование' if ru else 'Education',
        'recognition': 'Достижения' if ru else 'Recognition',
        'communication': 'Техническая коммуникация' if ru else 'Technical communication',
        'availability': 'Доступность' if ru else 'Availability',
    }
    proofs = ''.join(
        f'<div class="pcv-proof"><strong>{esc(title)}</strong><span>{esc(text)}</span></div>'
        for title, text in profile['proofs']
    )
    experience = []
    for date, title, bullets in profile['experience']:
        items = ''.join(f'<li>{esc(item)}</li>' for item in bullets)
        experience.append(
            f'<article class="pcv-entry"><div class="pcv-date">{esc(date)}</div>'
            f'<div><h3>{esc(title)}</h3><ul>{items}</ul></div></article>'
        )
    projects = []
    for title, text in profile['projects']:
        url = project_urls.get(title)
        heading = f'<a href="{esc(url)}">{esc(title)}</a>' if url else esc(title)
        projects.append(
            f'<article class="pcv-project"><div class="pcv-project-head"><h3>{heading}</h3></div>'
            f'<p>{esc(text)}</p></article>'
        )
    skills = ''.join(
        f'<div class="pcv-skill"><strong>{esc(title)}</strong><span>{esc(text)}</span></div>'
        for title, text in profile['skills']
    )
    density = esc(profile.get('density', 'normal'))
    return (
        f'<div class="print-cv pcv-{density}" aria-label="Focused one-page CV">'
        f'<header class="pcv-header"><div><h1>{esc(profile["name"])}</h1><h2>{esc(profile["role"])}</h2></div>'
        f'<div class="pcv-contact">{contact}</div></header>'
        f'<p class="pcv-summary">{esc(profile["summary"])}</p><div class="pcv-proofs">{proofs}</div>'
        f'<div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels["experience"]}</h2>'
        f'{"".join(experience)}</section><section><h2 class="pcv-section-title">{labels["projects"]}</h2>'
        f'{"".join(projects)}</section></main><aside class="pcv-side"><section><h2 class="pcv-section-title">{labels["skills"]}</h2>'
        f'{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["education"]}</h2><p>{esc(profile["education"])}</p></section>'
        f'<section class="pcv-compact"><h2 class="pcv-section-title">{labels["recognition"]}</h2><p>{esc(profile["recognition"])}</p></section>'
        f'<section class="pcv-compact"><h2 class="pcv-section-title">{labels["communication"]}</h2><p>{esc(profile["communication"])}</p></section>'
        f'<section class="pcv-compact"><h2 class="pcv-section-title">{labels["availability"]}</h2><p>{esc(profile["availability"])}</p></section>'
        f'</aside></div></div>'
    )


def inject(path: Path, block: str, write: bool) -> None:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    old = soup.select_one('.print-cv')
    expected = BeautifulSoup(block, 'html.parser').select_one('.print-cv')
    if old:
        old.replace_with(expected)
    else:
        soup.body.insert(0, expected)
    if write:
        path.write_text(str(soup), encoding='utf-8')
        return
    current = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser').select_one('.print-cv')
    if current is None or normalized(str(current)) != normalized(str(expected)):
        raise RuntimeError(f'Generated print block is stale: {path.name}')


def validate_pdf(path: Path) -> dict:
    doc = fitz.open(path)
    if doc.page_count != 1:
        raise RuntimeError(f'{path.name}: expected one page, got {doc.page_count}')
    page = doc[0]
    rect = page.rect
    if abs(rect.width - 595.28) > 3 or abs(rect.height - 841.89) > 3:
        raise RuntimeError(f'{path.name}: not A4: {rect}')
    text = page.get_text('text')
    if len(text.strip()) < 1200:
        raise RuntimeError(f'{path.name}: insufficient text layer: {len(text)}')
    sizes = [
        span['size']
        for block in page.get_text('dict')['blocks'] if 'lines' in block
        for line in block['lines'] for span in line['spans'] if span.get('text', '').strip()
    ]
    if not sizes or min(sizes) < 8.4:
        raise RuntimeError(f'{path.name}: minimum font size {min(sizes) if sizes else "none"}')
    links = page.get_links()
    if len(links) < 3:
        raise RuntimeError(f'{path.name}: too few links: {len(links)}')
    return {'file': path.name, 'pages': 1, 'text_chars': len(text), 'min_font': min(sizes), 'links': len(links)}


def render(pages: list[tuple[Path, Path, dict]], evidence_dir: Path | None) -> list[dict]:
    layout_reports = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 900, 'height': 1300}, device_scale_factor=2)
        page.emulate_media(media='print')
        for html_path, pdf_path, profile in pages:
            page.goto(html_path.resolve().as_uri(), wait_until='networkidle')
            metrics = page.eval_on_selector('.print-cv', '''el => {
              const root = el.getBoundingClientRect();
              let maxBottom = root.top;
              for (const node of el.querySelectorAll('*')) {
                const style = getComputedStyle(node);
                if (style.display === 'none' || style.visibility === 'hidden') continue;
                const rect = node.getBoundingClientRect();
                if (rect.width > 0 && rect.height > 0) maxBottom = Math.max(maxBottom, rect.bottom);
              }
              return {
                client: el.clientHeight,
                scroll: el.scrollHeight,
                width: el.scrollWidth,
                clientWidth: el.clientWidth,
                used: maxBottom - root.top,
                total: root.height,
                fill: (maxBottom - root.top) / root.height,
              };
            }''')
            if metrics['scroll'] > metrics['client'] + 2 or metrics['width'] > metrics['clientWidth'] + 2:
                raise RuntimeError(f'Print overflow in {html_path.name}: {metrics}')
            min_fill = float(profile.get('min_fill', 0.62))
            if metrics['fill'] < min_fill:
                raise RuntimeError(f'Print underfill in {html_path.name}: {metrics["fill"]:.3f} < {min_fill:.3f}')
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=True, scale=1.0, tagged=True, outline=True)
            if evidence_dir:
                evidence_dir.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(evidence_dir / (pdf_path.stem + '.png')), full_page=True)
            layout_reports.append({'html': html_path.name, 'fill_ratio': round(metrics['fill'], 4), 'used_px': round(metrics['used'], 1)})
        browser.close()
    return layout_reports


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-html', action='store_true')
    parser.add_argument('--check-html', action='store_true')
    parser.add_argument('--render-dir', type=Path)
    parser.add_argument('--evidence-dir', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    data = json.loads(DATA_PATH.read_text(encoding='utf-8'))
    project_urls = data.get('project_urls', {})
    pages = []
    for filename, profile in data['profiles'].items():
        html_path = ROOT / filename
        block = build_block(profile, project_urls)
        inject(html_path, block, args.write_html)
        if args.check_html:
            inject(html_path, block, False)
        if args.render_dir:
            pages.append((html_path, args.render_dir / profile['pdf'], profile))
    if pages:
        layout = render(pages, args.evidence_dir)
        report = []
        for (_, pdf, _), layout_result in zip(pages, layout, strict=True):
            report.append(validate_pdf(pdf) | layout_result)
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        else:
            print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
