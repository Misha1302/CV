# CV site — generated, role-specific, verifiable

This repository publishes Mikhail Razakov's CV site and role-specific PDFs.

## Canonical sources

The repository now separates factual evidence from rendered profile copy:

- `knowledge/resume-evidence.json` — canonical evidence/claim layer: facts, evidence strength, boundaries, metrics, role fit, and unresolved gaps.
- `data/site.json` — current canonical **render source** for public profile copy while the generator migration to evidence-backed projections is still pending.

A rendered CV must not make a stronger factual claim than the evidence layer supports. The generator currently produces:

- canonical RU/EN profile pages;
- the landing page;
- project case studies;
- redirect pages for deprecated profile URLs;
- metadata, Open Graph, JSON-LD, sitemap, and robots.txt;
- one-page role-specific PDFs.

Generated HTML and PDF files must not be edited manually.

## Canonical profiles

1. Software Engineer — Systems & Architecture (canonical)
2. C++ / LLVM Systems
3. .NET Backend / Platform Reliability
4. Compiler Infrastructure / Language Tooling Engineer
5. Compiler & Program Analysis Engineer
6. Compiler Backend / Code Generation Engineer
7. Static Analysis / Program Analysis Engineer
8. Quant Developer / Research Engineer
9. Quantitative Research / Research Software Engineering
10. Compiler / Software Protection Engineer (selective; evidence-limited)

The landing page uses Software Engineer — Systems & Architecture as the canonical identity and exposes role-specific alternatives. Compiler/runtime work remains a primary proof of technical depth, but it is not the site's only positioning axis. The architecture profile is deliberately a hands-on engineering profile rather than a `Software Architect` seniority claim. Profile navigation and landing-card labels are defined by the canonical `profile_ui` metadata in `data/site.json`. Older narrow URLs redirect to the nearest canonical profile.

## Local build

```bash
python -m pip install beautifulsoup4 pymupdf pillow playwright weasyprint
python tools/validate_resume_knowledge.py
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --evidence-dir /tmp/cv-pdf-evidence
python tools/build_site.py --manifest
python tools/validate_cv.py --pdf-dir pdf
```

For browser layout and screenshot regression:

```bash
python -m playwright install chromium
python tools/visual_regression.py --output-dir /tmp/cv-visual
```

The visual workflow keeps the established regression baseline for existing representative pages and additionally smoke-checks every generated RU/EN profile on desktop, mobile, and with JavaScript disabled. The capture directory also contains `current.json` with replayable layout metrics and image hashes.

## Validation contracts

The checks enforce:

- a valid, internally linked evidence knowledge base with explicit high-risk claim boundaries;
- `data/site.json` as the current deterministic render source;
- no content rewriting from JavaScript;
- matching title, description, Open Graph, JSON-LD, visible role, print role, and PDF role;
- no stale availability wording;
- no untranslated English sentences in Russian profiles or Cyrillic in English profiles;
- valid internal links and optional live external-link checks;
- local portrait asset, no remote avatar dependency;
- one-page A4 PDFs with text layers and links;
- desktop, mobile, and JavaScript-disabled screenshot regression/smoke checks;
- recursive SHA-256 manifest integrity.

## C++ / Systems Engineer — specialized ATS resume (13 November 2026)

The C++/LLVM-focused specialist route [RU](ru-cpp-systems.html) /
[EN](en-cpp-systems.html) is authored in the single canonical
`data/site.json -> profiles.systems` model. Its one-column, text-extractable
A4 PDF is optimized for ATS; the editorial website remains available for
direct technical outreach. Both languages have generated companion
DOCX and Markdown exports in the `pdf/` directory:

- RU: [PDF](pdf/Mikhail_Razakov_CPP_Systems_RU.pdf) ·
  [DOCX](pdf/Mikhail_Razakov_CPP_Systems_RU.docx) ·
  [Markdown](pdf/Mikhail_Razakov_CPP_Systems_RU.md)
- EN: [PDF](pdf/Mikhail_Razakov_CPP_Systems_EN.pdf) ·
  [DOCX](pdf/Mikhail_Razakov_CPP_Systems_EN.docx) ·
  [Markdown](pdf/Mikhail_Razakov_CPP_Systems_EN.md)

Rebuild using `python tools/build_cv.py --output-dir pdf`. Verify using
`python tools/validate_cv.py --pdf-dir pdf`; this checks the C++ PDF reading
order and the DOCX/Markdown synchronization as well as all existing profiles.
The LLVM 29/29 and MCST graph 14/14 cases are local, version-scoped
verification. An extended PS-form smoke suite passed 907/912 cases, with
five conservative `maybe` answers where the oracle expected `no`; these
are not the 104 official MCST selection cases.

