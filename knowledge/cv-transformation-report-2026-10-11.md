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


## H. Independent second-pass audit and corrections — 11 October 2026

This section records the follow-up review against PR #63, including inspection of actual CI PDF-preview PNGs rather than CSS alone.

### Evidence hierarchy used in this pass

- **VERIFIED:** an accessible direct source establishes the bounded claim (for example, organizer correspondence or inspectable project code); private evidence is explicitly not public evidence.
- **STRONGLY SUPPORTED:** multiple mutually consistent records establish most of the statement but leave a material attribution/detail gap.
- **USER-ATTESTED:** statement from the candidate without accessible independent confirmation.
- **NEEDS VERIFICATION:** should not become a strong public-facing claim until an appropriate artifact is available.

### What the second pass found

1. The backend CV placed CompilationLabLMS and VpnMediator inside the Professional Experience section, despite both being independently owned projects. The selective software-protection CV likewise placed a historical Unity licensing prototype and personal VpnMediator work there. The correction keeps verified employer/client categories distinct from project engineering. Their implementation evidence remains in project/independent-work sections.
2. The 5 June 2026 organizer's private MCST selection roundup reports 49 submitted solutions, the sole 104/104 official-test result, and the sole 5.0/5.0 top score. The candidate's reply to that same correspondence identifies his score as 5.0, consistent with the organizer's highest entry. This is **strong primary private organizer evidence**, not a public personal diploma or an independently published leaderboard. The 87 initial applicants are a different denominator. Result wording intentionally says "organizer correspondence".
3. Default architecture and backend PDF captures had small 7–8 pt body type despite substantial unused page area. Selected sizes were increased in print CSS for those profiles, without introducing decorative diagrams or rasterized CV text. A successful PDF build alone remains insufficient to assert absence of clipping: inspect final screenshots and extraction after CI.
4. In RU backend metadata, the '.NET' label lost its leading period, while project-work sections used inconsistent English and Russian headings. The source was corrected and experience copy simplified.
5. The original architecture summary emphasized abstract 'decision boundaries' more than concrete ownership. Revised bilingual copy names UniversalToolchain's plan/verifier and botay!'s offline web/Android implementation, and clearly notes the summer MCST internship.

### Strategy comparison and decision

- **Experience-first:** employer context is easy to identify, but a two-month internship does not fully represent the candidate's independently built architecture.
- **Engineering-evidence-first:** greatest technical detail; without categorical separation it can imply personal projects were paid jobs.
- **Hybrid Software Engineer — Systems & Architecture (chosen):** one genuine internship, different compiler/product/backend projects, independently supported recognition. The improvement over experience-first is coverage of real systems ownership; over evidence-first, clarity about employer vs project status.

### Before vs after — factual, nonnumeric review

| Criterion | Before PR #63 follow-up | After source revision | Grounding |
|---|---|---|---|
| Recruiter clarity | broad identity, abstract wording | compiler plan and offline product named | bilingual architecture summaries |
| Technical depth | strong but compressed | preserves LLVM LICM, planner/verifier, offline replay | actual project descriptions and sources |
| Differentiation | MCST selection rank not displayed | scoped top technical-selection distinction | private organizer message, 5 June 2026 |
| Evidence credibility | private/public validation blurred | explicitly attributed nonpublic distinction | evidence layer selection_result |
| Natural writing | ownership jargon repeated | simpler technical sentences | summaries and skill copy |
| Visual readability | tiny print body with excess space | larger selected print typography | changed CSS; final screenshot still must be assessed |
| ATS compatibility | text PDF with two-column flow | preserved text + links; two-column tradeoff remains | current generator, extraction validation |
| Role targeting | backend work misclassified | paid/client categories separated from projects | updated backend and selective protection CV |
| Interview defensibility | personal projects under employment | explicit independence and narrower stage attribution | source change and evidence boundaries |

### Adversarial findings and remaining limitations

- **MCST 104/104** is one technical challenge during selection, not 104 internship-related tests. Organizer evidence is private and its broadcast lists the highest scorer by school/location rather than the candidate's full name; identity is supported by the candidate's contemporaneous reply. Interviewers can be shown the dated original privately if appropriate.
- **botay!** Android release pipeline and offline idempotency do not prove active users or broad distribution.
- **VpnMediator/CompilationLabLMS** payment-state code and tests do not independently establish 24/7 production availability, full provider E2E readiness or revenue.
- **UniversalToolchain 1,324** is a repository-revision-scoped exact test manifest, not a time-independent or independent audit.
- **Two-column PDF** has a possible ATS read-order disadvantage. A single-column version should be considered if a job portal's actual parser loses sections; it was not introduced here without evidence.
- **Visual clipping and latest CI:** only claim pass when the exact post-change generated PDF and its screenshot have been checked. The previous workflow run is a baseline, not proof of the revised source.
- **Further evidence rather than marketing:** dated anonymized usage for VpnMediator, externally used UniversalToolchain package, first independent botay! users, and a shareable MCST selection/result artifact would materially improve the next version.
