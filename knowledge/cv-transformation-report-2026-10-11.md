# Evidence-led CV transformation — 11 October 2026

**Baseline:** `main` at `99fbea8cdb56de21a68306991e8e88853a05fad9` (10 Oct 2026).  
**Scope:** canonical `data/site.json`, `knowledge/resume-evidence.json`, role targeting and generated RU/EN HTML/PDF assets.  
**Evidence:** `Mikhail_Razakov_Project_Forensics_2026-10-10.md` (user-provided), existing `knowledge/achievement-audit-2026-10-10.md`, prior evidence map, and selected public source files.  
**Safety:** no claims of staff/architect seniority, production scale, full CI success for VpnMediator/LMS, unverified audience size, or ISP RAS employment.

## A. CV improvement audit

**Strengths before:** unusual depth in compiler/runtime infrastructure, a real LLVM internship, independently verifiable architectural boundaries in UniversalToolchain, LLVM and x86 codegen, multiple technically grounded role profiles and maintained evidence. Existing print generation has A4/text-layer/link guards.

**Material weaknesses:** the default architecture CV selected UniversalToolchain + VpnMediator + x86 codegen, making user-facing engineering nearly invisible; `student-execution-os` / botay! did not exist in the site project map. LangDev appeared as accepted rather than delivered. Program-analysis projects underweighted PS-form. Compiler infrastructure and broad compiler profiles repeated nearly the same portfolio signals. Shared achievement copy hid the most relevant external validation among old distinctions.

**Important corrections:** botay! is a product/release engineering artifact, not established as a widely used or commercial application; current VpnMediator and LMS CI must not be marketed as green; Global-IV was an independent LLVM project, not MCST work; ISP RAS was a selection task/offer and not employment as of 10 Oct.

## B. Selection, architecture and layout decisions

| Approach | Advantage | Limitation | Decision |
|---|---|---|---|
| Experience-first | Recognizable internship, quick recruiter context | Short professional tenure hides strongest independent engineering | Preserve MCST in a compact section, not as the entire pitch |
| Engineering-evidence-first | Demonstrates depth immediately | Risk of conflating personal projects with employment | Use for the project order, with clear project titles/links |
| **Hybrid architecture-first** | Professional internship + three distinct flagship domains | Needs deliberate compression | **Selected for default profile** |

**Default order:** summary, MCST internship, UniversalToolchain, botay!, VpnMediator, selected skills, HSE education/recognition. It presents architecture through implemented planning/state/recovery and independent verification rather than a senior job title.

**Role evidence order:** architecture: UniversalToolchain → botay! → VpnMediator; backend: VpnMediator → botay! → LMS; compiler infrastructure: UniversalToolchain → PlanFuzz → Global-IV; compiler/program analysis: Global-IV → UniversalToolchain → x86 backend; program analysis: Global-IV → PS-form → Roslyn; C++/systems: Global-IV → x86 backend → PS-form. Separate compiler-backend and quant profiles remain for genuinely distinct vacancies.

**Design directions considered:** (1) Technical Minimalism — minimal decoration, clear type, links and project proof; (2) Editorial Engineering — stronger typographic personality but more risk of density and ATS disruption. Preserve the repository's restrained, existing print template and generator instead of creating an incompatible new PDF pipeline. More extensive layout changes should be gated on page-render comparisons. No skill bars or rasterized resume text.

## C. Key before/after changes

| Before | After | Hiring value |
|---|---|---|
| Architecture triad included x86 backend | Replaced x86 entry with botay!, retaining low-level depth in specialized CVs | Makes product engineering and end-to-end delivery visible |
| LangDev described as accepted | Corrected to delivered on 9 Oct 2026 | Accurate external technical communication |
| No botay! source or case | Canonical project entry, linked case pages, and explicit evidence asset | Adds Android/offline state correctness without unsupported usage claims |
| Backend profile included compiler infra among top projects | VpnMediator / botay! / LMS | Stronger story about retries, partial failures, reconciliation and ledger |
| Program-analysis projects omitted PS-form | Global-IV / PS-form / Roslyn | Shows separate interprocedural, arithmetic and data-flow analyses |
| Generic architectural tone | Planning, evidence ownership, validated witnesses and recovery distinctions | Answers what was implemented and why correctness matters |
| Compiler versions duplicated selection | Split infrastructure/PlanFuzz from compiler optimization/codegen priorities | Less profile cannibalization |

