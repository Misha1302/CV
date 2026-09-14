# CV Engineering Trajectory Audit — 2026-09-14

## Scope and baseline

Baseline repository: `Misha1302/CV` at `482676aabdaae30784a7993c2b499213160060d8` (`origin/main` at start of work).

The audit separates software-development history from commercial/client work and from professional compiler/program-analysis employment. It does not convert personal projects, teaching, or competitions into professional tenure.

## Factual chronology

| Period | Activity | Category | What was actually built/done | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| 2022-07 | BigSharpCompiler | PERSONAL_PROJECT / OPEN_SOURCE | C# compiler prototype with separate lexer, parser, preprocessor and compiler projects. | Public repository; first commit `088e2e9` on 2022-07-25; repository tree contains `Lexer/`, `Parser/`, `Preprocessor/`, `BigSharpCompiler/`. | public verified |
| 2023-06 | Wist historical prototype | PERSONAL_PROJECT / OPEN_SOURCE | Language/runtime tooling; early commits already contain variables, comparisons, loops, functions, imports, exceptions and collections. | Public repository; first commit `b7e5ef8` on 2023-06-19. | public verified |
| 2025-01 or earlier | Diploma.school | CLIENT_WORK | Real product work: jQuery dropdown interactions, responsive mobile/desktop navigation and UI regression fixes. | Explicit user attestation; project materials support real product/deployment context. Start is confirmed no later than January 2025; a 2024 start is not promoted to fact. | user-attested/private |
| 2025-10 | Wist2 / UniversalToolchain line | PERSONAL_PROJECT / OPEN_SOURCE | Lexer, parser, bytecode translation and interpreter grow into a modular language-tooling/toolchain architecture. | Public history begins with `7a43f5a` on 2025-10-11; parser `2165071`; interpreter/bytecode `ae341c3`; later 1,788-commit history through 2026-09-05. | public verified |
| 2026-06 | VpnMediator | PERSONAL_PROJECT | ASP.NET/backend product engineering around subscription/access state, payments, device policy, deployment, backup/restore and rollback/recovery. | Public repository starts at `cdc741f` on 2026-06-01; repository includes deployment and operational runbooks. | public verified |
| 2026-07–08 | MCST | INTERNSHIP | LLVM 22 compiler engineering: LICM, loop/memory/side-effect/speculative-safety checks and Python before/after behavior harness. | Canonical CV facts plus user-approved claim boundaries. Global-IV is explicitly separate. | verified / bounded |
| 2026–present | ISP RAS | EMPLOYMENT | Static-analysis engineering in C#/.NET / SharpChecker context. | Canonical CV facts plus user-approved claim boundary; no private SharpChecker contribution is invented here. | verified / bounded |

## Category boundaries

- **Public/personal engineering history** starts no later than July 2022. This proves non-zero software-development background before 2026, but it is not commercial tenure.
- **Client work** is safely evidenced from 2025 through Diploma.school. The available evidence does not justify rewriting this as continuous freelance employment from 2023.
- **Professional compiler/program-analysis work** is a 2026 development: MCST internship and ISP RAS employment/context. This is distinct from earlier personal compiler/language projects.
- **VpnMediator** is classified as a personal production-like project, not automatically as freelance/client work.
- **Unity licensing** is accepted only at bounded technical scope: Unity client, server-side key activation, activation-count limits and client integration. The historical date is not independently established, so the revised selective profile does not claim one.
- **Teaching** is known as a real activity from available materials, but the audit did not recover a sufficiently strong dated start point for the multi-year trajectory. It is therefore omitted from the headline chronology rather than used to inflate software tenure.

## Claims accepted

- Public software/compiler work predates 2026; the earliest public compiler prototype found is from July 2022.
- Wist provides public language-tooling evidence from June 2023.
- Client/product development is confirmed by 2025 via Diploma.school.
- Professional compiler/static-analysis specialization is evidenced in 2026 through MCST and ISP RAS.
- The CV may show these as separate chronology events as long as it does not present the whole interval as professional or commercial experience.

## Claims rejected

- `3+ years commercial software engineering experience` — rejected: it would mix personal/open-source work, client work and employment.
- `Professional developer since 2022/2023` — rejected: public projects do not establish professional employment.
- `2023–2026 independent / freelance engineering` — rejected as a continuous tenure claim; the old CV combined unrelated categories without adequate date evidence.
- `Compiler specialization started only in 2026` — rejected literally: public compiler/language-tooling work exists in 2022 and 2023. The defensible statement is that **professional** compiler/program-analysis work begins in 2026.

## Alternatives compared

### A. Full timeline near the hero

Fast to scan and strong on progression, but a conventional `2022 → 2023 → 2025 → 2026` career timeline risks making personal projects, private client work and employment look like one continuous tenure. It also costs substantial vertical space on mobile and in the one-page PDF.

### B. Summary-only statement

A sentence such as `Building software since 2022` is compact and ATS-friendly, but it hides the category boundary that matters most: public/personal work is older than professional compiler employment. It also asks the recruiter to trust a compressed claim rather than inspect the evidence.

### C. Compact evidence chronology — selected

The selected web strip shows four evidence-backed events rather than invented career stages: 2022 public compiler project; 2023 Wist language tooling; 2025 client/product work plus UniversalToolchain; 2026 professional compiler/program-analysis roles. The PDF uses the same chronology as one compact line.

This representation wins on 5–10 second scan speed and progression while preserving category honesty. It also makes the compiler focus stronger, not weaker: the final node is explicitly professional compiler/program analysis.

## Design decision

The chronology is stored once in canonical structured data and rendered by the existing generator. It is enabled only on the four primary compiler-oriented profiles: Compiler Infrastructure, Compiler Backend / Code Generation, Program Analysis, and broad Compiler / Program Analysis.

The web version is a low-height four-column strip below the hero and above Experience; on mobile it becomes a compact vertical sequence. The PDF does not reproduce the full visual component: it uses one line between summary and the two-column body.

## Hostile hiring-manager review

### Reviewer A — compiler hiring manager, 8 seconds

Sees professional LLVM/static-analysis roles first, then a compact chronology showing that the candidate wrote compiler/language tooling before those roles. Expected reading: `compiler focus is current and professional; software/compiler projects did not begin in 2026`.

### Reviewer B — skeptical recruiter

The strip does not say `years of professional experience`. Client work is explicitly a 2025 evidence point, while 2022/2023 are public projects. The previous `2023–2026 freelance` ambiguity has been removed.

### Reviewer C — senior engineer

The sequence shows increasing engineering scope without pretending that every step is employment: compiler prototype → language/runtime tooling → client/product work and a larger toolchain → professional LLVM/static analysis.

Material findings fixed during review:
- removed the continuous `2023–2026 independent / freelance` claim from primary compiler profiles;
- removed the unsupported `2023` date from the Unity licensing item;
- narrowed Unity protection wording to the user-approved key-activation / activation-limit scope;
- classified VpnMediator as a personal project in the selective software-protection profile.

## Validation intent

Required gates: canonical regeneration, one-page PDF generation, source-of-truth validator, external links, desktop/mobile/no-JS visual smoke/regression, deterministic regeneration and final manifest validation. Results are recorded in the PR/final report rather than pre-declared here.
