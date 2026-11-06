# Ревью резюме Performance / Systems — 7 ноября 2026

Базовая ревизия CV: 931ca7e413d8cff98a668fb1b11a75d8240a317d.

## Решение

Переработаны две целевые версии из data/site.json: 02 Systems / Platform Engineer (вместо вводящего в заблуждение ожидания Tech Lead) и 03 Compiler / Runtime / Performance. 01 Backend ATS и общие факты об опыте оставлены неизменными. Старые имена 02_Tech_Lead, 03_Runtime_Compiler и URL страниц временно сохранены, чтобы не сломать существующие ссылки.

## Матрица проверяемости

| Объект | Проверенный код/источник | Границы утверждений |
|---|---|---|
| UniversalToolchain | [код, f362649](https://github.com/Misha1302/UniversalToolchain/tree/f362649872ca70cb924d5233eb965e3a71602015); LanguagePlan, LanguagePlanVerifier, backend contracts | Наличие тестов в манифесте не означает, что они только что запускались; нет утверждения о формальном доказательстве |
| LLVM Global-IV | [код, 0d759d](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization/tree/0d759dcf3af7a5652432eb0fea5b9ca27ec88f74); PromotionLegality и эффект-анализ | Экспериментальный pass; нет подтверждённых ускорений production |
| x86-64 backend | [код, dd0693](https://github.com/Misha1302/x86-64-codegen-ra-playground/tree/dd0693c3af06dc9a3612b68ecb94f9637d6b0514); SSA, liveness, verifier, native-vs-reference | Реализован ограниченный IR, не полный промышленный компилятор |
| Quark2 | [код, 7bc718](https://github.com/Misha1302/Quark2/tree/7bc718a2fd518559ec7c344942eec879216584bb); DynamicMethod/Reflection.Emit, BenchmarkDotNet | Микробенчмарки не доказывают ускорение веб-сервиса |
| VpnMediator | кейс CV и knowledge/resume-evidence.json | Архитектура по доступным исходникам; аудитория/uptime со слов кандидата |
| TuringSquare-LMS | кейс CV и knowledge/resume-evidence.json | В разработке, часть реализации агентами, оплаты sandbox; не подтверждён production |
| ИСП РАН, МЦСТ, коммерческий стаж | CV evidence knowledge | Даты, задачи и стаж из данных кандидата, независимые документы не проверены |

## Критические замечания и исправления

1. Должность Tech Lead/Software Architect предполагает многолетнюю ответственность за команды и production: в новой подаче Systems / Platform Engineer без искусственного seniority.
2. Прежняя compiler-версия чрезмерно перечисляла ключевые слова; теперь объясняет цепочку analysis → legality → transformation → independent check.
3. Вынесена граница между проверкой корректности оптимизации и измерением производительности. Нет выдуманных speedup %, метрик CPU/GC или ETW.
4. Systems-версия показывает конкретные решения: отделение платежа от доступа, обработка повторов, provider reconciliation, backup/rollback, проверяемые module contracts.
5. Фактическое описание работы в ИСП РАН/МЦСТ и агрегированный коммерческий стаж не усилены без новых свидетельств.
6. Оба языка используют общий canonical source. Генерируемые файлы вручную не редактируются.

## Непокрытые требования найма

- Не показан воспроизводимый end-to-end результат оптимизации .NET: CPU profile, GC/allocations, p95/p99 до/после.
- Есть код LLVM оптимизации, но нет опубликованной оценки ускорения на корпусе стабильных нагрузок с проверкой семантики.
- Нет подтверждённого опыта архитектуры нескольких команд или назначения на Tech Lead.
- Сервисные метрики VpnMediator и готовность LMS требуют независимого evidence.

## План закрытия пробелов

1. Quark2: зафиксировать .NET/CPU/GC, повторить BenchmarkDotNet и доверительные интервалы, отделить cold/warm и micro от end-to-end.
2. UniversalToolchain: зафиксировать commit, одинаковые программы, сравнить interpreter/CIL результаты до метрик; отдельно измерять compile vs hot execute.
3. LLVM Global IV: зафиксировать LLVM, negative regressions, differential before/after и реальный workload; только затем публиковать ускорение.
4. VpnMediator: с обезличенными разрешёнными метриками измерить задержку восстановления, частоту повторов, p95/p99 и время сверки оплаты.

## Как отправлять

- 03 — compiler, LLVM, runtime, language tooling, исследовательская оптимизация.
- 02 — архитектура .NET-сервисов, platform, reliability/state correctness.
- 01 — стандартный backend / ATS.
- Для senior .NET performance с обязательным ETW/GC/low-level concurrency позиция пока не доказана.

## Проверка сборки

Требуются проверка фактов, генерация всех форматов, одна страница A4, видимые ссылки, PDF text-layer, двуязычная согласованность, тесты валидаторов и визуальный просмотр PDF/DOCX. Отдельная проверка CI нужна после отправки ветки.


## Результат локальной QA (2026-11-07)

- validate_resume_knowledge: PASS (35 evidence assets).
- build_site / build_cv / build_release: PASS.
- validate_release / validate_application_sites / validate_cv: PASS.
- Четыре PDF 02/03 RU/EN: 1 страница A4 каждый, минимальный измеренный размер текста 8.6 pt, нижняя граница текста 587–657 pt при высоте листа 842 pt, ссылки и текстовый слой присутствуют.
- Четыре DOCX 02/03 RU/EN: открыты LibreOffice и преобразованы в 1-страничные PDF каждый, конец текста 595–641 pt; визуально просмотрены PDF и DOCX RU, видимых обрезаний нет.
- Источник 01 Backend ATS и общие experience records проверены на неизменность до генерации; бинарные 01 PDF/DOCX восстановлены из baseline, чтобы исключить побочное переформатирование.
- Публичный GitHub CI / проверка сайтов браузером: независимый статус ещё не получен на момент этой записи.

Остаточные ограничения: скорость или финансовый эффект оптимизаций на целевых нагрузках не измерялись в этой задаче; зависимые проекты не собирались и их тесты заново не запускались.
