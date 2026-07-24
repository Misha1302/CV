from pathlib import Path

GLOBAL = {
    'Проверенный baseline от 14.07.2026: 75 .NET-проектов собираются, 1 325 тестов проходят, 0 предупреждений и 0 ошибок.':
        'Последний полный прогон: 1 358 тестов пройдены, 0 сбоев; сборка успешна.',
    'baseline от 14.07.2026 — 75 .NET-проектов собираются, 1 325 тестов проходят, 0 предупреждений и 0 ошибок.':
        'последний полный прогон — 1 358 тестов пройдены, 0 сбоев; сборка успешна.',
    'baseline от 14.07.2026; 0 предупреждений и 0 ошибок':
        'последний полный прогон; 0 сбоев, сборка успешна',
    'Verified baseline dated July 14, 2026: 75 .NET projects building, 1,325 passing tests, 0 warnings and 0 errors.':
        'Latest full run: 1,358 tests passed, 0 failed; build succeeded.',
    'verified baseline dated July 14, 2026; 0 warnings and 0 errors':
        'latest full run; 0 failed, build succeeded',
    'differential testing, differential testing и изолированный запуск':
        'дифференциальные тесты и изолированный запуск',
    'differential tests, differential testing and isolated execution':
        'differential tests and isolated execution',
    'Ручной NASM-код для IA-32 и backend-лаборатория генерации x86-64: от ABI и стека до liveness, register allocation и проверки нативного кода.':
        'Ручной NASM-код для IA-32 и backend-лаборатория генерации x86-64: от CDECL и стека до анализа живости, распределения регистров и проверки нативного кода.',
    'Hand-written NASM for IA-32 and an x86-64 code-generation lab, spanning ABI and stack mechanics through liveness, register allocation and native-code validation.':
        'Hand-written NASM for IA-32 and an x86-64 code-generation lab, spanning cdecl and stack mechanics through liveness, register allocation and native-code validation.',
    '<li>ABI / x87</li>': '<li>CDECL / x87</li>',
    'NASM IA-32 · ABI · x87 · codegen': 'NASM IA-32 · CDECL/x87 · x86-64 codegen',
    'NASM/x86 · ABI/x87 · Linux · sanitizers': 'NASM IA-32 · CDECL/x87 · x86-64 codegen · sanitizers',
    'NASM/x86 · .NET': 'NASM IA-32 / x86-64 codegen · .NET',
}

