# Михаил Разаков

**C# / .NET · RUNTIME, COMPILERS & PERFORMANCE**

Москва / удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Работаю с CLR/CIL, инфраструктурой компиляторов, LLVM и статическим анализом. Сейчас — символьные вычисления в SharpChecker (ИСП РАН), ранее — LLVM 22 в МЦСТ. Дополнительно создаю и сопровождаю backend; около года суммарной коммерческой разработки на смешанном стеке.

## Технологии

- C#/.NET, CIL, Reflection.Emit, DynamicMethod, CLR internals, Roslyn, BenchmarkDotNet
- LLVM 22/C++23, CFG/SSA, x86-64/SysV, Rust, differential testing; ASP.NET Core, PostgreSQL, Git/Linux

## Опыт

**ИСП РАН · SharpChecker · октябрь 2026 — н. в.**

Символьные вычисления и структурная метаинформация C#-кода/деклараций для статического анализа и задач обнаружения ошибок.

**МЦСТ · стажировка по компиляторам · июль — август 2026**

C++23/LLVM 22: экспериментальный LICM с консервативными условиями допустимости; Python-проверки поведения до/после преобразования.

**Коммерческая разработка · C#/.NET и смежный стек · суммарно около 1 года**

Прикладные и серверные задачи на C#/.NET и Unity: ASP.NET Core, SQL/PostgreSQL, файловая система и серверное окружение. Продолжительность — по данным кандидата.

## Проекты

**[UniversalToolchain · модульная compiler/runtime-платформа](https://github.com/Misha1302/UniversalToolchain)**

Типизированные контракты и зависимости → проверяемый LanguagePlan → runtime; Bytecode/AIR, interpreter и CIL backend. Манифест заявляет 1 324 теста; паритет проверяется отдельными сценариями.

**[Quark2 · вызов сгенерированного кода](https://github.com/Misha1302/Quark2)**

DynamicMethod/Reflection.Emit, RuntimeMethodHandle и native pointer. BenchmarkDotNet сравнивает reflection Invoke, delegate и вызов по указателю; внутренние CLR API — только эксперимент.

**[x86-64 codegen · Rust](https://github.com/Misha1302/x86-64-codegen-ra-playground)**

SSA/CFG, liveness, register allocation, spills, phi-lowering, SysV ABI; для поддерживаемого подмножества — differential native execution с IR-интерпретатором.

**[LLVM Global IV / LICM · C++](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization)**

Межпроцедурный анализ эффектов и legality условий оптимизаций; негативные регрессии защищают от некорректных преобразований.

## Образование и достижения

НИУ ВШЭ — ФКН, Программная инженерия.

«Юниор» НИЯУ МИФИ, диплом I степени (2026); доклад LangDev 2026.
