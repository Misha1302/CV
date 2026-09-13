# CV Role-Specific Suite — Implementation & Validation Report

Date: 2026-09-13 / finalized 2026-09-14
Branch: `refactor/cv-role-specific-suite-2026-09`
Baseline: `acf7dad791b95285beb68a6f69e7723aaa20b9c0` (`origin/refactor/cv-evidence-first-rebuild-2026-09`)
Status: implementation complete pending final commit/CI identity at the time this report was written.

This report supersedes the earlier role-selection decision in `CV-REBUILD-RESEARCH-2026-09-13.md` where newer evidence or the explicit private software-protection attestation changes the conclusion.

## 1. Executive decision

The correct deliverable is **not one universal compiler CV**. The evidence and the 2026 hiring market support a small role-specific suite with a common evidence ledger and one canonical source of truth.

Primary variants:

- **Compiler Engineer — LLVM / Backend / Code Generation**: strongest fit for LLVM backend, codegen, register-allocation and optimization roles.
- **Static Analysis / Program Analysis Engineer**: strongest fit for SharpChecker, Roslyn data-flow and interprocedural-analysis roles.
- **Compiler Infrastructure / Language Tooling Engineer**: strongest fit for IR/pass infrastructure, language tooling and compiler architecture roles.
- **Compiler & Program Analysis Engineer — broad fallback**: only when the vacancy does not cleanly map to one specialist profile.
- **Compiler / Software Protection Engineer — selective, evidence-limited**: valid only for targeted hardening roles and intentionally bounded to verified public licensing history plus user-attested private client-side obfuscation.

The old backend, C++ systems and quant profiles remain separate products. The suite avoids turning every CV into a compiler CV.
## 2. Fresh 2026 market evidence

A 26-role sample was checked across NVIDIA, Apple, AMD, program-analysis vendors/research, and compiler-security companies. The point of the sample is not to count jobs; it is to identify repeated role boundaries and rejection filters.

| # | Employer / role | Role signal used for CV design |
|---:|---|---|
| 1 | NVIDIA — Compiler Engineer, Backend, New College Grad 2026 (JR2017290) | C++, LLVM codegen, register allocation, unit testing, IR/MIR |
| 2 | NVIDIA — Backend Compiler Engineer, New College Grad 2026 (JR2021242) | backend design/codegen, LLVM, register allocation, GlobalISel/TableGen |
| 3 | NVIDIA — Senior Code Generator Compiler Engineer (JR2017210) | codegen, register allocation, scheduling, production compiler quality |
| 4 | NVIDIA — Senior Graphics Shader Compiler Engineer (JR2024686) | LLVM optimization, GPU codegen, SPIR-V, performance |
| 5 | NVIDIA — Senior DL Compiler Engineer, CUDA Tile (JR2023315) | compiler optimization, IR design, MLIR/LLVM, performance analysis |
| 6 | NVIDIA — Senior CPU Compiler Engineer, HPC (JR2020843) | production compilers, optimizer internals, LLVM, HPC |
| 7 | NVIDIA — Senior Fortran Compiler Engineer (JR2015674) | LLVM Flang, language front end, optimization, OpenMP/OpenACC |
| 8 | NVIDIA — Senior GPU Compiler Development Engineer (JR2017242) | codegen/compiler infrastructure, ISA, LLVM IR/MLIR |
| 9 | NVIDIA — Senior ML Applications and Compiler Engineer (JR2012562) | IR design, passes, codegen, LLVM/MLIR, profiling |
| 10 | NVIDIA — Build and DevOps Engineer for Compilers (JR2018968) | compiler developer productivity, CI/CD, reliability |
| 11 | Apple — GPU Compiler Backend Engineer (200678185) | LLVM-based backend, productized optimizations, architecture feedback |
| 12 | Apple — GPU Compiler Backend/Research Engineer (200593210) | LLVM backend, code generation, hardware/compiler co-design |
| 13 | Apple — GPU Compiler Engineer (200641114) | language constructs, compiler transformations, developer tools |
| 14 | Apple — GPU Compiler Engineer (200649008) | compiler transformations and GPU tooling |
| 15 | Apple — Swift Compiler Backend Engineer (200661730) | language-runtime/backend specialization |
| 16 | Apple — GPU Compiler Backend Research Engineer (200646322) | codegen, optimizations, architecture research |
| 17 | AMD — GPU Compiler Development Engineer (87501) | MLIR lowering, LLVM/GPU, unit tests, performance |
| 18 | AMD — Senior GPU Compiler Development Engineer (87504) | MLIR dialects/lowering/passes, LLVM, graph IR |
| 19 | AMD — Principal Compiler & ML Acceleration Engineer (88512) | compiler infrastructure, MLIR lowering, scheduling/optimization |
| 20 | AMD — Senior Staff Compiler Software Engineer (88607) | MLIR/LLVM, lowering, target codegen, performance-regression infra |
| 21 | AMD — Rust, Compilers and GPU Systems Engineer (89874) | rustc/MIR, MLIR, LLVM IR, AMDGPU codegen, correctness boundaries |
| 22 | Endor Labs — Program Analysis Engineer (4691341005) | static analysis, call graphs, SAST/SCA, precision/recall/performance |
| 23 | Inria — Research Engineer, Static Analysis of OCaml Programs (2026-09842) | abstract interpretation, AST, analysis engine, precision/performance |
| 24 | Guardsquare — Senior Compiler Engineer C++/LLVM (8072068) | LLVM hardening, reverse engineering, static analysis/dynamic tampering |
| 25 | Guardsquare — Compiler Engineer C++/LLVM, Singapore (8078823) | compiler internals, code hardening, low-level debugging |
| 26 | Black Duck — Software Engineer 3 C++/Rust, Static Analysis | SAST/static-analysis engine, analysis depth, scalability/performance |
Representative sources checked during the final pass:

