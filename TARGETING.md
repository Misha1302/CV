# Targeting guide

## Compiler / Runtime / Program Analysis

Отправлять `ru-compiler.html` / `en-compiler.html` в compiler, runtime, VM, static-analysis и language-engineering команды.

Иерархия доказательств:

1. UniversalToolchain/Wist2 — многоуровневый IR/runtime pipeline, AIR → SSA → AIR, optimization passes, structural verifiers и interpreter/CIL parity;
2. PS-form Analyzer — conservative program analysis, exact oracle и результат 1/49, 104/104;
3. x86-64 Codegen & Register Allocation Playground — liveness, live intervals, register allocation, codegen и interpreter-vs-native validation;
4. `AdvancedAlgorithms` — дополнительная C++23-основа: 12 reusable modules, differential tests и invariants.

Стажировка МЦСТ остаётся в разделе опыта как C++23/build/test/review context; не использовать её как отдельный проект с повторным перечислением Dinic, Tarjan SCC и Dijkstra.

## Algorithms / Program Analysis

Отправлять `ru-algorithms.html` / `en-algorithms.html` в команды, где нужны algorithm engineering, C++ libraries, graph/tree/string algorithms, program analysis или compiler optimizations.

Основные доказательства:

1. `AdvancedAlgorithms` — 12 переиспользуемых C++23-модулей с контрактами, дифференциальными тестами, структурными инвариантами, sanitizers и крупными входами;
2. PS-form Analyzer — symbolic/affine reasoning, conservative semantics, exact oracle, randomized and metamorphic tests;
3. Wist2 — алгоритмы в compiler pipeline: lowering/emission, constant folding, SCCP-lite, branch/unreachable cleanup и DCE.

Не сводить профиль к олимпиадам или задачам стажировки.

## Compiler Tools / Testing

Отправлять `ru-devtools.html` / `en-devtools.html` в compiler testing/fuzzing, language tooling, diagnostics и build/test infrastructure.

Основные доказательства: Wist2 diagnostics/parity/verifiers/release checks, PS-form generative harness, `AdvancedAlgorithms` differential and large-input verification, x86-64 interpreter-vs-native validation.

## C++ Systems / Program Analysis

Отправлять `ru-cpp-systems.html` / `en-cpp-systems.html` в C++ systems internships, algorithm libraries, compiler infrastructure, program analysis и verification tooling.

Основные доказательства: PS-form Analyzer, `AdvancedAlgorithms`, x86-64 backend lab и Wist2 IR/SSA. МЦСТ — релевантный опыт, но не дублирующая project card.

## Backend / Reliability / EdTech

- `ru-backend.html` / `en-backend.html` — API, payments, state and data modeling.
- `ru-platform.html` / `en-platform.html` — recovery, diagnostics, deployment and operations.
- `ru-edtech.html` / `en-edtech.html` — LMS, roles, payments and learner-facing product workflows.

В hero этих версий не использовать нерелевантную стажировку МЦСТ.

## Full technical portfolio

`ru.html` / `en.html` использовать после первого контакта, для технического руководителя или как ссылку из короткого CV. Это подробное портфолио, а не замена целевой одностраничной версии.

## Не заявлять без новых доказательств

- HFT / low-latency / market-data experience;
- quant research;
- production-ready sandbox;
- formal verification;
- production suitability of every reusable algorithm for untrusted inputs;
- performance multipliers без актуального воспроизводимого benchmark report.

## Отправка

- Для первого контакта отправлять профильный PDF как вложение.
- HTML использовать локально или после публикации v25. Публичную ссылку `misha1302.github.io/CV/` не отправлять до обновления репозитория `Misha1302/CV`.
