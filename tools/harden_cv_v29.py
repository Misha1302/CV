from __future__ import annotations

from pathlib import Path
import re

RU_ACHIEVEMENT = (
    'Призёр «Высшей пробы» по олимпиадному и промышленному программированию; '
    '1-е место по итоговому баллу: «Юниор» 2025 — направление «Инженерные науки», '
    '2026 — секция «Информационные технологии»; диплом I степени и Главная премия Балтийского конкурса.'
)
EN_ACHIEVEMENT = (
    'HSE Olympiad prize-winner in competitive and industrial programming; top total score in MEPhI Junior '
    '(2025 Engineering Sciences; 2026 Information Technology); Baltic competition first-degree diploma and Grand Prize.'
)


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding='utf-8')


def replace_compact_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(encoding='utf-8')
    pattern = rf'(<section class="pcv-compact"><h2 class="pcv-section-title">{re.escape(heading)}</h2><p>).*?(</p></section>)'
    text, count = re.subn(pattern, rf'\1{body}\2', text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f'{path}: compact section {heading!r} not found exactly once')
    write(path, text)


html_files = sorted(Path('.').glob('*.html'))
if len(html_files) != 17:
    raise RuntimeError(f'Expected 17 HTML files, found {len(html_files)}')
ru_files = [p for p in html_files if p.name == 'ru.html' or p.name.startswith('ru-')]
en_files = [p for p in html_files if p.name == 'en.html' or p.name.startswith('en-')]

# Cache-bust the complete public surface.
for path in html_files:
    text = path.read_text(encoding='utf-8')
    write(path, text.replace('style.css?v=28', 'style.css?v=29').replace('script.js?v=28', 'script.js?v=29'))

# Replace stale Wist2 count claims, including <strong> markup inside list items.
ru_pattern = re.compile(
    r'<li>(?=(?:(?!</li>).)*75 \.NET-проектов)(?=(?:(?!</li>).)*1 325 тестов)(?:(?!</li>).)*</li>',
    re.DOTALL,
)
en_pattern = re.compile(
    r'<li>(?=(?:(?!</li>).)*75 \.NET projects)(?=(?:(?!</li>).)*1,325)(?:(?!</li>).)*</li>',
    re.DOTALL,
)
ru_replaced = 0
for path in ru_files:
    text = path.read_text(encoding='utf-8')
    text, count = ru_pattern.subn(
        '<li>Последний полный прогон от 23.07.2026: 1 358/1 358 тестов пройдены, 0 сбоев; сборка успешна.</li>',
        text,
    )
    ru_replaced += count
    write(path, text.replace('<strong>1 325 тестов</strong>', '<strong>1 358 тестов</strong>'))

en_replaced = 0
for path in en_files:
    text = path.read_text(encoding='utf-8')
    text, count = en_pattern.subn(
        '<li>The latest full run on July 23, 2026 completed 1,358/1,358 tests with 0 failures; the build succeeded.</li>',
        text,
    )
    en_replaced += count
    write(path, text.replace('<strong>1,325 tests</strong>', '<strong>1,358 tests</strong>'))

if ru_replaced < 3 or en_replaced < 3:
    raise RuntimeError(f'Expected at least three stale-count claims per language, replaced RU={ru_replaced}, EN={en_replaced}')

# Restore meaningful codegen evidence where a duplicated phrase had appeared.
for path in ru_files:
    text = path.read_text(encoding='utf-8').replace(
        'Дизассемблирование и анализ compiler output; differential testing, differential testing и изолированный запуск.',
        'Дизассемблирование и анализ compiler output; differential testing, метрики spills/code size и изолированный запуск.',
    )
    write(path, text)
for path in en_files:
    text = path.read_text(encoding='utf-8').replace(
        'Disassembly and compiler-output analysis; differential testing, differential testing and isolated execution.',
        'Disassembly and compiler-output analysis; differential testing, spill/code-size metrics and isolated execution.',
    ).replace(
        'differential tests, differential testing',
        'differential tests, spill/code-size metrics',
    ).replace(
        'differential tests, differential testing',
        'differential tests, spill/code-size metrics',
    )
    write(path, text)

