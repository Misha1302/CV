from __future__ import annotations

from pathlib import Path
import re
from textwrap import dedent

COURSE = "https://github.com/Misha1302/Nasm-X86-Course"
CODEGEN = "https://github.com/Misha1302/x86-64-codegen-ra-playground"


def literal(path: str, old: str, new: str, expected: int = 1) -> None:
    file = Path(path)
    text = file.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise RuntimeError(f"{path}: expected {expected}, found {count}: {old[:100]!r}")
    file.write_text(text.replace(old, new), encoding="utf-8")


def regex(path: str, pattern: str, replacement: str, expected: int = 1) -> None:
    file = Path(path)
    text = file.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=expected, flags=re.DOTALL)
    if count != expected:
        raise RuntimeError(f"{path}: expected {expected} regex replacement(s), found {count}: {pattern[:100]!r}")
    file.write_text(updated, encoding="utf-8")


RU_CARD = (
    '<article class="project-card"><span class="project-type">Assembly и backend · NASM / Rust · IA-32 / x86-64</span>'
    '<h3>x86 Assembly, Codegen &amp; Register Allocation</h3>'
    '<p>Ручной NASM-код для IA-32 и backend-лаборатория генерации x86-64: от ABI и стека до liveness, register allocation и проверки нативного кода.</p>'
    '<ul class="project-detail-list">'
    '<li>NASM IA-32: cdecl, стековые кадры, вызовы libc, структуры и адресация, x87; собираемые примеры и практический учебный курс.</li>'
    '<li>x86-64: SSA-подобная IR, live intervals, граф интерференции, linear scan и lowering/emission через iced-x86.</li>'
    '<li>Дизассемблирование и анализ compiler output; differential testing, метрики spills/code size и изолированный запуск.</li>'
    '</ul><div class="project-links">'
    f'<a href="{CODEGEN}" rel="noopener noreferrer" target="_blank">Codegen lab ↗</a>'
    f'<a href="{COURSE}" rel="noopener noreferrer" target="_blank">NASM course ↗</a>'
    '</div><ul class="inline-meta"><li>NASM/FASM</li><li>IA-32 / x86-64</li><li>ABI / x87</li></ul></article>'
)
EN_CARD = (
    '<article class="project-card"><span class="project-type">Assembly and backend · NASM / Rust · IA-32 / x86-64</span>'
    '<h3>x86 Assembly, Codegen &amp; Register Allocation</h3>'
    '<p>Hand-written NASM for IA-32 and an x86-64 code-generation lab, spanning ABI and stack mechanics through liveness, register allocation and native-code validation.</p>'
    '<ul class="project-detail-list">'
    '<li>NASM IA-32: cdecl, stack frames, libc calls, structures and addressing, x87; buildable examples and a practical course.</li>'
    '<li>x86-64: SSA-like IR, live intervals, interference graph, linear scan and lowering/emission through iced-x86.</li>'
    '<li>Disassembly and compiler-output analysis; differential tests, spill/code-size metrics and isolated execution.</li>'
    '</ul><div class="project-links">'
    f'<a href="{CODEGEN}" rel="noopener noreferrer" target="_blank">Codegen lab ↗</a>'
    f'<a href="{COURSE}" rel="noopener noreferrer" target="_blank">NASM course ↗</a>'
    '</div><ul class="inline-meta"><li>NASM/FASM</li><li>IA-32 / x86-64</li><li>ABI / x87</li></ul></article>'
)
CARD_PATTERN = (
    r'<article class="project-card"><span class="project-type">[^<]*(?:x86-64|backend/codegen)[^<]*</span>'
    r'<h3>(?:x86-64 )?Codegen &amp; Register Allocation Playground</h3>.*?</article>'
)

# Compiler variants.
literal("ru-compiler.html",
        "Резюме Михаила Разакова: Wist2, IR/SSA, compiler optimizations, structural verification, program analysis и C++23.",
        "Резюме Михаила Разакова: Wist2, IR/SSA, оптимизации, анализ программ, NASM/x86 Assembly, ABI и C++23.", 3)
