# Михаил Разаков

**C# / .NET BACKEND DEVELOPER · SYSTEMS & RELIABILITY**

Москва · удалённо · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Профиль

Разрабатываю C#/.NET-сервисы с фокусом на платежи, повторы запросов, частичные сбои и восстановление состояния. Веду работающий VpnMediator и развиваю compiler/runtime-инфраструктуру UniversalToolchain. Коммерческая практика — 1 год на смешанном стеке; работа в ИСП РАН, стажировка в МЦСТ.

## Практика И Ответственность

**ИСП РАН / SharpChecker  |  октябрь 2026 — н. в.**

- Разрабатываю компоненты символьных вычислений и инфраструктуру метаинформации о C#-коде и декларациях для задач анализа и распознавания ошибок.
**МЦСТ / LLVM 22  |  июль — август 2026**

- Сделал LICM-проход с консервативными legality checks: память, побочные эффекты, invariance и speculative safety. Сравнение исполняемого поведения до/после — через Python harness.
**Коммерческие заказы и разработка  |  суммарно 1 год**

- C#/.NET, Unity, ASP.NET Core, PostgreSQL, файловая система, серверные задачи. Опыт охватывает прикладную и серверную разработку.

## Инженерные Кейсы

**01 · VpnMediator — платёж не равен праву доступа**

- Сопровождаю действующий VPN-сервис для сотен пользователей. ASP.NET Core Mediator (доступ, устройства, signed links), Python Bot (заказы, платежи, диалоги), SQLite в обоих сервисах.
- При повторе или запоздалом событии система хранит payment evidence, проверяет связывание с заказом и восстанавливает операции через reconciliation. Тесты проверяют restart recovery, ownership claim и однократное применение outbox; релизные скрипты — backup, health checks и rollback. Кейc: github.com/Misha1302/CV/blob/main/cases/ru-vpn.html
**02 · UniversalToolchain — семантический выбор до runtime**

- Развиваю .NET-инфраструктуру композиции языковых модулей. LanguageCompiler строит неизменяемый LanguagePlan: зависимости, реализации, типизированные маршруты; отдельный verifier проверяет план до выполнения.
- Bytecode/AIR, interpreter и CIL, проверки паритета; манифест текущей ревизии — 1324 теста. Код: github.com/Misha1302/UniversalToolchain
**03 · TuringSquare-LMS — транзакции и защита платежей**

- Задаю архитектуру, критерии приёмки и ревью реализации ролей, course entitlements и T-Bank: Serializable/FOR SHARE при создании заказа; подтверждение через authoritative provider read до выдачи доступа. Участвую в координации агентной реализации и проверке решений; проект в разработке, платежи — sandbox.
**04 · Quark2 — что стоит вызов сгенерированного кода**

- Исследовал CIL/Reflection.Emit, DynamicMethod и приватные механизмы CLR; сравнение Invoke, делегата и function pointer в BenchmarkDotNet. Экспериментальная работа с внутренними API CLR. github.com/Misha1302/Quark2

## Стек

C#/.NET, ASP.NET Core, REST/OpenAPI, SQL, PostgreSQL, SQLite, EF Core, async, транзакции, webhooks, reconciliation; Python, C++/LLVM, CIL, Reflection.Emit; Git, Linux, Docker Compose, nginx, systemd.


## Образование И Достижения

НИУ ВШЭ — ФКН, «Программная инженерия». Диплом I степени «Юниор» НИЯУ МИФИ (2026) за UniversalToolchain; LangDev 2026 (доклад о проекте).
