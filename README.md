# Mikhail Razakov - targeted CV variants v27

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

## Изменения v27

- Четыре флагманских PDF получили отдельный print-only A4-макет; полный сайт больше не уменьшается до нечитаемого масштаба.
- PDF экспортируются строго при scale=1.0; сборка падает при переполнении, шрифте меньше 7.5 pt, второй странице или пропавшем текстовом маркере.
- Assembly scope уточнён: NASM IA-32/CDECL/x87 отделён от x86-64 SysV code generation через iced-x86; неподтверждённые FASM и обобщённый full-ABI claim удалены.
- В compiler-профиле восстановлена иерархия Wist2 -> program analysis -> x86 codegen; Assembly остаётся сильным доказательством, но не заменяет основной профиль.
- Преподавательская формулировка больше не создаёт впечатление, что все около 50 учеников изучали NASM.
- Wist2 baseline обновлён до пользовательского полного прогона: 1 358 тестов пройдены, 0 сбоев, сборка успешна.
- README, release metadata, QA, targeting, language/content/fact/link/experience audits синхронизированы как v27.

## Контакт

misha13022008@gmail.com

## Baseline

Предыдущая версия репозитория: v26, commit `6a67ea16513f08772a17c3aee19c0135d437cc2b`.

## Публикация

Для первого контакта отправлять профильный PDF. HTML-страницы остаются подробным публичным портфолио.
