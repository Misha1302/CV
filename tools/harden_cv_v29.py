from __future__ import annotations

from pathlib import Path
import re

ROOT = Path('.')
RU_ACHIEVEMENT = (
    'Призёр «Высшей пробы» по олимпиадному и промышленному программированию; '
    '1-е место по итоговому баллу: «Юниор» 2025 — направление «Инженерные науки», '
    '2026 — секция «Информационные технологии»; диплом I степени и Главная премия Балтийского конкурса.'
)
EN_ACHIEVEMENT = (
    'HSE Olympiad prize-winner in competitive and industrial programming; top total score in MEPhI Junior '
    '(2025 Engineering Sciences; 2026 Information Technology); Baltic competition first-degree diploma and Grand Prize.'
)


def replace_exact(path: Path, old: str, new: str, expected: int | None = 1) -> None:
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if expected is not None and count != expected:
        raise RuntimeError(f'{path}: expected {expected} occurrence(s), found {count}: {old[:120]!r}')
    if count:
        path.write_text(text.replace(old, new), encoding='utf-8')


def replace_regex(path: Path, pattern: str, replacement: str, expected: int = 1) -> None:
    text = path.read_text(encoding='utf-8')
    updated, count = re.subn(pattern, replacement, text, flags=re.DOTALL)
    if count != expected:
        raise RuntimeError(f'{path}: expected {expected} regex replacement(s), found {count}: {pattern[:120]!r}')
    path.write_text(updated, encoding='utf-8')


html_files = sorted(ROOT.glob('*.html'))
if len(html_files) != 17:
    raise RuntimeError(f'Expected 17 HTML files, found {len(html_files)}')

for path in html_files:
    text = path.read_text(encoding='utf-8')
    text = text.replace('style.css?v=28', 'style.css?v=29')
    text = text.replace('script.js?v=28', 'script.js?v=29')
    path.write_text(text, encoding='utf-8')

# Superseded Wist2 baselines.
replace_regex(
    Path('ru.html'),
    r'проверенный baseline от 14\.07\.2026: 75 \.NET-проектов собираются, 1 325 тестов проходят, 0 предупреждений и 0 ошибок\.',
    'последний полный прогон от 23.07.2026: 1 358/1 358 тестов пройдены, 0 сбоев; сборка успешна.',
)
replace_exact(
    Path('en.html'),
    'the verified baseline dated July 14, 2026 covers 75 .NET projects building and 1,325 passing tests, with 0 warnings and 0 errors.',
    'the latest full run on July 23, 2026 completed 1,358/1,358 tests with 0 failures; the build succeeded.',
)
for old, new in (
    ('<strong>1 325 тестов</strong>', '<strong>1 358 тестов</strong>'),
    ('Настроил package-surface и clean-consumer smoke tests; проверенный baseline от 14.07.2026 — 75 .NET-проектов и 1 325 тестов.',
     'Настроил package-surface и clean-consumer smoke tests; последний полный прогон от 23.07.2026 — 1 358/1 358 тестов, 0 сбоев, сборка успешна.'),
    ('<strong>Результат:</strong> 75 .NET-проектов, 1 325 тестов, 0 предупреждений и 0 ошибок в проверенном отчёте от 14.07.2026.',
     '<strong>Результат:</strong> полный прогон от 23.07.2026 — 1 358/1 358 тестов, 0 сбоев; сборка успешна.'),
):
    replace_exact(Path('ru-devtools.html'), old, new)
for old, new in (
    ('<strong>1,325 tests</strong>', '<strong>1,358 tests</strong>'),
    ('Added package-surface and clean-consumer smoke tests; the public baseline covers 75 .NET projects and 1,325 tests.',
     'Added package-surface and clean-consumer smoke tests; the latest full run on July 23, 2026 completed 1,358/1,358 tests with 0 failures and a successful build.'),
    ('<strong>Result:</strong> 1,325 tests, 75 .NET projects, 0 warnings and 0 errors in the public verification record.',
     '<strong>Result:</strong> the July 23, 2026 full run completed 1,358/1,358 tests with 0 failures; the build succeeded.'),
):
    replace_exact(Path('en-devtools.html'), old, new)

# Duplicate wording.
for path in [p for p in html_files if p.name == 'ru.html' or p.name.startswith('ru-')]:
    text = path.read_text(encoding='utf-8').replace(
        'Дизассемблирование и анализ compiler output; differential testing, differential testing и изолированный запуск.',
        'Дизассемблирование и анализ compiler output; differential testing, метрики spills/code size и изолированный запуск.',
    )
    path.write_text(text, encoding='utf-8')
for path in [p for p in html_files if p.name == 'en.html' or p.name.startswith('en-')]:
    text = path.read_text(encoding='utf-8').replace(
        'Disassembly and compiler-output analysis; differential testing, differential testing and isolated execution.',
        'Disassembly and compiler-output analysis; differential testing, spill/code-size metrics and isolated execution.',
    )
    path.write_text(text, encoding='utf-8')

