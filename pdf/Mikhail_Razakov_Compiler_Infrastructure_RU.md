# Михаил Разаков

**Compiler Infrastructure / Language Tooling Engineer**

Москва / удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Разрабатываю инфраструктуру модульных языков и компиляторов на C#/.NET и C++/LLVM. В UniversalToolchain разделяю разрешение зависимостей, выбор компонентов и построение проверяемого LanguagePlan от исполнения. Сейчас работаю над символьными вычислениями для SharpChecker в ИСП РАН; летом 2026 года проходил LLVM/C++-стажировку в МЦСТ.

## Технологии

- **Compiler SDK / .NET:** C#, .NET, LanguageCompiler, LanguagePlan, typed artifact contracts, зависимости и конфликты, backend routing, Bytecode/AIR, interpreter/CIL
- **Компиляторы и IR:** C++23, LLVM 22/IR, APInt, CFG/SSA, анализ циклов, межпроцедурные эффекты; Rust, x86-64
- **Проверка и инструменты:** Верификация планов, детерминированный порядок passes, regression/differential testing, LLVM Verifier, сравнение interpreter/CIL; Git, Linux, Python, CMake

## Опыт

**ИСП РАН · SharpChecker · октябрь 2026 — настоящее время**

- Работаю над символьными вычислениями для статического анализа программ на C#/.NET.

**МЦСТ · стажировка по разработке компиляторов · июль–август 2026**

- Работал над экспериментальным LLVM LICM: проверял условия допустимости переноса инструкций с учётом циклов, обращений к памяти и побочных эффектов; сравнивал поведение до/после с помощью Python.

## Инженерные проекты

**[UniversalToolchain / Wist2](https://github.com/Misha1302/UniversalToolchain)**

Разрабатываю модульную инфраструктуру: LanguageCompiler разрешает зависимости и конфликты и строит неизменяемый LanguagePlan. Verifier проверяет типизированные маршруты артефактов, владельцев backend, порядок contributions и хеш плана; runtime не выполняет повторный семантический выбор. Реализован pipeline frontend → Bytecode → AIR → optimizers → interpreter/CIL. Исследовательская подсистема PlanFuzz содержит replay и уменьшение контрпримеров, но ещё не завершена. Репозиторный манифест фиксирует 1324 ожидаемых тестовых прохождения.

**[LLVM Interprocedural Global IV Optimization](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization/tree/0d759dcf3af7a5652432eb0fea5b9ca27ec88f74)**

Экспериментальный LLVM pass локализует поддерживаемые обращения к глобальным целочисленным переменным в циклах. Межпроцедурный анализ эффектов и проверка допустимости отделены от IR-преобразования. На LLVM 22.1.8 пройдены 29/29 регрессионных сценариев, включая структурные проверки, идемпотентность и консервативные отказы.

**[x86-64 Compiler Backend & Register Allocation](https://github.com/Misha1302/x86-64-codegen-ra-playground)**

Реализовал экспериментальный backend для ограниченного IR: SSA/CFG, liveness, register allocation, spills, phi lowering и генерация SysV x86-64. Независимый verifier проверяет назначения регистров и stack slots; результат native-исполнения сравнивается с эталонным IR-интерпретатором.

## Образование

НИУ ВШЭ — Программная инженерия

## Достижения

- **2026 — LangDev — UniversalToolchain:** Доклад об архитектуре компиляторной инфраструктуры 9 октября 2026 года. [Запись доклада](https://youtu.be/2jqmw-1c7kE)
- **2026 — ФКН НИУ ВШЭ · Open Source:** UniversalToolchain — один из победителей студенческого конкурса проектов с открытым кодом.
- **2025–2026 — «Юниор» НИЯУ МИФИ:** Дипломы I степени в секции информационных технологий в 2025 и 2026 годах.
- **2026 — Отбор МЦСТ — LLVM/C++:** По письму организатора: 5,0/5,0 и 104/104 официальных тестов среди 49 представленных решений.
