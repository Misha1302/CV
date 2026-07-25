from __future__ import annotations

import json
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / 'data' / 'cv-print-profiles.json'

FACTS = {
    'ru': {
        'date': '1 июля — 31 августа 2026',
        'title': 'МЦСТ — стажёр по разработке компиляторов',
        'org': 'LLVM-направление · 0,25 ставки · удалённо',
        'detail': 'Изучаю алгоритмы на графах и устройство компиляторов; разрабатываю собственный оптимизационный проход для LLVM.',
        'web_bullets': [
            'Стажировка на 0,25 ставки: изучаю алгоритмы на графах, устройство компиляторов и LLVM.',
            'Разрабатываю собственный оптимизационный проход LLVM; реализую и тестирую графовые алгоритмы на C++23.',
        ],
        'pdf_title': 'МЦСТ · LLVM · 0,25 ставки',
        'pdf_bullets': [
            '0,25 ставки: графовые алгоритмы, устройство компиляторов и LLVM.',
            'Разрабатываю собственный оптимизационный проход LLVM.',
        ],
    },
    'en': {
        'date': 'July 1 — August 31, 2026',
        'title': 'MCST — Compiler Engineering Intern',
        'org': 'LLVM track · 0.25 FTE · remote',
        'detail': 'Studying graph algorithms and compiler construction; developing an LLVM optimization pass.',
        'web_bullets': [
            '0.25 FTE internship: studying graph algorithms, compiler construction, and LLVM.',
            'Developing an LLVM optimization pass; implementing and testing graph algorithms in C++23.',
        ],
        'pdf_title': 'MCST · LLVM · 0.25 FTE',
        'pdf_bullets': [
            '0.25 FTE: graph algorithms, compiler construction, and LLVM.',
            'Developing an LLVM optimization pass.',
        ],
    },
}


def set_text(tag, value: str) -> None:
    tag.clear()
    tag.append(value)


def replace_role_article(soup: BeautifulSoup, article, facts: dict[str, object]) -> None:
    article.clear()
    time = soup.new_tag('time')
    time['datetime'] = '2026-07-01'
    time.string = str(facts['date'])
    article.append(time)

    div = soup.new_tag('div')
    h3 = soup.new_tag('h3')
    h3.string = str(facts['title'])
    org = soup.new_tag('p')
    org['class'] = ['org']
    org.string = str(facts['org'])
    div.extend([h3, org])
    article.append(div)

    details = soup.new_tag('p')
    details['class'] = ['details']
    details.string = str(facts['detail'])
    article.append(details)


def replace_experience_article(soup: BeautifulSoup, article, facts: dict[str, object]) -> None:
    time = article.find('time')
    if time is not None:
        time.attrs.clear()
        set_text(time, str(facts['date']))

    heading = article.find('h3')
    if heading is not None:
        set_text(heading, str(facts['title']))

    org = article.find('p', class_='org')
    if org is not None:
        set_text(org, str(facts['org']))

    details = article.find('p', class_='details')
    if details is not None:
        details.decompose()

    bullets = article.find('ul', class_='timeline-details')
    if bullets is None:
        bullets = soup.new_tag('ul')
        bullets['class'] = ['timeline-details']
        article.append(bullets)
    bullets.clear()
    for value in facts['web_bullets']:
        item = soup.new_tag('li')
        item.string = str(value)
        bullets.append(item)


def update_html(path: Path) -> None:
    ru = path.name.startswith('ru')
    lang = 'ru' if ru else 'en'
    facts = FACTS[lang]
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')

    education = soup.select_one('#education')
    if education is not None:
        heading = education.select_one('.section-heading h2')
        if heading is not None:
            set_text(heading, 'Образование и текущая занятость.' if ru else 'Education and current role.')
        for article in education.find_all('article'):
            content = article.get_text(' ', strip=True)
            markers = [
                'Стажировка или неполная занятость',
                'Internship or part-time role',
                'С сентября 2026',
                'From September 2026',
                'МЦСТ — стажёр по разработке компиляторов',
                'MCST — Compiler Engineering Intern',
            ]
            if any(marker in content for marker in markers):
                replace_role_article(soup, article, facts)
                break

    experience = soup.select_one('#experience')
    if experience is not None:
        for article in experience.find_all('article'):
            heading = article.find('h3')
            title = heading.get_text(' ', strip=True) if heading else ''
            if 'МЦСТ' in title or 'MCST' in title:
                replace_experience_article(soup, article, facts)
                break

    for span in soup.select('.hero-context span'):
        current = span.get_text(' ', strip=True)
        lower = current.lower()
        if ru and 'мцст' in lower and ('июль' in lower or 'август' in lower):
            set_text(span, 'МЦСТ · 1 июля–31 августа 2026 · 0,25 ставки')
        elif not ru and 'mcst' in lower and ('july' in lower or 'august' in lower):
            set_text(span, 'MCST · July 1–August 31, 2026 · 0.25 FTE')
        elif ru and 'с сентября 2026' in lower and ('стажировка' in lower or 'неполная занятость' in lower):
            set_text(span, 'С сентября 2026: до 20 часов в неделю')
        elif not ru and 'from september 2026' in lower and ('internship' in lower or 'part-time' in lower):
            set_text(span, 'From September 2026: up to 20 hours/week')

    for item in soup.select('.career-item'):
        strong = item.find('strong')
        if strong is None:
            continue
        if strong.get_text(' ', strip=True) in {'МЦСТ', 'MCST'}:
            detail = item.find('span')
            if detail is not None:
                set_text(detail, 'LLVM · оптимизационный проход · графовые алгоритмы' if ru else 'LLVM · optimization pass · graph algorithms')

    contact = soup.select_one('#contact h2')
    if contact is not None:
        current = contact.get_text(' ', strip=True).lower()
        if ru and 'ищу стажировку' in current:
            set_text(contact, 'С сентября 2026 открыт к работе с неполной занятостью в LLVM, разработке компиляторов и анализе программ.')
        elif not ru and 'internship' in current:
            set_text(contact, 'Available for part-time LLVM, compiler, or program-analysis work from September 2026.')

    path.write_text(str(soup), encoding='utf-8')


