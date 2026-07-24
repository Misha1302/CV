# Mikhail Razakov — targeted CV variants v26

Статический bilingual-пакет целевых инженерных резюме и подробного технического портфолио.

## Флагманские версии

- `ru-compiler.html` / `en-compiler.html` — compiler/runtime, IR/SSA, оптимизации, program analysis и проверка семантики.
- `ru-devtools.html` / `en-devtools.html` — compiler testing, diagnostics, generative testing и release tooling.
- `ru-cpp-systems.html` / `en-cpp-systems.html` — C++ systems, program analysis, алгоритмические компоненты и low-level backend experiments.
- `ru-algorithms.html` / `en-algorithms.html` — алгоритмическая инженерия: `AdvancedAlgorithms`, PS-form Analyzer и оптимизации Wist2.

## Дополнительные версии

- `ru-backend.html` / `en-backend.html` — .NET backend.
- `ru-platform.html` / `en-platform.html` — service reliability и эксплуатация.
- `ru-edtech.html` / `en-edtech.html` — EdTech backend.
- `ru.html` / `en.html` — полное техническое портфолио. Для первого отклика предпочтительнее короткая профильная версия.

## Изменения v26

- Assembly вынесен в верхнюю часть compiler и C++ systems профилей: `x86 / x86-64 Assembly`, `NASM/FASM`, ABI, x87 и анализ compiler output видны до чтения деталей.
- Существующий codegen-проект объединён с подтверждаемым ручным NASM-опытом: IA-32/cdecl, стек, libc, структуры/адресация и x87; x86-64 lowering/emission описан отдельно.
- Добавлена ссылка на публичный `Nasm-X86-Course`; IA-32-содержание курса не смешивается с x86-64 codegen-лабораторией.
- Обновлены RU/EN compiler, C++ systems и полные технические страницы; четыре профильных PDF пересобраны и проверены.
- Образование остаётся обезличенным: только статус студента НИУ ВШЭ без года выпуска.

## Контакт

misha13022008@gmail.com

## Baseline

Предыдущая версия репозитория: targeted CV variants v25, commit `d752a7c9dc23058f21bf4d5e3f694b118438a0d7`.

## Публикация

PDF можно отправлять напрямую. Перед отправкой ссылки `misha1302.github.io/CV/` нужно обновить публичный репозиторий `Misha1302/CV`; этот архив сам по себе GitHub Pages не изменяет.
