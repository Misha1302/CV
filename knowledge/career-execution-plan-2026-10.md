# Career execution plan — October 2026 to June 2027

Status: **working strategy, not a CV fact source by itself**.

This document translates the evidence base into concrete career actions. It must not be used to upgrade a claim in `resume-evidence.json` unless independent evidence is added there.

## Objective

By June 2027, become a credible candidate for all three adjacent role families:

1. **Static / Program Analysis**
2. **C++ / Systems / Storage / Runtime**
3. **Compiler / Runtime Infrastructure**

The operating identity is broader than “compiler engineer”:

> **Systems / Program Analysis Engineer with compiler/runtime depth**

Compiler work remains a depth signal. Architecture is treated as an engineering responsibility to accumulate inside real systems, not as a junior job title to optimize for.

## Decision criteria

When comparing work, internships, projects, or offers, evaluate in this order:

1. **Task depth** — non-trivial correctness, performance, representation, state, or systems problems.
2. **Transferable engineering capital** — C/C++, Linux, concurrency, storage, distributed systems, LLVM/IR, debugging, profiling, verification, large-codebase work.
3. **External review / production ownership** — evidence that work survives review and constraints outside a personal repository.
4. **Mentorship quality** — access to engineers who can review design and implementation decisions.
5. **Market optionality** — skills should transfer across several teams/companies rather than bind the profile to one small niche.
6. **Compensation / practical sustainability** — do not optimize for “interesting” while making the path economically non-viable.

Do **not** optimize for a permanent profession label in 2026.

## Current interpretation of the evidence base

### Strong assets already present

- MCST compiler-engineering internship context with C++/LLVM-related work.
- UniversalToolchain/Wist as a substantial independent compiler/runtime architecture asset.
- Global-IV, x86-64 codegen, PS-form and related analysis/codegen work.
- Program-analysis direction around Roslyn/LLVM/static-analysis tasks.
- Service-system architecture in VpnMediator and CompilationLabLMS.
- Accepted LangDev 2026 talk.

### Main missing evidence

The bottleneck is **not another large personal compiler project**.

The highest-value missing signals are:

- successful entry into a mature external codebase;
- review from maintainers who did not design the project around the author;
- one substantial production/team case with measurable correctness/performance/operability impact;
- broader systems experience beyond compiler-specific code;
- interview evidence showing which gaps actually block systems roles.

## Role-family policy

### 1. Static / Program Analysis — near-term base

Use current/near-current work to build a strong professional case around:

- interprocedural/data-flow reasoning;
- fixed-point analyses;
- path sensitivity / symbolic reasoning where applicable;
- false-positive reduction;
- incremental/repeated analysis;
- performance and scaling of analyzers;
- verifier/oracle design.

Target output by January 2027: **one interview-grade production story** with problem → alternatives → chosen design → verification → measurable result.

### 2. C++ / Systems / Storage / Runtime — primary expansion

This is the main adjacency to build in 2026–2027.

Required competence blocks:

- Linux process/thread/VM/syscall model;
- concurrency and C++ memory model;
- profiling and performance diagnosis;
- storage basics: WAL, B-tree/LSM trade-offs, caching, durability;
- distributed-system basics: replication, consistency, idempotency, failure models;
- large-codebase debugging/build/test/review workflow.

Do not replace compiler work with generic CRUD/backend work. Expand into adjacent systems engineering.

### 3. Compiler / Runtime Infrastructure — retained specialization

Keep LLVM/compiler/runtime work active, but stop using it as the only market identity.

Prefer:

- upstream contributions;
- optimizations with correctness proof/testing;
- runtime/JIT/backend work;
- representations/IR/SSA/data-flow boundaries;
- performance work that transfers to other systems domains.

### 4. Architecture — responsibility, not entry-level title

Do not search for “junior software architect” as the primary job strategy.

Accumulate architecture evidence by owning:

- subsystem boundaries;
- invariants;
- data/state ownership;
- failure and recovery behavior;
- performance/correctness trade-offs;
- migration and compatibility decisions.

## Market snapshot — 2026-10-01

These are **current research anchors**, not promises of hiring.

### YDB / Yandex Infrastructure

Current YDB materials show active work in:

- distributed storage;
- system infrastructure;
- core/query processing;
- tablets/transactions;
- C++ and Linux-heavy distributed systems.

Yandex Infrastructure describes work across core infrastructure, storage, networking, containers, build/repository systems and other internal infrastructure.

A current YDB distributed-storage vacancy expects senior experience, so it is a **skill specification / target-team anchor**, not a junior opening.

An archived Yandex base-infrastructure intern vacancy is useful evidence that systems internships without prior commercial experience have existed; because it is archived, it must not be treated as open.

