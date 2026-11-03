# Михаил Разаков

**C# / .NET BACKEND · SYSTEMS & RELIABILITY**

Москва / удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Разрабатываю и сопровождаю .NET-сервисы с акцентом на повторы запросов, состояние платежей, восстановление и диагностируемость. Основной работающий сервис — VpnMediator; в UniversalToolchain исследую границу семантического планирования и исполнения. Коммерческая практика на смешанном стеке — около года суммарно.

## Технологии

- C#/.NET, ASP.NET Core, EF Core, SQL/PostgreSQL, SQLite, REST/OpenAPI, async/await
- Idempotency, provider reconciliation, transactions, operational recovery; CIL, Reflection.Emit, C++/LLVM, Python, Linux

## Опыт

**ИСП РАН · SharpChecker · октябрь 2026 — н. в.**

Символьные вычисления и структурная метаинформация C#-кода/деклараций для статического анализа и задач обнаружения ошибок.

**МЦСТ · стажировка по компиляторам · июль — август 2026**

C++23/LLVM 22: экспериментальный LICM с консервативными условиями допустимости; Python-проверки поведения до/после преобразования.

**Коммерческая разработка · C#/.NET и смежный стек · суммарно около 1 года**

Прикладные и серверные задачи на C#/.NET и Unity: ASP.NET Core, SQL/PostgreSQL, файловая система и серверное окружение. Продолжительность — по данным кандидата.

## Проекты

**[VpnMediator · платеж не равен праву доступа](https://misha1302.github.io/CV/cases/ru-vpn.html)**

Состояния доступа и платежей разделены; проверка привязки события к заказу, идемпотентная обработка, reconciliation и restart recovery. Скрипты выпуска содержат backup, health gates и rollback.

**[UniversalToolchain · план до выполнения](https://github.com/Misha1302/UniversalToolchain)**

LanguageCompiler формирует проверяемый LanguagePlan с зависимостями и типизированными маршрутами; Bytecode/AIR, interpreter/CIL. 1 324 теста указаны в репозиторном манифесте, не выдаются за повторно пройденные.

**[TuringSquare-LMS · архитектура и ревью](https://misha1302.github.io/CV/cases/ru-lms.html)**

Определяю инварианты ролей/доступа и критерии проверки T-Bank sandbox. Часть реализации выполнена AI-агентами; релиз в production не заявляется.

**[Quark2 · исследование CLR](https://github.com/Misha1302/Quark2)**

Эксперименты DynamicMethod/Reflection.Emit и внутренних CLR API; сравнение Invoke, delegate и native pointer через BenchmarkDotNet.

## Образование и достижения

НИУ ВШЭ — ФКН, Программная инженерия.

«Юниор» НИЯУ МИФИ, диплом I степени (2026); LangDev 2026, доклад об UniversalToolchain.
