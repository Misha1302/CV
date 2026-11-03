# CV overhaul — evidence and adversarial QA, 3 November 2026

## Scope and provenance

- Source repository: `Misha1302/CV`; base `main` commit: `e65862c8904701efa1d3a9bb51b207bc64830b31`.
- Isolated worktree used; the pre-existing older Fedora `CV` working directory with uncommitted changes was not overwritten.
- Editable model: `data/site.json`; claim/evidence limits: `knowledge/resume-evidence.json` (35 assets).
- Outputs: site + 20 retained profile PDFs + six ATS/engineering/runtime application CVs, each in PDF/DOCX/Markdown; separate detailed RU/EN engineering pages.
- Scope excludes changing VpnMediator, UniversalToolchain, Quark2, LMS and other reference repositories.

## Claim-to-evidence risk matrix

| Claim | Evidence inspected / role | Confidence boundary |
| --- | --- | --- |
| ISP RAS / SharpChecker, symbolic computation from Oct 2026 | Candidate account and recorded private-document research, `experience_isp_ras_2026` | User-attested employment and task scope; confidential code not exposed |
| MCST internship, LLVM 22 LICM | `LLVM-basic-LICM-implementation` Git HEAD `7abafde796ba6b4de6a0e0f52473938e2825eb4f`, candidate attestation and prior evidence | Internship details not independently verified against employment records here |
| About one year total commercial practice | `experience_commercial_aggregate_2026` | Candidate-attested; not represented as continuous one-employer production .NET tenure |
| VpnMediator: ASP.NET Core access service + Python payment bot; payment reconciliation | Private code inspected with candidate authorization; payment-recovery tests observed in the repository | Source reviewed, not executed; user counts/live health independently unverified |
| UniversalToolchain: LanguagePlan, verifier and interpreter/CIL routes | Repo HEAD `5626a5e7fdd1c5d85158fab21752ef74c34926a3`; `UniversalToolchain.LanguageSdk/LanguageCompiler.cs`, `LanguagePlan.cs`, `LanguagePlanVerifier.cs`; `eng/test-counts.json` | Repository reports `totalPassed:1324`; this is **not a fresh 1324-test execution result** |
| Quark2: DynamicMethod/Reflection.Emit and experimental CLR invocation benchmarks | Public repository HEAD `7bc718a2fd518559ec7c344942eec879216584bb`, 03 Nov research release, existing evidence `history_quark2` | Prototype only; no demonstrated general production speedup or current-runtime benchmarks |
| TuringSquare-LMS: course entitlements, T-Bank sandbox and agent-assisted implementation | Candidate input and internal research; private main branch differs from ongoing agent-assisted development | Not production and not exclusive personal authorship; sandbox is not go-live; latest code cannot be verified from old main |
| x86-64 codegen, global-IV, other research | Public repo HEADs checked for x86 codegen `dd0693c3af06dc9a3612b68ecb94f9637d6b0514`, global-IV `0d759dcf3af7a5652432eb0fea5b9ca27ec88f74`; evidence ledger | Research prototypes, not equivalent to employer production ownership |

No seniority title is asserted. Private operational details remain excluded from distributed CVs. The case narrative describes scope and constraints rather than inventing throughput or payment KPIs.

## Independent adversarial reviews

### A. HR / 20-second screen

**Challenge:** Earlier root landing foregrounded broad architecture; C#/.NET target was harder to find and a generic PDF link was insufficient. Exact total employment tenure could be mistaken for independently verified continuous production experience.

**Repair:** Main headline now explicitly names C#/.NET Backend; default download is the 1-page ATS edition. Three role-targeted editions plus English versions are visible at once. Commercial duration is labeled candidate-reported in public CV copy. Employment comes before awards and research details.

**Residual risk:** One year aggregate commercial practice and employer claims may need reference documents before offer/verification. Specialist-role fit still depends on vacancy.

### B. Senior .NET team lead

