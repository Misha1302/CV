# Михаил Разаков

**C# / .NET ENGINEER · RUNTIME / COMPILERS / PERFORMANCE**

Москва · удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Разрабатываю инструменты компиляции и выполнения на .NET, работаю с CLR/CIL и анализом программ. Помимо исследования компиляторов, создаю и сопровождаю backend-сервисы: 1 год совокупной коммерческой разработки на смешанном стеке и собственный действующий VpnMediator. Целевые задачи: runtime internals, developer tooling, статический анализ и инженерный .NET backend.

## Профессиональный Опыт

**ИСП РАН / SharpChecker  |  октябрь 2026 — н. в.**

- Символьные вычисления и подготовка структурной метаинформации C#-кода/деклараций для анализа и задач распознавания ошибок с помощью ИИ.
**МЦСТ / LLVM 22  |  июль — август 2026**

- C++23, LICM с условиями допустимости трансформации, контроль side effects и памяти; differential checks до/после преобразования через Python.
**Коммерческая разработка  |  1 год суммарно**

- C#/.NET, Unity, ASP.NET Core, PostgreSQL, файловая система и серверы; решал задачи серверной и прикладной разработки.

## Проекты: Исходники, Механизмы, Границы

**UniversalToolchain / Wist · C#/.NET · github.com/Misha1302/UniversalToolchain**

- Развиваю модульную compiler/runtime-инфраструктуру. Typed contracts → разрешение зависимостей и конфликтов → immutable LanguagePlan → проверка маршрутов артефактов → LanguageRuntime. Разделены Bytecode/AIR, interpreter и CIL backends.
- В репозитории хранится манифест на 1324 теста и тесты паритета backend. Wist — экспериментальная alpha-ветка.
**Quark2 · C#/.NET, CIL · github.com/Misha1302/Quark2**

- DynamicMethod/Reflection.Emit; исследование GetMethodDescriptor, RuntimeMethodHandle и native pointer. BenchmarkDotNet сравнивает reflection Invoke, delegate и вызов по указателю; внутренние CLR API используются только экспериментально.
**x86-64 codegen / register allocation · Rust · github.com/Misha1302/x86-64-codegen-ra-playground**

- SSA/CFG, liveness/interference, регистровая аллокация, spills, phi-lowering, SysV x86-64; независимая проверка раскладки и сравнение native исполнения с интерпретатором для поддерживаемого подмножества.
**LLVM Global IV и LICM · C++ / LLVM**

- Межпроцедурный анализ эффектов, условия допустимости подъёма переменных, контроль may-throw/atomic и MustExecute; тесты включают случаи запрета преобразований. github.com/Misha1302/LLVM-interprocedural-global-IV-optimization
**VpnMediator · практический backend · ASP.NET Core, SQLite, Python**

- Действующий VPN-сервис: сотни пользователей. Архитектура прав доступа, HMAC, платежей, recovery и release workflow; .NET Mediator отделён от Python Telegram Bot.

## Технологии

C#/.NET, CIL/MSIL, Reflection.Emit, DynamicMethod, CLR internals, Roslyn, CFG/SSA, LLVM 22/C++23, Rust, x86-64/SysV ABI, BenchmarkDotNet, ASP.NET Core, PostgreSQL, SQLite, Git/Linux.


## Образование И Достижения

НИУ ВШЭ — ФКН, «Программная инженерия». Диплом I степени «Юниор» НИЯУ МИФИ (2026) за UniversalToolchain; LangDev 2026 (программный доклад).