## Static Analysis / Program Analysis — ATS specialist (13 November 2026)

The specialist route [RU](ru-program-analysis.html) / [EN](en-program-analysis.html)
keeps the editorial HTML presentation while producing single-column, text-extractable
A4 PDF, DOCX and Markdown from the canonical model
`data/site.json -> profiles.program_analysis`.

- RU: [PDF](pdf/Mikhail_Razakov_Program_Analysis_RU.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Program_Analysis_RU.docx) /
  [Markdown](pdf/Mikhail_Razakov_Program_Analysis_RU.md)
- EN: [PDF](pdf/Mikhail_Razakov_Program_Analysis_EN.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Program_Analysis_EN.docx) /
  [Markdown](pdf/Mikhail_Razakov_Program_Analysis_EN.md)

Generate only this specialist without changing unrelated PDFs:
`python tools/build_cv.py --output-dir pdf --profile program_analysis`.

Checks: `python tools/validate_cv.py --pdf-dir pdf` verifies ATS reading order,
pinned project links and synchronized DOCX/MD alongside the C++ specialist.
DerefAfterNullAnalyzer is a separate public project from ISP RAS SharpChecker.
The reproducible pinned runs are 18/18 Roslyn and 29/29 LLVM 22.1.8;
these do not prove arbitrary program soundness, production integration or speedup.
The PS-form extended smoke run of 907/912 is recorded separately, with
five conservative `maybe` returns where the oracle expected `no`.

## Compiler Infrastructure / Language Tooling — ATS pair (13 November 2026)

The canonical infrastructure CV uses `data/site.json -> profiles.general`, with
editorial HTML at [RU](ru.html) and [EN](en.html). Its one-column ATS-compatible
PDF, DOCX and Markdown are generated from that same canonical profile,
without editing any exported artifacts directly.

- RU: [PDF](pdf/Mikhail_Razakov_Compiler_Infrastructure_RU.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Compiler_Infrastructure_RU.docx) /
  [Markdown](pdf/Mikhail_Razakov_Compiler_Infrastructure_RU.md)
- EN: [PDF](pdf/Mikhail_Razakov_Compiler_Infrastructure_EN.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Compiler_Infrastructure_EN.docx) /
  [Markdown](pdf/Mikhail_Razakov_Compiler_Infrastructure_EN.md)

Build only this specialist with
`python tools/build_cv.py --output-dir pdf --profile general`.
Then regenerate the site manifest with `python tools/build_site.py --manifest`
and run `python tools/validate_cv.py --pdf-dir pdf`.

Evidence limits: UniversalToolchain's checked-in test manifest declares
1,324 expected passes; this is not presented as a freshly rerun whole-suite
result. The LLVM Global IV result is tied to a fixed LLVM 22.1.8 commit and
29/29 selected tests. PlanFuzz is an experimental UT subsystem with replay
and counterexample reduction, not a complete compiler fuzzer or an
independent proof of compiler correctness. The Rust x86-64 codegen is
experimental and separate from LLVM/UT production integration.

## Compiler Backend / Code Generation — ATS specialist (14 November 2026)

The specialist [RU](ru-compiler-backend.html) and
[EN](en-compiler-backend.html) pages are generated from
`data/site.json -> profiles.compiler_backend`. The editorial HTML
remains separate from the one-column ATS PDF, DOCX and Markdown exports:

- RU: [PDF](pdf/Mikhail_Razakov_Compiler_Backend_RU.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Compiler_Backend_RU.docx) /
  [Markdown](pdf/Mikhail_Razakov_Compiler_Backend_RU.md)
- EN: [PDF](pdf/Mikhail_Razakov_Compiler_Backend_EN.pdf) /
  [DOCX](pdf/Mikhail_Razakov_Compiler_Backend_EN.docx) /
  [Markdown](pdf/Mikhail_Razakov_Compiler_Backend_EN.md)

Regenerate without touching other specialty PDF files:

```bash
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --profile compiler_backend
python tools/build_site.py --manifest
python tools/validate_cv.py --pdf-dir pdf
```

