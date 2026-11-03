# Михаил Разаков — доказательная карта, стратегия и независимое ревью CV

**Срез:** 3 ноября 2026 года. **Назначение:** рабочий материал кандидата. **Резюме для отправки:** `01_Backend_ATS` / `02_Tech_Lead` / `03_Runtime_Compiler`; этот документ не следует автоматически прикладывать к первому отклику.

## 1. Вывод редакторской комиссии

**Основной рынок:** C#/.NET backend — особенно команды с платежными интеграциями, состоянием данных, ASP.NET Core, SQL, системной инженерией. **Дополнительный рынок:** .NET runtime, compiler tooling, static analysis, performance. Формальная метка Junior/Middle/Senior в заголовке проигрывает демонстрируемым компетенциям; достаточно указать целевую должность.

**Сильное:** действующий VPN-продукт с конечными пользователями по свидетельству кандидата, код обработки повторных платежей/сбоев, текущая работа в ИСП РАН, стажировка над LLVM, длительная линия собственных compiler/runtime-проектов и конкретная работа с CLR internals. **Уязвимое:** неразмеченный год коммерческой разработки, отсутствие приватных delivery/production-метрик, нет независимой атрибуции всего кода больших репозиториев, большой разрыв между технической глубиной и подтверждёнными сроками работы в команде над коммерческим backend. Беседа с техлидом рациональна; автоматическое присвоение Middle/Senior — нет.

### Как читать таблицу

- `PUBLIC_CODE`: присутствует в открытом исходном коде на указанной ревизии.
- `PRIVATE_CODE_AUTHORIZED`: читаемо через подключенный авторизованный GitHub или Fedora, **не** публичный proof для работодателя.
- `REPO_DOCUMENTATION`: утверждается в репозиторном README/manifest/сценарии теста; не означает независимого исполнения.
- `OFFICIAL_EXTERNAL`: независимая страница организатора/конференции.
- `CANDIDATE_ATTESTED`: кандидат сообщает факт, независимая проверка ограничена; допустимо от первого лица, не как аудированная метрика.
- `NOT_VERIFIED`: заявлять не следует.

Проверка исходников = подтверждение реализации механизма. Она **не** доказывает, что кандидат лично набирал каждую строку, что тесты прошли в этой сессии, что код выкатили в production или что приложение имеет конкретный SLA.

## 2. Claim-by-claim evidence map

