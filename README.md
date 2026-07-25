# Mikhail Razakov - targeted CV variants v31

Статический bilingual-пакет целевых инженерных резюме и подробного технического портфолио.

## Флагманские версии

- `ru-compiler.html` / `en-compiler.html` - compiler/runtime, IR/SSA, оптимизации и program analysis.
- `ru-cpp-systems.html` / `en-cpp-systems.html` - C++ systems, program analysis, алгоритмические компоненты и low-level codegen.
- `ru-devtools.html` / `en-devtools.html` - compiler testing, diagnostics, generative testing и release tooling.
- `ru-algorithms.html` / `en-algorithms.html` - алгоритмическая инженерия: AdvancedAlgorithms, PS-form Analyzer и оптимизации Wist2.

## Дополнительные версии

- `ru-backend.html` / `en-backend.html` - .NET backend.
- `ru-platform.html` / `en-platform.html` - service reliability и эксплуатация.
- `ru-edtech.html` / `en-edtech.html` - EdTech backend.
- `ru.html` / `en.html` - полное техническое портфолио для технического follow-up, не замена целевому PDF.

## Изменения v30

- Compiler RU/EN подтверждают актуальный статус: студент программы «Программная инженерия» НИУ ВШЭ / Software Engineering student at HSE University.
- Wist2 proof strip привязан к полному прогону 23.07.2026 без старых qualifiers от 14 июля.
- LLVM-направление возвращено в focused PDF и связано с C++23 graph-analysis infrastructure.
- Proof cards упорядочены как инженерная глубина → внешняя оценка → корректность; тестовый claim раскрывает IR transforms, contracts и interpreter/CIL parity.
- Русский Compiler PDF языково вычищен, typographic defect в Wist2 project card исправлен, teaching block переосмыслен как technical communication.
- Compiler RU/EN PDF пересобраны и проверены на A4, одну страницу, scale=1.0, читаемость, ATS-порядок, ссылки и отсутствие overflow.

## Изменения v29

- Подробные HTML-страницы синхронизированы с актуальным Wist2 baseline: 1 358/1 358 тестов, 0 сбоев, сборка успешна; удалены устаревшие 75 проектов / 1 325 тестов.
- Удалено дублирование `differential testing`; формулировки про codegen снова содержат метрики spills/code size.
- Русская C++ systems-версия языково вычищена: ключевые заголовки, алгоритмы и toolchain-описания переведены без потери технической точности.
- В focused PDF восстановлена конкретика по двум профилям «Высшей пробы», сохранены точные категории первых результатов «Юниора» и Балтийская Главная премия.
- Минимальный шрифт четырёх focused PDF поднят до 8.5 pt при A4, одной странице и `scale=1.0`; ATS-порядок и ссылки перепроверены.
- README, release metadata, QA, targeting и evidence-аудиты синхронизированы как v29.

## Изменения v28

- В блоке достижений явно указаны два первых результата по итоговому баллу во Всероссийском конкурсе «Юниор»: направление «Инженерные науки» (2025) и секция «Информационные технологии» (2026).
- Балтийская награда названа точно: диплом I степени и Главная премия «Совершенство как надежда».
- RU/EN web-версии и focused compiler/C++ systems PDF синхронизированы; формулировка «1-е место в РФ» не используется без категории.

- Четыре флагманских PDF получили отдельный print-only A4-макет; полный сайт больше не уменьшается до нечитаемого масштаба.
- PDF экспортируются строго при scale=1.0; сборка падает при переполнении, шрифте меньше 7.5 pt, второй странице или пропавшем текстовом маркере.
- Assembly scope уточнён: NASM IA-32/CDECL/x87 отделён от x86-64 SysV code generation через iced-x86; неподтверждённые FASM и обобщённый full-ABI claim удалены.
- В compiler-профиле восстановлена иерархия Wist2 -> program analysis -> x86 codegen; Assembly остаётся сильным доказательством, но не заменяет основной профиль.
- Преподавательская формулировка больше не создаёт впечатление, что все около 50 учеников изучали NASM.
- Wist2 baseline обновлён до пользовательского полного прогона: 1 358 тестов пройдены, 0 сбоев, сборка успешна.
- README, release metadata, QA, targeting, language/content/fact/link/experience audits синхронизированы как v28.

## Контакт

misha13022008@gmail.com

## Baseline

Предыдущая версия репозитория: v29, commit `fae03e5adb4152bd1aaa43e56f49d383dc8f9e6d`.

## Публикация

Для первого контакта отправлять профильный PDF. HTML-страницы остаются подробным публичным портфолио.


## Current release: v31

v31 performs a strong Wist2 positioning and reproducibility hardening:

- Compiler RU/EN now lead with typed cross-package language plans, exact manifest binding, callable-first SSA, the Wist facade and PlanFuzz;
- Compiler Tools RU/EN are rebuilt around PlanFuzz, seven oracle families, fresh-process confirmation, exact fingerprints and deterministic program/plan reduction;
- the canonical Wist2 gate is updated to 1,459/1,459 tests, 0 failures, 0 build warnings/errors, nine verified packages and clean consumers;
- all targeted variants use the canonical HSE Software Engineering education statement and one Baltic Grand Prize wording;
- Backend proof cards now prioritize deployed systems, payments/recovery and the actual .NET/PostgreSQL/Linux stack;
- the selector promotes three flagship variants and marks product variants as specialized;
- all 14 targeted PDFs now have generated print sources and are rebuilt at scale 1.0 from canonical profile data;
- `data/cv-print-profiles.json`, `tools/build_cv.py`, `tools/validate_cv.py` and the permanent CI workflow prevent future HTML/PDF/fact drift.

Verified Wist2 source: canonical integration record dated 2026-07-25.
Previous CV baseline: v30, merge commit `dd725723029479767fadc788b925ad2dfdcb4f4e`.
