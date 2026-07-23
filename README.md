# Mikhail Razakov — targeted CV variants v25

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

## Изменения v25

- Переписан проблемный раздел компетенций в compiler RU/EN: вместо смеси русских и английских заголовков и перечня ключевых слов используются четыре ясных блока — архитектура и IR, анализ и оптимизации, проверка корректности, языки и инструменты.
- Полные `ru.html` / `en.html` получили такую же содержательную иерархию: основной профиль отделён от дополнительной backend/system-компетенции.
- На всех 16 страницах резюме неоформленный `skills-grid` заменён на существующий строковый компонент `stack-lines`; разделы теперь имеют устойчивую визуальную структуру на desktop и mobile.
- В русской compiler-версии дополнительно очищены описания hero и проектов: устранены ненужные англоязычные рекламные вставки, а `AdvancedAlgorithms` описан как самостоятельная библиотека, а не «подтверждение» навыков.
- Compiler PDF RU/EN пересобраны с теми же исправленными формулировками. Остальные 12 профильных PDF перенесены без изменений из проверенного v24.
- Cache-busting локальных CSS/JS обновлён до `?v=25`.

## Контакт

misha13022008@gmail.com

## Baseline

Предыдущий release: `mikhail-razakov-targeted-cv-v24-2026-07-23.tar.xz`  
SHA-256: `ca01f7676fa8bdec3186383fa9e632abcd2e3c93463a92e688436fbd0d3b08bb`

## Публикация

PDF можно отправлять напрямую. Перед отправкой ссылки `misha1302.github.io/CV/` нужно обновить публичный репозиторий `Misha1302/CV`; этот архив сам по себе GitHub Pages не изменяет.