## D. Claim-to-evidence matrix

Levels follow the forensic vocabulary. **VERIFIED (report)** indicates verification performed in the 10 Oct forensic audit, not an independent fresh full-code rerun by this CV editing pass. Report scopes and limitations must travel with copy.

| Material claim / final bounded wording | Primary evidence anchor | Level / attribution | Scope and skeptical interviewer challenge |
|---|---|---|---|
| UniversalToolchain freezes feature decisions and typed routes into immutable `LanguagePlan` | `UniversalToolchain.LanguageSdk/LanguageCompiler.cs`, `LanguagePlan.cs` | VERIFIED (report); main independent-project owner | Ask whether runtime can recalculate decisions; never call this enterprise/production infrastructure |
| Independent plan verifier checks exact registration/route identity | `LanguagePlanVerifier.cs` | VERIFIED (report); main project owner | Distinguish runtime validation from formal verification |
| CI-checked 1,324-test exact manifest at 9 Oct inspected revision | `eng/test-counts.json`, inspected 2026-10-09 workflows | VERIFIED (report); project-owned | Revision-scoped; not a live permanent claim or generic code-quality score |
| PlanFuzz supports isolated replay, fingerprints and reduction | UniversalToolchain PlanFuzz source/contract experiments | VERIFIED (report); primary owner | Ask which invariants/oracles are checked and whether control experiments reproduce |
| botay! separates external observations and canonical/derived state | `docs/adr/0005*`, persistence/reconciliation | VERIFIED (report); primary independent owner | Architecture claim, not proof of adoption |
| botay! LLM proposals have no mutation authority | `docs/adr/0007-llm-extraction-action-boundary.md` | VERIFIED (fresh partial code + report); primary owner | Explain real server-scoped intent, principal, idempotency and confirmation boundary |
| botay! FEASIBLE requires a validated witness | `src/student_execution_os/planning/feasibility.py`, `witness.py` | VERIFIED (fresh source + report) | `UNKNOWN` is not `INFEASIBLE`; it is not a general formal solver |
| botay! offline operations replay idempotently | `src/student_execution_os/sync/commands.py` | VERIFIED (fresh source + report) | Precisely server operation ID/result atomicity; never imply network-level exactly-once delivery |
| Signed Android 0.8.3 release workflow passed 10 Oct | GitHub Actions release workflow, 10 Oct snapshot | VERIFIED (report) | Release pipeline ≠ actual users/install distribution |
| VpnMediator persists payment evidence before access mutation | payment inbox / entitlement state source | VERIFIED (report); personal project with contributor | Service code is private; cannot expose client details or claim sales |
| VpnMediator quarantines ambiguous remote/local state | reconciliation/operation state machine | VERIFIED (report) | Asked to prove safe handling of unknown effects; no green-CI claim |
| VpnMediator 'dozens of active users' | Maintained private/user claim only | USER-ATTESTED | **Omitted** from external CV until dated anonymized snapshot |
| CompilationLabLMS re-verifies provider payments before ledger credit | LMS payment service / release report | VERIFIED (report); some imported/agent commits | Not unrestricted-production ready; backend environment gates pending |
| LLVM 22 Global-IV pass rejects unsupported cases before mutation | LLVM effect/evolution/legality source | VERIFIED (report); independent project | Not the MCST internship task; not a full ScalarEvolution replacement |
| Global-IV 29 positive/negative regressions incl. idempotence and execution | regression runner + CI snapshot | VERIFIED (report) | Cases ≠ benchmark/performance improvement |
| x86-64 backend independent allocator verifier and native/interpreter diff | Rust IR/RA/codegen/tests | VERIFIED (report); independent project | Limited supported subset, not a production compiler backend |
| PS-form conservative C17 dependence `yes/no/maybe` | solver and exact/metamorphic harness | VERIFIED (report); independent project | Lack of proof returns maybe; no inferred official competition rank |
| Roslyn CFG fixed-point null-state analyzer | DerefAfterNullAnalyzer source/tests | VERIFIED (report); selection task | Selection task/offer, not ISP RAS employment |
| MCST compiler internship summer 2026 | Maintained career evidence + public companion code | USER-ATTESTED / PUBLIC_REPO_DIRECT | Official job-title/contract evidence not independently public-verifiable here |
| LangDev talk delivered 9 Oct 2026 | `achievement_langdev_2026` program + user-supplied event photos | PUBLIC PRIMARY + user-attested identity provenance | Delivered wording supported; avoid declaring independent facial identification |
| HSE FCS open-source winner | Official contest and private organizer evidence | STRONGLY SUPPORTED | 'One of the winners' safe; rank '1st' still user-attested |
| MEPhI Junior/Baltic distinctions | Achievement audit's primary result references | VERIFIED (report) | Preserve exact categories, no generalized Grand Prize |