# Natural Russian wording for the C++ systems page and its focused print source.
ru_cpp = Path('ru-cpp-systems.html')
text = ru_cpp.read_text(encoding='utf-8')
translations = {
    'C++23, C17, анализ программ, NASM IA-32, x86-64 codegen, Linux и строгий toolchain.': 'C++23, C17, анализ программ, NASM IA-32, генерация x86-64-кода, Linux и строгая сборка.',
    '<span>C++ systems · program analysis</span>': '<span>C++ systems · анализ программ</span>',
    '<strong>C17 analyzer</strong><span>нормализация + exact/conservative strategies</span>': '<strong>C17-анализатор</strong><span>нормализация, точные и консервативные стратегии</span>',
    '<strong>C++23 graph core</strong><span>RPO, shortest paths, SCC, max-flow</span>': '<strong>C++23-ядро графов</strong><span>RPO, кратчайшие пути, SCC, максимальный поток</span>',
    '<p class="org">Compiler/runtime architecture · verification engineering</p>': '<p class="org">Архитектура compiler/runtime · проверка корректности</p>',
    '<span class="project-type">C17 · Python · program analysis</span>': '<span class="project-type">C17 · Python · анализ программ</span>',
    'точный аффинный анализ, monotonic scan и ограниченный перебор.': 'точный аффинный анализ, монотонный проход и ограниченный перебор.',
    '<strong>Strict toolchain</strong><span>CMake, -Werror, ASan/UBSan, clang-tidy</span>': '<strong>Строгая сборка</strong><span>CMake, -Werror, ASan/UBSan, clang-tidy</span>',
    'Разработал общее ядро ориентированного графа и компоненты RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic.': 'Разработал ядро ориентированного графа, RPO с обнаружением циклов, алгоритм Дейкстры, SCC Тарьяна и максимальный поток Диница.',
    '<span>C17 / program analysis</span>': '<span>C17 / анализ программ</span>',
    '<strong>Program analysis</strong>': '<strong>Анализ программ</strong>',
    '<strong>Low-level</strong>': '<strong>Низкоуровневая разработка</strong>',
    '<strong>Toolchain</strong>': '<strong>Инструменты и качество</strong>',
    'графы, деревья, строки, структуры данных, max-flow, SCC и кратчайшие пути': 'графы, деревья, строки, структуры данных, максимальный поток, SCC и кратчайшие пути',
    'отдельный x86-64 SysV emitter с анализом живости, распределением регистров, iced-x86 и изолированным запуском нативного кода.': 'отдельный генератор x86-64 SysV-кода с анализом живости, распределением регистров, iced-x86 и изолированным запуском нативного кода.',
}
for old, new in translations.items():
    text = text.replace(old, new)
write(ru_cpp, text)

for name in ('en-compiler.html', 'en-cpp-systems.html'):
    path = Path(name)
    write(path, path.read_text(encoding='utf-8').replace('cdecl, stack/x87;', 'cdecl, stack frames and x87;'))

replace_compact_section(Path('ru-compiler.html'), 'Достижения', RU_ACHIEVEMENT)
replace_compact_section(Path('ru-cpp-systems.html'), 'Достижения', RU_ACHIEVEMENT)
replace_compact_section(Path('en-compiler.html'), 'Recognition', EN_ACHIEVEMENT)
replace_compact_section(Path('en-cpp-systems.html'), 'Recognition', EN_ACHIEVEMENT)

# Increase the real print font floor; export remains scale=1.0.
style = Path('style.css')
style_text = style.read_text(encoding='utf-8')
if 'v29: focused-PDF readability hardening' in style_text:
    raise RuntimeError('style.css already contains the v29 patch')
write(style, style_text.rstrip() + '''

/* v29: focused-PDF readability hardening; keep scale=1.0 */
@media print {
  .pcv-contact { font-size: 9.35pt; }
  .pcv-summary { font-size: 10.35pt; }
  .pcv-proof span { font-size: 8.95pt; }
  .pcv-date { font-size: 8.55pt; }
  .pcv-entry li { font-size: 9.25pt; }
  .pcv-project-head span { font-size: 8.5pt; }
  .pcv-project p { font-size: 9.2pt; }
  .pcv-skill strong { font-size: 9.3pt; }
  .pcv-skill span { font-size: 8.75pt; }
  .pcv-compact p { font-size: 9.05pt; }
}
''')

# Promote release review files.
for old, new in (
    (Path('CONTENT-REVIEW-v28.md'), Path('CONTENT-REVIEW-v29.md')),
    (Path('QA-report-targeted-cv-v28.md'), Path('QA-report-targeted-cv-v29.md')),
):
    if not old.exists() or new.exists():
        raise RuntimeError(f'Cannot rename {old} -> {new}')
    old.rename(new)

