from pathlib import Path


def replace(path_name: str, replacements: dict[str, str]) -> None:
    path = Path(path_name)
    text = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        if old not in text:
            raise RuntimeError(f'{path}: missing text to replace: {old!r}')
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')


# The web pages are already localized; these replacements target the injected print-only CV.
for name in ('en-compiler.html', 'en-cpp-systems.html'):
    replace(name, {
        '<h1>Михаил Разаков</h1>': '<h1>Mikhail Razakov</h1>',
        'AIR -> SSA -> AIR': 'AIR → SSA → AIR',
    })

replace('ru-compiler.html', {
    'Разрабатываю UniversalToolchain/Wist2 - модульную .NET-платформу с несколькими IR, эталонным интерпретатором, CIL/DynamicMethod backend и проверяемым маршрутом AIR -> SSA -> AIR. Дополнительная глубина: консервативный анализ программ, C++23 и x86 code generation.':
        'Разрабатываю UniversalToolchain/Wist2 — модульную .NET-платформу с несколькими IR, эталонным интерпретатором, backend на CIL/DynamicMethod и проверяемым маршрутом AIR → SSA → AIR. Дополнительная глубина — консервативный анализ программ, C++23 и генерация x86-кода.',
    'AIR -> SSA -> AIR': 'AIR → SSA → AIR',
    'Спроектировал Source -> AST -> Bytecode -> AIR -> execution, эталонный интерпретатор и CIL/DynamicMethod backend.':
        'Спроектировал конвейер Source → AST → Bytecode → AIR → execution, эталонный интерпретатор и backend на CIL/DynamicMethod.',
    'Реализовал opt-in AIR → SSA → AIR: constant folding, SCCP-lite, branch folding, unreachable cleanup и DCE.':
        'Реализовал подключаемый маршрут AIR → SSA → AIR: свёртку констант, SCCP-lite, упрощение ветвлений, удаление недостижимого кода и DCE.',
    'Добавил capability contracts, structural verifiers и сравнение interpreter/CIL для поддерживаемой семантики.':
        'Добавил контракты возможностей, структурные верификаторы и сравнение интерпретатора с CIL для поддерживаемой семантики.',
    'C++23-компоненты анализа графов; CMake, warnings-as-errors, ASan/UBSan, clang-tidy и явные include-зависимости.':
        'Разработал C++23-компоненты анализа графов; использовал CMake, warnings-as-errors, ASan/UBSan, clang-tidy и явные include-зависимости.',
    'RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic поверх общей модели графа и воспроизводимых I/O-тестов.':
        'Реализовал RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic поверх общей модели графа; добавил воспроизводимые I/O-тесты.',
    'Консервативный анализ межитерационных зависимостей памяти. 1-е место среди 49 решений, единственные 5,0/5,0 и 104/104; exact oracle, randomized и metamorphic testing.':
        'Консервативный анализ межитерационных зависимостей памяти. 1-е место среди 49 решений, единственные 5,0/5,0 и 104/104; точный эталон, рандомизированные и метаморфные тесты.',
    'NASM IA-32: CDECL, стековые кадры, libc, структуры, адресация и x87. Отдельная x86-64 SysV emitter-лаборатория: liveness, live intervals, linear scan, iced-x86 и interpreter-vs-native validation.':
        'NASM IA-32: CDECL, стековые кадры, libc, структуры, адресация и x87. Отдельная лаборатория x86-64 SysV emitter: анализ живости, live intervals, linear scan, iced-x86 и сравнение с эталонным интерпретатором.',
    'parsing, AST, Bytecode, AIR, CFG, SSA, CIL/DynamicMethod':
        'лексический и синтаксический анализ, AST, Bytecode, AIR, CFG, SSA, CIL/DynamicMethod',
    'dominance, liveness, SCCP-lite, DCE, анализ зависимостей памяти':
        'доминирование, анализ живости, SCCP-lite, DCE и анализ зависимостей памяти',
    'structural verifiers, exact oracle, differential и metamorphic testing':
        'структурные верификаторы, точные эталоны, дифференциальные и метаморфные тесты',
    'NASM IA-32, CDECL, stack/x87; x86-64 SysV codegen, objdump/disassembly':
        'NASM IA-32, CDECL, стек и x87; генерация x86-64 SysV-кода, objdump и анализ дизассемблирования',
    'C#/.NET, C++23, C17, Python; CMake, GitHub Actions, sanitizers, clang-tidy':
        'C#/.NET, C++23, C17, Python; CMake, GitHub Actions, ASan/UBSan и clang-tidy',
})

