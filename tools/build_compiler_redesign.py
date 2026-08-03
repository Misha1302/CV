from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "site.json"


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def load_data() -> dict[str, Any]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


COPY: dict[str, dict[str, Any]] = {
    "ru": {
        "title": "Михаил Разаков — инженер по компиляторам и языковым платформам",
        "description": "Compiler Engineer: UniversalToolchain/Wist2, IR, SSA, runtime, LLVM и проверка компиляторов.",
        "hero_role": "Инженер по компиляторам и языковым платформам",
        "summary": "Строю компиляторы и языковые платформы для .NET — от IR, SSA и оптимизаций до runtime, SDK и инструментов проверки. Автор UniversalToolchain/Wist2; прохожу стажировку по разработке компиляторов в МЦСТ.",
        "availability": "Доступен с сентября 2026 · Москва / удалённо · возможна частичная занятость",
        "education": "НИУ ВШЭ · «Программная инженерия» · поступление в 2026 году",
        "nav": [("experience", "Опыт"), ("recognition", "Достижения"), ("work", "Проекты"), ("skills", "Компетенции"), ("contact", "Контакты")],
        "contact": "Связаться", "download": "PDF", "menu": "Меню", "case": "Кейс", "docs": "Документация",
        "experience_heading": "Опыт и ответственность", "experience_intro": "Что именно сделал и чем подтверждён результат.",
        "recognition_heading": "Внешние результаты", "projects_heading": "Ключевые проекты", "projects_intro": "Три проекта, которые лучше всего показывают compiler/runtime-профиль.",
        "skills_heading": "Компетенции", "skills_intro": "Задачи, которые умею решать, а не просто список технологий.",
        "proofs": [
            ("1 465 тестов", "Wist2: 0 падений, clean consumers и parity интерпретатора/CIL"),
            ("1-е место из 49", "PS-form analyzer: 104/104 тестов и воспроизводимые контрпримеры"),
            ("Олимпиадные результаты", "«Высшая проба», двукратный абсолютный победитель «Юниора», Балтийский конкурс"),
        ],
        "recognition": [
            ("2026", "Высшая проба", "Призёр по промышленному программированию и отдельно по олимпиадному программированию."),
            ("2025–2026", "Юниор НИЯУ МИФИ", "Двукратный абсолютный победитель."),
            ("2026", "Балтийский инженерно-научный конкурс", "Абсолютный победитель, диплом I степени и Главная премия."),
        ],
        "mcst_bullet": "Изучаю инфраструктуру LLVM и разрабатываю оптимизационный проход; реализовал и протестировал графовые алгоритмы на C++23.",
        "project_status": {"wist": "Активная разработка · публичный SDK", "planfuzz": "Экспериментальная подсистема", "psform": "Завершённый конкурсный проект"},
        "project_labels": {"purpose": "Назначение", "ownership": "Мой вклад", "outcome": "Результат"},
        "wist_ownership": "Архитектура платформы, IR/SSA, runtime, система пакетов и стратегия проверки.",
        "planfuzz_ownership": "Модель исходов, oracle core, replay, fingerprints и reducers.",
        "psform_ownership": "Алгоритм анализа, точный oracle, stress infrastructure и разбор контрпримеров.",
        "skills": [
            ("Архитектура языковых платформ", "Модульная композиция, контракты компонентов, возможности и конфликты, manifests и lifecycle."),
            ("IR и оптимизации", "CFG, dominance, SSA, constant folding, SCCP-lite, unreachable elimination и DCE."),
            ("Runtime и code generation", "Интерпретатор, CIL backend, typed delegates и проверка эквивалентности backend-ов."),
            ("Проверка компиляторов", "Exact oracles, differential/metamorphic testing, replay, reducers, ASan/UBSan."),
        ],
        "contact_heading": "Обсудить compiler, C++ или systems-позицию",
        "updated": "Обновлено",
    },
    "en": {
        "title": "Mikhail Razakov — Compiler and Language Platform Engineer",
        "description": "Compiler Engineer: UniversalToolchain/Wist2, IR, SSA, runtime, LLVM, and compiler verification.",
        "hero_role": "Compiler and Language Platform Engineer",
        "summary": "I build compilers and .NET language platforms, from IR, SSA, and optimizations to runtimes, SDKs, and verification tooling. I created UniversalToolchain/Wist2 and am completing a compiler-engineering internship at MCST.",
        "availability": "Available from September 2026 · Moscow / remote · part-time possible",
        "education": "HSE University · Software Engineering · incoming in 2026",
        "nav": [("experience", "Experience"), ("recognition", "Recognition"), ("work", "Projects"), ("skills", "Skills"), ("contact", "Contact")],
        "contact": "Contact", "download": "PDF", "menu": "Menu", "case": "Case study", "docs": "Documentation",
        "experience_heading": "Experience and ownership", "experience_intro": "What I built and how the result was verified.",
        "recognition_heading": "External results", "projects_heading": "Selected projects", "projects_intro": "Three projects that best represent my compiler/runtime work.",
        "skills_heading": "Capabilities", "skills_intro": "Engineering problems I can solve, not just a technology list.",
        "proofs": [
            ("1,465 tests", "Wist2: zero failures, clean consumers, and interpreter/CIL parity"),
            ("1st of 49", "PS-form analyzer: 104/104 tests and reproducible counterexamples"),
            ("Competition results", "HSE Vysshaya Proba, two-time MEPhI Junior absolute winner, Baltic competition"),
        ],
        "recognition": [
            ("2026", "HSE Vysshaya Proba", "Prize-winner in industrial programming and separately in competitive programming."),
            ("2025–2026", "MEPhI Junior", "Two-time absolute winner."),
            ("2026", "Baltic engineering and science competition", "Absolute winner, first-degree diploma, and Grand Prize."),
        ],
        "mcst_bullet": "Studying LLVM infrastructure and developing an optimization pass; implemented and tested graph algorithms in C++23.",
        "project_status": {"wist": "Active development · public SDK", "planfuzz": "Experimental subsystem", "psform": "Completed competition project"},
        "project_labels": {"purpose": "Purpose", "ownership": "Ownership", "outcome": "Outcome"},
        "wist_ownership": "Platform architecture, IR/SSA, runtime, package system, and verification strategy.",
        "planfuzz_ownership": "Outcome model, oracle core, replay, fingerprints, and reducers.",
        "psform_ownership": "Analysis algorithm, exact oracle, stress infrastructure, and counterexample analysis.",
        "skills": [
            ("Language-platform architecture", "Modular composition, component contracts, capabilities/conflicts, manifests, and lifecycle."),
            ("IR and optimizations", "CFG, dominance, SSA, constant folding, SCCP-lite, unreachable elimination, and DCE."),
            ("Runtime and code generation", "Interpreter, CIL backend, typed delegates, and backend-equivalence checks."),
            ("Compiler verification", "Exact oracles, differential/metamorphic testing, replay, reducers, and ASan/UBSan."),
        ],
        "contact_heading": "Discuss a compiler, C++, or systems role",
        "updated": "Updated",
    },
}


