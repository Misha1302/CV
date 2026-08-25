from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "data" / "site.json"


def award_ru() -> list[list[str]]:
    return [
        ["2026", "UniversalToolchain — Балтийский научно-инженерный конкурс", "Диплом I степени и Главная премия «Совершенство как надежда» за UniversalToolchain."],
        ["2026", "НИЯУ МИФИ «Юниор»", "Диплом I степени, 96/100 за проект UniversalToolchain."],
    ]


def award_en() -> list[list[str]]:
    return [
        ["2026", "UniversalToolchain — Baltic Science and Engineering Competition", "First-degree diploma and the Grand Prize “Perfection as Hope” for UniversalToolchain."],
        ["2026", "MEPhI Junior", "First-degree diploma, 96/100 for the UniversalToolchain project."],
    ]


def main() -> None:
    data = json.loads(SITE.read_text(encoding="utf-8"))
    if data.get("version") != 45:
        raise SystemExit(f"Expected CV source v45, got {data.get('version')!r}")

    data["version"] = 46
    data["updated_at"] = "2026-08-25"

    data["profile_ui"]["compiler"].update({
        "label_ru": "Compiler Infrastructure",
        "label_en": "Compiler Infrastructure",
        "landing_title": "Compiler Infrastructure / Language Platforms",
        "landing_description_ru": "LLVM-анализы и passes, IR/runtime architecture, language-platform composition и независимая проверка корректности.",
    })
    data["profile_ui"]["backend"].update({
        "label_ru": ".NET Backend / Reliability",
        "label_en": ".NET Backend / Reliability",
        "landing_title": ".NET Backend / Platform Reliability",
        "landing_description_ru": "Payment state, idempotency, durable recovery, provider verification, migrations и rollback.",
    })

    compiler_ru = data["profiles"]["compiler"]["ru"]
    compiler_ru.update({
        "title": "Михаил Разаков — Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "role": "Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "brand": "LLVM · compiler infrastructure · IR/runtime · verification",
        "eyebrow": "LLVM analysis · language platforms · IR · correctness",
        "summary": "Разрабатываю compiler infrastructure, где решения о composition, IR/runtime и корректности выражены явно: LLVM-анализы и passes, детерминированное планирование language platform, Bytecode/AIR/SSA, backends и независимые verifier/oracle проверки.",
        "description": "Compiler / Platform Engineer Михаил Разаков: LLVM-анализы и passes, compiler infrastructure, language platforms, IR/runtime, SSA и verification-driven engineering.",
        "proofs": [
            ["LLVM analysis", "LICM и межпроцедурные линейные summaries глобальных значений; неподдерживаемые CFG/call cases дают conservative unknown"],
            ["Language infrastructure", "UniversalToolchain: один immutable LanguagePlan владеет dependencies, capabilities, pass ordering и backend routes"],
            ["Independent verification", "Interpreter/CIL parity, exact package binding, allocator verifier и differential execution против reference interpreter"],
        ],
        "experience": [
            {
                "date": "1 июля — 31 августа 2026",
                "title": "МЦСТ — стажёр по разработке компиляторов",
                "org": "LLVM · C++23 · 0,25 ставки · удалённо",
                "bullets": [
                    "Реализовал LLVM LICM-pass и развиваю межпроцедурный анализ эволюции глобальных значений: линейные summaries компонуются там, где это доказуемо; unsupported loops/calls/CFG переходят в unknown.",
                    "Проверяю преобразования через opt/lli, verifier и negative cases, где pass обязан сохранить исходный IR или отказаться от вывода.",
                ],
            },
            {
                "date": "2024 — сейчас",
                "title": "UniversalToolchain — создатель и основной разработчик",
                "org": ".NET language platform · compiler/runtime infrastructure",
                "bullets": [
                    "Сделал LanguageCompiler единственным владельцем composition: dependencies/conflicts, capability selection, pass ordering и backend routes фиксируются до runtime в immutable LanguagePlan.",
                    "Разделил syntax → semantic binding → Bytecode → AIR → optimizations → backend явными representation boundaries; архитектурные contracts защищены exact binding и regression tests, текущий exact manifest — 1 306/1 306 passed.",
                ],
            },
            {
                "date": "2026",
                "title": "x86-64 Codegen & Register Allocation Playground",
                "org": "Rust · SSA/CFG · x86-64",
                "bullets": [
                    "Отделил allocation strategy от correctness policy: allocators выдают единый Assignment, который независимо проверяется по liveness/interference invariants перед codegen.",
                    "Сравниваю native x86-64 execution с reference interpreter в отдельном resource-bounded процессе.",
                ],
            },
        ],
        "project_ids": ["wist", "codegen", "psform", "planfuzz"],
        "skills": [
            ["LLVM / Program Analysis", "C++23, LLVM passes, LoopInfo, CFG, dominance, SSA, interprocedural summaries, conservative analysis"],
            ["Compiler Infrastructure", "typed language packages, deterministic planning, capabilities/conflicts, pass ordering, exact runtime binding"],
            ["IR / Runtime / Backend", ".NET, Bytecode/AIR, SSA routes, interpreter, CIL backend, register allocation, x86-64"],
            ["Verification / Tooling", "reference oracles, differential/metamorphic tests, verifier-gated transforms, CMake, Linux, ASan/UBSan"],
        ],
        "contact_heading": "Целевые роли: Compiler Infrastructure / LLVM / Language Platform / Program Analysis Engineer.",
        "footer": "Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "recognition": award_ru(),
        "project_summaries": {
            "wist": {
                "solution": "Композиция языка вынесена в один typed planner: dependencies/conflicts, capability selection, pass ordering и artifact/backend routes фиксируются в immutable plan до runtime.",
                "result": "Runtime материализует уже выбранный граф; exact binding и regression tests проверяют ownership и package identity, текущий exact manifest — 1 306/1 306 passed."
            },
            "codegen": {
                "solution": "Allocator возвращает общий Assignment, а отдельный verifier проверяет completeness, допустимые registers, spills и live-interval conflicts до codegen.",
                "result": "Generated x86-64 поведение сравнивается с reference interpreter; ошибки allocation и emitter локализуются раздельно."
            },
            "psform": {
                "solution": "Portfolio solver сочетает дешёвые доказательства, exact affine reasoning, bounded exhaustive search и witness search; недоказанные случаи остаются unknown/maybe.",
                "result": "Малые области проверяются независимым exact oracle, дополнительно используются randomized и metamorphic tests."
            },
            "planfuzz": {
                "solution": "Экспериментальный fuzzer типизирует outcomes, сохраняет fingerprints, перепроверяет failure в свежем процессе и минимизирует программу/конфигурацию.",
                "result": "Подтверждённые сбои сохраняют воспроизводимый минимальный пример; flaky/infrastructure outcomes не маскируются под compiler bugs."
            },
        },
    })

    compiler_en = data["profiles"]["compiler"]["en"]
    compiler_en.update({
        "title": "Mikhail Razakov — Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "role": "Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "brand": "LLVM · compiler infrastructure · IR/runtime · verification",
        "eyebrow": "LLVM analysis · language platforms · IR · correctness",
        "summary": "I build compiler infrastructure where composition, IR/runtime decisions, and correctness are explicit: LLVM analyses and passes, deterministic language-platform planning, Bytecode/AIR/SSA, backends, and independent verifier/oracle checks.",
        "description": "Compiler / Platform Engineer Mikhail Razakov: LLVM analyses and passes, compiler infrastructure, language platforms, IR/runtime, SSA, and verification-driven engineering.",
        "proofs": [
            ["LLVM analysis", "LICM plus interprocedural linear summaries for global values; unsupported CFG/call cases conservatively fall back to unknown"],
            ["Language infrastructure", "UniversalToolchain: one immutable LanguagePlan owns dependencies, capabilities, pass ordering, and backend routes"],
            ["Independent verification", "Interpreter/CIL parity, exact package binding, allocator verification, and differential execution against a reference interpreter"],
        ],
        "experience": [
            {
                "date": "July 1 — August 31, 2026",
                "title": "MCST — Compiler Engineering Intern",
                "org": "LLVM · C++23 · 0.25 FTE · remote",
                "bullets": [
                    "Implemented an LLVM LICM pass and am developing interprocedural global-value evolution analysis: linear summaries compose where justified, while unsupported loops/calls/CFG cases fall back to unknown.",
                    "Validate transformations with opt/lli, verifier checks, and negative cases where the pass must preserve the original IR or decline an inference.",
                ],
            },
            {
                "date": "2024 — present",
                "title": "UniversalToolchain — creator and primary developer",
                "org": ".NET language platform · compiler/runtime infrastructure",
                "bullets": [
                    "Made LanguageCompiler the single owner of composition: dependencies/conflicts, capability selection, pass ordering, and backend routes are fixed in an immutable LanguagePlan before runtime.",
                    "Separated syntax → semantic binding → Bytecode → AIR → optimization → backend through explicit representation boundaries; exact binding and regression tests enforce the contracts, with a current exact manifest of 1,306/1,306 passing.",
                ],
            },
            {
                "date": "2026",
                "title": "x86-64 Codegen & Register Allocation Playground",
                "org": "Rust · SSA/CFG · x86-64",
                "bullets": [
                    "Separated allocation strategy from correctness policy: allocators return a common Assignment that an independent verifier checks against liveness/interference invariants before code generation.",
                    "Differentially compare native x86-64 execution with a reference interpreter in a separate resource-bounded process.",
                ],
            },
        ],
        "project_ids": ["wist", "codegen", "psform", "planfuzz"],
        "skills": [
            ["LLVM / Program Analysis", "C++23, LLVM passes, LoopInfo, CFG, dominance, SSA, interprocedural summaries, conservative analysis"],
            ["Compiler Infrastructure", "typed language packages, deterministic planning, capabilities/conflicts, pass ordering, exact runtime binding"],
            ["IR / Runtime / Backend", ".NET, Bytecode/AIR, SSA routes, interpreter, CIL backend, register allocation, x86-64"],
            ["Verification / Tooling", "reference oracles, differential/metamorphic tests, verifier-gated transforms, CMake, Linux, ASan/UBSan"],
        ],
        "contact_heading": "Targeting Compiler Infrastructure, LLVM, Language Platform, and Program Analysis roles.",
        "footer": "Compiler / Platform Engineer · LLVM & Language Infrastructure",
        "recognition": award_en(),
        "project_summaries": {
            "wist": {
                "solution": "Language composition is owned by one typed planner: dependencies/conflicts, capability selection, pass ordering, and artifact/backend routes are fixed in an immutable plan before runtime.",
                "result": "Runtime materializes the selected graph; exact binding and regression tests enforce ownership and package identity, with a current exact manifest of 1,306/1,306 passing."
            },
            "codegen": {
                "solution": "Allocators return a common Assignment while an independent verifier checks completeness, valid registers, spills, and live-interval conflicts before code generation.",
                "result": "Generated x86-64 behavior is compared with a reference interpreter, separating allocation failures from emitter failures."
            },
            "psform": {
                "solution": "A portfolio solver combines cheap global proofs, exact affine reasoning, bounded exhaustive search, and witness search; unproved cases remain unknown/maybe.",
                "result": "Small domains are checked by an independent exact oracle, with randomized and metamorphic tests on top."
            },
            "planfuzz": {
                "solution": "Experimental fuzzing uses typed outcomes, failure fingerprints, fresh-process confirmation, and reduction of both program and configuration.",
                "result": "Confirmed failures retain a reproducible minimized case, while flaky and infrastructure outcomes are kept distinct from compiler bugs."
            },
        },
    })

    backend_ru = data["profiles"]["backend"]["ru"]
    backend_ru.update({
        "title": "Михаил Разаков — .NET Backend / Platform Engineer · State & Reliability",
        "role": ".NET Backend / Platform Engineer · State & Reliability",
        "brand": ".NET · payment state · recovery · platform reliability",
        "eyebrow": "ASP.NET Core · idempotency · recovery · rollback",
        "summary": "Разрабатываю .NET backend-системы, где платежи, доступ и состояние должны переживать retries и restarts: explicit state machines, provider re-verification, durable inbox/outbox, idempotency, reconciliation, migrations и проверяемый rollback.",
        "description": ".NET Backend / Platform Engineer Михаил Разаков: payment state, idempotency, durable inbox/outbox, provider verification, recovery, migrations и rollback.",
        "proofs": [
            ["Payment correctness", "Webhook не считается источником истины: provider payment повторно запрашивается и проверяется по id/status/environment/metadata/amount/currency"],
            ["Recovery ownership", "Durable inbox/outbox, idempotency, reconciliation, restart recovery, leases и manual review для конфликтующих evidence"],
            ["Release safety", "Versioned releases, coordinated backup, atomic switch, health gates и rollback на предыдущую версию"],
        ],
        "experience": [
            {
                "date": "2026 — сейчас",
                "title": "CompilationLabLMS — payment/backend architecture",
                "org": "ASP.NET Core · payment state · provider verification",
                "bullets": [
                    "Сделал PaymentOrder владельцем допустимых state transitions, retry scheduling и status-check leases; webhook flow повторно запрашивает payment у provider перед внутренним событием.",
                    "Проверяю payment id/status/environment/metadata/amount/currency и отделяю malformed/unverifiable provider events от подтверждённого состояния.",
                ],
            },
            {
                "date": "2026 — сейчас",
                "title": "VpnMediator — state/recovery backend",
                "org": "ASP.NET Core · SQLite/PostgreSQL · Python · Linux",
                "bullets": [
                    "Спроектировал durable payment inbox/outbox, idempotent reconciliation и manual-review path для конфликтующих provider evidence; recovery после restart проверяется отдельными тестами.",
                    "Построил versioned release path с coordinated backup, atomic switch, readiness/liveness gates и возвратом на предыдущий release при неуспешном запуске.",
                ],
            },
            {
                "date": "2024 — сейчас",
                "title": "UniversalToolchain — .NET platform architecture",
                "org": ".NET · typed contracts · deterministic composition",
                "bullets": [
                    "Применяю тот же подход к platform code: single-owner planning, exact package binding и regression contracts; текущий exact manifest — 1 306/1 306 passed.",
                ],
            },
        ],
        "project_ids": ["lms", "vpn", "wist"],
        "skills": [
            [".NET Backend", "C#/.NET, ASP.NET Core, REST/OpenAPI, webhooks, background services, provider integrations"],
            ["State & Data", "PostgreSQL, SQLite, transactions, explicit state machines, idempotency keys, inbox/outbox, leases"],
            ["Reliability", "provider re-verification, reconciliation, retry ownership, restart recovery, audit/manual review, backup/restore"],
            ["Operations / Platform", "Linux, Docker Compose, nginx, systemd, health gates, versioned releases, atomic switch, rollback"],
        ],
        "contact_heading": "Целевые роли: .NET Backend / Platform Engineer с ответственностью за состояние, recovery и эксплуатационную корректность.",
        "footer": ".NET Backend / Platform Engineer · State & Reliability",
        "recognition": award_ru(),
    })

    backend_en = data["profiles"]["backend"]["en"]
    backend_en.update({
        "title": "Mikhail Razakov — .NET Backend / Platform Engineer · State & Reliability",
        "role": ".NET Backend / Platform Engineer · State & Reliability",
        "brand": ".NET · payment state · recovery · platform reliability",
        "eyebrow": "ASP.NET Core · idempotency · recovery · rollback",
        "summary": "I build .NET backend systems where payments, access, and state must survive retries and restarts: explicit state machines, provider re-verification, durable inbox/outbox, idempotency, reconciliation, migrations, and verifiable rollback.",
        "description": ".NET Backend / Platform Engineer Mikhail Razakov: payment state, idempotency, durable inbox/outbox, provider verification, recovery, migrations, and rollback.",
        "proofs": [
            ["Payment correctness", "A webhook is not treated as ground truth: provider payment state is re-fetched and checked for id/status/environment/metadata/amount/currency"],
            ["Recovery ownership", "Durable inbox/outbox, idempotency, reconciliation, restart recovery, leases, and manual review for conflicting evidence"],
            ["Release safety", "Versioned releases, coordinated backup, atomic switching, health gates, and rollback to the previous release"],
        ],
        "experience": [
            {
                "date": "2026 — present",
                "title": "CompilationLabLMS — payment/backend architecture",
                "org": "ASP.NET Core · payment state · provider verification",
                "bullets": [
                    "Made PaymentOrder the owner of allowed state transitions, retry scheduling, and status-check leases; the webhook flow re-fetches payment state from the provider before emitting an internal event.",
                    "Validate payment id/status/environment/metadata/amount/currency and keep malformed or unverifiable provider events separate from confirmed state.",
                ],
            },
            {
                "date": "2026 — present",
                "title": "VpnMediator — state/recovery backend",
                "org": "ASP.NET Core · SQLite/PostgreSQL · Python · Linux",
                "bullets": [
                    "Designed a durable payment inbox/outbox, idempotent reconciliation, and a manual-review path for conflicting provider evidence; restart recovery is covered by dedicated tests.",
                    "Built a versioned release path with coordinated backup, atomic switching, readiness/liveness gates, and restoration of the previous release after failed startup.",
                ],
            },
            {
                "date": "2024 — present",
                "title": "UniversalToolchain — .NET platform architecture",
                "org": ".NET · typed contracts · deterministic composition",
                "bullets": [
                    "Apply the same reliability discipline to platform code through single-owner planning, exact package binding, and regression contracts; the current exact manifest is 1,306/1,306 passing.",
                ],
            },
        ],
        "project_ids": ["lms", "vpn", "wist"],
        "skills": [
            [".NET Backend", "C#/.NET, ASP.NET Core, REST/OpenAPI, webhooks, background services, provider integrations"],
            ["State & Data", "PostgreSQL, SQLite, transactions, explicit state machines, idempotency keys, inbox/outbox, leases"],
            ["Reliability", "provider re-verification, reconciliation, retry ownership, restart recovery, audit/manual review, backup/restore"],
            ["Operations / Platform", "Linux, Docker Compose, nginx, systemd, health gates, versioned releases, atomic switching, rollback"],
        ],
        "contact_heading": "Targeting .NET Backend / Platform Engineer roles with ownership of state, recovery, and operational correctness.",
        "footer": ".NET Backend / Platform Engineer · State & Reliability",
        "recognition": award_en(),
    })

    SITE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    review = ROOT / "CONTENT-REVIEW-v46.md"
    review.write_text(
        """# Content review — targeted CV v46\n\n## Decision\n\nPASS for three primary narratives: Architecture / Platforms, Compiler Infrastructure, and .NET Backend / Reliability.\n\n## Routing\n\n- `ru.html` / `en.html`: broad architecture-heavy Software / Platform Engineer roles.\n- `ru-compiler.html` / `en-compiler.html`: LLVM, compiler infrastructure, language-platform, IR/runtime, program-analysis roles.\n- `ru-backend.html` / `en-backend.html`: .NET backend/platform roles where state correctness, payments, recovery, and release safety dominate.\n\n## Strongest alternative considered\n\nKeeping the older Compiler Engineer and generic .NET Backend pages would preserve more keywords, but it fragments the evidence and retains stale or weak claims. The v46 versions instead reuse the master architecture narrative and reorder only verified evidence by role.\n\n## Anti-overclaim review\n\n- No Staff/Principal/Senior Architect title.\n- No production-scale/high-load/Kubernetes/cloud claims.\n- Compiler page does not claim a production optimization; unsupported analysis cases explicitly fall back to unknown.\n- Targeted compiler/backend pages contain no LangDev acceptance claim, no `#1 of 49` claim, and no `104/104 official tests` claim.\n- Current UniversalToolchain test count remains 1,306/1,306 only where useful.\n- Backend claims are about concrete state/recovery mechanisms, not generic “distributed systems” seniority.\n\n## Recruiter read\n\nEach page answers three questions within the first screen: target role, strongest proof, and why the engineering decisions matter. Technology names are supporting evidence rather than the primary narrative.\n\n## Principal/Staff read\n\nThe bullets expose decision ownership and failure semantics: single planning owner, representation boundaries, conservative unknown, independent verifier, provider re-verification, durable recovery, and rollback. These are inspectable design decisions rather than architecture buzzwords.\n\n## Remaining gaps\n\nMulti-team architecture, long-lived high-scale production ownership, and formal organizational leadership are still not established and are not claimed.\n""",
        encoding="utf-8",
    )

    targeting = ROOT / "TARGETING.md"
    targeting.write_text(
        """# Targeting guide — v46\n\n## Primary profiles\n\n1. `Software Engineer — Architecture & Platforms` — default for hands-on architecture/platform roles spanning typed contracts, state/recovery, and compiler/runtime systems.\n2. `Compiler / Platform Engineer — LLVM & Language Infrastructure` — LLVM/compiler infrastructure, language SDK/runtime, IR/SSA, program analysis, and compiler-backend roles.\n3. `.NET Backend / Platform Engineer — State & Reliability` — backend/platform roles where payments, idempotency, recovery, migrations, and release correctness dominate.\n\n## Secondary profiles\n\n- `C++ / LLVM Systems` — narrower low-level/C++ systems applications.\n- `Quantitative Research / Research Software Engineering` — only when algorithmic experimentation is central.\n\nUse the three primary profiles first. They share the same facts and differ only in evidence ordering and role-specific vocabulary.\n""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