## E. Before release: execution checks

Required executable contract from the repository:

```sh
python tools/validate_resume_knowledge.py
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --evidence-dir /tmp/cv-pdf-evidence
python tools/validate_cv.py --pdf-dir pdf --skip-manifest
python tools/visual_regression.py --output-dir /tmp/cv-visual
python tools/build_site.py --manifest
python tools/validate_cv.py --pdf-dir pdf
```

Check all relevant PDFs are **one A4 page with extractable text, 3+ links, readable font and a stable visual layout**. Existing validator checks role consistency, translations, source-of-truth and internal links. These tests must be reported with their actual workflow status, not presumed from the code. Visually inspect especially the longer RU architecture/backend and three-project program-analysis variants. 1-page output by itself does not prove content was not clipped, because print CSS sets an explicit fixed-height block.

## F. Interview/ATS adversarial review

- **10-second recruiter:** broad Software Engineer identity should be clear; MCST signals real workplace context; UniversalToolchain + botay! demonstrates architecture *and* product.
- **60-second engineer:** demand concrete details—planner/verifier separation, server operation atomicity, durable provider evidence and conservative legality; these replace generic phrases such as 'architected complex systems'.
- **Skeptical principal:** investigate use of 'exactly-once' (server idempotency boundary only), 'signed release' (not installs), '1,324' (9 Oct snapshot only), and 'reliable payments' (code/partial verification, not green CI).
- **ATS:** canonical role words and conventional technology spellings are explicit; PDF text-layer and reading order require separate checks.
- **Anti-AI:** retain concrete mechanisms and natural asymmetry; don't present every project as an identical 'Designed X to ensure Y' bullet.

## G. Application recommendation

| Vacancy | Preferred CV | Highest-value proof |
|---|---|---|
| General SWE, startups, architecture-heavy new grad | **Systems & Architecture** | UniversalToolchain + botay! + MCST |
| C++/LLVM systems | **C++ / Systems** | Global-IV legality + native codegen + independent verification |
| LLVM/compiler analysis | **Compiler & Program Analysis** | Global-IV + UniversalToolchain; codegen if relevant |
| Compiler tooling/infrastructure | **Compiler Infrastructure** | Immutable plans + PlanFuzz |
| Backend/platform | **Backend** | Payment evidence + reconciliation/quarantine + offline replay |
| Static/program analysis | **Program Analysis** | LLVM legality + PS-form oracles + Roslyn fixed point |

**Highest marginal next evidence:** (1) anonymized live usage for VpnMediator, (2) independent botay! installs/uptime, (3) external UniversalToolchain package consumer, (4) shareable MCST role/review artifact, (5) exact paid/client-work scope for Diploma.school.

**Remaining uncertainty:** successful release/build checks are revision- and environment-specific; VpnMediator and LMS public-production claims remain unsupported. Do not turn source-level tests or a green workflow into measured user or operational scale.