- NVIDIA backend NCG: https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Compiler-Engineer--Backend--New-College-Grad-2026_JR2017290
- NVIDIA backend NCG: https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Backend-Compiler-Engineer---New-College-Grad-2026_JR2021242
- NVIDIA senior codegen: https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-Compiler-Engineer---Backend_JR2017210
- Apple GPU backend: https://jobs.apple.com/es-cl/details/200678185-0836/apple-gpu-compiler-backend-engineer
- Apple GPU backend/research: https://jobs.apple.com/en-au/details/200593210/apple-gpu-compiler-backend-research-engineer-graphics-game-and-ml
- AMD GPU compiler: https://careers.amd.com/careers-home/jobs/87501?lang=en-us
- AMD senior GPU compiler: https://careers.amd.com/careers-home/jobs/87504
- AMD principal compiler/ML: https://careers.amd.com/careers-home/jobs/88512
- AMD senior staff compiler: https://careers.amd.com/careers-home/jobs/88607
- AMD Rust/compiler/GPU systems: https://careers.amd.com/careers-home/jobs/89874
- Endor Labs program analysis: https://job-boards.greenhouse.io/endorlabs/jobs/4691341005
- Inria static analysis: https://recrutement.inria.fr/public/classic/en/offres/2026-09842
- Guardsquare LLVM hardening: https://job-boards.greenhouse.io/guardsquare/jobs/8072068
- Guardsquare compiler/security: https://job-boards.greenhouse.io/guardsquare/jobs/8078823

### Market conclusion

The strongest early-career differentiator is not a generic `compiler engineer` label. It is **role-shaped proof**. Backend roles repeatedly reward codegen/register-allocation evidence; analysis roles reward CFG/data-flow/interprocedural reasoning; infrastructure roles reward IR/pass/lowering/tooling architecture. Software-protection roles are adjacent but demand direct hardening evidence and often 2–5+ years of relevant experience.

The largest real competency gaps remain **MLIR**, GPU/SIMT-specific compiler work, and upstream/open-source compiler contribution. Those are career gaps, not wording problems, and the CV must not disguise them.
## 3. Evidence ledger and claim boundaries

