# Mikhail Razakov — targeted CV variants v31

Статический bilingual-пакет целевых инженерных резюме и подробного технического портфолио.

## Флагманские версии

- `ru-compiler.html` / `en-compiler.html` — compiler/runtime и языковые платформы: typed cross-package plans, callable-first SSA, Wist и PlanFuzz.
- `ru-devtools.html` / `en-devtools.html` — compiler testing, configuration-aware fuzzing, diagnostics и reproducible evidence.
- `ru-cpp-systems.html` / `en-cpp-systems.html` — C++ systems, program analysis, алгоритмические компоненты и low-level codegen.

## Специализированные версии

- `ru-algorithms.html` / `en-algorithms.html` — algorithm / solver engineering.
- `ru-backend.html` / `en-backend.html` — .NET backend с платежами, состоянием и восстановлением.
- `ru-platform.html` / `en-platform.html` — reliability-focused .NET backend; не отдельная SRE-специализация.
- `ru-edtech.html` / `en-edtech.html` — EdTech backend.
- `ru.html` / `en.html` — полное техническое портфолио для follow-up, не замена целевому PDF.

## Что изменилось в v31

- Compiler RU/EN теперь начинаются с типизированного Language Authoring SDK: cross-package routes, deterministic pass ordering, exact manifest binding и fail-closed runtime selection.
- Compiler Tools RU/EN перестроены вокруг PlanFuzz: семь oracle families, fresh-process confirmation, exact fingerprints и deterministic program/plan reduction.
- Callable-first SSA показан как descriptor-driven semantics с effects, determinism и trust, а не как перечень отдельных оптимизаций.
- Канонический Wist2 gate обновлён до `1 459 / 1 459` тестов, 0 падений, 0 предупреждений/ошибок сборки, 9 проверенных packages и clean consumers.
- Все версии используют единый статус образования: программа «Программная инженерия» НИУ ВШЭ / Software Engineering at HSE University.
- Награда Балтийского конкурса унифицирована как диплом I степени и Главная премия «Совершенство как надежда».
- Selector выделяет три флагманские версии, а продуктовые варианты помечены как специализированные.
- Все 14 targeted PDF воспроизводимо генерируются из `data/cv-print-profiles.json` через `tools/build_cv.py`.
- Permanent CI пересобирает PDF в чистой директории и проверяет A4, одну страницу, scale 1.0, текстовый слой, ссылки, минимальный кегль 8.4 pt, канонические факты и `MANIFEST.sha256`.

## Использование

Для первого контакта отправлять профильный PDF. HTML-страницы использовать как подробное публичное портфолио на следующем этапе общения.

## Канонические источники

- Wist2 verification record: 2026-07-25.
- CV release metadata: `RELEASE-METADATA.md`.
- Targeting guide: `TARGETING.md`.
- Release QA: `QA-report-targeted-cv-v31.md`.

## Baseline

Предыдущая версия: v30, merge commit `dd725723029479767fadc788b925ad2dfdcb4f4e`.

## Контакт

misha13022008@gmail.com