readme = Path('README.md')
readme_text = readme.read_text(encoding='utf-8')
readme_text = readme_text.replace('# Mikhail Razakov - targeted CV variants v28', '# Mikhail Razakov - targeted CV variants v29', 1)
v29_section = '''## Изменения v29

- Подробные HTML-страницы синхронизированы с актуальным Wist2 baseline: 1 358/1 358 тестов, 0 сбоев, сборка успешна; удалены устаревшие 75 проектов / 1 325 тестов.
- Удалено дублирование `differential testing`; формулировки про codegen снова содержат метрики spills/code size.
- Русская C++ systems-версия языково вычищена: ключевые заголовки, алгоритмы и toolchain-описания переведены без потери технической точности.
- В focused PDF восстановлена конкретика по двум профилям «Высшей пробы», сохранены точные категории первых результатов «Юниора» и Балтийская Главная премия.
- Минимальный шрифт четырёх focused PDF поднят до 8.5 pt при A4, одной странице и `scale=1.0`; ATS-порядок и ссылки перепроверены.
- README, release metadata, QA, targeting и evidence-аудиты синхронизированы как v29.

'''
if '## Изменения v28\n' not in readme_text:
    raise RuntimeError('README v28 history section missing')
readme_text = readme_text.replace('## Изменения v28\n', v29_section + '## Изменения v28\n', 1)
readme_text = readme_text.replace(
    'Предыдущая версия репозитория: v27, commit `31a7c75144d1555b3c3fa8ca1eb7e14969770561`.',
    'Предыдущая версия репозитория: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`.',
    1,
)
write(readme, readme_text)

metadata = Path('RELEASE-METADATA.md')
metadata_text = metadata.read_text(encoding='utf-8').replace('- Version: v28', '- Version: v29', 1)
metadata_text = re.sub(
    r'- Previous repository baseline: .*',
    '- Previous repository baseline: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`',
    metadata_text,
    count=1,
)
metadata_text += '''
## v29 consistency boundary

- Detailed HTML and focused PDFs use the same 1,358/1,358 Wist2 full-run claim.
- Four focused PDFs remain one A4 page at scale=1.0 with a minimum extracted font size of 8.45 pt.
- Russian C++ systems headings are localized; conventional identifiers remain unchanged.
'''
write(metadata, metadata_text)

for name in (
    'TARGETING.md', 'LANGUAGE-REVIEW.md', 'EXPERIENCE-AUDIT.md', 'FACT-RETENTION.md',
    'LINK-AUDIT.md', 'CONTENT-REVIEW-v29.md', 'QA-report-targeted-cv-v29.md',
):
    path = Path(name)
    write(path, path.read_text(encoding='utf-8').replace('v28', 'v29'))

qa = Path('QA-report-targeted-cv-v29.md')
write(qa, qa.read_text(encoding='utf-8') + '''

## v29 review scope

- detailed HTML baseline consistency and duplicate-wording checks;
- Russian C++ systems language pass;
- focused PDF font floor raised from 7.99 pt to at least 8.45 pt;
- precise RU/EN achievement wording retained after reflow;
- before/after render review required before merge.
''')

# Source-level gates.
corpus = '\n'.join(path.read_text(encoding='utf-8') for path in html_files)
for stale in (
    '75 .NET-проектов', '1 325 тестов', '75 .NET projects', '1,325 tests',
    '1,325 passing tests', 'differential testing, differential testing',
):
    if stale in corpus:
        raise RuntimeError(f'Stale HTML wording remains: {stale}')
for required in (
    RU_ACHIEVEMENT, EN_ACHIEVEMENT, '1 358/1 358', '1,358/1,358',
    'метрики spills/code size', 'spill/code-size metrics',
):
    if required not in corpus:
        raise RuntimeError(f'Required HTML wording missing: {required}')
ru_cpp_text = ru_cpp.read_text(encoding='utf-8')
for stale in ('Strict toolchain', '<strong>Program analysis</strong>', '<strong>Low-level</strong>', '<strong>Toolchain</strong>'):
    if stale in ru_cpp_text:
        raise RuntimeError(f'Russian C++ label remains: {stale}')
for required in ('Строгая сборка', 'Анализ программ', 'Низкоуровневая разработка', 'Инструменты и качество'):
    if required not in ru_cpp_text:
        raise RuntimeError(f'Russian C++ label missing: {required}')

print(f'Applied CV v29 source changes; stale list claims replaced RU={ru_replaced}, EN={en_replaced}')