| Claim | Status | Final handling |
|---|---|---|
| ISP RAS / SharpChecker: contributes to industrial C#/.NET static analysis platform | VERIFIED / bounded professional fact | Used in all relevant compiler/analysis variants |
| Personal ownership of SharpChecker symbolic-execution engine | DO_NOT_USE without stronger attribution | Removed from role CVs |
| MCST internship, July–August 2026, LLVM 22/C++ compiler work | VERIFIED | Used as primary professional compiler evidence |
| LLVM LICM implementation and conservative Global-IV prototype | VERIFIED | Used with legality/unsupported-case boundaries |
| Global-IV regression surface: 29 positive/negative cases | VERIFIED from prior repository audit | Used as project evidence |
| DerefAfterNullAnalyzer: Roslyn CFG fixed-point null-state analysis | VERIFIED | Primary program-analysis project |
| x86-64 backend/register-allocation lab | VERIFIED | Primary backend/codegen project |
| UniversalToolchain compiler/language infrastructure | VERIFIED | Primary infrastructure project |
| UniversalToolchain exact test manifest 1,324/1,324 | VERIFIED from prior repository audit | Used in infrastructure/backend supporting proof |
| KeyAuth/LoginAsset public licensing/activation prototypes | VERIFIED, historical | Used only in selective software-protection variant |
| Public KeyAuth/LoginAsset date | VERIFIED as November 2023 public history | Final CV uses `2023`, not the earlier unsupported `2022–2024` range |
| Private client-side obfuscation of sensitive config/service URLs | USER_ATTESTED_PRIVATE | Allowed only as a conservative private-version statement |
| Anti-debugging, CFF, virtualization, anti-tamper, packing, string encryption, custom obfuscation algorithms | DO_NOT_USE | Explicitly excluded; no inference from the private attestation |

## 4. Architecture and source of truth

`data/site.json` is the canonical CV data source. Role-specific HTML and PDF files are generated outputs, not independently edited documents.

Generation and verification flow:

`data/site.json -> tools/build_site.py -> EN/RU HTML -> tools/build_cv.py -> PDFs -> tools/validate_cv.py + tools/visual_regression.py`

New profile keys are `compiler_backend`, `program_analysis`, and `software_protection`; `general` is the compiler-infrastructure profile and `compiler` is the broad fallback. Existing `backend`, `systems`, `quantdev`, and `quant` records were intentionally preserved.

The GitHub Actions rebuild workflow no longer calls the old one-off `tools/rebuild_compiler_profile_20260913.py`, because that migration script would overwrite the new canonical role suite after every build.
## 5. Profile design: OLD → NEW → WHY

| OLD | NEW | WHY |
|---|---|---|
| One broad compiler/program-analysis CV carried backend, analysis and infrastructure signals together | Dedicated LLVM/backend, program-analysis, infrastructure and broad-fallback variants | Recruiters can match the first 8 seconds of the CV to the vacancy's actual role boundary |
| `general` mixed general compiler signals | `general` is explicitly Compiler Infrastructure / Language Tooling | UniversalToolchain and deterministic compiler composition are now the center of this variant |
| Broad compiler CV included stronger private/production side narratives | Broad compiler fallback now stays inside professional compiler + public compiler/program-analysis evidence | Reduces “does everything” ambiguity and evidence risk |
| SharpChecker wording could imply more ownership than directly attributable | High-level contribution to industrial C#/.NET static-analysis platform only | Keeps professional signal while avoiding unsupported symbolic-engine ownership |
| No dedicated backend/codegen CV | LLVM / Backend / Code Generation profile | Market repeatedly asks for codegen, register allocation, scheduling, IR/MIR and backend testing |
| No dedicated static/program-analysis CV | Static Analysis / Program Analysis profile | Makes Roslyn CFG, fixed-point data flow and conservative interprocedural analysis immediately visible |
| No publishable software-protection profile under public evidence alone | Selective/evidence-limited software-protection profile | User-attested private obfuscation allows a bounded adjacent profile, but not invented hardening mechanisms |
| Software-protection history used an unsupported `2022–2024` range during drafting | Historical public licensing/protection prototype dated `2023` | Public KeyAuth/LoginAsset histories inspected in the final audit are from November 2023 |
| Visual regression depended on live GitHub avatar timing | Validator routes the avatar CDN request to checked-in portrait bytes and waits for fonts/images | Removes screenshot flakiness while still exercising the same runtime DOM/CSS path |