**Challenge:** Source-level mechanisms could be conflated with measured production outcomes; repository test manifests might be presented as freshly passed tests; LMS implementation could be falsely attributed to one person; Quark2 benchmarks are experimental.

**Repair:** Kept the ASP.NET Core/Python boundary explicit; separated payment evidence, entitlement, reconciliation and restart recovery; preserved source links; marked UT 1324 as manifest count; called out agent implementation and sandbox status for LMS; marked Quark2 as a research prototype. Added RU/EN deep-dive and honest case ownership paragraphs.

**Residual risk:** Live VPN operational metrics, T-Bank production readiness and benchmark reproducibility outside the repo were not independently demonstrated here. No claims of externally validated live usage or 1,324 freshly executed UT tests.

### C. Senior product designer / independent frontend QA

**Challenge:** Original first-screen heading had an orphaned ".NET" fragment and its brand still advertised a different primary role; project cards were overly dense, with a lone fourth card on its own row.

**Repair:** Separate typographically balanced candidate/role lines; align brand, OG preview and SEO titles; turn main projects into a two-column editorial list with progressive technical disclosure through case pages; preserve 10 specialist profiles and redirects. Mobile menu and download targets were browser-tested; visible focus states, reduced-motion handling and responsive widths retained.

**Residual risk:** Visual taste remains subjective, but layout/overflow behavior was measured in a browser.

## Reproducible technical QA

| Check | Status | Actual evidence |
| --- | --- | --- |
| Knowledge-base schema and fact references | PASS | 35 assets, 9 levels, 7 playbooks |
| Canonical source and generated HTML, SEO, internal links | PASS | `tools/validate_cv.py --pdf-dir pdf --skip-manifest` |
| Retained specialist PDF generation | PASS | 20 PDFs from `tools/build_cv.py`; old URLs preserved |
| Release CV synchronization | PASS | `tools/validate_release.py`: 6 PDFs + 6 DOCXs + 6 MD |
| PDF format and copyability | PASS | Six A4 one-page PDFs, textual layers, embedded DejaVu fonts, 6–7 live links, minimum font 8.35pt |
| DOCX opening and single-page rendering | PASS | Six DOCX documents converted through LibreOffice: one page each |
| Playwright visual regression | PASS | 10 golden cases, 59 smoke views (including three backend updates and new RU/EN engineering views) |
| Browser integration, desktop/mobile, downloads | PASS | `browser-qa.json`: seven screenshots, zero errors/overflow, downloadable PDF/DOCX/MD HTTP 200 |
| Accessibility exploratory check | PARTIAL | Semantic H1, accessible links, keyboard focus and reduced-motion styles; full automated WCAG audit not run |
| Live employer-site SEO indexing | NOT RUN | Search crawler indexing cannot be guaranteed by local checks |
| Upstream VpnMediator / UT / LMS project test suites | NOT RUN | Out of CV repository test scope; source-level evidence inspection only |
| GitHub Actions and public Pages deployment | Verify from the GitHub PR and deployment statuses | Local QA is not a substitute |

## Public-release privacy and limitations

The former `releases/2026-11-03/04_Evidence_Research_and_Review.md` contained internal paths and private-repository evidence. It has been removed from the current tree and excluded from the rebuilt ZIP. A sanitized public `04_Public_Evidence_Boundaries.md` replaces it. The old file may remain reachable through historical Git commits; Git history has **not** been rewritten, as the task forbids force pushes or destructive rewriting.

The product content and docs can be sent to employers; the separate technical QA report is for author review, not a claim of certification.

## Screenshots

- [Landing / desktop](screenshots/landing-desktop.webp)
- [Landing / mobile](screenshots/landing-mobile.webp)
- [Extended engineering profile](screenshots/engineering-desktop.webp)
- [VpnMediator case](screenshots/vpn-case-desktop.webp)
- [Backend profile / mobile](screenshots/backend-profile-mobile.webp)
- [Quark2 / mobile](screenshots/quark2-case-mobile.webp)
- [PDF / ATS](screenshots/ats-pdf.webp)