def update_validator() -> None:
    path = ROOT / 'tools' / 'validate_cv.py'
    source = path.read_text(encoding='utf-8')

    data_anchor = "    for filename in ['ru-devtools.html', 'en-devtools.html']:\n"
    data_check = '''    required_mcst_profiles = {'ru-compiler.html', 'en-compiler.html', 'ru-cpp-systems.html', 'en-cpp-systems.html'}
    for filename, profile in DATA['profiles'].items():
        ru = profile.get('lang') == 'ru'
        mcst = next((entry for entry in profile['experience'] if 'МЦСТ' in entry[1] or 'MCST' in entry[1]), None)
        if filename in required_mcst_profiles and mcst is None:
            raise RuntimeError(f'{filename}: missing MCST internship')
        if mcst is None:
            continue
        joined = ' '.join([mcst[0], mcst[1], *mcst[2]])
        required = ['1 июля — 31 августа 2026', '0,25 ставки', 'оптимизационный проход LLVM'] if ru else ['July 1 — August 31, 2026', '0.25 FTE', 'LLVM optimization pass']
        for marker in required:
            if marker.casefold() not in joined.casefold():
                raise RuntimeError(f'{filename}: incomplete MCST fact {marker!r}')
'''
    if data_check not in source:
        if data_anchor not in source:
            raise RuntimeError('validate_data insertion anchor missing')
        source = source.replace(data_anchor, data_check + data_anchor)

    html_anchor = "    compiler = (ROOT / 'ru-compiler.html').read_text(encoding='utf-8')\n"
    html_check = '''    current_role_pages = ['ru.html', 'en.html', 'ru-compiler.html', 'en-compiler.html', 'ru-cpp-systems.html', 'en-cpp-systems.html']
    for filename in current_role_pages:
        page = (ROOT / filename).read_text(encoding='utf-8')
        required = ['1 июля — 31 августа 2026', '0,25 ставки', 'оптимизационный проход'] if filename.startswith('ru') else ['July 1 — August 31, 2026', '0.25 FTE', 'optimization pass']
        for marker in required:
            if marker.casefold() not in page.casefold():
                raise RuntimeError(f'{filename}: missing current MCST fact {marker!r}')
'''
    if html_check not in source:
        if html_anchor not in source:
            raise RuntimeError('validate_html insertion anchor missing')
        source = source.replace(html_anchor, html_check + html_anchor)

    path.write_text(source, encoding='utf-8')


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding='utf-8'))
    targets = [ROOT / filename for filename in data['profiles']] + [ROOT / 'ru.html', ROOT / 'en.html']
    for path in targets:
        update_html(path)

    for filename, profile in data['profiles'].items():
        lang = 'ru' if profile.get('lang') == 'ru' else 'en'
        facts = FACTS[lang]
        entry = next((item for item in profile['experience'] if 'МЦСТ' in item[1] or 'MCST' in item[1]), None)
        if entry is None:
            continue
        entry[:] = [facts['date'], facts['pdf_title'], facts['pdf_bullets']]
        for index, marker in enumerate(profile.get('ats_order', [])):
            if 'МЦСТ' in marker or 'MCST' in marker:
                profile['ats_order'][index] = facts['pdf_title']

    required_profiles = {'ru-compiler.html', 'en-compiler.html', 'ru-cpp-systems.html', 'en-cpp-systems.html'}
    for filename in required_profiles:
        profile = data['profiles'][filename]
        if not any('МЦСТ' in item[1] or 'MCST' in item[1] for item in profile['experience']):
            raise RuntimeError(f'{filename}: MCST experience unexpectedly absent')

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    update_validator()


if __name__ == '__main__':
    main()