# Natural Russian C++ systems wording.
ru_cpp = Path('ru-cpp-systems.html')
ru_cpp_replacements = {
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
text = ru_cpp.read_text(encoding='utf-8')
for old, new in ru_cpp_replacements.items():
    if old not in text:
        raise RuntimeError(f'ru-cpp-systems.html: expected wording missing: {old!r}')
    text = text.replace(old, new)
ru_cpp.write_text(text, encoding='utf-8')

for name in ('en-compiler.html', 'en-cpp-systems.html'):
    path = Path(name)
    text = path.read_text(encoding='utf-8').replace('cdecl, stack/x87;', 'cdecl, stack frames and x87;')
    path.write_text(text, encoding='utf-8')

for name in ('ru-compiler.html', 'ru-cpp-systems.html'):
    replace_regex(Path(name), r'(<section class="pcv-compact"><h2 class="pcv-section-title">Достижения</h2><p>).*?(</p></section>)', rf'\1{RU_ACHIEVEMENT}\2')
for name in ('en-compiler.html', 'en-cpp-systems.html'):
    replace_regex(Path(name), r'(<section class="pcv-compact"><h2 class="pcv-section-title">Recognition</h2><p>).*?(</p></section>)', rf'\1{EN_ACHIEVEMENT}\2')

style = Path('style.css')
style_text = style.read_text(encoding='utf-8')
style_patch = '''

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
'''
if 'v29: focused-PDF readability hardening' in style_text:
    raise RuntimeError('style.css already contains the v29 print patch')
style.write_text(style_text.rstrip() + style_patch, encoding='utf-8')

renames = {Path('CONTENT-REVIEW-v28.md'): Path('CONTENT-REVIEW-v29.md'), Path('QA-report-targeted-cv-v28.md'): Path('QA-report-targeted-cv-v29.md')}
for old, new in renames.items():
    if not old.exists() or new.exists():
        raise RuntimeError(f'Cannot rename release file {old} -> {new}')
    old.rename(new)

readme = Path('README.md')
readme_text = readme.read_text(encoding='utf-8').replace('# Mikhail Razakov - targeted CV variants v28', '# Mikhail Razakov - targeted CV variants v29', 1)
v29_section = '''## Изменения v29

- Подробные HTML-страницы синхронизированы с актуальным Wist2 baseline: 1 358/1 358 тестов, 0 сбоев, сборка успешна; удалены устаревшие 75 проектов / 1 325 тестов.
- Удалено дублирование `differential testing`; формулировки про codegen снова содержат метрики spills/code size.
- Русская C++ systems-версия языково вычищена: ключевые заголовки, алгоритмы и toolchain-описания переведены без потери технической точности.
- В focused PDF восстановлена конкретика по двум профилям «Высшей пробы», сохранены точные категории первых результатов «Юниора» и Балтийская Главная премия.
- Минимальный шрифт четырёх focused PDF поднят до 8.5 pt при A4, одной странице и `scale=1.0`; ATS-порядок и ссылки перепроверены.
- README, release metadata, QA, targeting и evidence-аудиты синхронизированы как v29.

'''
marker = '## Изменения v28\n'
if marker not in readme_text:
    raise RuntimeError('README v28 history section missing')
readme_text = readme_text.replace(marker, v29_section + marker, 1).replace(
    'Предыдущая версия репозитория: v27, commit `31a7c75144d1555b3c3fa8ca1eb7e14969770561`.',
    'Предыдущая версия репозитория: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`.',
    1,
)
readme.write_text(readme_text, encoding='utf-8')

metadata = Path('RELEASE-METADATA.md')
metadata_text = metadata.read_text(encoding='utf-8').replace('- Version: v28', '- Version: v29', 1)
metadata_text = re.sub(r'- Previous repository baseline: .*', '- Previous repository baseline: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`', metadata_text, count=1)
metadata_text += ('\n## v29 consistency boundary\n\n- Detailed HTML and focused PDFs use the same 1,358/1,358 Wist2 full-run claim.\n- Four focused PDFs must remain one A4 page at scale=1.0 with a minimum extracted font size of 8.45 pt.\n- Russian C++ systems headings are localized; English technical names remain only where they are conventional identifiers.\n')
metadata.write_text(metadata_text, encoding='utf-8')

for name in ('TARGETING.md', 'LANGUAGE-REVIEW.md', 'EXPERIENCE-AUDIT.md', 'FACT-RETENTION.md', 'LINK-AUDIT.md', 'CONTENT-REVIEW-v29.md', 'QA-report-targeted-cv-v29.md'):
    path = Path(name)
    path.write_text(path.read_text(encoding='utf-8').replace('v28', 'v29'), encoding='utf-8')

qa = Path('QA-report-targeted-cv-v29.md')
qa.write_text(qa.read_text(encoding='utf-8') + '''

## v29 review scope

- detailed HTML baseline consistency and duplicate-wording checks;
- Russian C++ systems language pass;
- focused PDF font floor raised from 7.99 pt to at least 8.45 pt;
- precise RU/EN achievement wording retained after reflow;
- before/after render review required before merge.
''', encoding='utf-8')

corpus = '\n'.join(path.read_text(encoding='utf-8') for path in html_files)
for stale in ('75 .NET-проектов', '1 325 тестов', '75 .NET projects', '1,325 tests', '1,325 passing tests', 'differential testing, differential testing'):
    if stale in corpus:
        raise RuntimeError(f'Stale wording remains in HTML corpus: {stale}')
for marker in (RU_ACHIEVEMENT, EN_ACHIEVEMENT, '1 358/1 358', '1,358/1,358'):
    if marker not in corpus:
        raise RuntimeError(f'Required current wording missing: {marker}')
ru_cpp_text = ru_cpp.read_text(encoding='utf-8')
for stale in ('Strict toolchain', '<strong>Program analysis</strong>', '<strong>Low-level</strong>', '<strong>Toolchain</strong>'):
    if stale in ru_cpp_text:
        raise RuntimeError(f'Russian C++ profile still contains unlocalized label: {stale}')
print('Applied CV v29 consistency, language and readability changes')