Sources:
- https://yandex.ru/jobs/services/ydb
- https://yandex.ru/jobs/services/infrastructure
- https://yandex.ru/jobs/vacancies/razrabotchik-na-s-v-komandu-raspredelyonnogo-hranilischa-ydb-21947
- https://yandex.ru/jobs/vacancies/sistemniy-razrabotchik-stazhyor-v-sluzhbu-bazovoy-infrastrukturi-44923

### YADRO

Current YADRO careers material confirms several adjacent systems directions:

- Linux/OpenBMC/firmware;
- RISC-V/CPU work;
- QEMU/system simulation;
- storage systems;
- embedded C/C++.

This is useful as a map of transferable systems skills, even when a specific opening is senior-level.

Sources:
- https://careers.yadro.com/
- https://careers.yadro.com/vacancy/18719
- https://careers.yadro.com/vacancy/14718

### ISP RAS

Current student/research pages show adjacent areas including:

- source-code static analysis;
- interprocedural/path-sensitive analysis;
- Clang Static Analyzer detectors;
- .NET/Svace/SharpChecker analysis;
- LLM-assisted program analysis;
- LLVM/GCC static compiler optimization;
- JIT/runtime work;
- binary analysis and systems topics.

Sources:
- https://education.at.ispras.ru/static-analysis
- https://education.at.ispras.ru/optimization
- https://education.at.ispras.ru/compile-projects

## Immediate execution plan

### 2026-10-01 → 2026-10-05

**Deliverable A — positioning**

Use this ordering in career-facing material:

1. systems / program-analysis engineering;
2. compiler/runtime depth;
3. architecture ownership;
4. research/verification discipline.

Do not lead with age or “first-year student” in voluntary self-presentation. Do not omit required application fields where a form explicitly asks for them.

**Deliverable B — one-page engineering evidence sheet**

Create four case cards:

1. UniversalToolchain architecture;
2. LLVM / MCST work;
3. program/static-analysis case;
4. native/x86-64 or another low-level correctness case.

Each card must contain exactly:

- problem;
- constraints;
- alternatives/trade-off;
- implemented decision;
- verification/result;
- link/evidence where public.

No technology dump.

### LangDev 2026 — 2026-10-08 → 2026-10-09

The published schedule currently lists the talk:

> “Build the Language, Then Make the Abstractions Disappear: Extensible Programming on .NET”

for **Friday, October 9 at 10:00**. The conference marks the schedule as draft, so re-check it before the event.

Source:
- https://langdevcon.org/2026/program

Networking target:

- 5 substantive technical conversations;
- 3 contacts worth following up with;
- 2 explicit asks for introductions/recommended teams in Europe.

Useful verified conference contacts include:

- Alessio Stalla — Strumenta;
- Klaus Birken — itemis;
- Ana-Maria Sutii — Xlinq;
- Ulyana Tikhonova — F1RE / Xlinq;
- Sergej Koščejev — MPS/agent tooling session.

Conversation framing:

> I work on static/program analysis and compiler/runtime infrastructure, but I am intentionally expanding toward core systems. Which teams or engineers in Europe would you recommend I speak with if I want hard systems/runtime problems rather than generic backend work?

Do not open with “are you hiring me?”. Ask for technical direction and introductions first.

### 2026-10-10 → 2026-10-20

**Goal: enter at least one mature external codebase and get a real review loop.**

Warm-up option:

- YDB C++ SDK issue #553 — currently open, labels `student-projects`, `30min`.
- https://github.com/ydb-platform/ydb-cpp-sdk/issues/553

Use it only to learn build/conventions/review. Do **not** count a tiny patch as the final systems proof.

Then choose one substantive external contribution.

Current LLVM good-first-issue examples:

- InstCombine #216127 — currently open.
  - https://github.com/llvm/llvm-project/issues/216127
- RISC-V missed optimization #222933 — currently open.
  - https://github.com/llvm/llvm-project/issues/222933

Success criterion for October:

- one external PR opened;
- at least one non-author maintainer/reviewer interaction;
- review feedback incorporated.

Merged/accepted is better, but not fully under personal control, so it is not the only success criterion.

### 2026-10-20 → 2026-11-30

Run **12 targeted outreaches**, not mass applications:

- 3 — YDB / Yandex Infrastructure;
- 3 — YADRO systems/firmware/storage/RISC-V adjacent teams;
- 2 — compiler/runtime teams;
- 2 — static-analysis/devtools teams;
- 2 — European contacts originating from LangDev.

Target technical leads, heads, hiring managers, or strong senior engineers close to the team. Recruiters are secondary when there is no matching published opening.

Message structure:

1. one sentence: current strongest evidence;
2. one sentence: why this exact team;
3. one concrete technical question;
4. one small ask: 15-minute conversation or pointer to the right engineer.