## 6. Protected-region check

The unrelated `backend`, `systems`, `quantdev`, and `quant` profile records in `data/site.json` were treated as protected content.

Mechanical comparison against baseline `acf7dad` showed:

- generated legacy HTML content is unchanged after excluding the intentional global profile-navigation expansion;
- all eight legacy PDFs have identical extracted text and identical link sets to baseline;
- binary PDF hashes can differ because the PDFs were regenerated, but their user-visible/ATS text and hyperlinks did not drift.

This is stronger than relying on a visual impression that unrelated profiles “look the same.”
## 7. Remaining evidence and career gaps

These are intentionally **not** fixed with stronger adjectives:

- **MLIR:** recurring in NVIDIA/AMD/Apple modern compiler stacks; current CV evidence is LLVM-centric.
- **GPU/SIMT compiler depth:** relevant to many high-value backend roles; current codegen evidence is x86-64 and LLVM optimization rather than a production GPU backend.
- **Upstream compiler contribution:** repeated plus signal for LLVM/Clang/MLIR roles; no upstream contribution is claimed.
- **Industrial duration:** many senior compiler/security roles require 2–5+ years; an evidence-dense CV cannot remove this filter.
- **SharpChecker attribution:** the professional platform is strong evidence, but exact personal production components should be added only when independently attributable or safely user-attested with enough specificity.
- **Software hardening depth:** the selective profile is adjacent evidence, not proof of anti-tamper/virtualization/control-flow-hardening ownership.

## 8. Adversarial omission / overclaim review

The strongest alternative was to keep one broad compiler CV and avoid role fragmentation. It loses because the current market uses materially different screening vocabularies and proof expectations for backend/codegen, program analysis, and compiler infrastructure. The cost of maintaining variants is low because generation remains centralized in `data/site.json`.

The strongest objection to the software-protection profile was that it could become keyword laundering. The repair is structural: the variant is labeled `SELECTIVE / EVIDENCE-LIMITED`, dates only the public 2023 prototype history, marks the private obfuscation statement as bounded historical evidence, and excludes unverified hardening mechanisms.

A second adversarial finding was in the visual test system itself: live GitHub-avatar loading could produce partial screenshots or timeouts. The final validator removes that external timing dependency instead of accepting a flaky baseline.

## 9. Publication/use recommendation

Use the most specific matching profile whenever the vacancy cleanly maps to one of the specialist variants. Use the broad compiler/program-analysis profile only as a fallback. Use the software-protection version selectively and never as the default compiler CV.

The suite is a presentation layer over a shared evidence model, not permission to mutate facts per vacancy.
## 10. Final local validation

Final checks were run from the isolated worktree after all claim corrections and generator changes.

- `tools/build_site.py --check`: **PASS**.
- `tools/build_cv.py`: **18/18 PDFs are exactly one page**. All ten compiler-role PDFs have a 7.9 pt minimum font and six PDF links; extracted text ranges from 2,889 to 3,302 characters.
- `tools/validate_cv.py --check-external`: **PASS** over 18 profile/language PDF outputs and 43 generated HTML pages. GitHub/Telegram links returned HTTP 200; LinkedIn returned HTTP 405 to the validator's probe and is treated as reachable/probe-restricted rather than a broken link.
- Manual PDF render inspection: **PASS** for all ten target EN/RU compiler-role PDFs; no clipping, overlap, broken glyphs, or unreadable hierarchy was observed.
- Browser visual regression: **PASS**, 10 golden regression cases plus 47 desktop/mobile/no-JS smoke views, with horizontal-overflow checks.
- Protected legacy profiles: **PASS**. Eight legacy backend/systems/quant HTML pages match baseline after removing the intentional global profile-menu expansion; eight legacy PDFs have identical extracted text and link sets to baseline.
- Forbidden-claim audit: **PASS** for the role-specific source/generated set; no `2022–2024`, symbolic-execution ownership, anti-debugging, anti-tamper, control-flow-flattening, virtualization, string-encryption, or packing claims remain.
- `git diff --check`: **PASS**.

No merge, deployment, or mutation of `main` is part of this branch.