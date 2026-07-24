# Mikhail Razakov - targeted CV variants v29

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

Предыдущая версия репозитория: v28, commit `d655f6854a1d5ac8d87393cc1f4c82567ac1ddee`.

## Публикация

Для первого контакта отправлять профильный PDF. HTML-страницы остаются подробным публичным портфолио.
