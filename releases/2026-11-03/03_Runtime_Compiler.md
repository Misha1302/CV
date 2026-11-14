# Михаил Разаков

**SOFTWARE ENGINEER · COMPILERS, RUNTIME & PROGRAM ANALYSIS**

Москва / удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Разрабатываю компиляторную инфраструктуру, средства анализа программ и runtime-компоненты на C#/.NET, C++/LLVM и Rust. В ИСП РАН работаю с символьными вычислениями в SharpChecker; в МЦСТ проходил стажировку по компиляторам. В собственных проектах занимаюсь LLVM IR-преобразованиями, Roslyn CFG/data-flow, CIL и x86-64 codegen; корректность проверяю регрессионными и дифференциальными тестами.

## Технологии

- Компиляторы и runtime: C#/.NET, CIL/CLR, Roslyn, DynamicMethod, Reflection.Emit; C++23, LLVM 22, LLVM IR; Rust, x86-64 SysV ABI
- Анализ и проверки: CFG/SSA, data-flow, анализ эффектов, проверка допустимости преобразований, register allocation, phi lowering, differential/regression testing; Python, Git, Linux

## Опыт

**ИСП РАН · SharpChecker · октябрь 2026 — н. в.**

Работаю над символьными вычислениями для статического анализа программ на C#/.NET.

**МЦСТ · стажировка по разработке компиляторов · июль — август 2026**

C++23/LLVM 22: экспериментальный LICM, проверка условий допустимости преобразований и сравнение поведения до/после с помощью Python.

**Заказная разработка · C#/.NET и Unity · отдельные проекты с 2023 года**

Разработал API лицензирования KeyAuth на ASP.NET Core с EF Core/PostgreSQL, интеграцией с Unity-клиентами и последующей поддержкой совместимости.

## Проекты

**[UniversalToolchain · compiler/runtime-инфраструктура](https://github.com/Misha1302/UniversalToolchain)**

Разрабатываю модульную инфраструктуру языков с Bytecode/AIR и маршрутами interpreter/CIL. Типизированный LanguagePlan проверяет компоненты и зависимости до исполнения; тесты сопоставляют результаты разных способов выполнения.

**[LLVM Global IV · межпроцедурная оптимизация](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization/tree/0d759dcf3af7a5652432eb0fea5b9ca27ec88f74)**

Экспериментальный LLVM 22 pass локализует поддерживаемые обращения к целочисленным globals в циклах. Анализ эффектов и PromotionLegality отделены от IR-преобразования. На LLVM 22.1.8 пройдены 29/29 сценариев преобразований и консервативных отказов.

**[DerefAfterNullAnalyzer · Roslyn CFG / data-flow](https://github.com/Misha1302/DerefAfterNullAnalyzer/tree/a18102e988dbf854e67b356a44e1d81caba5b080)**

Разработал fixed-point анализ null-state с учётом ветвлений, циклов и слияния состояний. На зафиксированном Git-снимке пройдены 18/18 тестов. Это отдельный проект, не заявленная интеграция в SharpChecker.

**[x86-64 Codegen & Register Allocation Lab · Rust](https://github.com/Misha1302/x86-64-codegen-ra-playground)**

Экспериментальный backend для ограниченного IR: SSA/CFG, liveness, register allocation, spills и phi lowering. Назначения регистров проверяются независимо; результаты native-кода сравниваются с эталонным IR-интерпретатором.

## Образование и достижения

НИУ ВШЭ, ФКН — Программная инженерия, с 2026 года.

Конкурс «Юниор» НИЯУ МИФИ — диплом I степени (2025 и 2026). Доклад об UniversalToolchain на LangDev 2026 — [Официальная видеозапись](https://youtu.be/2jqmw-1c7kE)
