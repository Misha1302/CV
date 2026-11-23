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
- **PDFs rebuilt from the current `data/site.json`**: each profile PDF must contain its profile summary verbatim, and the PDF set must match `profile_order` exactly (no orphaned or missing files). This catches the case where the source is edited and the PDFs are left at the previous revision, so the site and the PDF describe different CVs;
- **release artifacts built from the current source**: every `.md` and `.pdf` in `releases/<date>/` must contain the current variant summary and project texts. Once a single PDF was stale while its Markdown was fresh, and nothing failed;
- desktop, mobile, and JavaScript-disabled screenshot regression/smoke checks;
- recursive SHA-256 manifest integrity.

The artifact checks are regression-tested by `tools/test_validate_cv.py`, which CI runs
after the validators. Each test is paired with a mutation: deleting the check makes the
test fail. Run it locally with `python3 tools/test_validate_cv.py -v`.

## CV release — 2026-11-03

Send-ready, one-page C#/.NET resumes (Russian): **[choose the right version](releases/2026-11-03/README.md)**.

- [Backend / ATS PDF](releases/2026-11-03/01_Backend_ATS.pdf) — default for HR applications.
- [Tech Lead PDF](releases/2026-11-03/02_Tech_Lead.pdf) — for direct engineering outreach.
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
| Backend / Engineering Lead | [RU](ru-tech-lead.html) | [EN](en-tech-lead.html) |
| Runtime / Compilers / Performance | [RU](ru-runtime-compiler.html) | [EN](en-runtime-compiler.html) |

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

- Systems / Platform: [RU](ru-tech-lead.html) / [EN](en-tech-lead.html)
- Compiler / Runtime / Performance: [RU](ru-runtime-compiler.html) / [EN](en-runtime-compiler.html)
- [Independent review and measurement roadmap](reviews/PERFORMANCE_SYSTEMS_CV_REVIEW_2026-11-07.md)

Application CVs and generated HTML, DOCX, PDF and Markdown are all owned by data/site.json, with claim boundaries in knowledge/resume-evidence.json. Never hand-edit generated outputs.

## 2026-11-24 — company-targeted variants and KeyAuth

Eight employer-targeted one-page CVs (RU/EN) are generated from the same canon:

- Yandex — algorithms / C++ / systems
- Huawei — LLVM / compiler engineering, olympiad track first
- MCST — LLVM optimization and microarchitecture
- Google — algorithms and systems (EN-first)
- Amazon — backend state, recovery and operations (EN-first)
- T1 — .NET / SQL / integrations
- Kaspersky — C++ / low level / code analysis
- Sber — backend / SQL / algorithms

`data/company-variants.json` only reorders and re-emphasises existing evidence
(role, summary, three proof rows, skills order, project and experience order,
recognition order). It cannot introduce new claims: `validate_cv.py` rejects
unknown project or experience references, a non-permutation recognition order,
age disclosure, and evidence-bounded forbidden claims. The landing page lists
them in section 02 · Компании.

KeyAuth is now a first-class project (`projects.keyauth`, `cases/{ru,en}-keyauth.html`)
with evidence asset `project_keyauth_licensing`. The anti-piracy outcome is
`USER_ATTESTED` and worded as such; no claim of a verified or impossible-to-bypass
protection is made.

Rebuild and verify:

    python tools/build_site.py
    python tools/build_cv.py --output-dir pdf
    python tools/build_release.py
    python tools/build_site.py --manifest
    python tools/validate_cv.py
    python tools/validate_release.py
    python tools/validate_application_sites.py
    python tools/validate_resume_knowledge.py
    python tools/test_validate_cv.py -v