literal("en-compiler.html",
        "Mikhail Razakov CV: Wist2, IR/SSA, compiler optimizations, structural verification, program analysis and C++23.",
        "Mikhail Razakov CV: Wist2, IR/SSA, compiler optimizations, program analysis, NASM/x86 Assembly, ABI and C++23.", 3)
for path, old_eye, new_eye, old_id, new_id, old_career, new_career, old_org, new_org in (
    ("ru-compiler.html",
     ".NET · IR/SSA · compiler optimizations · program analysis",
     ".NET · IR/SSA · compiler optimizations · x86 Assembly",
     "IR/SSA · verifiers · optimizations · parity",
     "IR/SSA · optimizations · NASM/x86 · ABI",
     '<div class="career-item"><strong>C/C++ program analysis</strong><span>PS-form analyzer и инженерная стажировка</span></div>',
     '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · compiler output</span></div>',
     '<p class="org">C/C++ · C# · Python · алгоритмы</p>',
     '<p class="org">C/C++ · C# · Python · NASM · алгоритмы</p>'),
    ("en-compiler.html",
     ".NET · IR/SSA · compiler optimizations · program analysis",
     ".NET · IR/SSA · compiler optimizations · x86 Assembly",
     "IR/SSA · verifiers · optimizations · parity",
     "IR/SSA · optimizations · NASM/x86 · ABI",
     '<div class="career-item"><strong>C/C++ program analysis</strong><span>PS-form analyzer and engineering internship</span></div>',
     '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · compiler output</span></div>',
     '<p class="org">C/C++ · C# · Python · algorithms</p>',
     '<p class="org">C/C++ · C# · Python · NASM · algorithms</p>'),
):
    literal(path, old_eye, new_eye)
    literal(path, old_id, new_id)
    literal(path, old_career, new_career)
    literal(path, old_org, new_org)

regex("ru-compiler.html", CARD_PATTERN, RU_CARD)
regex("en-compiler.html", CARD_PATTERN, EN_CARD)
literal(
    "ru-compiler.html",
    '<div class="stack-line"><strong>Языки и инструменты</strong><p>C#/.NET, C++23, C17 и Python; CMake, GitHub Actions, ASan/UBSan и clang-tidy.</p></div>',
    '<div class="stack-line"><strong>Ассемблер и ABI</strong><p>NASM/FASM, IA-32 и x86-64; cdecl и System V AMD64 ABI; стековые кадры, вызовы libc, структуры и адресация, x87; GDB/objdump и анализ дизассемблирования.</p></div>'
    '<div class="stack-line"><strong>Языки и инструменты</strong><p>C#/.NET, C++23, C17 и Python; CMake, GitHub Actions, ASan/UBSan и clang-tidy.</p></div>',
)
literal(
    "en-compiler.html",
    '<div class="stack-line"><strong>Languages and toolchain</strong><p>C#/.NET, C++23, C17 and Python; CMake, GitHub Actions, ASan/UBSan and clang-tidy.</p></div>',
    '<div class="stack-line"><strong>Assembly and ABI</strong><p>NASM/FASM, IA-32 and x86-64; cdecl and System V AMD64 ABI; stack frames, libc interop, structures and addressing, x87; GDB/objdump and disassembly analysis.</p></div>'
    '<div class="stack-line"><strong>Languages and toolchain</strong><p>C#/.NET, C++23, C17 and Python; CMake, GitHub Actions, ASan/UBSan and clang-tidy.</p></div>',
)

# C++ systems variants.
literal("ru-cpp-systems.html",
        "Резюме Михаила Разакова: C++23, C17, PS-form Analyzer, AdvancedAlgorithms, IR/SSA и x86-64 backend experiments.",
        "Резюме Михаила Разакова: C++23, C17, анализ программ, NASM/FASM, x86/x86-64 Assembly, ABI и backend experiments.", 2)