replace('ru-cpp-systems.html', {
    '<h2>Инженер C++ и анализа программ</h2>': '<h2>C++-инженер: системная разработка и анализ программ</h2>',
    'Разрабатываю анализаторы и переиспользуемые системные компоненты на C++/C. Профиль подтверждают PS-form Analyzer, 12 модулей AdvancedAlgorithms, стажировка МЦСТ, NASM IA-32 и отдельная x86-64 codegen/register-allocation лаборатория.':
        'Разрабатываю анализаторы и переиспользуемые системные компоненты на C++/C. Профиль подтверждают PS-form Analyzer, 12 модулей AdvancedAlgorithms, стажировка МЦСТ, NASM IA-32 и отдельная лаборатория генерации x86-64-кода и распределения регистров.',
    'Общее ядро ориентированного графа и компоненты RPO/cycle detection, Dijkstra, Tarjan SCC и Dinic.':
        'Разработал общее ядро ориентированного графа и компоненты RPO с обнаружением циклов, Dijkstra, Tarjan SCC и Dinic.',
    'C++23/CMake, warnings-as-errors, ASan/UBSan, clang-tidy, явные include-зависимости и I/O-тесты.':
        'Настроил C++23/CMake, warnings-as-errors, ASan/UBSan, clang-tidy, явные include-зависимости и I/O-тесты.',
    'Несколько IR, interpreter/CIL execution paths и opt-in AIR -> SSA -> AIR.':
        'Спроектировал несколько IR, пути исполнения через интерпретатор и CIL, а также подключаемый маршрут AIR → SSA → AIR.',
    'Capability contracts, structural verifiers и parity-тесты; последний полный прогон: 1 358/1 358 тестов.':
        'Добавил контракты возможностей, структурные верификаторы и parity-тесты; последний полный прогон — 1 358/1 358 тестов.',
    'Conservative yes/no/maybe semantics; normalization, range/residue/GCD filters, exact affine analysis, bounded search and exact/randomized/metamorphic verification.':
        'Консервативная семантика yes/no/maybe; нормализация, range/residue/GCD-фильтры, точный аффинный анализ, ограниченный поиск, точные, рандомизированные и метаморфные проверки.',
    '12 reusable modules: centroid decomposition, HLD, LCA, Dinic, iterative Tarjan, bridges, Dijkstra, Aho-Corasick, segment tree and others; differential tests, invariants and large inputs.':
        '12 переиспользуемых модулей: центроидная декомпозиция, HLD, LCA, Dinic, итеративный Tarjan, мосты, Dijkstra, Aho-Corasick, дерево отрезков и другие; дифференциальные тесты, инварианты и крупные входы.',
    'CDECL, stack frames, libc, structures/addressing and x87 in NASM IA-32; separate x86-64 SysV emitter with liveness, register allocation, iced-x86 and isolated native execution.':
        'NASM IA-32: CDECL, стековые кадры, libc, структуры, адресация и x87; отдельный x86-64 SysV emitter с анализом живости, распределением регистров, iced-x86 и изолированным запуском нативного кода.',
    'C++23, C17, generic components, explicit contracts and error models':
        'C++23, C17, переиспользуемые компоненты, явные контракты и модели ошибок',
    'graphs, trees, strings, data structures, max-flow, SCC, shortest paths':
        'графы, деревья, строки, структуры данных, max-flow, SCC и кратчайшие пути',
    'conservative semantics, affine reasoning, exact oracle and counterexamples':
        'консервативная семантика, аффинный анализ, точный эталон и контрпримеры',
    'NASM IA-32, CDECL, stack/x87; x86-64 SysV codegen and disassembly':
        'NASM IA-32, CDECL, стек и x87; генерация x86-64 SysV-кода и анализ дизассемблирования',
    'Linux, CMake, GitHub Actions, ASan/UBSan, clang-tidy, reproducible tests':
        'Linux, CMake, GitHub Actions, ASan/UBSan, clang-tidy и воспроизводимые тесты',
})

print('Polished v27 print-only CV language and English name')
