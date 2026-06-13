# Михаил Разаков — Compiler/Runtime Engineer

**Стажёр МЦСТ · создатель UniversalToolchain/Wist · C#/.NET · компиляторы · runtime · алгоритмы**

[Открыть сайт-резюме](https://misha1302.github.io/CV/) · [English version](https://misha1302.github.io/CV/en.html) · [GitHub](https://github.com/Misha1302) · [Telegram](https://t.me/Micodiy)

## Кратко

Я занимаюсь compiler/runtime engineering на .NET: frontend-ами языков, AST, Bytecode и AIR, интерпретаторами, CIL-кодогенерацией, JIT и оптимизацией hot path. Мой основной проект — [UniversalToolchain/Wist](https://github.com/Misha1302/Wist2), модульный framework для встраиваемых DSL с interpreter и compiled typed execution.

В 2026 году принят на стажировку МЦСТ по направлению «Системы программирования: компилятор LLVM». По итогам отбора занял первое место: **5,0/5,0** и единственный результат **104/104 теста** среди 49 присланных решений.

## Ключевые факты

- Первое место в отборе МЦСТ на LLVM-направление: 87 заявок, 49 решений, 6 мест.
- Призёр «Высшей пробы» по олимпиадному и промышленному программированию.
- Двукратный абсолютный победитель олимпиады «Юниор» НИЯУ МИФИ.
- Диплом I степени Балтийского научно-инженерного конкурса.
- Победитель «Высшего пилотажа» ВШЭ по Computer Science.
- Призёр регионального этапа ВсОШ по информатике, профиль «Программирование».
- Преподаю программирование с 2021 года; работал примерно с 50 учениками, включая студентов НИУ ВШЭ.

## Основной проект — UniversalToolchain/Wist

[Репозиторий](https://github.com/Misha1302/Wist2) · [Документация](https://misha1302.github.io/Wist2/) · [NuGet preview](https://www.nuget.org/packages/UniversalToolchain.Wist/0.1.0-preview.1)

- Pipeline: Source → Lexer/Parser → AST → Bytecode → AIR → Optimization → Backend → Execution.
- Interpreter backend и compiled execution через CIL/DynamicMethod.
- Модульная композиция языковых возможностей и declarative dialect files.
- Intrinsics, IR optimizers и semantic parity tests между backend-ами.
- CLI, application facade, GitHub Actions, NuGet package smoke tests и VitePress docs.
- BenchmarkDotNet, profiling и анализ generated CIL/assembly.

## Опыт преподавания

С 2021 года преподаю Python, C#, C/C++, Unity, алгоритмы и проектную разработку. Консультирую студентов ВШЭ по курсовым проектам: архитектура, алгоритмы, debugging, code review и подготовка к защите.

## Интересы

Compiler/runtime/JIT engineering, developer tools, performance и low-latency systems, database/query engines, системное R&D, теория графов и теория чисел.

## Публикации

- [«Моё видение универсального языка программирования»](https://habr.com/ru/articles/942134/)
- [Telegram-канал «Шиза и компиляторы»](https://t.me/shizaicompilers)

## Локальный просмотр

```bash
python3 -m http.server 8000
```

После запуска откройте `http://localhost:8000`.
