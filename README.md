# Mikhail Razakov — targeted CV variants v32

Статический bilingual-пакет целевых инженерных резюме и подробного технического портфолио.

## Флагманские версии

- `ru-compiler.html` / `en-compiler.html` — compiler/runtime и typed language composition: callable-first SSA, Wist и experimental PlanFuzz.
- `ru-devtools.html` / `en-devtools.html` — compiler testing, configuration-aware fuzzing, diagnostics и reproducible evidence.
- `ru-cpp-systems.html` / `en-cpp-systems.html` — C++ systems, program analysis, алгоритмические компоненты и low-level codegen.

## Специализированные версии

- Algorithms — solver/research engineering.
- Backend — .NET-сервисы с платежами, состоянием и восстановлением.
- Reliability — reliability-focused backend, не SRE-overclaim.
- EdTech — backend для образовательных продуктов.
- Full portfolio — follow-up материал, не первое вложение.

## Что изменилось в v32

- Wist2 сформулирован как typed language composition/runtime SDK, а не как широкий grammar/type-system workbench.
- PlanFuzz явно обозначен как experimental tooling; указан фактический scope: language-neutral core, Acme adapter и ограниченный Wist Int32 adapter.
- Canonical gate синхронизирован с Wist2: 1 465/1 465 тестов, 0 failures/skips, 9 packages и clean consumers; source commit `ee218b4b5b5c6648ab74df2d54a8a906bd2e30db`.
- В Compiler опыт callable-first SSA и PlanFuzz разделён на независимые evidence claims.
- В DevTools test-count proof заменён на deterministic program/plan reduction.
- В C++ Systems обязательная гигиена toolchain заменена доказательством масштаба — stress-gates до 500 тыс. вершин.
- Названия публичных проектов в PDF стали прямыми кликабельными ссылками.
- Флагманские PDF используют отдельную roomy-плотность и проверяются на заполнение страницы.
- CI проверяет ATS-порядок, direct project links, актуальные canonical facts, clean rebuild parity и recursive manifest.

## Использование

Для первого контакта отправлять профильный PDF. HTML использовать как подробное техническое портфолио на следующем этапе.

## Canonical sources

- Wist2 verification: `Misha1302/Wist2@ee218b4b5b5c6648ab74df2d54a8a906bd2e30db`.
- Release metadata: `RELEASE-METADATA.md`.
- Targeting: `TARGETING.md`.
- QA: `QA-report-targeted-cv-v32.md`.

## Baseline

Предыдущая версия: v31, merge commit `0c13b0617c5e06b09b7223247fb77c6010fa9d8b`.

## Контакт

misha13022008@gmail.com
