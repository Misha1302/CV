from __future__ import annotations

from pathlib import Path


def replace_exact(path: Path, old: str, new: str, *, count: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    actual = text.count(old)
    if actual != count:
        raise RuntimeError(f"{path}: expected {count} occurrence(s), found {actual}: {old[:100]!r}")
    path.write_text(text.replace(old, new, count), encoding="utf-8")


# Cache-bust the complete public HTML surface so updated compiler pages cannot be
# combined with stale shared assets in browsers or GitHub Pages caches.
html_files = sorted(Path(".").glob("*.html"))
if len(html_files) != 17:
    raise RuntimeError(f"Expected 17 HTML files, found {len(html_files)}")
for path in html_files:
    text = path.read_text(encoding="utf-8")
    text = text.replace("style.css?v=29", "style.css?v=30")
    text = text.replace("script.js?v=29", "script.js?v=30")
    path.write_text(text, encoding="utf-8")

ru = Path("ru-compiler.html")
en = Path("en-compiler.html")

# Public-page factual consistency and recruiter-screen ordering.
replace_exact(ru, "<span>Студент НИУ ВШЭ</span>", "<span>Студент ПИ НИУ ВШЭ</span>")
replace_exact(
    ru,
    '<section aria-label="Ключевые доказательства" class="shell proof-strip"><div class="proof-item"><strong>AIR → SSA → AIR</strong><span>lowering/emission и оптимизации под контролем структурных верификаторов</span></div><div class="proof-item"><strong>1 358 / 1 358 тестов</strong><span>baseline от 14.07.2026; 0 предупреждений и 0 ошибок</span></div><div class="proof-item"><strong>1-е место · 104/104</strong><span>консервативный анализ зависимостей памяти</span></div></section>',
    '<section aria-label="Ключевые доказательства" class="shell proof-strip"><div class="proof-item"><strong>AIR → SSA → AIR</strong><span>lowering/emission и оптимизации под контролем структурных верификаторов</span></div><div class="proof-item"><strong>1-е место · 104/104</strong><span>консервативный анализ зависимостей памяти</span></div><div class="proof-item"><strong>1 358 / 1 358 тестов</strong><span>полный прогон 23.07.2026: 0 сбоев, сборка успешна</span></div></section>',
)
replace_exact(
    en,
    '<section aria-label="Key evidence" class="shell proof-strip"><div class="proof-item"><strong>AIR → SSA → AIR</strong><span>lowering/emission and optimization passes under structural verifiers</span></div><div class="proof-item"><strong>1,358 / 1,358 tests</strong><span>verified baseline dated July 14, 2026; 0 warnings and 0 errors</span></div><div class="proof-item"><strong>1st place · 104/104</strong><span>conservative memory-dependence analyzer</span></div></section>',
    '<section aria-label="Key evidence" class="shell proof-strip"><div class="proof-item"><strong>AIR → SSA → AIR</strong><span>lowering/emission and optimization passes under structural verifiers</span></div><div class="proof-item"><strong>1st place · 104/104</strong><span>conservative memory-dependence analyzer</span></div><div class="proof-item"><strong>1,358 / 1,358 tests</strong><span>full run on July 23, 2026: 0 failures, build succeeded</span></div></section>',
)

# Fix missing separators in the Russian featured-project evidence list.
for old, new in {
    '<li><strong>Конвейер</strong>Лексер, парсер, AST, Bytecode, AIR, эталонный интерпретатор и генерация CIL/DynamicMethod.</li>': '<li><strong>Конвейер:</strong> лексер, парсер, AST, Bytecode, AIR, эталонный интерпретатор и генерация CIL/DynamicMethod.</li>',
    '<li><strong>Маршрут SSA</strong>Неизменяемая модель, явные привязки вызовов, проходы с проверкой возможностей backend и контролируемый возврат к исходному маршруту.</li>': '<li><strong>Маршрут SSA:</strong> неизменяемая модель, явные привязки вызовов, проходы с проверкой возможностей backend и контролируемый возврат к исходному маршруту.</li>',
    '<li><strong>Проверка</strong>Структурные проверки до и после преобразований, сравнение путей исполнения и целевые регрессионные тесты.</li>': '<li><strong>Проверка:</strong> структурные проверки до и после преобразований, сравнение путей исполнения и целевые регрессионные тесты.</li>',
}.items():
    replace_exact(ru, old, new)

# Confirmed education programme, public-page copy and release date.
replace_exact(
    ru,
    '<div class="section-heading"><p class="section-label">05 · Образование</p><div><h2>Образование и доступность.</h2><p class="section-intro">Студент НИУ ВШЭ.</p></div></div>',
    '<div class="section-heading"><p class="section-label">05 · Образование</p><div><h2>Образование и доступность.</h2><p class="section-intro">Студент программы «Программная инженерия» НИУ ВШЭ.</p></div></div>',
)
replace_exact(
    ru,
    '<article><time>Студент</time><div><h3><a href="https://www.hse.ru/" rel="noopener noreferrer" target="_blank">НИУ ВШЭ</a></h3><p class="org">Москва</p></div><p class="details">Студент НИУ ВШЭ.</p></article>',
    '<article><time>Студент</time><div><h3><a href="https://www.hse.ru/" rel="noopener noreferrer" target="_blank">НИУ ВШЭ</a></h3><p class="org">Программная инженерия · Москва</p></div><p class="details">Учусь на программе «Программная инженерия» НИУ ВШЭ.</p></article>',
)
replace_exact(en, "<span>HSE University student</span>", "<span>HSE Software Engineering student</span>")
replace_exact(
    en,
    '<div class="section-heading"><p class="section-label">05 · Education</p><div><h2>Education and availability.</h2><p class="section-intro">HSE University student.</p></div></div>',
    '<div class="section-heading"><p class="section-label">05 · Education</p><div><h2>Education and availability.</h2><p class="section-intro">Software Engineering student at HSE University.</p></div></div>',
)
replace_exact(
    en,
    '<article><time>Student</time><div><h3><a href="https://www.hse.ru/en/" rel="noopener noreferrer" target="_blank">HSE University</a></h3><p class="org">Moscow</p></div><p class="details">HSE University student.</p></article>',
    '<article><time>Student</time><div><h3><a href="https://www.hse.ru/en/" rel="noopener noreferrer" target="_blank">HSE University</a></h3><p class="org">Software Engineering · Moscow</p></div><p class="details">Studying Software Engineering at HSE University.</p></article>',
)
replace_exact(ru, "Обновлено 24 июля 2026", "Обновлено 25 июля 2026")
replace_exact(en, "Updated July 24, 2026", "Updated July 25, 2026")

# Focused RU PDF copy: natural language, LLVM context, localized labels and compact evidence.
replace_exact(
    ru,
    '<p class="pcv-summary">Разрабатываю UniversalToolchain/Wist2 — модульную .NET-платформу с несколькими IR, эталонным интерпретатором, backend на CIL/DynamicMethod и проверяемым маршрутом AIR → SSA → AIR. Дополнительная глубина — консервативный анализ программ, C++23 и генерация x86-кода.</p>',
    '<p class="pcv-summary">Разрабатываю UniversalToolchain/Wist2 — модульную .NET compiler/runtime-платформу с несколькими IR, эталонным интерпретатором, backend на CIL/DynamicMethod и проверяемым маршрутом AIR → SSA → AIR. Также работаю с консервативным анализом программ, C++23-компонентами и генерацией x86-кода.</p>',
)
replace_exact(
    ru,
    '<div class="pcv-proofs"><div class="pcv-proof"><strong>AIR → SSA → AIR</strong><span>Оптимизации и структурные верификаторы</span></div><div class="pcv-proof"><strong>1 358 / 1 358 тестов</strong><span>Последний полный прогон; сборка успешна</span></div><div class="pcv-proof"><strong>1-е место из 49</strong><span>PS-form Analyzer, 104/104</span></div></div>',
    '<div class="pcv-proofs"><div class="pcv-proof"><strong>AIR → SSA → AIR</strong><span>Оптимизации и структурные верификаторы</span></div><div class="pcv-proof"><strong>1-е место из 49</strong><span>PS-form Analyzer, 104/104</span></div><div class="pcv-proof"><strong>1 358 / 1 358 тестов</strong><span>IR-преобразования, interpreter/CIL parity и контракты</span></div></div>',
)
replace_exact(ru, "МЦСТ - стажёр по разработке компиляторов</h3>", "МЦСТ - стажёр по разработке компиляторов, LLVM-направление</h3>")
replace_exact(
    ru,
    '<li>Разработал C++23-компоненты анализа графов; использовал CMake, warnings-as-errors, ASan/UBSan, clang-tidy и явные include-зависимости.</li><li>Реализовал RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic поверх общей модели графа; добавил воспроизводимые I/O-тесты.</li>',
    '<li>Разработал общее графовое ядро и C++23-компоненты анализа в рамках LLVM-направления.</li><li>Реализовал RPO с обнаружением циклов, алгоритм Дейкстры, SCC Тарьяна и максимальный поток Диница; использовал CMake, warnings-as-errors, ASan/UBSan, clang-tidy, явные include-зависимости и воспроизводимые I/O-тесты.</li>',
)
replace_exact(ru, '<span>C17 / program analysis</span>', '<span>C17 / анализ программ</span>')
replace_exact(ru, '<strong>Compiler / IR</strong>', '<strong>Компиляторы и IR</strong>')
replace_exact(ru, '<strong>Low-level</strong>', '<strong>Низкоуровневая разработка</strong>')
replace_exact(
    ru,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Образование и доступность</h2><p>Студент НИУ ВШЭ. Москва / удалённо. С сентября 2026: до 20 часов в неделю.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Образование и доступность</h2><p>Студент программы «Программная инженерия» НИУ ВШЭ. Москва / удалённо. С сентября 2026: до 20 часов в неделю.</p></section>',
)
replace_exact(
    ru,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Преподавание</h2><p>Обучил около 50 учеников C/C++, Python и алгоритмам; разработал практический курс по NASM IA-32.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Техническая коммуникация</h2><p>Обучил около 50 учеников; разработал практический курс NASM IA-32, документацию и технические материалы по compiler/runtime.</p></section>',
)
replace_exact(
    ru,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Достижения</h2><p>Призёр «Высшей пробы» по олимпиадному и промышленному программированию; 1-е место по итоговому баллу: «Юниор» 2025 — направление «Инженерные науки», 2026 — секция «Информационные технологии»; диплом I степени и Главная премия Балтийского конкурса.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Достижения</h2><p>Призёр «Высшей пробы» по олимпиадному и промышленному программированию; лучший итоговый балл «Юниора»: инженерные науки (2025) и секция ИТ (2026); Главная премия Балтийского конкурса.</p></section>',
)

# Focused EN PDF parity.
replace_exact(
    en,
    '<p class="pcv-summary">I build UniversalToolchain/Wist2, a modular .NET platform with multiple IRs, a reference interpreter, a CIL/DynamicMethod backend and a verifier-gated AIR → SSA → AIR route. Additional depth includes conservative program analysis, C++23 and x86 code generation.</p>',
    '<p class="pcv-summary">I build UniversalToolchain/Wist2, a modular .NET compiler/runtime platform with multiple IRs, a reference interpreter, a CIL/DynamicMethod backend and a verifier-gated AIR → SSA → AIR route. I also work on conservative program analysis, C++23 components and x86 code generation.</p>',
)
replace_exact(
    en,
    '<div class="pcv-proofs"><div class="pcv-proof"><strong>AIR → SSA → AIR</strong><span>Optimizations and structural verifiers</span></div><div class="pcv-proof"><strong>1,358 / 1,358 tests</strong><span>Latest full run; build succeeded</span></div><div class="pcv-proof"><strong>1st of 49</strong><span>PS-form Analyzer, 104/104</span></div></div>',
    '<div class="pcv-proofs"><div class="pcv-proof"><strong>AIR → SSA → AIR</strong><span>Optimizations and structural verifiers</span></div><div class="pcv-proof"><strong>1st of 49</strong><span>PS-form Analyzer, 104/104</span></div><div class="pcv-proof"><strong>1,358 / 1,358 tests</strong><span>IR transforms, interpreter/CIL parity and contracts</span></div></div>',
)
replace_exact(en, "MCST - compiler engineering intern</h3>", "MCST - compiler engineering intern, LLVM track</h3>")
replace_exact(
    en,
    '<li>C++23 graph-analysis components under CMake, warnings-as-errors, ASan/UBSan, clang-tidy and explicit includes.</li><li>RPO with cycle detection, Dijkstra, Tarjan SCC and Dinic over a shared graph model and reproducible I/O tests.</li>',
    '<li>Developed a shared graph core and C++23 analysis components for the LLVM track.</li><li>Implemented RPO with cycle detection, Dijkstra, Tarjan SCC and Dinic; used CMake, warnings-as-errors, ASan/UBSan, clang-tidy, explicit include dependencies and reproducible I/O tests.</li>',
)
replace_exact(
    en,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Education and availability</h2><p>HSE University student. Moscow / remote. From September 2026: up to 20 hours per week.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Education and availability</h2><p>Software Engineering student at HSE University. Moscow / remote. From September 2026: up to 20 hours per week.</p></section>',
)
replace_exact(
    en,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Teaching</h2><p>Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Technical communication</h2><p>Taught about 50 students; authored a practical NASM IA-32 course, documentation and compiler/runtime technical materials.</p></section>',
)
replace_exact(
    en,
    '<section class="pcv-compact"><h2 class="pcv-section-title">Recognition</h2><p>HSE Olympiad prize-winner in competitive and industrial programming; top total score in MEPhI Junior (2025 Engineering Sciences; 2026 Information Technology); Baltic competition first-degree diploma and Grand Prize.</p></section>',
    '<section class="pcv-compact"><h2 class="pcv-section-title">Recognition</h2><p>HSE Olympiad prize-winner in competitive and industrial programming; top MEPhI Junior score in Engineering Sciences (2025) and the IT section (2026); Baltic competition Grand Prize.</p></section>',
)

# Versioned release documentation.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
text = text.replace("# Mikhail Razakov - targeted CV variants v29", "# Mikhail Razakov - targeted CV variants v30", 1)
v30 = """## Изменения v30

- Compiler RU/EN подтверждают актуальный статус: студент программы «Программная инженерия» НИУ ВШЭ / Software Engineering student at HSE University.
- Исправлен proof strip Wist2: результат 1 358/1 358 привязан к полному прогону 23.07.2026 без переноса старых qualifiers про 14 июля и warnings.
- LLVM-направление возвращено в focused PDF; графовые компоненты связаны с compiler internship, а не выглядят отдельным учебным набором.
- Proof cards упорядочены как инженерная глубина → внешнее подтверждение → качество; тестовый claim объясняет IR transforms, contracts и interpreter/CIL parity.
- Русский Compiler PDF языково вычищен, типографика Wist2 на подробной странице исправлена, преподавание переосмыслено как техническая коммуникация.
- Compiler RU/EN PDF пересобраны и проверены на A4, одну страницу, scale=1.0, читаемость, ATS-порядок, ссылки и отсутствие overflow.

"""
if "## Изменения v29\n" not in text:
    raise RuntimeError("README v29 history missing")
text = text.replace("## Изменения v29\n", v30 + "## Изменения v29\n", 1)
text = text.replace(
    "Предыдущая версия репозитория: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`.",
    "Предыдущая версия репозитория: v29, commit `fae03e5adb4152bd1aaa43e56f49d383dc8f9e6d`.",
    1,
)
readme.write_text(text, encoding="utf-8")

metadata = Path("RELEASE-METADATA.md")
text = metadata.read_text(encoding="utf-8")
text = text.replace("- Version: v29", "- Version: v30", 1)
text = text.replace("- Date: 2026-07-24", "- Date: 2026-07-25", 1)
text = text.replace(
    "- Previous repository baseline: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`",
    "- Previous repository baseline: v29, commit `fae03e5adb4152bd1aaa43e56f49d383dc8f9e6d`",
    1,
)
text = text.replace("- Rebuilt PDFs: compiler RU/EN and C++ systems RU/EN", "- Rebuilt PDFs: compiler RU/EN", 1)
text += """

## v30 compiler boundary

- Education claim is user-confirmed on 2026-07-25: Software Engineering student at HSE University.
- The 1,358/1,358 test result is tied to the full rerun on 2026-07-23; no stale July 14 warnings qualifier is attached to it.
- MCST experience is described as LLVM-track graph-analysis infrastructure, without claiming upstream LLVM integration.
- Compiler RU/EN remain one-page A4 PDFs at scale=1.0 with an extracted font floor of at least 8.45 pt.
"""
metadata.write_text(text, encoding="utf-8")

for old_name, new_name in (
    ("CONTENT-REVIEW-v29.md", "CONTENT-REVIEW-v30.md"),
    ("QA-report-targeted-cv-v29.md", "QA-report-targeted-cv-v30.md"),
):
    old = Path(old_name)
    new = Path(new_name)
    if not old.exists() or new.exists():
        raise RuntimeError(f"Cannot rename {old} -> {new}")
    old.rename(new)

Path("CONTENT-REVIEW-v30.md").write_text(
    """# Content review - v30

## Compiler first-contact hierarchy

1. Wist2 and verifier-gated AIR → SSA → AIR.
2. External program-analysis evidence: PS-form Analyzer, 1st of 49 and 104/104.
3. Correctness evidence: 1,358/1,358 tests covering IR transforms, contracts and interpreter/CIL parity.
4. LLVM-track C++23 graph-analysis infrastructure at MCST.
5. NASM IA-32 and the separate x86-64 code-generation laboratory as low-level depth.

## Factual boundaries

- Education: user-confirmed Software Engineering student at HSE University.
- Wist2 full run: user-reported 1,358/1,358 tests, 0 failures and successful build on 2026-07-23.
- MCST: LLVM-track internship and graph-analysis components; no claim of upstream LLVM integration.
- Assembly: NASM IA-32/CDECL/x87 is distinct from the x86-64 SysV code-generation laboratory.

## Language and density

The Russian focused CV localizes section labels while preserving conventional compiler identifiers. Recognition and teaching are compact supporting evidence; technical work remains dominant.

Verdict: suitable for focused first-contact compiler applications after automated and human render validation.
""",
    encoding="utf-8",
)
Path("QA-report-targeted-cv-v30.md").write_text(
    """# QA report - targeted CV v30

This report is finalized by CI after source mutation, PDF generation and validation.
""",
    encoding="utf-8",
)

for name in ("TARGETING.md", "LANGUAGE-REVIEW.md", "EXPERIENCE-AUDIT.md", "FACT-RETENTION.md", "LINK-AUDIT.md"):
    path = Path(name)
    path.write_text(path.read_text(encoding="utf-8").replace("v29", "v30"), encoding="utf-8")

sitemap = Path("sitemap.xml")
sitemap.write_text(sitemap.read_text(encoding="utf-8").replace("2026-07-24", "2026-07-25"), encoding="utf-8")

# Source-level postconditions before PDF generation.
ru_text = ru.read_text(encoding="utf-8")
en_text = en.read_text(encoding="utf-8")
for stale in (
    "baseline от 14.07.2026",
    "verified baseline dated July 14, 2026",
    "Студент НИУ ВШЭ.",
    "HSE University student.",
    "<strong>Compiler / IR</strong>",
    "<strong>Low-level</strong>",
    "<strong>Конвейер</strong>Лексер",
):
    if stale in ru_text + en_text:
        raise RuntimeError(f"Stale compiler wording remains: {stale}")
for required in (
    "Студент программы «Программная инженерия» НИУ ВШЭ",
    "Software Engineering student at HSE University",
    "LLVM-направление",
    "LLVM track",
    "полный прогон 23.07.2026",
    "full run on July 23, 2026",
    "Техническая коммуникация",
    "Technical communication",
):
    if required not in ru_text + en_text:
        raise RuntimeError(f"Required compiler wording missing: {required}")

print("Compiler CV v30 source hardening applied successfully")