def project_links(project: dict[str, Any], lang: str, copy: dict[str, Any]) -> str:
    links = [f'<a href="{esc(project[f"case_{lang}"])}">{esc(copy["case"])} ↗</a>']
    if project.get("repo"):
        links.append(f'<a href="{esc(project["repo"])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a>')
    if project.get("docs"):
        links.append(f'<a href="{esc(project["docs"])}" target="_blank" rel="noopener noreferrer">{esc(copy["docs"])} ↗</a>')
    return "".join(links)


def print_cv(data: dict[str, Any], lang: str, profile: dict[str, Any], copy: dict[str, Any]) -> str:
    person = data["person"]
    experiences = []
    for index, item in enumerate(profile["experience"][:2]):
        bullets = list(item["bullets"][:2])
        if index == 1:
            bullets = [copy["mcst_bullet"]]
        experiences.append(
            f'<article class="pcv-entry"><div class="pcv-date">{esc(item["date"])}</div><div><h3>{esc(item["title"])}</h3><ul>'
            + "".join(f"<li>{esc(bullet)}</li>" for bullet in bullets)
            + "</ul></div></article>"
        )
    projects = []
    for project_id in ("wist", "planfuzz", "psform"):
        project = data["projects"][project_id]
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(project[f"case_{lang}"])}">{esc(project["title"])}</a></h3><p>{esc(project[f"result_{lang}"])}</p></article>')
    skills = "".join(f'<div class="pcv-skill"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in copy["skills"])
    proof_html = "".join(f'<div class="pcv-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in copy["proofs"])
    recognition = "; ".join(f"{title}: {body}" for _, title, body in copy["recognition"])
    labels = {
        "experience": "Опыт" if lang == "ru" else "Experience",
        "projects": "Проекты" if lang == "ru" else "Projects",
        "skills": "Компетенции" if lang == "ru" else "Capabilities",
        "education": "Образование" if lang == "ru" else "Education",
        "recognition": "Достижения" if lang == "ru" else "Recognition",
    }
    return f'''<div class="print-cv" aria-label="Focused one-page CV">
<header class="pcv-header"><div><h1>{esc(person[f"name_{lang}"])}</h1><h2>{esc(profile["role"])}</h2></div><div class="pcv-contact"><a href="mailto:{esc(person["email"])}">{esc(person["email"])}</a><br><a href="{esc(person["telegram"])}">{esc(person["telegram_label"])}</a><br><a href="{esc(person["github"])}">{esc(person["github_label"])}</a></div></header>
<p class="pcv-summary">{esc(copy["summary"])}</p><div class="pcv-proofs">{proof_html}</div>
<div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels["experience"]}</h2>{''.join(experiences)}</section><section><h2 class="pcv-section-title">{labels["projects"]}</h2>{''.join(projects)}</section></main>
<aside class="pcv-side"><section><h2 class="pcv-section-title">{labels["skills"]}</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["recognition"]}</h2><p>{esc(recognition)}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["education"]}</h2><p>{esc(copy["education"])}</p></section><section class="pcv-compact"><p>{esc(copy["availability"])}</p></section></aside></div></div>'''


def header(data: dict[str, Any], lang: str, copy: dict[str, Any], other_file: str) -> str:
    person = data["person"]
    links = "".join(f'<a href="#{esc(key)}">{esc(label)}</a>' for key, label in copy["nav"])
    other_label = "EN" if lang == "ru" else "RU"
    return f'''<a class="skip-link" href="#main">{"К содержанию" if lang == "ru" else "Skip to content"}</a>
<header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(person[f"name_{lang}"])}</strong><span>compiler · runtime · verification</span></span></a><nav class="primary-nav">{links}</nav><div class="header-actions"><a class="cr-language" href="{esc(other_file)}">{other_label}</a><a class="button compact" href="#contact">{esc(copy["contact"])}</a><details class="mobile-menu"><summary>{esc(copy["menu"])}</summary><div class="mobile-panel"><nav>{links}</nav></div></details></div></div></header>'''


def hero(data: dict[str, Any], lang: str, profile: dict[str, Any], copy: dict[str, Any]) -> str:
    person = data["person"]
    photo = "https://avatars.githubusercontent.com/u/77919295?v=4&s=760"
    return f'''<section class="shell cr-hero" id="top"><div class="cr-hero-copy"><p class="eyebrow">IR · SSA · runtime · LLVM · program analysis</p><h1>{esc(person[f"name_{lang}"])}</h1><p class="cr-role">{esc(copy["hero_role"])}</p><p class="cr-summary">{esc(copy["summary"])}</p><div class="hero-actions"><a class="button primary" href="mailto:{esc(person["email"])}">{esc(copy["contact"])}</a><a class="button" href="{esc(person["github"])}" target="_blank" rel="noopener noreferrer">GitHub</a><a class="button" href="pdf/{esc(profile["pdf"])}" download>{esc(copy["download"])}</a></div><p class="cr-availability">{esc(copy["availability"])}</p></div><aside class="cr-photo-card"><img class="cr-photo" src="{photo}" alt="{esc(person[f"name_{lang}"])}" width="460" height="575" onerror="this.onerror=null;this.src='assets/portrait.svg'"><div><strong>{esc(copy["hero_role"])}</strong><span>Wist2 · MCST · C++23 · .NET</span></div></aside></section>'''


def proof_strip(copy: dict[str, Any]) -> str:
    return '<section class="shell cr-proofs" aria-label="Key evidence">' + "".join(f'<article><strong>{esc(title)}</strong><span>{esc(body)}</span></article>' for title, body in copy["proofs"]) + "</section>"


def experience(data: dict[str, Any], lang: str, profile: dict[str, Any], copy: dict[str, Any]) -> str:
    rows = []
    for index, item in enumerate(profile["experience"][:2]):
        bullets = list(item["bullets"][:2])
        if index == 1:
            bullets = [copy["mcst_bullet"]]
        rows.append(f'<article class="cr-timeline"><time>{esc(item["date"])}</time><div><h3>{esc(item["title"])}</h3><p>{esc(item["org"])}</p></div><ul>' + "".join(f"<li>{esc(bullet)}</li>" for bullet in bullets) + "</ul></article>")
    return f'<section class="shell section" id="experience"><div class="section-heading"><p class="section-label">01 · {"Опыт" if lang == "ru" else "Experience"}</p><div><h2>{esc(copy["experience_heading"])}</h2><p class="section-intro">{esc(copy["experience_intro"])}</p></div></div><div>{"".join(rows)}</div></section>'


def recognition(lang: str, copy: dict[str, Any]) -> str:
    rows = "".join(f'<article><time>{esc(year)}</time><div><h3>{esc(title)}</h3><p>{esc(body)}</p></div></article>' for year, title, body in copy["recognition"])
    return f'<section class="shell section cr-recognition-section" id="recognition"><div class="section-heading"><p class="section-label">02 · {"Достижения" if lang == "ru" else "Recognition"}</p><div><h2>{esc(copy["recognition_heading"])}</h2></div></div><div class="cr-recognition">{rows}</div></section>'


def pipeline(lang: str) -> str:
    verify = "Проверка / PlanFuzz" if lang == "ru" else "Verification / PlanFuzz"
    return f'''<div class="cr-pipeline" aria-label="Wist2 pipeline"><div class="cr-flow-row"><span>Source</span><b>→</b><span>Lexer</span><b>→</b><span>Parser</span><b>→</b><span>AST</span></div><div class="cr-flow-row"><span>Bytecode</span><b>→</b><span>AIR</span><b>→</b><span>SSA</span><b>→</b><span>Optimizations</span></div><div class="cr-branches"><span>Interpreter</span><span>CIL</span></div><div class="cr-verify">{esc(verify)}</div></div>'''


def projects(data: dict[str, Any], lang: str, copy: dict[str, Any]) -> str:
    labels = copy["project_labels"]
    p = data["projects"]
    wist = p["wist"]
    secondary = []
    for project_id, ownership, tags in (
        ("planfuzz", copy["planfuzz_ownership"], ("fuzzing", "oracles", "replay")),
        ("psform", copy["psform_ownership"], ("C17", "program analysis", "stress testing")),
    ):
        project = p[project_id]
        secondary.append(f'''<article class="cr-project-secondary"><header><span>{esc(copy["project_status"][project_id])}</span><h3>{esc(project["title"])}</h3></header><p>{esc(project[f"problem_{lang}"])}</p><dl><div><dt>{esc(labels["ownership"])}</dt><dd>{esc(ownership)}</dd></div><div><dt>{esc(labels["outcome"])}</dt><dd>{esc(project[f"result_{lang}"])}</dd></div></dl><div class="cr-tags">{"".join(f"<span>{esc(tag)}</span>" for tag in tags)}</div><div class="cr-project-links">{project_links(project, lang, copy)}</div></article>''')
    return f'''<section class="shell section" id="work"><div class="section-heading"><p class="section-label">03 · {"Проекты" if lang == "ru" else "Projects"}</p><div><h2>{esc(copy["projects_heading"])}</h2><p class="section-intro">{esc(copy["projects_intro"])}</p></div></div><article class="cr-project-featured"><div class="cr-project-copy"><header><span>{esc(copy["project_status"]["wist"])}</span><h3>{esc(wist["title"])}</h3></header><p>{esc(wist[f"problem_{lang}"])}</p><dl><div><dt>{esc(labels["ownership"])}</dt><dd>{esc(copy["wist_ownership"])}</dd></div><div><dt>{esc(labels["outcome"])}</dt><dd>{esc(wist[f"result_{lang}"])}</dd></div></dl><div class="cr-tags"><span>C#</span><span>.NET</span><span>AIR</span><span>SSA</span><span>CIL</span></div><div class="cr-project-links">{project_links(wist, lang, copy)}</div></div>{pipeline(lang)}</article><div class="cr-project-grid">{"".join(secondary)}</div></section>'''


def skills(lang: str, copy: dict[str, Any]) -> str:
    rows = "".join(f'<article><h3>{esc(title)}</h3><p>{esc(body)}</p></article>' for title, body in copy["skills"])
    return f'<section class="shell section" id="skills"><div class="section-heading"><p class="section-label">04 · {"Компетенции" if lang == "ru" else "Capabilities"}</p><div><h2>{esc(copy["skills_heading"])}</h2><p class="section-intro">{esc(copy["skills_intro"])}</p></div></div><div class="cr-skills">{rows}</div></section>'


def contact(data: dict[str, Any], lang: str, copy: dict[str, Any]) -> str:
    person = data["person"]
    return f'''<section class="shell cr-bottom"><div class="cr-education"><span>{"Образование" if lang == "ru" else "Education"}</span><strong>{esc(copy["education"])}</strong></div><div class="contact-panel" id="contact"><div><h2>{esc(copy["contact_heading"])}</h2><p><a href="mailto:{esc(person["email"])}">{esc(person["email"])}</a> · <a href="{esc(person["telegram"])}" target="_blank" rel="noopener noreferrer">Telegram</a> · <a href="{esc(person["linkedin"])}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p></div><div class="contact-links"><a class="button primary" href="mailto:{esc(person["email"])}">{esc(copy["contact"])}</a><a class="button" href="{esc(person["github"])}" target="_blank" rel="noopener noreferrer">GitHub</a></div></div></section>'''


def page(data: dict[str, Any], lang: str) -> str:
    copy = COPY[lang]
    profile = data["profiles"]["compiler"][lang]
    person = data["person"]
    other = "en" if lang == "ru" else "ru"
    other_file = data["profiles"]["compiler"][other]["filename"]
    canonical = data["site_url"] + profile["filename"]
    schema = {"@context": "https://schema.org", "@type": "Person", "name": person[f"name_{lang}"], "jobTitle": profile["role"], "email": f"mailto:{person['email']}", "url": canonical, "sameAs": [person["github"], person["telegram"], person["linkedin"]]}
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0f0c0d"><title>{esc(copy["title"])}</title><meta name="description" content="{esc(copy["description"])}"><meta property="og:type" content="profile"><meta property="og:title" content="{esc(copy["title"])}"><meta property="og:description" content="{esc(copy["description"])}"><meta property="og:url" content="{esc(canonical)}"><meta property="og:image" content="{esc(data["site_url"])}assets/og-card.svg"><link rel="canonical" href="{esc(canonical)}"><link rel="alternate" hreflang="{lang}" href="{esc(canonical)}"><link rel="alternate" hreflang="{other}" href="{esc(data["site_url"] + other_file)}"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css?v={esc(data["version"])}"><link rel="stylesheet" href="compiler-redesign.css?v=2"><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script></head><body class="compiler-redesign">{print_cv(data, lang, profile, copy)}{header(data, lang, copy, other_file)}<main id="main">{hero(data, lang, profile, copy)}{proof_strip(copy)}{experience(data, lang, profile, copy)}{recognition(lang, copy)}{projects(data, lang, copy)}{skills(lang, copy)}{contact(data, lang, copy)}</main><footer class="shell site-footer"><span>{esc(person[f"name_{lang}"])} · {esc(profile["role"])}</span><span>{esc(copy["updated"])} {esc(data["updated_at"])}</span></footer><script src="script.js?v={esc(data["version"])}" defer></script></body></html>\n'''


def build_outputs(data: dict[str, Any]) -> dict[Path, str]:
    return {ROOT / data["profiles"]["compiler"][lang]["filename"]: page(data, lang) for lang in ("ru", "en")}


def write_or_check(outputs: dict[Path, str], check: bool) -> None:
    stale: list[str] = []
    for path, content in outputs.items():
        normalized = content.rstrip() + "\n"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != normalized:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.write_text(normalized, encoding="utf-8")
    if stale:
        raise SystemExit("Generated compiler pages are stale: " + ", ".join(stale))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    write_or_check(build_outputs(load_data()), args.check)


if __name__ == "__main__":
    main()