The Rust backend's local verification is pinned to commit
`dd0693c3af06dc9a3612b68ecb94f9637d6b0514` (42/42 debug
tests, fmt and strict Clippy on 2026-11-14). The release-test attempt
did not reach testing because the local build exceeded disk quota.
GitHub Actions run 34896109843 independently reports success for the
same commit on 2026-09-14. This is a restricted i64 IR playground,
not a full x86-64 target backend or a security sandbox. The separate
LLVM IR Global IV project passed 29/29 selected tests on pinned LLVM
22.1.8; the UT 1324 figure refers to the checked-in test manifest,
not a freshly rerun entire test suite.

## CV release — 2026-11-03

Send-ready, one-page C#/.NET resumes (Russian): **[choose the right version](releases/2026-11-03/README.md)**.

- [Backend / ATS PDF](releases/2026-11-03/01_Backend_ATS.pdf) — default for HR applications.
- [Systems / Reliability PDF](releases/2026-11-03/02_Systems_Platform.pdf) — for direct engineering outreach (legacy 02_Tech_Lead link preserved).
- [Runtime / Compiler PDF](releases/2026-11-03/03_Runtime_Compiler.pdf) — for systems and compiler teams.
- [Full package ZIP](releases/2026-11-03/Mikhail_Razakov_CV_Complete_Package_2026-11-03.zip) — PDFs, editable DOCX, Markdown, evidence review and outreach texts.

The application CVs and site are now generated from the same data/site.json presentation model, checked against the evidence knowledge base. Run python tools/build_release.py and python tools/validate_release.py after changing public CV content.

## Unified bilingual application edition (2026-11-03)

The landing page presents C#/.NET Backend as the default recruiting route while retaining all ten established specialist profiles. A new RU/EN engineering deep-dive is available at ru-engineering.html and en-engineering.html. Quark2 has a source-backed research case; TuringSquare-LMS is explicitly scoped as work in progress with agent contributions and T-Bank sandbox.

Rebuild with:

    python tools/validate_resume_knowledge.py
    python tools/build_site.py
    python tools/build_cv.py --output-dir pdf
    python tools/build_release.py
    python tools/build_site.py --manifest
    python tools/validate_cv.py --pdf-dir pdf
    python tools/validate_release.py

The public release ZIP intentionally excludes internal research notes. No Git history rewriting or force pushes are used. The previous public attachment may remain in immutable Git history; treat any underlying private information in that old attachment separately.

## Complete application portfolio websites (3 November 2026)

Three independent, shareable editorial CV websites are now built from the same
data/site.json application_cvs variant records as PDF/DOCX/Markdown.

| Target | Russian website | English website |
| --- | --- | --- |
| C#/.NET Backend / ATS | [RU](ru-backend-ats.html) | [EN](en-backend-ats.html) |
| Systems / Reliability | [RU](ru-systems-platform.html) | [EN](en-systems-platform.html) |
| Compiler / Runtime / Program Analysis | [RU](ru-runtime-compiler.html) | [EN](en-runtime-compiler.html) |

Each page contains the full CV profile, all three professional experience rows,
all variant-specific technical skills and project claims, detailed problem/approach/
outcome sections, source/case links, education, recognition and explicit evidence
limitations. It also offers the corresponding one-page PDF, DOCX and Markdown.
The previously published ru-engineering.html/en-engineering.html URLs remain
functional and now show the current Tech Lead edition.

Regenerate using:

    python tools/build_site.py
    python tools/build_release.py
    python tools/validate_application_sites.py
    python tools/validate_cv.py --pdf-dir pdf

No production code in portfolio reference projects is changed by this work.
The application-sites.css stylesheet is self-contained and requires no JS or
remote asset services. The canonical public fact model remains data/site.json,
bounded by knowledge/resume-evidence.json.


## 2026-11-07 — specialized performance and architecture CVs

The existing November 3 release is retargeted: **02 Systems / Platform** and **03 Compiler / Runtime / Performance**. Legacy filenames and page URLs are preserved for previously shared links; visible headings and role selectors are updated. 01 Backend ATS remains unchanged.

- Systems / Reliability: [RU](ru-systems-platform.html) / [EN](en-systems-platform.html) (legacy Tech Lead URLs retained)
- Compiler / Runtime / Program Analysis: [RU](ru-runtime-compiler.html) / [EN](en-runtime-compiler.html)
- [Independent review and measurement roadmap](reviews/PERFORMANCE_SYSTEMS_CV_REVIEW_2026-11-07.md)

Application CVs and generated HTML, DOCX, PDF and Markdown are all owned by data/site.json, with claim boundaries in knowledge/resume-evidence.json. Never hand-edit generated outputs.
