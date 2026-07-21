# Mikhail Razakov — targeted CV variants v18-quant

Статический пакет целевых инженерных резюме на русском и английском языках. Версия `v18-quant` добавляет отдельный профиль для software-engineering ролей в quantitative research и trading infrastructure, не выдавая целевую область за уже полученный профессиональный опыт.

## Страницы

- `ru-master.html` / `en-master.html` — полный инженерный профиль.
- `ru-quant.html` / `en-quant.html` — C++/Python, solver engineering, compiler/runtime infrastructure и differential validation для quantitative/trading infrastructure.
- `ru-compiler.html` / `en-compiler.html` — компиляторы, среды исполнения и анализ программ.
- `ru-algorithms.html` / `en-algorithms.html` — алгоритмы, C++23, solver engineering и анализ программ.
- `ru-backend.html` / `en-backend.html` — .NET-бэкенд, API, платежи и надёжность сервисов.
- `ru-platform.html` / `en-platform.html` — .NET-бэкенд, надёжность и эксплуатация сервисов.
- `ru-devtools.html` / `en-devtools.html` — инструменты разработчика и автоматизация.
- `ru-edtech.html` / `en-edtech.html` — EdTech/LMS и преподавательский опыт.
- `index.html` — выбор роли, языка и доступных PDF.

## Quantitative & trading infrastructure profile

Профиль построен для ранних software-engineering позиций, где важны алгоритмы, корректность и execution infrastructure:

- на первом месте находятся PS-form Memory Dependence Analyzer, UniversalToolchain/Wist2 и x86-64 codegen lab;
- результат отбора МЦСТ сформулирован как проверяемое достижение: 1-е место среди 49, единственная оценка 5,0/5,0 и единственный результат 104/104;
- Wist2 описан через фактические архитектурные результаты: lexer/parser → AST → Bytecode → AIR, interpreter/CIL execution, verifier-gated AIR → SSA → AIR и manifest-backed runtime composition;
- число 1 325 привязано к verification baseline от 14 июля 2026 года, а не представлено как постоянно актуальное состояние репозитория;
- x86-64 codegen project явно обозначен как educational laboratory;
- профиль не заявляет production trading, HFT, low-latency networking, alpha research, pricing models, PnL, Sharpe или профессиональный quant experience.

Новые страницы используют общие `style.css`, `script.js` и assets репозитория; существующие профили не изменены.

## PDF для откликов

Каталог `pdf/` содержит ранее проверенные двухстраничные A4-резюме. Для quantitative/trading infrastructure профиля PDF пока не добавлен: опубликована только браузерная RU/EN версия.

## Проверки

Self-review нового профиля находится в `QUANT_SELF_REVIEW.md`. Проверены:

- фактическая сдержанность и позиционирование;
- порядок чтения для HR и технического интервьюера;
- desktop/tablet/mobile layout;
- отсутствие горизонтального overflow;
- внутренние anchors и локальные assets;
- JSON-LD, языковые ссылки и mobile menu.

## Использование

Откройте `index.html` локально либо разместите содержимое каталога в корне GitHub Pages. Внутренние ссылки относительные. Внешние ссылки открываются в новой вкладке с `noopener noreferrer`.

Контактный email: `razakov.misha@mail.ru`.
