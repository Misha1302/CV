from __future__ import annotations

from pathlib import Path
import re
from textwrap import dedent

REPO = "https://github.com/Misha1302"
EMAIL = "misha13022008@gmail.com"
TELEGRAM = "https://t.me/Micodiy"


def replace_all(path: Path, old: str, new: str, minimum: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count < minimum:
        raise RuntimeError(f"{path}: expected at least {minimum} occurrence(s) of {old!r}, found {count}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def replace_optional(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")


def regex_replace(path: Path, pattern: str, replacement: str, expected: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=expected, flags=re.DOTALL)
    if count != expected:
        raise RuntimeError(f"{path}: expected {expected} regex replacement(s), found {count}: {pattern[:100]!r}")
    path.write_text(updated, encoding="utf-8")


def print_shell(language: str, kind: str) -> str:
    ru = language == "ru"
    compiler = kind == "compiler"

    if ru and compiler:
        role = "Инженер по компиляторам и средам исполнения"
        summary = (
            "Разрабатываю UniversalToolchain/Wist2 - модульную .NET-платформу с несколькими IR, "
            "эталонным интерпретатором, CIL/DynamicMethod backend и проверяемым маршрутом AIR -> SSA -> AIR. "
            "Дополнительная глубина: консервативный анализ программ, C++23 и x86 code generation."
        )
        proofs = [
            ("AIR -> SSA -> AIR", "Оптимизации и структурные верификаторы"),
            ("1 358 / 1 358 тестов", "Последний полный прогон; сборка успешна"),
            ("1-е место из 49", "PS-form Analyzer, 104/104"),
        ]
        left_title = "Опыт"
        exp = [
            (
                "2024 - сейчас",
                "UniversalToolchain / Wist2 - создатель и основной разработчик",
                [
                    "Спроектировал Source -> AST -> Bytecode -> AIR -> execution, эталонный интерпретатор и CIL/DynamicMethod backend.",
                    "Реализовал opt-in AIR -> SSA -> AIR: constant folding, SCCP-lite, branch folding, unreachable cleanup и DCE.",
                    "Добавил capability contracts, structural verifiers и сравнение interpreter/CIL для поддерживаемой семантики.",
                ],
            ),
            (
                "Июль - август 2026",
                "МЦСТ - стажёр по разработке компиляторов",
                [
                    "C++23-компоненты анализа графов; CMake, warnings-as-errors, ASan/UBSan, clang-tidy и явные include-зависимости.",
                    "RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic поверх общей модели графа и воспроизводимых I/O-тестов.",
                ],
            ),
        ]
        projects_title = "Избранные проекты"
        projects = [
            (
                "PS-form Memory Dependence Analyzer",
                "C17 / program analysis",
                "Консервативный анализ межитерационных зависимостей памяти. 1-е место среди 49 решений, единственные 5,0/5,0 и 104/104; exact oracle, randomized и metamorphic testing.",
                f"{REPO}/ps_form_analizer",
            ),
            (
                "NASM IA-32 и x86-64 codegen",
                "Assembly / backend",
                "NASM IA-32: CDECL, стековые кадры, libc, структуры, адресация и x87. Отдельная x86-64 SysV emitter-лаборатория: liveness, live intervals, linear scan, iced-x86 и interpreter-vs-native validation.",
                f"{REPO}/x86-64-codegen-ra-playground",
            ),
        ]
        skills = [
            ("Compiler / IR", "parsing, AST, Bytecode, AIR, CFG, SSA, CIL/DynamicMethod"),
            ("Анализ и оптимизации", "dominance, liveness, SCCP-lite, DCE, анализ зависимостей памяти"),
            ("Корректность", "structural verifiers, exact oracle, differential и metamorphic testing"),
            ("Low-level", "NASM IA-32, CDECL, stack/x87; x86-64 SysV codegen, objdump/disassembly"),
            ("Языки / инструменты", "C#/.NET, C++23, C17, Python; CMake, GitHub Actions, sanitizers, clang-tidy"),
        ]
        education = "Студент НИУ ВШЭ. Москва / удалённо. С сентября 2026: до 20 часов в неделю."
        teaching = "Обучил около 50 учеников C/C++, Python и алгоритмам; разработал практический курс по NASM IA-32."
        achievements = "Призёр «Высшей пробы» по олимпиадному и промышленному программированию; двукратный абсолютный победитель «Юниора» НИЯУ МИФИ."
        side_titles = ("Ключевые компетенции", "Образование и доступность", "Преподавание", "Достижения")
    elif ru:
        role = "Инженер C++ и анализа программ"
        summary = (
            "Разрабатываю анализаторы и переиспользуемые системные компоненты на C++/C. "
            "Профиль подтверждают PS-form Analyzer, 12 модулей AdvancedAlgorithms, стажировка МЦСТ, "
            "NASM IA-32 и отдельная x86-64 codegen/register-allocation лаборатория."
        )
        proofs = [
            ("1-е место из 49", "PS-form Analyzer, 104/104"),
            ("12 C++23-модулей", "Графы, деревья, строки и структуры данных"),
            ("Strict toolchain", "CMake, -Werror, ASan/UBSan, clang-tidy"),
        ]
        left_title = "Опыт"
        exp = [
            (
                "Июль - август 2026",
                "МЦСТ - стажёр по разработке компиляторов",
                [
                    "Общее ядро ориентированного графа и компоненты RPO/cycle detection, Dijkstra, Tarjan SCC и Dinic.",
                    "C++23/CMake, warnings-as-errors, ASan/UBSan, clang-tidy, явные include-зависимости и I/O-тесты.",
                ],
            ),
            (
                "2024 - сейчас",
                "UniversalToolchain / Wist2 - создатель и основной разработчик",
                [
                    "Несколько IR, interpreter/CIL execution paths и opt-in AIR -> SSA -> AIR.",
                    "Capability contracts, structural verifiers и parity-тесты; последний полный прогон: 1 358/1 358 тестов.",
                ],
            ),
        ]
        projects_title = "Избранные проекты"
        projects = [
            (
                "PS-form Memory Dependence Analyzer",
                "C17 / program analysis",
                "Conservative yes/no/maybe semantics; normalization, range/residue/GCD filters, exact affine analysis, bounded search and exact/randomized/metamorphic verification.",
                f"{REPO}/ps_form_analizer",
            ),
            (
                "AdvancedAlgorithms",
                "C++23 / header-only",
                "12 reusable modules: centroid decomposition, HLD, LCA, Dinic, iterative Tarjan, bridges, Dijkstra, Aho-Corasick, segment tree and others; differential tests, invariants and large inputs.",
                f"{REPO}/AdvancedAlgorithms",
            ),
            (
                "NASM IA-32 и x86-64 codegen",
                "Assembly / backend",
                "CDECL, stack frames, libc, structures/addressing and x87 in NASM IA-32; separate x86-64 SysV emitter with liveness, register allocation, iced-x86 and isolated native execution.",
                f"{REPO}/x86-64-codegen-ra-playground",
            ),
        ]
        skills = [
            ("C++ / C", "C++23, C17, generic components, explicit contracts and error models"),
            ("Алгоритмы", "graphs, trees, strings, data structures, max-flow, SCC, shortest paths"),
            ("Program analysis", "conservative semantics, affine reasoning, exact oracle and counterexamples"),
            ("Low-level", "NASM IA-32, CDECL, stack/x87; x86-64 SysV codegen and disassembly"),
            ("Toolchain", "Linux, CMake, GitHub Actions, ASan/UBSan, clang-tidy, reproducible tests"),
        ]
        education = "Студент НИУ ВШЭ. Москва / удалённо. С сентября 2026: до 20 часов в неделю."
        teaching = "Обучил около 50 учеников C/C++, Python и алгоритмам; разработал практический курс по NASM IA-32."
        achievements = "Призёр «Высшей пробы»; двукратный абсолютный победитель «Юниора» НИЯУ МИФИ; победитель Балтийского конкурса."
        side_titles = ("Ключевые компетенции", "Образование и доступность", "Преподавание", "Достижения")
    elif compiler:
        role = "Compiler and Runtime Engineer"
        summary = (
            "I build UniversalToolchain/Wist2, a modular .NET platform with multiple IRs, a reference interpreter, "
            "a CIL/DynamicMethod backend and a verifier-gated AIR -> SSA -> AIR route. Additional depth includes "
            "conservative program analysis, C++23 and x86 code generation."
        )
        proofs = [
            ("AIR -> SSA -> AIR", "Optimizations and structural verifiers"),
            ("1,358 / 1,358 tests", "Latest full run; build succeeded"),
            ("1st of 49", "PS-form Analyzer, 104/104"),
        ]
        left_title = "Experience"
        exp = [
            (
                "2024 - present",
                "UniversalToolchain / Wist2 - creator and primary developer",
                [
                    "Designed Source -> AST -> Bytecode -> AIR -> execution, a reference interpreter and a CIL/DynamicMethod backend.",
                    "Implemented opt-in AIR -> SSA -> AIR with constant folding, SCCP-lite, branch folding, unreachable cleanup and DCE.",
                    "Added capability contracts, structural verifiers and interpreter/CIL parity checks for supported semantics.",
                ],
            ),
            (
                "Jul - Aug 2026",
                "MCST - compiler engineering intern",
                [
                    "C++23 graph-analysis components under CMake, warnings-as-errors, ASan/UBSan, clang-tidy and explicit includes.",
                    "RPO with cycle detection, Dijkstra, Tarjan SCC and Dinic over a shared graph model and reproducible I/O tests.",
                ],
            ),
        ]
        projects_title = "Selected projects"
        projects = [
            (
                "PS-form Memory Dependence Analyzer",
                "C17 / program analysis",
                "Conservative inter-iteration memory-dependence analysis. Ranked 1st of 49 with the only 5.0/5.0 and 104/104 result; exact oracle plus randomized and metamorphic tests.",
                f"{REPO}/ps_form_analizer",
            ),
            (
                "NASM IA-32 and x86-64 codegen",
                "Assembly / backend",
                "NASM IA-32: cdecl, stack frames, libc, structures/addressing and x87. Separate x86-64 SysV emitter lab: liveness, live intervals, linear scan, iced-x86 and interpreter-vs-native validation.",
                f"{REPO}/x86-64-codegen-ra-playground",
            ),
        ]
        skills = [
            ("Compiler / IR", "parsing, AST, Bytecode, AIR, CFG, SSA, CIL/DynamicMethod"),
            ("Analysis / optimization", "dominance, liveness, SCCP-lite, DCE, memory-dependence analysis"),
            ("Correctness", "structural verifiers, exact oracles, differential and metamorphic testing"),
            ("Low-level", "NASM IA-32, cdecl, stack/x87; x86-64 SysV codegen, objdump/disassembly"),
            ("Languages / tools", "C#/.NET, C++23, C17, Python; CMake, GitHub Actions, sanitizers, clang-tidy"),
        ]
        education = "HSE University student. Moscow / remote. From September 2026: up to 20 hours per week."
        teaching = "Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course."
        achievements = "HSE Olympiad prize-winner in competitive and industrial programming; two-time absolute winner of the MEPhI Junior contest."
        side_titles = ("Core skills", "Education and availability", "Teaching", "Recognition")
    else:
        role = "C++ Systems and Program Analysis Engineer"
        summary = (
            "I build analyzers and reusable systems components in C++/C. Evidence includes the PS-form Analyzer, "
            "12 AdvancedAlgorithms modules, an MCST internship, NASM IA-32 and a separate x86-64 "
            "codegen/register-allocation laboratory."
        )
        proofs = [
            ("1st of 49", "PS-form Analyzer, 104/104"),
            ("12 C++23 modules", "Graphs, trees, strings and data structures"),
            ("Strict toolchain", "CMake, -Werror, ASan/UBSan, clang-tidy"),
        ]
        left_title = "Experience"
        exp = [
            (
                "Jul - Aug 2026",
                "MCST - compiler engineering intern",
                [
                    "Shared directed-graph core and RPO/cycle detection, Dijkstra, Tarjan SCC and Dinic components.",
                    "C++23/CMake, warnings-as-errors, ASan/UBSan, clang-tidy, explicit includes and I/O tests.",
                ],
            ),
            (
                "2024 - present",
                "UniversalToolchain / Wist2 - creator and primary developer",
                [
                    "Multiple IRs, interpreter/CIL execution paths and an opt-in AIR -> SSA -> AIR route.",
                    "Capability contracts, structural verifiers and parity tests; latest full run: 1,358/1,358 tests.",
                ],
            ),
        ]
        projects_title = "Selected projects"
        projects = [
            (
                "PS-form Memory Dependence Analyzer",
                "C17 / program analysis",
                "Conservative yes/no/maybe semantics; normalization, range/residue/GCD filters, exact affine analysis, bounded search and exact/randomized/metamorphic verification.",
                f"{REPO}/ps_form_analizer",
            ),
            (
                "AdvancedAlgorithms",
                "C++23 / header-only",
                "12 reusable modules covering graphs, trees, strings and data structures; differential tests, structural invariants, sanitizers and large inputs.",
                f"{REPO}/AdvancedAlgorithms",
            ),
            (
                "NASM IA-32 and x86-64 codegen",
                "Assembly / backend",
                "cdecl, stack frames, libc, structures/addressing and x87 in NASM IA-32; separate x86-64 SysV emitter with liveness, register allocation, iced-x86 and isolated native execution.",
                f"{REPO}/x86-64-codegen-ra-playground",
            ),
        ]
        skills = [
            ("C++ / C", "C++23, C17, reusable components, explicit contracts and error models"),
            ("Algorithms", "graphs, trees, strings, data structures, max-flow, SCC and shortest paths"),
            ("Program analysis", "conservative semantics, affine reasoning, exact oracles and counterexamples"),
            ("Low-level", "NASM IA-32, cdecl, stack/x87; x86-64 SysV codegen and disassembly"),
            ("Toolchain", "Linux, CMake, GitHub Actions, ASan/UBSan, clang-tidy and reproducible tests"),
        ]
        education = "HSE University student. Moscow / remote. From September 2026: up to 20 hours per week."
        teaching = "Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course."
        achievements = "HSE Olympiad prize-winner; two-time absolute winner of the MEPhI Junior contest; Baltic Science and Engineering Competition winner."
        side_titles = ("Core skills", "Education and availability", "Teaching", "Recognition")

    def proof_html() -> str:
        return "".join(f'<div class="pcv-proof"><strong>{a}</strong><span>{b}</span></div>' for a, b in proofs)

    def exp_html() -> str:
        out = []
        for period, title, bullets in exp:
            out.append(
                f'<article class="pcv-entry"><div class="pcv-date">{period}</div><div><h3>{title}</h3>'
                f'<ul>{"".join(f"<li>{item}</li>" for item in bullets)}</ul></div></article>'
            )
        return "".join(out)

    def projects_html() -> str:
        return "".join(
            f'<article class="pcv-project"><div class="pcv-project-head"><h3><a href="{url}">{name}</a></h3>'
            f'<span>{tag}</span></div><p>{text}</p></article>'
            for name, tag, text, url in projects
        )

    def skills_html() -> str:
        return "".join(f'<div class="pcv-skill"><strong>{name}</strong><span>{text}</span></div>' for name, text in skills)

    github_url = f"{REPO}"
    return dedent(
        f"""
        <section class="print-cv" aria-label="Printable CV">
          <header class="pcv-header">
            <div>
              <h1>Михаил Разаков</h1>
              <h2>{role}</h2>
            </div>
            <div class="pcv-contact">
              <a href="mailto:{EMAIL}">{EMAIL}</a><br/>
              <a href="{TELEGRAM}">t.me/Micodiy</a> · <a href="{github_url}">github.com/Misha1302</a>
            </div>
          </header>
          <p class="pcv-summary">{summary}</p>
          <div class="pcv-proofs">{proof_html()}</div>
          <div class="pcv-columns">
            <main class="pcv-main">
              <section><h2 class="pcv-section-title">{left_title}</h2>{exp_html()}</section>
              <section><h2 class="pcv-section-title">{projects_title}</h2>{projects_html()}</section>
            </main>
            <aside class="pcv-side">
              <section><h2 class="pcv-section-title">{side_titles[0]}</h2>{skills_html()}</section>
              <section class="pcv-compact"><h2 class="pcv-section-title">{side_titles[1]}</h2><p>{education}</p></section>
              <section class="pcv-compact"><h2 class="pcv-section-title">{side_titles[2]}</h2><p>{teaching}</p></section>
              <section class="pcv-compact"><h2 class="pcv-section-title">{side_titles[3]}</h2><p>{achievements}</p></section>
            </aside>
          </div>
        </section>
        """
    ).strip()


# 1. Package-wide version, dates and current Wist2 run.
for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    text = text.replace('style.css?v=25', 'style.css?v=27').replace('script.js?v=25', 'script.js?v=27')
    text = text.replace('Обновлено 23 июля 2026', 'Обновлено 24 июля 2026')
    text = text.replace('Updated July 23, 2026', 'Updated July 24, 2026')
    text = text.replace('1 325 тестов · 75 .NET-проектов', '1 358 / 1 358 тестов')
    text = text.replace('1,325 tests · 75 .NET projects', '1,358 / 1,358 tests')
    text = text.replace(
        'Проверенный baseline от 14.07.2026: 75 .NET-проектов, 1 325 тестов, 0 предупреждений и 0 ошибок.',
        'Последний полный прогон: 1 358 тестов пройдены, 0 сбоев; сборка успешна.'
    )
    text = text.replace(
        'Verified baseline dated 2026-07-14: 75 .NET projects, 1,325 tests, 0 warnings and 0 errors.',
        'Latest full run: 1,358 tests passed, 0 failed; build succeeded.'
    )
    path.write_text(text, encoding='utf-8')

# 2. Tighten Assembly claims and restore compiler hierarchy.
for name in ('ru-compiler.html', 'ru-cpp-systems.html', 'ru.html'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    replacements = {
        'NASM/FASM': 'NASM IA-32',
        'NASM / Rust · IA-32 / x86-64': 'NASM IA-32 / Rust x86-64',
        'x86 / x86-64 Assembly': 'NASM IA-32 / x86-64 codegen',
        'System V AMD64 ABI': 'x86-64 SysV code generation',
        'GDB/objdump': 'objdump',
        'метрики spills/code size и изолированный запуск': 'differential testing и изолированный запуск',
        'Обучил около 50 учеников C/C++, Python, NASM и алгоритмам; провожу ревью кода и объясняю модели выполнения.':
            'Обучил около 50 учеников C/C++, Python и алгоритмам; разработал практический курс по NASM IA-32 и провожу ревью кода.',
        'Обучил около 50 учеников; провожу диагностику знаний, объясняю модели выполнения и ревьюю код.':
            'Обучил около 50 учеников C/C++, Python и алгоритмам; разработал практический курс по NASM IA-32 и провожу ревью кода.',
        'Compiler/runtime, program analysis и low-level backend experiments.': 'Компиляторы, анализ программ и эксперименты с codegen.',
        'Анализ программ, C++ components и low-level backend experiments.': 'Анализ программ, C++-компоненты и эксперименты с codegen.',
        'C++ · анализ программ · compiler infrastructure': 'C++ · анализ программ · инфраструктура компиляторов',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

for name in ('en-compiler.html', 'en-cpp-systems.html', 'en.html'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    replacements = {
        'NASM/FASM': 'NASM IA-32',
        'NASM / Rust · IA-32 / x86-64': 'NASM IA-32 / Rust x86-64',
        'x86 / x86-64 Assembly': 'NASM IA-32 / x86-64 codegen',
        'System V AMD64 ABI': 'x86-64 SysV code generation',
        'GDB/objdump': 'objdump',
        'spill/code-size metrics and isolated execution': 'differential testing and isolated execution',
        'Taught about 50 students in C/C++, Python, NASM, and algorithms; I review code and explain execution models.':
            'Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course and review code.',
        'Taught about 50 students; I diagnose knowledge gaps, explain execution models, and review code.':
            'Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course and review code.',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

# Compiler page: Assembly is evidence, not the primary headline.
for path_name in ('ru-compiler.html', 'en-compiler.html'):
    path = Path(path_name)
    text = path.read_text(encoding='utf-8')
    text = text.replace('.NET · IR/SSA · compiler optimizations · x86 Assembly', '.NET · IR/SSA · compiler optimizations · program analysis')
    text = text.replace('IR/SSA · optimizations · NASM/x86 · ABI', 'IR/SSA · verifiers · optimizations · x86 codegen')
    text = re.sub(
        r'<div class="career-item"><strong>NASM IA-32 / x86-64 codegen</strong><span>.*?</span></div>',
        '<div class="career-item"><strong>Program analysis &amp; correctness</strong><span>exact oracles · structural verifiers · backend parity</span></div>',
        text,
        count=1,
    )
    path.write_text(text, encoding='utf-8')

# More precise metadata and summaries.
replace_optional(
    Path('ru-cpp-systems.html'),
    'Резюме Михаила Разакова: C++23, C17, анализ программ, NASM IA-32, x86/x86-64 Assembly, ABI и backend experiments.',
    'Резюме Михаила Разакова: C++23, C17, анализ программ, NASM IA-32, x86-64 codegen, Linux и строгий toolchain.'
)
replace_optional(
    Path('en-cpp-systems.html'),
    'Mikhail Razakov CV: C++23, C17, program analysis, NASM IA-32, x86/x86-64 Assembly, ABI and backend experiments.',
    'Mikhail Razakov CV: C++23, C17, program analysis, NASM IA-32, x86-64 codegen, Linux and a strict toolchain.'
)

# 3. Inject dedicated one-page print CVs.
for filename, language, kind in (
    ('ru-compiler.html', 'ru', 'compiler'),
    ('en-compiler.html', 'en', 'compiler'),
    ('ru-cpp-systems.html', 'ru', 'cpp'),
    ('en-cpp-systems.html', 'en', 'cpp'),
):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'\s*<section class="print-cv".*?</section>\s*</body>', '</body>', text, flags=re.DOTALL)
    text = text.replace('</body>', print_shell(language, kind) + '\n</body>', 1)
    path.write_text(text, encoding='utf-8')

# 4. Print-only layout. No scaling below 100% is allowed.
style = Path('style.css')
css = style.read_text(encoding='utf-8')
marker = '/* v27: dedicated readable A4 CV layout */'
if marker in css:
    css = css[:css.index(marker)].rstrip() + '\n'
css += dedent(r'''

/* v27: dedicated readable A4 CV layout */
.print-cv { display: none; }
@media print {
  @page { size: A4; margin: 0; }
  html, body { width: 210mm; height: 297mm; margin: 0 !important; padding: 0 !important; background: #fff !important; }
  body::before { display: none !important; }
  body > :not(.print-cv) { display: none !important; }
  .print-cv {
    display: block !important;
    width: 210mm;
    height: 297mm;
    overflow: hidden;
    padding: 9mm 10mm 8mm;
    box-sizing: border-box;
    background: #fff;
    color: #171717;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 9pt;
    line-height: 1.27;
  }
  .print-cv *, .print-cv *::before, .print-cv *::after { box-sizing: border-box; }
  .print-cv a { color: inherit; text-decoration: none; }
  .pcv-header { display: flex; justify-content: space-between; align-items: flex-start; gap: 8mm; padding-bottom: 3mm; border-bottom: 1.3pt solid #852737; }
  .pcv-header h1 { margin: 0; font-size: 23pt; line-height: 1; letter-spacing: -.5pt; }
  .pcv-header h2 { margin: 1.5mm 0 0; font-size: 11.5pt; line-height: 1.15; font-weight: 600; color: #852737; }
  .pcv-contact { flex: 0 0 61mm; text-align: right; font-size: 8.4pt; line-height: 1.38; overflow-wrap: anywhere; }
  .pcv-summary { margin: 3mm 0 2.7mm; font-size: 9.2pt; line-height: 1.32; }
  .pcv-proofs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2mm; margin-bottom: 3.2mm; }
  .pcv-proof { min-height: 16mm; padding: 2.4mm 2.7mm; border: .65pt solid #cfcfcf; border-radius: 1.5mm; }
  .pcv-proof strong { display: block; font-size: 10.2pt; line-height: 1.12; color: #852737; }
  .pcv-proof span { display: block; margin-top: 1mm; font-size: 7.8pt; line-height: 1.2; color: #444; }
  .pcv-columns { display: grid; grid-template-columns: minmax(0, 1.67fr) minmax(0, 1fr); gap: 5mm; }
  .pcv-main, .pcv-side { min-width: 0; }
  .pcv-main section + section, .pcv-side section + section { margin-top: 3mm; }
  .pcv-section-title { margin: 0 0 1.7mm; padding-bottom: .8mm; border-bottom: .8pt solid #b78c95; color: #852737; font-size: 10.5pt; line-height: 1.15; text-transform: uppercase; letter-spacing: .35pt; }
  .pcv-entry { display: grid; grid-template-columns: 26mm minmax(0, 1fr); gap: 2.5mm; padding: 1.5mm 0 2mm; border-bottom: .45pt solid #dedede; break-inside: avoid; }
  .pcv-date { padding-top: .3mm; font-size: 7.5pt; font-weight: 700; color: #666; text-transform: uppercase; }
  .pcv-entry h3, .pcv-project h3 { margin: 0; font-size: 9.2pt; line-height: 1.18; }
  .pcv-entry ul { margin: 1mm 0 0; padding-left: 3.6mm; }
  .pcv-entry li { margin: 0 0 .75mm; font-size: 8.25pt; line-height: 1.23; }
  .pcv-project { padding: 1.5mm 0 1.7mm; border-bottom: .45pt solid #dedede; break-inside: avoid; }
  .pcv-project-head { display: flex; justify-content: space-between; gap: 2mm; align-items: baseline; }
  .pcv-project-head span { flex: 0 0 auto; font-size: 7.2pt; color: #777; text-transform: uppercase; }
  .pcv-project p { margin: .8mm 0 0; font-size: 8.15pt; line-height: 1.24; }
  .pcv-skill { padding: 1.25mm 0; border-bottom: .45pt solid #dedede; }
  .pcv-skill strong { display: block; font-size: 8.3pt; line-height: 1.15; }
  .pcv-skill span { display: block; margin-top: .55mm; font-size: 7.75pt; line-height: 1.22; color: #444; }
  .pcv-compact p { margin: 0; font-size: 8pt; line-height: 1.27; }
}
''')
style.write_text(css, encoding='utf-8')

# 5. Selector page and package documentation.
index = Path('index.html')
text = index.read_text(encoding='utf-8')
text = text.replace('AdvancedAlgorithms на C++23, C17-анализатор зависимостей памяти, Wist2/SSA, sanitizers и low-level codegen lab.',
                    'PS-form Analyzer, AdvancedAlgorithms на C++23, строгий toolchain, NASM IA-32 и x86-64 codegen lab.')
text = text.replace('Обновлено 23 июля 2026', 'Обновлено 24 июля 2026')
index.write_text(text, encoding='utf-8')

Path('README.md').write_text(dedent('''
# Mikhail Razakov - targeted CV variants v27

Статический bilingual-пакет целевых инженерных резюме и подробного технического портфолио.

## Флагманские версии

- `ru-compiler.html` / `en-compiler.html` - compiler/runtime, IR/SSA, оптимизации и program analysis.
- `ru-cpp-systems.html` / `en-cpp-systems.html` - C++ systems, program analysis, алгоритмические компоненты и low-level codegen.
- `ru-devtools.html` / `en-devtools.html` - compiler testing, diagnostics, generative testing и release tooling.
- `ru-algorithms.html` / `en-algorithms.html` - алгоритмическая инженерия: AdvancedAlgorithms, PS-form Analyzer и оптимизации Wist2.

## Дополнительные версии

- `ru-backend.html` / `en-backend.html` - .NET backend.
- `ru-platform.html` / `en-platform.html` - service reliability и эксплуатация.
- `ru-edtech.html` / `en-edtech.html` - EdTech backend.
- `ru.html` / `en.html` - полное техническое портфолио для технического follow-up, не замена целевому PDF.

## Изменения v27

- Четыре флагманских PDF получили отдельный print-only A4-макет; полный сайт больше не уменьшается до нечитаемого масштаба.
- PDF экспортируются строго при scale=1.0; сборка падает при переполнении, шрифте меньше 7.5 pt, второй странице или пропавшем текстовом маркере.
- Assembly scope уточнён: NASM IA-32/CDECL/x87 отделён от x86-64 SysV code generation через iced-x86; неподтверждённые FASM и обобщённый full-ABI claim удалены.
- В compiler-профиле восстановлена иерархия Wist2 -> program analysis -> x86 codegen; Assembly остаётся сильным доказательством, но не заменяет основной профиль.
- Преподавательская формулировка больше не создаёт впечатление, что все около 50 учеников изучали NASM.
- Wist2 baseline обновлён до пользовательского полного прогона: 1 358 тестов пройдены, 0 сбоев, сборка успешна.
- README, release metadata, QA, targeting, language/content/fact/link/experience audits синхронизированы как v27.

## Контакт

misha13022008@gmail.com

## Baseline

Предыдущая версия репозитория: v26, commit `6a67ea16513f08772a17c3aee19c0135d437cc2b`.

## Публикация

Для первого контакта отправлять профильный PDF. HTML-страницы остаются подробным публичным портфолио.
''').lstrip(), encoding='utf-8')

Path('RELEASE-METADATA.md').write_text(dedent('''
# Release metadata

- Version: v27
- Date: 2026-07-24
- Previous repository baseline: v26, commit `6a67ea16513f08772a17c3aee19c0135d437cc2b`
- HTML surface: 17 files
- Downloadable CV surface: 14 one-page A4 PDFs
- Rebuilt PDFs: compiler RU/EN and C++ systems RU/EN
- Canonical email: `misha13022008@gmail.com`

## Evidence boundaries

- NASM evidence: IA-32 course and buildable examples covering CDECL, stack frames, libc calls, structures/addressing and x87.
- x86-64 evidence: educational Rust backend lab with liveness, register allocation, SysV emitter through iced-x86, disassembly and interpreter-vs-native validation.
- No FASM proficiency claim and no blanket full System V AMD64 ABI implementation claim.
- Wist2 test count 1,358/1,358 and successful build come from the user-reported full rerun on 2026-07-23; the former 75-project/1,325-test public baseline is superseded for CV wording.
- Wist2 AIR -> SSA -> AIR remains experimental and verifier-gated.
- x86-64 runner remains constrained but is not presented as a hardened sandbox.

## Publication boundary

Role PDFs contain email, Telegram and GitHub. The full HTML portfolio may include LinkedIn and additional evidence links.
''').lstrip(), encoding='utf-8')

Path('TARGETING.md').write_text(dedent('''
# Targeting guide - v27

## Compiler / Runtime / Program Analysis

Send `ru-compiler.html` / `en-compiler.html` or the corresponding PDF to compiler, runtime, VM, static-analysis and language-engineering teams.

Evidence hierarchy:
1. UniversalToolchain/Wist2 - multi-IR runtime pipeline, verifier-gated AIR -> SSA -> AIR, optimization passes and interpreter/CIL parity.
2. PS-form Analyzer - conservative program analysis, exact oracle and 1/49, 104/104 result.
3. NASM IA-32 plus x86-64 codegen lab - machine-level understanding, liveness, register allocation and native validation.
4. AdvancedAlgorithms - additional C++23 foundation.

Assembly must remain supporting evidence in this version, not the primary headline.

## C++ Systems / Program Analysis

Send `ru-cpp-systems.html` / `en-cpp-systems.html` to C++ systems internships, algorithm libraries, compiler infrastructure, program analysis and verification tooling.
Primary evidence: PS-form Analyzer, AdvancedAlgorithms, MCST internship, x86 codegen lab and Wist2 IR/SSA.

## Algorithms / Compiler Tools / Backend

- algorithms: `ru/en-algorithms.html`;
- compiler testing/tooling: `ru/en-devtools.html`;
- backend/reliability/EdTech: corresponding focused variants.

## Full portfolio

Use `ru.html` / `en.html` after first contact or as a technical-lead follow-up. Do not attach it instead of a focused PDF.

## Do not claim without new evidence

- FASM proficiency;
- complete System V AMD64 ABI support;
- HFT/quant experience;
- production-ready sandbox or formal verification;
- performance multipliers without a fresh reproducible benchmark.
''').lstrip(), encoding='utf-8')

Path('LANGUAGE-REVIEW.md').write_text(dedent('''
# Language review - v27

- Russian role headings prefer natural Russian phrasing; IR, SSA, backend, runtime, codegen, SCCP and DCE remain where they are standard role vocabulary.
- Compiler RU no longer promotes Assembly in the eyebrow or top proof hierarchy.
- `NASM IA-32` and `x86-64 codegen` are separate claims; `NASM/FASM`, broad `x86/x86-64 Assembly` and blanket ABI wording are absent.
- Teaching states about 50 students in C/C++, Python and algorithms, plus authorship of a NASM IA-32 course.
- English pages contain no unintended Cyrillic except the expected language-switch accessibility label.

Verdict: PASS after PDF visual validation.
''').lstrip(), encoding='utf-8')

Path('EXPERIENCE-AUDIT.md').write_text(dedent('''
# Experience audit - v27

## Confirmed differentiators

- Wist2: multiple IRs, reference interpreter, CIL/DynamicMethod backend, verifier-gated AIR -> SSA -> AIR and optimization passes.
- PS-form Analyzer: 1st of 49, only 5.0/5.0 and 104/104; conservative semantics and exact/randomized/metamorphic verification.
- AdvancedAlgorithms: 12 C++23 modules with contracts, differential tests, structural invariants, sanitizers and large inputs.
- MCST internship: C++23, shared graph model, RPO/cycle detection, Dijkstra, Tarjan SCC, Dinic, CMake and strict tooling.
- NASM IA-32 course/examples: CDECL, stack frames, libc, structures/addressing and x87.
- x86-64 educational lab: liveness, linear scan/simulated annealing allocation, iced-x86 emitter, disassembly and isolated interpreter-vs-native validation.

## Boundaries

- Do not conflate the IA-32 course with hand-written x86-64 application code.
- Do not present the emitter as complete ABI/call support; calls and callee-saved allocation remain outside its documented scope.
- MCST remains experience, not a duplicate algorithm project card.

Verdict: GO when the generated focused PDF passes scale, font, overflow, text-order and visual checks.
''').lstrip(), encoding='utf-8')

Path('FACT-RETENTION.md').write_text(dedent('''
# Fact retention - v27

| Fact | Evidence boundary |
|---|---|
| Wist2 has an experimental verifier-gated AIR -> SSA -> AIR route | current architecture/repository evidence |
| Latest full rerun: 1,358 tests passed, 0 failed; build succeeded | user-reported run, 2026-07-23 |
| PS-form Analyzer ranked 1/49 with the only 5.0/5.0 and 104/104 | public project/result evidence |
| AdvancedAlgorithms contains 12 C++23 modules with differential/invariant/sanitizer/large-input checks | checked public repository |
| NASM course is IA-32 only and covers CDECL, stack, libc, structures/addressing and x87 | checked public course README/examples |
| x86-64 lab implements a SysV emitter via iced-x86, liveness, allocation and interpreter-vs-native validation | checked public lab README |
| x86-64 lab does not yet implement calls or callee-saved register allocation | checked public lab limitations |
| MCST uses C++23, CMake, warnings-as-errors, sanitizers, clang-tidy and reproducible I/O tests | checked internship repository/context |

Implemented, experimental, user-reported and unsupported claims remain explicitly separated.
''').lstrip(), encoding='utf-8')

Path('LINK-AUDIT.md').write_text(dedent('''
# Link audit - v27

- 17 HTML files and 17 sitemap entries are retained.
- All local HTML/PDF/paper/stylesheet/script/asset paths are checked by CI.
- Fragment links and duplicate IDs are checked.
- Every `target="_blank"` link must include `noopener noreferrer`.
- Compiler and C++ systems pages/PDFs include links to PS-form, AdvancedAlgorithms where relevant, Nasm-X86-Course and x86-64 codegen lab.
- PDF links are validated as clickable annotations after export.

Verdict: PASS only together with the v27 CI report.
''').lstrip(), encoding='utf-8')

Path('CONTENT-REVIEW-v27.md').write_text(dedent('''
# Content review - v27

## Primary correction

The web pages remain detailed portfolios. Four focused PDFs now use dedicated concise print markup instead of shrinking the full web page.

## Compiler hierarchy

1. Wist2 and IR/runtime architecture.
2. Program analysis and correctness evidence.
3. x86 codegen and NASM IA-32 as low-level depth.
4. AdvancedAlgorithms as supporting C++ evidence.

## Assembly wording

- Confirmed: NASM IA-32, CDECL, stack frames, libc, structures/addressing and x87.
- Confirmed separately: x86-64 SysV code generation via iced-x86, liveness, register allocation, disassembly and native validation.
- Removed: FASM proficiency, broad hand-written x86-64 implication and complete ABI support.

## Density control

The PDF keeps one summary, one proof strip, two experience entries, two or three selected projects, compact skills, education/availability, teaching and recognition. Repeated full project descriptions and duplicate proof layers remain on the web page only.

Verdict: content structure suitable for focused first-contact PDFs.
''').lstrip(), encoding='utf-8')

Path('QA-report-targeted-cv-v27.md').write_text(dedent('''
# QA report - targeted CV v27

This report is finalized by CI after generation.

Required checks:
- all 17 HTML files parse;
- all local links/fragments resolve and IDs are unique;
- four focused print layouts have no DOM overflow at print media;
- four rebuilt PDFs are exactly one A4 page at scale=1.0;
- minimum extracted span font size is at least 7.5 pt, body text markers remain present and links are clickable;
- rendered PNGs show no clipping, overlap, broken glyphs or unreadably small columns;
- all 14 role PDFs remain one page;
- stale v25 review files are removed;
- recursive `MANIFEST.sha256` verifies after clean checkout.

Verdict is assigned only after workflow completion and human render review.
''').lstrip(), encoding='utf-8')

for stale in ('CONTENT-REVIEW-v25.md', 'QA-report-targeted-cv-v25.md'):
    Path(stale).unlink(missing_ok=True)

# 6. Static assertions before export.
for page in ('ru-compiler.html', 'en-compiler.html', 'ru-cpp-systems.html', 'en-cpp-systems.html'):
    text = Path(page).read_text(encoding='utf-8')
    if text.count('class="print-cv"') != 1:
        raise RuntimeError(f"{page}: expected exactly one print CV")
    for forbidden in ('NASM/FASM', 'System V AMD64 ABI', 'GDB/objdump'):
        if forbidden in text:
            raise RuntimeError(f"{page}: forbidden overclaim remains: {forbidden}")
    for required in ('NASM IA-32', 'x86-64', '1 358' if page.startswith('ru') else '1,358'):
        if required not in text:
            raise RuntimeError(f"{page}: missing required marker: {required}")

print('Prepared v27 content, dedicated print CVs and synchronized release documents')