literal("en-cpp-systems.html",
        "Mikhail Razakov CV: C++23, C17, PS-form Analyzer, AdvancedAlgorithms, IR/SSA and x86-64 backend experiments.",
        "Mikhail Razakov CV: C++23, C17, program analysis, NASM/FASM, x86/x86-64 Assembly, ABI and backend experiments.", 2)
for path, changes in {
    "ru-cpp-systems.html": (
        ("C++23 · C17 · Python · Linux · анализ программ", "C++23 · C17 · NASM/x86 · Linux · анализ программ"),
        ("Пишу анализаторы и переиспользуемые системные компоненты на C++ и C. Основные доказательства — PS-form Analyzer с консервативной семантикой и точным оракулом, 12 модулей AdvancedAlgorithms, IR/SSA-оптимизации Wist2 и учебная лаборатория x86-64 codegen/register allocation.",
         "Пишу анализаторы и переиспользуемые системные компоненты на C++ и C. Основные доказательства — PS-form Analyzer с точным оракулом, 12 модулей AdvancedAlgorithms, ручной NASM-код и практический курс по IA-32, а также лаборатория x86-64 codegen/register allocation."),
        ("Linux · CMake · sanitizers · exact oracles", "NASM/x86 · ABI/x87 · Linux · sanitizers"),
        ('<div class="career-item"><strong>Low-level lab</strong><span>IR, liveness, register allocation, x86-64</span></div>',
         '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · codegen</span></div>'),
        ('<p class="org">C/C++ · Python · алгоритмы</p>', '<p class="org">C/C++ · Python · NASM · алгоритмы</p>'),
        ("Обучил около 50 учеников C/C++, Python и алгоритмам; провожу ревью кода.",
         "Обучил около 50 учеников C/C++, Python, NASM и алгоритмам; провожу ревью кода и объясняю модели выполнения."),
        ('<div class="stack-line"><strong>Low-level</strong><p>IR/SSA, liveness, register allocation, x86-64 code generation, isolated native execution</p></div>',
         '<div class="stack-line"><strong>Low-level / Assembly</strong><p>NASM/FASM, IA-32 и x86-64, cdecl и System V AMD64 ABI, стековые кадры, libc interop, структуры/адресация, x87, GDB/objdump, compiler-output analysis</p></div>'),
    ),
    "en-cpp-systems.html": (
        ("C++23 · C17 · Python · Linux · program analysis", "C++23 · C17 · NASM/x86 · Linux · program analysis"),
        ("I build analyzers and reusable systems components in C++ and C. The primary evidence is the conservative PS-form Analyzer with an exact oracle, 12 AdvancedAlgorithms modules, IR/SSA optimizations in Wist2 and an educational x86-64 codegen/register-allocation laboratory.",
         "I build analyzers and reusable systems components in C++ and C. The evidence includes the PS-form Analyzer with an exact oracle, 12 AdvancedAlgorithms modules, hand-written NASM and a practical IA-32 course, plus an x86-64 codegen/register-allocation laboratory."),
        ("Linux · CMake · sanitizers · exact oracles", "NASM/x86 · ABI/x87 · Linux · sanitizers"),
        ('<div class="career-item"><strong>Low-level lab</strong><span>IR, liveness, register allocation, x86-64</span></div>',
         '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · codegen</span></div>'),
        ('<p class="org">C/C++ · Python · algorithms</p>', '<p class="org">C/C++ · Python · NASM · algorithms</p>'),
        ("Taught about 50 students in C/C++, Python, and algorithms; regularly review code.",
         "Taught about 50 students in C/C++, Python, NASM, and algorithms; I review code and explain execution models."),
        ('<div class="stack-line"><strong>Low-level</strong><p>IR/SSA, liveness, register allocation, x86-64 code generation, isolated native execution</p></div>',
         '<div class="stack-line"><strong>Low-level / Assembly</strong><p>NASM/FASM, IA-32 and x86-64, cdecl and System V AMD64 ABI, stack frames, libc interop, structures/addressing, x87, GDB/objdump, compiler-output analysis</p></div>'),
    ),
}.items():
    for old, new in changes:
        literal(path, old, new)