| Claim ID | Конкретный тезис в CV | Источник и ревизия | Состояние и личный вклад | Граница |
|---|---|---|---|---|
| C01 | 1 год суммарной коммерческой разработки на смешанном стеке | `02_CANDIDATE_FACTS_AND_CORRECTIONS.md`, раздел A.2; прежнее CV подтверждает отдельную Diploma.school-практику | `CANDIDATE_ATTESTED`; распределение по компаниям не восстановлено | Не выдавать за «год только ASP.NET Core» и не выдумывать непрерывное трудоустройство |
| C02 | Работа в ИСП РАН над SharpChecker с октября 2026, символика и метаинформация для AI error detection | `02_CANDIDATE_FACTS_AND_CORRECTIONS.md`, A.3; [публичный CV/knowledge](https://github.com/Misha1302/CV/blob/03a34350fe2fc6dcffc0b181e0379e189e511939/knowledge/resume-evidence.json) | `CANDIDATE_ATTESTED`; приватный рабочий код не анализировался | Не утверждать, что лично обучил ML-модель или реализовал весь SharpChecker |
| C03 | Стажировка МЦСТ, июль–август 2026; консервативный LICM | [src/LicmOptimizationPass.cpp](https://github.com/Misha1302/LLVM-basic-LICM-implementation/blob/7abafde796ba6b4de6a0e0f52473938e2825eb4f/src/LicmOptimizationPass.cpp), `can_be_moved_to_preheader`, а также исходный Python harness в репозитории | `PUBLIC_CODE` + период стажировки `CANDIDATE_ATTESTED`. Реализация подтверждается публичным кодом в авторском репозитории, line ownership отдельно не аттестован | Не называть production pass LLVM upstream и не переносить результаты отбора на internship |
| C04 | Разрабатывает и сопровождает VpnMediator, им пользуются сотни человек | Сведения кандидата из `02_CANDIDATE_FACTS...`, B; [открытый кейс](https://github.com/Misha1302/CV/blob/main/cases/ru-vpn.html) | Число пользователей `CANDIDATE_ATTESTED`; владение продуктом — заявление кандидата | Не превращать «сотни пользователей» в MAU, paid users, 24/7 availability или RPS |
| C05 | ASP.NET Core Mediator и отдельный Python Telegram Bot; SQLite | `VpnMediator` private main `8d1b9d6685dd1af63886136b4565d0d7ba61ab96`, `Program.cs` и `MediatorStorage.cs` (`SqliteMediatorRepository`); `VpnAccessBot/vpn_access_bot/payment_processing.py` | `PRIVATE_CODE_AUTHORIZED`; архитектура проверена по исходникам | Telegram Bot — Python, а не C#; PostgreSQL относится к другим проектам |
| C06 | Идемпотентная запись событий/согласование и тестируемое восстановление платежей | VpnMediator private commit выше: `VpnAccessBot/tests/test_payment_recovery.py`: `test_payment_inbox_survives_restart_and_reconciles_order` (стр. 82), duplicate/conflict (164), claim lease (290), outbox once (341); `repositories.py` (`PaymentInboxRepository`), `yookassa_reconciliation.py` | `PRIVATE_CODE_AUTHORIZED`; тест-кейсы существуют, **не запускались** в этой сессии | Реализация YooKassa recovery не подтверждает промышленный go-live YooKassa/SBP; не приписывать все строки лично |
| C07 | Release workflow: backup, readiness, atomic switch/rollback | VpnMediator private commit выше: `update_vpn_mediator.sh`, `docs/canary-rollback-plan.md`, `docs/release-checklist.md`, `Program.cs` (`/health/live`, `/health/ready`) | `PRIVATE_CODE_AUTHORIZED` + `REPO_DOCUMENTATION`. Скрипты и чек-листы проверены, действующий release-host — нет | Самоописанный PASS в репозитории != заново проверенный production rollout |
| C08 | UniversalToolchain фиксирует типизированный immutable LanguagePlan | UT master `5626a5e7fdd1c5d85158fab21752ef74c34926a3`: [LanguagePlan.cs](https://github.com/Misha1302/UniversalToolchain/blob/5626a5e7fdd1c5d85158fab21752ef74c34926a3/UniversalToolchain/UniversalToolchain.LanguageSdk/LanguagePlan.cs), [LanguagePlanVerifier.cs](https://github.com/Misha1302/UniversalToolchain/blob/5626a5e7fdd1c5d85158fab21752ef74c34926a3/UniversalToolchain/UniversalToolchain.LanguageSdk/LanguagePlanVerifier.cs) | `PUBLIC_CODE`; архитектурная роль кандидата `CANDIDATE_ATTESTED` | План проверяет representable typed contracts и route identity, не является доказательством семантики всех возможных модулей |
| C09 | UT: Bytecode/AIR, interpreter/CIL, 1324 теста в манифесте | [CURRENT_ARCHITECTURE_STATUS.md](https://github.com/Misha1302/UniversalToolchain/blob/5626a5e7fdd1c5d85158fab21752ef74c34926a3/docs/CURRENT_ARCHITECTURE_STATUS.md), [eng/test-counts.json](https://github.com/Misha1302/UniversalToolchain/blob/5626a5e7fdd1c5d85158fab21752ef74c34926a3/eng/test-counts.json) | `REPO_DOCUMENTATION` + manifest `PUBLIC_CODE`; **1324 — заявленная сохранённая сумма, не новый прогон** | Wist 0.1.0-alpha.7 source candidate не считать опубликованным NuGet-релизом |
| C10 | Quark2 напрямую исследует CLR/CIL, DynamicMethod, native pointer и benchmark | Quark2 master `7bc718a2fd518559ec7c344942eec879216584bb`: [RuntimeHacks.cs](https://github.com/Misha1302/Quark2/blob/7bc718a2fd518559ec7c344942eec879216584bb/RuntimeHacks/RuntimeHacks.cs), [TranslatorBenchmarks/Program.cs](https://github.com/Misha1302/Quark2/blob/7bc718a2fd518559ec7c344942eec879216584bb/TranslatorBenchmarks/Program.cs), [QuarkBenchmarks/QuarkTest.cs](https://github.com/Misha1302/Quark2/blob/7bc718a2fd518559ec7c344942eec879216584bb/QuarkBenchmarks/QuarkTest.cs) | `PUBLIC_CODE`, экспериментальная реализация | Reflection в приватный API несовместим с переносимым production ABI, результат ускорения не заявлен; `dotnet/runtime` upstream PR отсутствует в проверенных доказательствах |
| C11 | Native x86-64 backend: register allocation, spills, phi lowering, differential run | [crates/alloc/src/lib.rs](https://github.com/Misha1302/x86-64-codegen-ra-playground/blob/dd0693c3af06dc9a3612b68ecb94f9637d6b0514/crates/alloc/src/lib.rs), [crates/codegen/src/emitter.rs](https://github.com/Misha1302/x86-64-codegen-ra-playground/blob/dd0693c3af06dc9a3612b68ecb94f9637d6b0514/crates/codegen/src/emitter.rs), repo root | `PUBLIC_CODE`; direct low-level work visible | Поддерживаемое i64-подмножество, не полный LLVM/x86 ISA и не песочница недоверенного кода |
| C12 | Межпроцедурный анализ effects и условия допустимости global-IV преобразования | [src/PromotionLegality.cpp](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization/blob/0d759dcf3af7a5652432eb0fea5b9ca27ec88f74/src/PromotionLegality.cpp), `MustExecute` и guards for exceptions/atomics | `PUBLIC_CODE`; результат тестов 29 scenarios `REPO_DOCUMENTATION` | Не универсально доказанная коррекция любых LLVM-программ |
| C13 | TuringSquare-LMS: PostgreSQL Serializable/FOR SHARE, TBank authoritative re-read; проект не запущен | Fedora `/home/micodiy/razakov/sites/TuringSquare-LMS`, `codex/turingsquare-full-implementation` at `bb9f577a93a73ff2eb446f5548e12363626a41bf` (2026-11-01); `src/CompilationLab.InternalService/Application/Payments/CoursePurchaseOrderService.cs`, `CourseTBankPaymentService.cs`; GitHub main **другая ревизия** `17ac3fd19b3ad3a2cea053689af21a7d1798a9ac` | `PRIVATE_CODE_AUTHORIZED` / user working copy. Кандидат — требования/архитектурный контроль/ревью; часть реализации агентами | T-Bank sandbox; one-time/subscription без user coin wallet; не production, не весь код личный |
| C14 | НИЯУ МИФИ «Юниор» 2026, диплом I степени; LangDev 2026 программа | [Список победителей 2026](https://olymp.mephi.ru/junior/winners/2026), [LangDev 2026 program](https://langdevcon.org/2026/program.html) | `OFFICIAL_EXTERNAL`. Утверждение о фактическом выступлении также от кандидата | Диплом — не доказательство рабочего грейда и не коммерческий опыт |
| C15 | Существуют исторические assembler/runtime и Roslyn-proекты | [OwnAssembler](https://github.com/Misha1302/OwnAssembler), [Wist2Msil](https://github.com/Misha1302/Wist2Msil) (README предупреждает: исторический), [Aochivapi](https://github.com/Misha1302/Aochivapi), [Visk](https://github.com/Misha1302/Visk), [DerefAfterNullAnalyzer](https://github.com/Misha1302/DerefAfterNullAnalyzer) (CFG/data-flow + ограничения), [ps_form_analizer](https://github.com/Misha1302/ps_form_analizer) (C17, memory dependence) | Реальное наличие репозиториев `PUBLIC_CODE`; выборочная проверка README/описаний. Полноценный code audit этих исторических репозиториев **не выполнен** | Нельзя делать вывод об их полноте, актуальности или измеренном качестве только из присутствия в GitHub |
| C16 | Личный опыт чтения CoreCLR, performance/memory analysis и оптимизации x64 | Уточнения кандидата в пакете, `Quark2` эксперименты и BenchmarkDotNet как косвенное подтверждение | `CANDIDATE_ATTESTED` + частично `PUBLIC_CODE` | Fork [Misha1302/runtime](https://github.com/Misha1302/runtime) зафиксирован на upstream коммитах ноября 2023; поиск PR владельца `Misha1302` в `dotnet/runtime` вернул 0 записей. Нет проверенного upstream .NET Runtime коммита, версии среды и чисел ускорения; из публичного CV исключены крупные неподтверждённые claims |

### Примечания о provenance и личном вкладе

1. `git log author=Михаил` на рабочих ветках Codex **не** доказывает, что код набран вручную. Надёжно можно говорить о проектировании требований, постановке проверок, организации работы и code review; по каждому конкретному файлу авторство нужно доказывать отдельной историей PR, перепиской или личным commit/diff.
2. Код VpnMediator и пользовательские базы приватны: публичным доказательством для работодателя служит [открытый кейс](https://github.com/Misha1302/CV/blob/main/cases/ru-vpn.html), а не ссылки на недоступные private files.
3. GitHub CV `03a34350fe2fc6dcffc0b181e0379e189e511939` проверялся отдельно от сохранённого HTML-снимка 16.10.2026; в прежнем шаблоне коммерческий год и Quark2 были раскрыты недостаточно. Текущий публичный CV **не изменялся**.
4. На Fedora локальный checkout UT находится на исследовательской ветке сентября 2026, VpnMediator checkout — на более старом июньском commit. **Они не заменяли** текущие GitHub master/main. LMS напротив проверена именно на поздней локальной ветке, а не по отстающему GitHub main.
5. Тесты UT/VpnMediator/LLVM и LMS целиком **не запускались** в этой сессии; это ревью кода, тестов и репозиторных манифестов, а не независимая сертификация correctness.

## 3. Сверка проектов и позиционирование

| Кейс | Что хорошо продаёт | Что не продавать |
|---|---|---|
| VpnMediator | реальный сервис, C# API, state/recovery, Linux/release discipline | платёжную систему Python как «целиком .NET», непроверенные RPS/MAU, production YooKassa |
| ИСП РАН | реальный профессиональный опыт статического анализа C# и символьных вычислений | «обучал ИИ/построил модель» без личного proof |
| МЦСТ | LLVM legality, тестируемость оптимизаций, performance reasoning | отбор 104/104 как результат работ в МЦСТ |
| UT | typed contracts, deterministic planning, CLR pipeline | универсально доказанный compiler, upstream/commercial adoption |
| Quark2 | реальное копание в CLR, динамический CIL, benchmark methodology | производственный JIT, предсказуемое ускорение без чисел |
| LMS | SQL locking/consistency, authorization, инженерное ревью agent-produced code | production payments, личное авторство всего репозитория |
| Rust codegen | низкоуровневая глубина, проверка backends | полноценный промышленный компилятор |

**ATS CV** начинается с backend+стека+опыта, VPN и UT укрупнены, LMS сжата. **Tech Lead CV** показывает 4 инженерные проблемы и ссылается на код. **Runtime CV** углубляет языковые маршруты, CLR и x86, но сохраняет внятную коммерческую подложку. Все версии описывают **одного кандидата** и не создают три противоречащие биографии.

## 4. Рынок РФ: реальные примеры, проверенные 03.11.2026

Ниже **не статистика рынка** и **не перечень гарантированно открытых вакансий**: содержимое страниц быстро меняется. Приведены датированные объявления октября 2026. «Подходит» означает *сопоставление по задачам*, не обещание прохождения формальных фильтров. Для собственной логистики учитывай доступную нагрузку и формат, не раскрывай её автоматически в резюме.

| Приоритет | Работодатель / должность | Дата на странице | Формат / требования | Комментарий для отклика |
|---|---|---|---|---|
| **A** | [Action tech — Разработчик C# (.NET)](https://career.habr.com/vacancies/1000129519) | 26.10.2026 | Middle, удалённо; .NET Core, ASP.NET, EF, PostgreSQL, SQL, unit tests | Лучшее соответствие предметным кейсам. Рекомендуется прямое письмо разработчикам с кейсом VpnMediator; заранее проверить рабочую нагрузку |
| **B** | [МТС Web Services — C# Telco Platform](https://career.habr.com/vacancies/1000168153) | 31.10.2026 | Middle на площадке; remote, Kafka/Oracle/Pg, highload | Содержательно близки платежные состояния, но highload/Kafka/Oracle и team ownership не доказаны; обоснованный stretch |
| **C** | [«Лоция» — .NET стажёр](https://career.habr.com/vacancies/1000168354) | 27.10.2026 | Intern, remote, договор 3 мес., REST/SQL/PostgreSQL; до 30 ч/нед. | По стеку подходит, но технический уровень может быть ниже и требования к графику следует сверить до отклика |
| **D** | [Extyl — .NET аутстафф](https://career.habr.com/vacancies/1000166928) | 29.10.2026 | Middle remote, **от 3 лет**, обязательный Diasoft FA#, ИП/самозанятость | **Не откликаться без Diasoft FA#**; пример фильтра, который не компенсирует compiler depth |
| **D** | [Extyl — .NET / MS SQL аутстафф](https://career.habr.com/vacancies/1000166905) | 29.10.2026 | Middle, первый период офис, полная занятость, от 3 лет | Не совпадают формальные условия/график/стаж; не приоритет |
| **D** | [Extyl — .NET Solar/Lekton](https://career.habr.com/vacancies/1000167056) | 30.10.2026 | Middle remote, 3+ .NET и 2+ Solar/Lekton, full-time | Не подходит без узкой платформенной экспертизы |
| **D** | [«Лоция» — Технический руководитель .NET](https://career.habr.com/vacancies/1000168727) | 31.10.2026 | Lead remote, архитектура, Kafka/Redis, management | Не соответствует задокументированной team leadership истории |
| **D** | [Employ City — Senior .NET](https://career.habr.com/vacancies/1000169572) | 29.10.2026 | Lead remote, 5+ лет, Kafka/Rabbit/NoSQL/1000 RPS | Контрольный отрицательный пример: его требования **не** доказывают наличие этого у кандидата |
| **D** | [ПлеядаТех — C#/.NET](https://career.habr.com/vacancies/1000169343) | 19.10.2026 | Senior remote, ASP.NET/MongoDB/Kubernetes | Не заявлять Senior без требуемого соответствия |

Дополнительная выдача hh.ru, не заменяющая прямую вакансию: [Middle .NET remote, Москва](https://hh.ru/vacancies/middle-net-developer/udalennaya_rabota), на дату анализа там присутствовали «Институт Инноваций и Права» (1–3 года, удалённо), SkillStaff (1–3 года) и более senior-ориентированные предложения. Для непосредственного отклика проверить карточку и дату ещё раз.

**Вывод по грейду:** на интервью для Middle Backend *можно выходить* там, где индивидуально оценивают консистентность данных, код и диагностику, не требуя фиксированного числа лет. На строгих HR-фильтрах «3–5 лет коммерческого backend, Kafka at scale, прод-дежурства» вероятен автоматический отсев. На compiler/runtime ролях сильнее конкурентное преимущество по глубине, но нужно доказывать собственный вклад и тестируемость.

## 5. Red-team: 11 независимых причин отказа и редакторское исправление

| Кто возражает | Возможная причина отказа | Что проверено / сделано |
|---|---|---|
| HR | «Где именно коммерческий год?» | В каждой версии — **год суммарного смешанного коммерческого опыта**, отдельным пунктом. Работодателей и неуточнённый календарь не выдумывали; это остаётся главным слабым местом |
| HR | «Слишком много compiler-навыков, а нужен API» | В `01` начинаем с C#/ASP.NET Core/SQL, опыт и VPN раньше UT; отдельно compiler CV |
| Тимлид | «Сотни пользователей — откуда число?» | Сохранено только то, что сообщил владелец; не указаны RPS/MAU/платёжная конверсия; публичный кейс и вопрос о телеметрии |
| Тимлид | «Вы выдаёте Python Telegram Bot за .NET?» | Прямо разделены Python Bot и ASP.NET Core Mediator, SQLite обеих частей |
| Тимлид | «Реально обработали платёжные гонки?» | Проверены конкретные `test_payment_recovery.py` кейсы: restart, conflicts, claim, outbox once; no fresh test run claim |
| Staff .NET | «Quark2 нарушает приватные CLR API, зачем в CV?» | Уточнено: исследование internals/benchmark, не готовый production JIT и не upstream patch |
| Staff Compiler | «UT типизированный план доказывает семантическую совместимость?» | Нет; в отчёте явно ограничили гарантии синтаксическими/структурными контрактами и verifier; не заявляется глобальная формальная верификация |
| Тимлид | «LMS уже запущена? Кто писал код?» | Указано **в разработке / sandbox**, архитектура + QA/review + агентная реализация, без единоличного авторства |
| HR/ATS | «Одностраничный CV читабелен? Контакты доступны?» | Перед финалом все версии вышли на 2 страницы с висящим последним разделом. **Фактически исправлено**: конденсация без шрифта ниже 10pt, все три теперь 1 страница, contact/project URLs — OOXML hyperlinks |
| Рекрутер | «Провокационные оговорки отталкивают» | Удалены самозащитные фразы «не production патч», «не мой свежий тест» из публичного CV там, где граница выражена стадией и предметным описанием. Подробная доказательная оговорка перенесена в карту |
| Менеджер | «Можно ли доверять написанному при агентной разработке?» | Обозначен архитектурный и ревью-вклад человека; git author field **не** признан доказательством ручной реализации |

**Явная итерация:** первый программный рендер дал `01:2 страницы`, `02:2`, `03:2` с отдельными короткими блоками на последней странице. После независимого чтения внесены изменения в типографику, сокращена защитная и повторяющаяся речь, переданы ссылки в обычный текст и затем — в настоящие кликабельные OOXML hyperlinks. Итоговая PDF-проверка: каждая версия **1 страница**. Это конкретные исправления после ревью, не обещание будущего.

## 6. 10 вопросов, на которые стоит ответить на собеседовании

1. При каких условиях Telegram Stars платёж может прийти повторно, а выдача entitlement — только один раз? Покажите цепочку inbox → claim → order → outbox.
2. Что произойдёт после падения процесса между записью денег и выдачей доступа? Где хранится доказательство выполнения шага?
3. Чем state в SQLite каждого сервиса согласован с upstream provider? Что нельзя решить локальной транзакцией?
4. Что делать при спорящих payment evidence для одного charge? Почему нужен manual review?
5. Почему `Serializable` в PostgreSQL сам по себе не заменяет бизнес-идемпотентность и уникальные ограничения?
6. В каком смысле `LanguagePlan` immutable и какие ошибки проверяет `LanguagePlanVerifier`? Чего он не способен доказать?
7. Как устроен parity test между interpreter и CIL? Что считать наблюдаемым поведением?
8. Почему LICM не должен выносить instruction с mayReadOrWriteMemory без alias/effects доказательств? Какие контрпримеры?
9. Чем отличается `DynamicMethod.Invoke` от делегата/native pointer, и почему сравнение нужно прогревать и измерять на конкретной платформе?
10. Как проверяется корректность phi-lowering при циклах parallel moves и spills? Какие свойства подтверждает differential execution, а какие нет?

## 7. План укрепления доказательств и подготовки GitHub

**Публичные GitHub pins** в рекомендуемом порядке: `UniversalToolchain`, `Quark2`, `DerefAfterNullAnalyzer`, `x86-64-codegen-ra-playground`, `LLVM-interprocedural-global-IV-optimization`, `VpnMediator-public` (если содержимое действительно безопасно публиковать). Сайт CV может ссылаться на эти кейсы, но его обновление не выполнялось.

Для каждого pinned репозитория желательно 4 предложения в README: **задача**, **что лично сделал**, **минимальная воспроизводимая команда**, **граница доказанного**. Ссылки на `LanguagePlan.cs`, `LanguagePlanVerifier.cs`, Quark benchmark и тесты платежного восстановления ценнее списка из 30 технологий. Не размещать пользовательские данные, токены, журналы заказов или приватные конфиги.

**5 наиболее полезных уточнений, если позже решите собрать доказательства:**

1. **Коммерческие проекты:** для каждого — работодатель/заказ, месяцы, функция, какой компонент написан лично, контакт/акт/коммит. Это позволяет заменить неопределённое «1 год суммарно» на достоверную строку опыта.
2. **VpnMediator:** обезличенная телеметрия *конкретного* показателя (зарегистрированные / воспользовавшиеся / активные за N дней), срок эксплуатации, пример реального инцидента и собственное действие при устранении. Не нужны персональные данные пользователей.
3. **ИСП РАН:** безопасно публикуемая формулировка личного task-scope: контракты метаданных, результаты, тесты и степень законченности, без закрытого кода.
4. **Quark2/performance:** версия .NET, CPU, конфигурация benchmark, warmup, distributions, аллокации, сравнимые эталоны, commit; без этого не добавлять speedup.
5. **Авторство UT/LMS:** 2–3 собственных PR/diff с рецензией, решения архитектуры и отчёты о принятых/отклонённых агентных изменениях. Разделить design, manual code, code review и agent execution.

## 8. Технический контроль итоговых файлов

- A4, одна колонка, нормальная последовательность чтения, **Noto Sans 10 pt** в основной верстке; заголовки и роль крупнее; нет таблиц/плавающих блоков в CV.
- Все три DOCX были отрендерены в PDF и PNG; PDF проверены после финальной итерации на количество страниц, Unicode text extraction и наличия URI links. Содержимое Markdown и DOCX генерируется из одного набора формулировок.
- Тексты составлены без возраста, даты рождения, ограничений часов, фиктивного full-time и выдуманных KPI. В исходном исследовательском пакете такие условия есть, но **не в материалах работодателю**.
- **Не проверено:** реальный ATS работодателя, собеседование/грейд, актуальность открытости вакансий после 03.11.2026, эксплуатационные числа с независимым мониторингом, личные contribution percentages, запуск тестов проектов в этой сессии.