PER_FILE = {
    'ru-compiler.html': {
        '<div class="career-item"><strong>Program analysis &amp; correctness</strong><span>exact oracles · structural verifiers · backend parity</span></div>':
            '<div class="career-item"><strong>Анализ и корректность</strong><span>точные эталоны · структурные верификаторы · backend parity</span></div>',
        '<div class="stack-line"><strong>Ассемблер и ABI</strong><p>NASM IA-32, IA-32 и x86-64; cdecl и x86-64 SysV code generation; стековые кадры, вызовы libc, структуры и адресация, x87; objdump и анализ дизассемблирования.</p></div>':
            '<div class="stack-line"><strong>Assembly и машинный уровень</strong><p>NASM IA-32: CDECL, стековые кадры, вызовы libc, структуры, адресация и x87; x86-64 SysV codegen через iced-x86; objdump и анализ дизассемблирования.</p></div>',
    },
    'en-compiler.html': {
        '<div class="stack-line"><strong>Assembly and ABI</strong><p>NASM IA-32, IA-32 and x86-64; cdecl and x86-64 SysV code generation; stack frames, libc interop, structures and addressing, x87; objdump and disassembly analysis.</p></div>':
            '<div class="stack-line"><strong>Assembly and machine-level work</strong><p>NASM IA-32: cdecl, stack frames, libc calls, structures/addressing and x87; x86-64 SysV code generation through iced-x86; objdump and disassembly analysis.</p></div>',
        '<p class="details">Taught about 50 students; I diagnose gaps, explain execution models and review code.</p>':
            '<p class="details">Taught about 50 students in C/C++, Python and algorithms; authored a practical NASM IA-32 course and review code.</p>',
    },
    'ru-cpp-systems.html': {
        '<div class="career-item"><strong>C17 analyzer</strong><span>нормализация + exact/conservative strategies</span></div>':
            '<div class="career-item"><strong>C17-анализатор</strong><span>нормализация · точный эталон · консервативная семантика</span></div>',
        '<div class="career-item"><strong>C++23 graph core</strong><span>RPO, shortest paths, SCC, max-flow</span></div>':
            '<div class="career-item"><strong>Графовое ядро C++23</strong><span>RPO, кратчайшие пути, SCC, max-flow</span></div>',
        '<h2>C++ systems, анализ программ и compiler infrastructure.</h2>':
            '<h2>Системная разработка на C++, анализ программ и инфраструктура компиляторов.</h2>',
        '<div class="stack-line"><strong>Low-level / Assembly</strong><p>NASM IA-32, IA-32 и x86-64, cdecl и x86-64 SysV code generation, стековые кадры, libc interop, структуры/адресация, x87, objdump, compiler-output analysis</p></div>':
            '<div class="stack-line"><strong>Машинный уровень / Assembly</strong><p>NASM IA-32: CDECL, стековые кадры, libc, структуры/адресация и x87; x86-64 SysV codegen через iced-x86; objdump и анализ compiler output</p></div>',
    },
    'en-cpp-systems.html': {
        '<div class="stack-line"><strong>Low-level / Assembly</strong><p>NASM IA-32, IA-32 and x86-64, cdecl and x86-64 SysV code generation, stack frames, libc interop, structures/addressing, x87, objdump, compiler-output analysis</p></div>':
            '<div class="stack-line"><strong>Low-level / Assembly</strong><p>NASM IA-32: cdecl, stack frames, libc calls, structures/addressing and x87; x86-64 SysV code generation through iced-x86; objdump and compiler-output analysis</p></div>',
    },
    'ru.html': {
        'Полное техническое портфолио · compiler/runtime · анализ программ · x86 Assembly':
            'Полное техническое портфолио · compiler/runtime · анализ программ · NASM IA-32 / x86-64 codegen',
        'Преподаю C/C++, C#, Python, NASM и алгоритмы; объясняю ABI и модели выполнения, провожу диагностику знаний и ревью кода.':
            'Преподаю C/C++, C#, Python и алгоритмы; разработал практический курс по NASM IA-32, объясняю модели выполнения и провожу ревью кода.',
    },
    'en.html': {
        'Full technical portfolio · compiler/runtime · program analysis · x86 Assembly':
            'Full technical portfolio · compiler/runtime · program analysis · NASM IA-32 / x86-64 codegen',
        'Teaching C/C++, C#, Python, NASM and algorithms; explaining ABI and execution models, diagnosing gaps and reviewing code.':
            'Teaching C/C++, C#, Python and algorithms; authored a practical NASM IA-32 course, explain execution models and review code.',
    },
}

pages = sorted(Path('.').glob('*.html'))
for path in pages:
    text = path.read_text(encoding='utf-8')
    if '<section class="print-cv"' in text:
        web, print_part = text.split('<section class="print-cv"', 1)
        suffix = '<section class="print-cv"' + print_part
    else:
        web, suffix = text, ''
    for old, new in GLOBAL.items():
        web = web.replace(old, new)
    for old, new in PER_FILE.get(path.name, {}).items():
        if old not in web:
            raise RuntimeError(f'{path}: expected web fragment missing: {old[:100]!r}')
        web = web.replace(old, new)
    path.write_text(web + suffix, encoding='utf-8')

corpus = '\n'.join(path.read_text(encoding='utf-8') for path in pages)
for marker in (
    '1 325', '1,325', '75 .NET-проектов', '75 .NET projects',
    'differential testing, differential testing', 'NASM IA-32, IA-32',
    '<li>ABI / x87</li>', 'NASM IA-32 · ABI · x87', 'NASM/FASM', 'System V AMD64 ABI',
):
    if marker in corpus:
        raise RuntimeError(f'Forbidden stale/overbroad marker remains: {marker}')
for marker in ('1 358', '1,358', 'Nasm-X86-Course', 'x86-64-codegen-ra-playground'):
    if marker not in corpus:
        raise RuntimeError(f'Required v27 marker missing: {marker}')

print('Patched detailed HTML pages and verified web/PDF claim consistency')