regex("ru-cpp-systems.html", CARD_PATTERN, RU_CARD)
regex("en-cpp-systems.html", CARD_PATTERN, EN_CARD)

# Full portfolio variants.
for path, changes in {
    "ru.html": (
        ("Полное техническое портфолио · compiler/runtime · анализ программ · .NET",
         "Полное техническое портфолио · compiler/runtime · анализ программ · x86 Assembly"),
        ("Разрабатываю инфраструктуру компиляторов, анализаторы и переиспользуемые алгоритмические компоненты. В UniversalToolchain/Wist2 спроектировал многоуровневый IR/runtime-конвейер и экспериментальный проверяемый маршрут AIR → SSA → AIR; PS-form Analyzer занял 1-е место среди 49 решений и прошёл 104/104 тестов; AdvancedAlgorithms объединяет 12 модулей на C++23. Также проектирую и сопровождаю .NET-сервисы с платежами, подписками и восстановлением операций.",
         "Разрабатываю инфраструктуру компиляторов, анализаторы и переиспользуемые алгоритмические компоненты. В UniversalToolchain/Wist2 спроектировал многоуровневый IR/runtime-конвейер и проверяемый маршрут AIR → SSA → AIR; PS-form Analyzer занял 1-е место среди 49 решений; AdvancedAlgorithms объединяет 12 модулей на C++23. Low-level профиль подтверждают ручной NASM-код, практический курс по IA-32 и x86-64 codegen/register-allocation лаборатория. Также сопровождаю .NET-сервисы с платежами и recovery."),
        ("IR/SSA · алгоритмы · .NET · эксплуатация", "IR/SSA · алгоритмы · NASM/x86 · .NET"),
        ('<div class="career-item"><strong>2021 — сейчас</strong><span>преподавание и ревью кода</span></div>',
         '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · codegen</span></div>'),
        ("Преподаю C/C++, C#, Python, Unity и алгоритмы; провожу диагностику знаний и ревью кода.",
         "Преподаю C/C++, C#, Python, NASM и алгоритмы; объясняю ABI и модели выполнения, провожу диагностику знаний и ревью кода."),
        ('<div class="stack-line"><strong>Алгоритмы и системное программирование</strong><p>Переиспользуемые алгоритмы для графов, деревьев, строк и структур данных; C++23/C17; эксперименты с генерацией x86-64.</p></div>',
         '<div class="stack-line"><strong>Алгоритмы и системное программирование</strong><p>Переиспользуемые алгоритмы для графов, деревьев, строк и структур данных; C++23/C17; NASM/FASM, IA-32 и x86-64, cdecl/System V ABI, x87, дизассемблирование и codegen.</p></div>'),
    ),
    "en.html": (
        ("Full technical portfolio · compiler/runtime · program analysis · .NET",
         "Full technical portfolio · compiler/runtime · program analysis · x86 Assembly"),
        ("I build compiler infrastructure, program analyzers and reusable algorithmic components. In UniversalToolchain/Wist2, I designed a multi-IR runtime pipeline and an experimental verifier-gated AIR → SSA → AIR route; the PS-form Analyzer ranked 1st among 49 submissions and passed 104/104 tests; AdvancedAlgorithms provides 12 C++23 modules. I also design and operate .NET services with payments, subscriptions and recovery workflows.",
         "I build compiler infrastructure, program analyzers and reusable algorithmic components. In UniversalToolchain/Wist2, I designed a multi-IR runtime pipeline and a verifier-gated AIR → SSA → AIR route; the PS-form Analyzer ranked 1st among 49 submissions; AdvancedAlgorithms provides 12 C++23 modules. My low-level evidence includes hand-written NASM, a practical IA-32 course and an x86-64 codegen/register-allocation lab. I also operate .NET services with payments and recovery workflows."),
        ("IR/SSA · algorithms · .NET · operations", "IR/SSA · algorithms · NASM/x86 · .NET"),
        ('<div class="career-item"><strong>2021 — present</strong><span>teaching and code review</span></div>',
         '<div class="career-item"><strong>x86 / x86-64 Assembly</strong><span>NASM/FASM · ABI · x87 · codegen</span></div>'),
        ("Teaching C/C++, C#, Python, Unity and algorithms; diagnosing gaps and reviewing code.",
         "Teaching C/C++, C#, Python, NASM and algorithms; explaining ABI and execution models, diagnosing gaps and reviewing code."),
        ('<div class="stack-line"><strong>Algorithms and low-level work</strong><p>Reusable graph, tree, string and data-structure algorithms; C++23/C17; x86-64 code-generation experiments.</p></div>',
         '<div class="stack-line"><strong>Algorithms and low-level work</strong><p>Reusable graph, tree, string and data-structure algorithms; C++23/C17; NASM/FASM, IA-32 and x86-64, cdecl/System V ABI, x87, disassembly and code generation.</p></div>'),
    ),
}.items():
    for old, new in changes:
        literal(path, old, new)