Track:

- sent;
- response;
- technical conversation;
- referral/introduction;
- interview;
- rejection reason / missing skill.

### By 2027-01-15

Produce one **heavyweight team/production story**.

Preferred shapes:

- interprocedural/data-flow algorithm;
- material false-positive reduction;
- incremental-analysis improvement;
- analyzer/runtime performance work;
- new language/model support with non-trivial architecture;
- verifier/oracle design that catches real regressions.

Record:

- baseline;
- constraints;
- rejected alternatives;
- chosen design;
- correctness validation;
- performance/quality result;
- what was personally owned.

If the work is private, store only sanitized architecture/result facts allowed for interview/CV use.

### 2027-01 → 2027-03

Run a real market test: **6–10 interviews/conversations for hard engineering teams**.

After each, classify the primary blocker:

- algorithms/CS;
- systems fundamentals;
- C++ depth;
- production ownership;
- communication/system-design;
- role mismatch/no junior headcount.

After five meaningful data points, update this plan based on observed blockers rather than assumptions.

## Weekly execution cadence

Until the March market test:

- **2 × 90 min** — systems fundamentals + implementation exercise;
- **1 × 2 h** — external OSS contribution/review loop;
- **1 × 60 min** — algorithms/CS interview maintenance;
- **1 × 30 min** — outreach/follow-up ledger;
- **1 × 30 min** — convert current work into an engineering story/evidence update.

University/work deadlines override the cadence; missed sessions should not create debt. Resume from the next block.

## Systems curriculum order

Do not start another compiler course first.

### Block 1 — Linux internals
- processes/threads;
- virtual memory;
- mmap;
- syscalls;
- /proc;
- strace/ltrace;
- scheduler basics;
- perf basics.

### Block 2 — concurrency
- atomics;
- memory ordering;
- mutex/condvar;
- contention;
- false sharing;
- lock-free vs wait-free trade-offs.

### Block 3 — storage
- WAL;
- B-tree vs LSM;
- page/cache behavior;
- replication/durability basics;
- write amplification.

### Block 4 — distributed systems
- replication;
- consistency;
- quorum;
- leader/coordination basics;
- failure models;
- idempotency and retries.

### Block 5 — performance
- perf;
- flamegraphs;
- allocation profiling;
- cache behavior;
- benchmark methodology.

## Interview packaging

Prepare three reusable engineering stories.

### Story A — architecture
Use UniversalToolchain.

Must show:
- why the obvious design was insufficient;
- architectural alternatives;
- explicit invariants;
- extension/composition boundaries;
- testing/verification.

### Story B — compiler / low-level correctness
Use MCST/LLVM, Global-IV, x86-64 backend, or the strongest available case.

Must show:
- representation/analysis issue;
- correctness boundary;
- debugging process;
- verifier/test design.

### Story C — team/production program analysis
Use the strongest shareable work available by January.

Must show:
- actual user/team constraint;
- measurable result;
- review/iteration;
- ownership.

## Things to stop doing

- Do not start another standalone compiler/runtime project merely to add one more project.
- Do not spend months adding low-signal features to UniversalToolchain when packaging/review/adoption evidence is missing.
- Do not pivot to generic CRUD/backend solely because the market is broader.
- Do not optimize for the title “software architect” before enough production context exists.
- Do not try to become simultaneously expert in compilers, DBs, HFT, embedded, distributed systems and architecture. Build the **shared systems core** first.
- Do not count repository size, number of side projects or LLM-generated code volume as career evidence.

## Private mentoring follow-up queue

A private mentoring conversation on 2026-09-30 produced two promised introductions/leads:

1. a contact working in the drone domain;
2. a contact who develops a programming language / has language-engineering context.

The raw conversation is intentionally **not committed** to this public repository.

Action:

- if no update arrives within 7–10 days, send one short follow-up;
- do not treat either as an opportunity until a concrete company/team/task is known;
- evaluate any resulting role with the decision criteria at the top of this document.

## Review checkpoints

### 2026-10-20
- engineering evidence sheet exists;
- LangDev contacts recorded;
- external PR/review loop started.

### 2026-11-30
- 12 targeted outreaches completed;
- response/conversation/referral data recorded;
- next systems knowledge gap selected from real feedback.

### 2027-01-15
- one heavyweight team/production story ready.

### 2027-03-31
- 6–10 market-test conversations/interviews attempted;
- observed blocker distribution recorded;
- target role mix updated.

### 2027-06-30
Decide among actual options using:
- task depth;
- mentorship;
- transferable systems capital;
- production/external-review ownership;
- compensation;
- market optionality.

Do not decide based on profession labels alone.