regex("ru.html", CARD_PATTERN, RU_CARD)
regex("en.html", CARD_PATTERN, EN_CARD)

# Dates on the six changed pages.
for page in ("ru-compiler.html", "ru-cpp-systems.html", "ru.html"):
    literal(page, "Обновлено 23 июля 2026", "Обновлено 24 июля 2026")
for page in ("en-compiler.html", "en-cpp-systems.html", "en.html"):
    literal(page, "Updated July 23, 2026", "Updated July 24, 2026")

# Release notes.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
text = text.replace("# Mikhail Razakov — targeted CV variants v25",
                    "# Mikhail Razakov — targeted CV variants v26", 1)
start = text.index("## Изменения v25")
end = text.index("## Контакт", start)
changes = dedent("""\
## Изменения v26

- Assembly вынесен в верхнюю часть compiler и C++ systems профилей: `x86 / x86-64 Assembly`, `NASM/FASM`, ABI, x87 и анализ compiler output видны до чтения деталей.
- Существующий codegen-проект объединён с подтверждаемым ручным NASM-опытом: IA-32/cdecl, стек, libc, структуры/адресация и x87; x86-64 lowering/emission описан отдельно.
- Добавлена ссылка на публичный `Nasm-X86-Course`; IA-32-содержание курса не смешивается с x86-64 codegen-лабораторией.
- Обновлены RU/EN compiler, C++ systems и полные технические страницы; четыре профильных PDF пересобраны и проверены.
- Образование остаётся обезличенным: только статус студента НИУ ВШЭ без года выпуска.

""")
text = text[:start] + changes + text[end:]
text = text.replace(
    "Предыдущий release: `mikhail-razakov-targeted-cv-v24-2026-07-23.tar.xz`  \n"
    "SHA-256: `ca01f7676fa8bdec3186383fa9e632abcd2e3c93463a92e688436fbd0d3b08bb`",
    "Предыдущая версия репозитория: targeted CV variants v25, commit "
    "`d752a7c9dc23058f21bf4d5e3f694b118438a0d7`.",
    1,
)
readme.write_text(text, encoding="utf-8")

# Final evidence assertions.
for page in ("ru-compiler.html", "en-compiler.html", "ru-cpp-systems.html",
             "en-cpp-systems.html", "ru.html", "en.html"):
    text = Path(page).read_text(encoding="utf-8")
    for marker in ("NASM", "x86-64", "cdecl", "x87", COURSE, CODEGEN):
        if marker not in text:
            raise RuntimeError(f"{page}: missing {marker}")
    if text.count(COURSE) != 1 or text.count(CODEGEN) != 1:
        raise RuntimeError(f"{page}: evidence links must occur exactly once")
print("Updated six HTML variants and README")
