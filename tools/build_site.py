from __future__ import annotations

import argparse
import hashlib
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


def language_name(lang: str) -> str:
    return "RU" if lang == "ru" else "EN"


def other_language(lang: str) -> str:
    return "en" if lang == "ru" else "ru"


def person_name(data: dict[str, Any], lang: str) -> str:
    return data["person"][f"name_{lang}"]


def page_url(data: dict[str, Any], filename: str) -> str:
    return data["site_url"] + filename


def profile_links(data: dict[str, Any], lang: str) -> list[tuple[str, str]]:
    return [
        (data["profile_ui"][key][f"label_{lang}"], data["profiles"][key][lang]["filename"])
        for key in data["profile_order"]
    ]


def recognition_items(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> list[list[str]]:
    return profile.get("recognition", data["recognition"][lang])


def common_head(data: dict[str, Any], lang: str, filename: str, title: str, description: str, role: str, canonical: str | None = None) -> str:
    canonical_url = canonical or page_url(data, filename)
    other = other_language(lang)
    alternate = filename.replace(f"{lang}-", f"{other}-") if f"{lang}-" in filename else ("en.html" if lang == "ru" else "ru.html")
    schema_name = person_name(data, lang)
    schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": schema_name,
        "jobTitle": role,
        "email": f"mailto:{data['person']['email']}",
        "url": canonical_url,
        "sameAs": [data["person"]["github"], data["person"]["telegram"], data["person"]["linkedin"]],
    }
    return f"""<!doctype html>
<html lang="{esc(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0f0c0d">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical_url)}">
<meta property="og:image" content="{esc(data['site_url'])}assets/og-card.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(data['site_url'])}assets/og-card.svg">
<link rel="canonical" href="{esc(canonical_url)}">
<link rel="alternate" hreflang="{esc(lang)}" href="{esc(canonical_url)}">
<link rel="alternate" hreflang="{esc(other)}" href="{esc(page_url(data, alternate))}">
<link rel="alternate" hreflang="x-default" href="{esc(data['site_url'])}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css?v={esc(data['version'])}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':')).replace("</", "<\\/")}</script>
</head>"""


def header(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    nav_labels = {
        "experience": "Опыт" if lang == "ru" else "Experience",
        "work": "Проекты" if lang == "ru" else "Projects",
        "skills": "Стек" if lang == "ru" else "Skills",
        "recognition": "Достижения" if lang == "ru" else "Recognition",
        "contact": "Контакты" if lang == "ru" else "Contact",
    }
    other = other_language(lang)
    alternate = data["profiles"][next(k for k, v in data["profiles"].items() if v[lang]["filename"] == profile["filename"])][other]["filename"]
    links = "".join(f'<a href="#{key}">{esc(label)}</a>' for key, label in nav_labels.items())
    mobile_profiles = "".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in profile_links(data, lang))
    return f"""
<a class="skip-link" href="#main">{'К содержанию' if lang == 'ru' else 'Skip to content'}</a>
<header class="site-header">
  <div class="shell header-inner">
    <a class="brand" href="index.html" aria-label="{esc(person_name(data, lang))}">
      <span class="brand-mark">MR</span>
      <span class="brand-copy"><strong>{esc(person_name(data, lang))}</strong><span>{esc(profile['brand'])}</span></span>
    </a>
    <nav class="primary-nav" aria-label="{'Разделы' if lang == 'ru' else 'Sections'}">{links}</nav>
    <div class="header-actions">
      <div class="language-switch" aria-label="{'Язык страницы' if lang == 'ru' else 'Page language'}">
        <span aria-current="page">{language_name(lang)}</span><span aria-hidden="true">/</span><a href="{esc(alternate)}">{language_name(other)}</a>
      </div>
      <a class="button compact" href="#contact">{'Связаться' if lang == 'ru' else 'Contact'}</a>
      <details class="mobile-menu">
        <summary>{'Меню' if lang == 'ru' else 'Menu'}</summary>
        <div class="mobile-panel"><nav>{links}</nav><div class="mobile-links">{mobile_profiles}</div></div>
      </details>
    </div>
  </div>
</header>"""


def action_links(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    labels = {
        "mail": "Написать" if lang == "ru" else "Email",
        "github": "GitHub",
        "profiles": "Другие версии" if lang == "ru" else "Other profiles",
        "pdf": "Скачать PDF" if lang == "ru" else "Download PDF",
    }
    return f"""
<div class="hero-actions">
  <a class="button primary" href="mailto:{esc(data['person']['email'])}">{labels['mail']}</a>
  <a class="button" href="{esc(data['person']['github'])}" rel="noopener noreferrer" target="_blank">{labels['github']}</a>
  <a class="button" href="index.html">{labels['profiles']}</a>
  <a class="button" href="pdf/{esc(profile['pdf'])}" download>{labels['pdf']}</a>
</div>"""


def hero(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    person = data["person"]
    location = person[f"location_{lang}"]
    education = person[f"education_{lang}"]
    role_description = "Архитектура, реализация и проверка сложных систем" if lang == "ru" else "Architecture, implementation, and verification of complex systems"
    return f"""
<section class="shell hero" id="top">
  <div class="hero-copy">
    <div class="hero-intro"><p class="eyebrow">{esc(profile['eyebrow'])}</p><h1>{esc(person_name(data, lang))}</h1><p class="hero-role">{esc(profile['role'])}</p></div>
    <div class="hero-detail"><p class="hero-summary">{esc(profile['summary'])}</p>{action_links(data, lang, profile)}
      <div class="hero-context"><span>{esc(location)}</span><span>{esc(education)}</span></div>
      <div class="hero-contact-line"><a href="mailto:{esc(person['email'])}">{esc(person['email'])}</a> · <a href="{esc(person['telegram'])}" rel="noopener noreferrer" target="_blank">{esc(person['telegram_label'])}</a> · <a href="{esc(person['github'])}" rel="noopener noreferrer" target="_blank">{esc(person['github_label'])}</a> · <a href="{esc(person['linkedin'])}" rel="noopener noreferrer" target="_blank">LinkedIn</a></div>
    </div>
  </div>
  <aside class="identity-card" aria-label="{'Профиль' if lang == 'ru' else 'Profile'}"><img class="identity-mark" src="assets/portrait.svg" alt="{esc(person_name(data, lang))}" width="460" height="460"><strong>{esc(role_description)}</strong><span>{esc(profile['brand'])}</span></aside>
</section>"""


def proof_strip(profile: dict[str, Any]) -> str:
    items = "".join(f'<div class="proof-item"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["proofs"])
    return f'<section class="shell proof-strip" aria-label="Key evidence">{items}</section>'


def experience_section(lang: str, profile: dict[str, Any]) -> str:
    heading = "Опыт и ответственность" if lang == "ru" else "Experience and ownership"
    intro = "Роли описаны через границы ответственности и проверяемый результат." if lang == "ru" else "Roles are described through ownership boundaries and verifiable outcomes."
    articles = []
    for item in profile["experience"]:
        bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"])
        articles.append(f'<article><time>{esc(item["date"])}</time><div><h3>{esc(item["title"])}</h3><p class="org">{esc(item["org"])}</p></div><ul class="timeline-details">{bullets}</ul></article>')
    return f"""
<section class="shell section" id="experience"><div class="section-heading"><p class="section-label">01 · {'Опыт' if lang == 'ru' else 'Experience'}</p><div><h2>{esc(heading)}</h2><p class="section-intro">{esc(intro)}</p></div></div><div class="timeline">{''.join(articles)}</div></section>"""


def project_card(data: dict[str, Any], lang: str, project_id: str, featured: bool = False) -> str:
    project = data["projects"][project_id]
    case_url = project[f"case_{lang}"]
    problem = project[f"problem_{lang}"]
    solution = project[f"solution_{lang}"]
    result = project[f"result_{lang}"]
    type_label = project[f"type_{lang}"]
    labels = {
        "problem": "Проблема" if lang == "ru" else "Problem",
        "solution": "Решение" if lang == "ru" else "Solution",
        "result": "Результат" if lang == "ru" else "Result",
        "case": "Архитектурный разбор" if lang == "ru" else "Architecture case study",
        "repo": "GitHub",
        "docs": "Документация" if lang == "ru" else "Documentation",
    }
    links = [f'<a href="{esc(case_url)}">{labels["case"]} ↗</a>']
    if project.get("repo"):
        links.append(f'<a href="{esc(project["repo"])}" rel="noopener noreferrer" target="_blank">{labels["repo"]} ↗</a>')
    if project.get("docs"):
        links.append(f'<a href="{esc(project["docs"])}" rel="noopener noreferrer" target="_blank">{labels["docs"]} ↗</a>')
    points = f"""<ul class="project-points"><li><strong>{labels['problem']}</strong>{esc(problem)}</li><li><strong>{labels['solution']}</strong>{esc(solution)}</li><li><strong>{labels['result']}</strong>{esc(result)}</li></ul>"""
    if featured:
        return f'<article class="project-featured"><div><span class="project-type">{esc(type_label)}</span><h3>{esc(project["title"])}</h3><p>{esc(problem)}</p><div class="project-links">{"".join(links)}</div></div>{points}</article>'
    return f'<article class="project-card"><span class="project-type">{esc(type_label)}</span><h3>{esc(project["title"])}</h3><div class="project-mini"><p><strong>{labels["problem"]}:</strong> {esc(problem)}</p><p><strong>{labels["solution"]}:</strong> {esc(solution)}</p><p><strong>{labels["result"]}:</strong> {esc(result)}</p></div><div class="project-links">{"".join(links)}</div></article>'


def projects_section(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    ids = profile["project_ids"]
    featured = project_card(data, lang, ids[0], True)
    rest = "".join(project_card(data, lang, project_id) for project_id in ids[1:])
    heading = "Проекты как инженерные кейсы" if lang == "ru" else "Projects as engineering cases"
    intro = "Каждый кейс показывает исходную проблему, принятое решение и проверяемый результат." if lang == "ru" else "Each case presents the original problem, the chosen design, and a verifiable outcome."
    return f"""
<section class="shell section" id="work"><div class="section-heading"><p class="section-label">02 · {'Проекты' if lang == 'ru' else 'Projects'}</p><div><h2>{esc(heading)}</h2><p class="section-intro">{esc(intro)}</p></div></div>{featured}<div class="project-grid">{rest}</div></section>"""


def skills_section(lang: str, profile: dict[str, Any]) -> str:
    rows = "".join(f'<div class="stack-line"><strong>{esc(title)}</strong><p>{esc(body)}</p></div>' for title, body in profile["skills"])
    return f'<section class="shell section" id="skills"><div class="section-heading"><p class="section-label">03 · {"Компетенции" if lang == "ru" else "Skills"}</p><div><h2>{"Ключевые технические области." if lang == "ru" else "Core technical areas."}</h2></div></div><div class="stack-lines">{rows}</div></section>'


def recognition_section(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    rows = "".join(f'<article class="recognition-item"><span class="recognition-year">{esc(year)}</span><div><h3>{esc(title)}</h3><p>{esc(body)}</p></div></article>' for year, title, body in recognition_items(data, lang, profile))
    return f'<section class="shell section" id="recognition"><div class="section-heading"><p class="section-label">04 · {"Достижения" if lang == "ru" else "Recognition"}</p><div><h2>{"Внешние результаты и техническая коммуникация." if lang == "ru" else "External results and technical communication."}</h2></div></div><div class="recognition-list">{rows}</div></section>'


def education_section(data: dict[str, Any], lang: str) -> str:
    education = data["person"][f"education_{lang}"]
    title = "Образование" if lang == "ru" else "Education"
    return f'<section class="shell section compact-section" id="education"><div class="section-heading"><p class="section-label">05 · {title}</p><div><h2>{esc(education)}</h2><p class="section-intro">{"Москва" if lang == "ru" else "Moscow"}</p></div></div></section>'


def contact_section(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    p = data["person"]
    return f"""
<section class="shell contact-section" id="contact"><div class="contact-panel"><div><h2>{esc(profile['contact_heading'])}</h2><p>{esc(p[f'location_{lang}'])}</p></div><div class="contact-links"><a class="button primary" href="mailto:{esc(p['email'])}">{'Почта' if lang == 'ru' else 'Email'}</a><a class="button" href="{esc(p['telegram'])}" target="_blank" rel="noopener noreferrer">Telegram</a><a class="button" href="{esc(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a><a class="button" href="pdf/{esc(profile['pdf'])}" download>PDF</a></div></div></section>"""


def print_cv(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    labels = {
        "experience": "Опыт" if lang == "ru" else "Experience",
        "projects": "Проекты" if lang == "ru" else "Projects",
        "skills": "Компетенции" if lang == "ru" else "Skills",
        "education": "Образование" if lang == "ru" else "Education",
        "recognition": "Достижения" if lang == "ru" else "Recognition",
    }
    p = data["person"]
    contacts = f'<a href="mailto:{esc(p["email"])}">{esc(p["email"])}</a><br><a href="{esc(p["telegram"])}">{esc(p["telegram_label"])}</a><br><a href="{esc(p["github"])}">{esc(p["github_label"])}</a>'
    proofs = "".join(f'<div class="pcv-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["proofs"])
    experiences = []
    for item in profile["experience"][:3]:
        bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"][:2])
        experiences.append(f'<article class="pcv-entry"><div class="pcv-date">{esc(item["date"])}</div><div><h3>{esc(item["title"])}</h3><ul>{bullets}</ul></div></article>')
    projects = []
    for project_id in profile["project_ids"][:3]:
        project = data["projects"][project_id]
        case = project[f"case_{lang}"]
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(case)}">{esc(project["title"])}</a></h3><p>{esc(project[f"result_{lang}"])}</p></article>')
    skills = "".join(f'<div class="pcv-skill"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["skills"])
    education = p[f"education_{lang}"]
    recognition = recognition_items(data, lang, profile)[0][2]
    return f"""
<div class="print-cv" aria-label="Focused one-page CV">
  <header class="pcv-header"><div><h1>{esc(person_name(data, lang))}</h1><h2>{esc(profile['role'])}</h2></div><div class="pcv-contact">{contacts}</div></header>
  <p class="pcv-summary">{esc(profile['summary'])}</p><div class="pcv-proofs">{proofs}</div>
  <div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels['experience']}</h2>{''.join(experiences)}</section><section><h2 class="pcv-section-title">{labels['projects']}</h2>{''.join(projects)}</section></main>
  <aside class="pcv-side"><section><h2 class="pcv-section-title">{labels['skills']}</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['education']}</h2><p>{esc(education)}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['recognition']}</h2><p>{esc(recognition)}</p></section><section class="pcv-compact"><p>{esc(p[f'location_{lang}'])}</p></section></aside></div>
</div>"""


def profile_page(data: dict[str, Any], profile_key: str, lang: str) -> str:
    profile = data["profiles"][profile_key][lang]
    head = common_head(data, lang, profile["filename"], profile["title"], profile["description"], profile["role"])
    footer_label = "Обновлено" if lang == "ru" else "Updated"
    return f"""{head}
<body>{print_cv(data, lang, profile)}{header(data, lang, profile)}<main id="main">{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}</main><footer class="shell site-footer"><span>{esc(person_name(data, lang))} · {esc(profile['footer'])}</span><span>{footer_label} {esc(data['updated_at'])}</span></footer><script src="script.js?v={esc(data['version'])}" defer></script></body></html>
"""


def landing_page(data: dict[str, Any]) -> str:
    lang = "ru"
    general = data["profiles"]["general"][lang]
    title = "Михаил Разаков — Software Engineer"
    description = general["description"]
    head = common_head(data, lang, "index.html", title, description, general["role"], data["site_url"])
    cards = []
    for key in (profile_key for profile_key in data["profile_order"] if profile_key != "general"):
        ru = data["profiles"][key]["ru"]
        en = data["profiles"][key]["en"]
        ui = data["profile_ui"][key]
        heading = ui["landing_title"]
        body = ui["landing_description_ru"]
        cards.append(f'<article class="selector-card"><span>RU / EN</span><h2>{esc(heading)}</h2><p>{esc(body)}</p><div class="selector-links"><a href="{esc(ru["filename"])}">Русская версия</a><a href="{esc(en["filename"])}">English version</a></div><div class="selector-pdf-links"><a href="pdf/{esc(ru["pdf"])}" download>PDF RU</a><a href="pdf/{esc(en["pdf"])}" download>PDF EN</a></div></article>')
    project_cases = "".join(project_card(data, "ru", project_id) for project_id in ["wist", "vpn", "psform"])
    p = data["person"]
    return f"""{head}
<body class="selector-page">
<header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(p['name_ru'])}</strong><span>Software Engineer</span></span></a><nav class="primary-nav"><a href="#profiles">Профили</a><a href="#cases">Кейсы</a><a href="#contact">Контакты</a></nav><div class="header-actions"><a class="button compact" href="en.html">EN</a><a class="button compact" href="#contact">Связаться</a><details class="mobile-menu"><summary>Меню</summary><div class="mobile-panel"><nav><a href="#profiles">Профили</a><a href="#cases">Кейсы</a><a href="#contact">Контакты</a></nav></div></details></div></div></header>
<main id="main" class="shell landing-main"><section class="selector-intro landing-hero"><p class="eyebrow">Архитектура платформ · .NET backend · compiler/runtime</p><h1>Проектирую и реализую сложные программные системы.</h1><p>{esc(general['summary'])}</p><div class="hero-actions"><a class="button primary" href="ru.html">Открыть резюме</a><a class="button" href="pdf/{esc(general['pdf'])}" download>Скачать PDF</a><a class="button" href="#cases">Посмотреть проекты</a></div><div class="landing-evidence"><span>1 465/1 465 тестов Wist2</span><span>1-е место из 49 · 104/104</span><span>.NET backend · LLVM · x86-64</span></div></section>
<section id="profiles" class="landing-section"><div class="section-heading"><p class="section-label">01 · Профили</p><div><h2>Профили под конкретные роли.</h2><p class="section-intro">Основной профиль — универсальный Software Engineer. Специализированные версии меняют приоритет доказательств, но не противоречат друг другу.</p></div></div><div class="selector-grid">{''.join(cards)}</div><p class="portfolio-link"><a href="ru.html">Полное техническое портфолио →</a></p></section>
<section id="cases" class="landing-section"><div class="section-heading"><p class="section-label">02 · Кейсы</p><div><h2>Проблема → решение → проверяемый результат.</h2><p class="section-intro">Открытые проекты ведут к коду и документации; закрытые — к публичному архитектурному разбору без секретов и пользовательских данных.</p></div></div><div class="project-grid">{project_cases}</div></section>
<section class="contact-section" id="contact"><div class="contact-panel"><div><h2>Связаться по инженерной роли или проекту.</h2><p>{esc(p['location_ru'])}</p></div><div class="contact-links"><a class="button primary" href="mailto:{esc(p['email'])}">Почта</a><a class="button" href="{esc(p['telegram'])}" target="_blank" rel="noopener noreferrer">Telegram</a><a class="button" href="{esc(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a></div></div></section></main>
<footer class="shell site-footer"><span>{esc(p['name_ru'])} · Software Engineer</span><span>Обновлено {esc(data['updated_at'])}</span></footer><script src="script.js?v={esc(data['version'])}" defer></script></body></html>
"""


def case_page(data: dict[str, Any], project_id: str, lang: str) -> str:
    project = data["projects"][project_id]
    filename = project[f"case_{lang}"]
    title = f"{project['title']} — {'архитектурный кейс' if lang == 'ru' else 'architecture case study'}"
    description = project[f"result_{lang}"]
    role = data["profiles"]["general"][lang]["role"]
    head = common_head(data, lang, filename, title, description, role)
    # Paths from cases/ need one level up.
    head = head.replace('href="assets/', 'href="../assets/').replace('href="style.css', 'href="../style.css').replace('content="https://misha1302.github.io/CV/cases/', 'content="https://misha1302.github.io/CV/cases/')
    labels = {
        "problem": "Проблема" if lang == "ru" else "Problem",
        "constraints": "Ограничения" if lang == "ru" else "Constraints",
        "solution": "Решение" if lang == "ru" else "Solution",
        "result": "Результат" if lang == "ru" else "Outcome",
        "verification": "Как проверялось" if lang == "ru" else "Verification",
        "role": "Моя ответственность" if lang == "ru" else "My ownership",
        "back": "Вернуться к резюме" if lang == "ru" else "Back to CV",
        "private": "Код проекта закрыт. Разбор намеренно не содержит секретов, персональных данных и эксплуатационных идентификаторов." if lang == "ru" else "The project code is private. This case study intentionally excludes secrets, personal data, and operational identifiers.",
    }
    constraints = {
        "wist": "Независимые версии пакетов, разные backend-ы, детерминизм и обратная совместимость." if lang == "ru" else "Independent package versions, multiple backends, determinism, and compatibility.",
        "planfuzz": "Нестабильные исполнения, инфраструктурные сбои и необходимость сохранять точный тип расхождения." if lang == "ru" else "Flaky executions, infrastructure failures, and preserving the exact mismatch category.",
        "vpn": "Повторные webhooks, сетевые таймауты, перезапуски, миграции и невозможность раскрывать production-данные." if lang == "ru" else "Duplicate webhooks, network timeouts, restarts, migrations, and private production data.",
        "lms": "Финансовые операции и пользовательские workflows должны развиваться независимо, не нарушая ledger-инварианты." if lang == "ru" else "Financial operations and user workflows must evolve independently without violating ledger invariants.",
        "psform": "Анализ должен быть консервативным, быстрым на больших диапазонах и проверяемым на малых областях." if lang == "ru" else "The analysis must be conservative, fast on large domains, and checkable on small domains.",
        "codegen": "Нужно сравнивать высокоуровневую семантику и машинный код в изолированном процессе с ограничениями ресурсов." if lang == "ru" else "High-level semantics and machine code must be compared in an isolated, resource-limited process.",
    }[project_id]
    verification = {
        "wist": "Canonical test gate, clean-consumer projects, interpreter/CIL parity, deterministic manifests and replayable failures." if lang == "en" else "Канонический тестовый gate, clean-consumer проекты, parity интерпретатора/CIL, детерминированные манифесты и воспроизводимые падения.",
        "planfuzz": "Fresh-process confirmation, exact fingerprints, typed outcomes, and deterministic reduction." if lang == "en" else "Подтверждение в свежем процессе, exact fingerprints, типизированные исходы и детерминированное сокращение.",
        "vpn": "State-transition checks, negative webhook cases, audit records, backup/restore rehearsal, health gates, and rollback verification." if lang == "en" else "Проверки переходов состояния, негативные webhook-сценарии, audit records, репетиция backup/restore, health gates и проверка rollback.",
        "lms": "Ledger invariants, idempotent payment completion, role checks, migrations, and critical-flow acceptance." if lang == "en" else "Ledger-инварианты, идемпотентное завершение платежа, проверки ролей, миграции и acceptance критических flows.",
        "psform": "Exact brute-force oracle on small domains, metamorphic generation, sanitizers, and reproducible WA/TL examples." if lang == "en" else "Точный brute-force oracle на малых областях, метаморфная генерация, sanitizers и воспроизводимые WA/TL-примеры.",
        "codegen": "Differential comparison with an IR interpreter, isolated execution, disassembly, and spill/reload metrics." if lang == "en" else "Дифференциальное сравнение с IR-интерпретатором, изолированный запуск, дизассемблирование и метрики spill/reload.",
    }[project_id]
    ownership = {
        "wist": "Архитектура, ключевые контракты, runtime, SSA, тестовая стратегия и публичная документация." if lang == "ru" else "Architecture, core contracts, runtime, SSA, verification strategy, and public documentation.",
        "planfuzz": "Модель исходов, ядро оракулов, replay, fingerprinting и reducers." if lang == "ru" else "Outcome model, oracle core, replay, fingerprinting, and reducers.",
        "vpn": "Backend-архитектура, состояния, платежные интеграции, recovery, миграции и эксплуатационные gates." if lang == "ru" else "Backend architecture, state transitions, payment integrations, recovery, migrations, and operational gates.",
        "lms": "Роли, баланс, платежные workflows, инварианты и release-проверки." if lang == "ru" else "Roles, balances, payment workflows, invariants, and release checks.",
        "psform": "Алгоритм анализа, точный оракул, stress infrastructure и разбор контрпримеров." if lang == "ru" else "Analysis algorithm, exact oracle, stress infrastructure, and counterexample analysis.",
        "codegen": "IR, liveness, register allocation, code emission и differential harness." if lang == "ru" else "IR, liveness, register allocation, code emission, and the differential harness.",
    }[project_id]
    links = []
    if project.get("repo"):
        links.append(f'<a class="button" href="{esc(project["repo"])}" target="_blank" rel="noopener noreferrer">GitHub</a>')
    if project.get("docs"):
        links.append(f'<a class="button" href="{esc(project["docs"])}" target="_blank" rel="noopener noreferrer">Documentation</a>')
    return f"""{head}
<body class="case-page"><header class="site-header"><div class="shell header-inner"><a class="brand" href="../index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(person_name(data, lang))}</strong><span>{'инженерный кейс' if lang == 'ru' else 'engineering case'}</span></span></a><div></div><div class="header-actions"><a class="button compact" href="../{esc(data['profiles']['general'][lang]['filename'])}">{labels['back']}</a></div></div></header>
<main class="shell case-main" id="main"><section class="case-hero"><p class="eyebrow">{esc(project[f'type_{lang}'])}</p><h1>{esc(project['title'])}</h1><p>{esc(project[f'problem_{lang}'])}</p>{'<div class="case-note">'+esc(labels['private'])+'</div>' if not project['public'] else ''}<div class="hero-actions">{''.join(links)}</div></section>
<section class="case-grid"><article><span>01</span><h2>{labels['problem']}</h2><p>{esc(project[f'problem_{lang}'])}</p></article><article><span>02</span><h2>{labels['constraints']}</h2><p>{esc(constraints)}</p></article><article><span>03</span><h2>{labels['solution']}</h2><p>{esc(project[f'solution_{lang}'])}</p></article><article><span>04</span><h2>{labels['result']}</h2><p>{esc(project[f'result_{lang}'])}</p></article><article><span>05</span><h2>{labels['verification']}</h2><p>{esc(verification)}</p></article><article><span>06</span><h2>{labels['role']}</h2><p>{esc(ownership)}</p></article></section></main>
<footer class="shell site-footer"><span>{esc(project['title'])}</span><span>{'Обновлено' if lang == 'ru' else 'Updated'} {esc(data['updated_at'])}</span></footer></body></html>
"""


def redirect_page(data: dict[str, Any], source: str, target: str) -> str:
    lang = "ru" if source.startswith("ru") else "en"
    title = "Перенаправление" if lang == "ru" else "Redirect"
    text = "Страница объединена с основным профилем." if lang == "ru" else "This page has been consolidated into the main profile."
    target_url = page_url(data, target.split("#", 1)[0])
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="{esc(target_url)}"><meta http-equiv="refresh" content="0; url={esc(target)}"><script>location.replace({json.dumps(target)});</script></head><body><p>{esc(text)} <a href="{esc(target)}">{'Продолжить' if lang == 'ru' else 'Continue'}</a></p></body></html>"""


def sitemap(data: dict[str, Any]) -> str:
    urls = [data["site_url"]]
    for key in data["profile_order"]:
        for lang in ["ru", "en"]:
            urls.append(page_url(data, data["profiles"][key][lang]["filename"]))
    for project in data["projects"].values():
        urls.append(page_url(data, project["case_ru"]))
        urls.append(page_url(data, project["case_en"]))
    body = "".join(f"<url><loc>{esc(url)}</loc><lastmod>{esc(data['updated_at'])}</lastmod></url>" for url in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def build_outputs(data: dict[str, Any]) -> dict[Path, str]:
    outputs: dict[Path, str] = {ROOT / "index.html": landing_page(data)}
    for key in data["profile_order"]:
        for lang in ["ru", "en"]:
            profile = data["profiles"][key][lang]
            outputs[ROOT / profile["filename"]] = profile_page(data, key, lang)
    for project_id, project in data["projects"].items():
        outputs[ROOT / project["case_ru"]] = case_page(data, project_id, "ru")
        outputs[ROOT / project["case_en"]] = case_page(data, project_id, "en")
    for source, target in data["redirects"].items():
        outputs[ROOT / source] = redirect_page(data, source, target)
    outputs[ROOT / "sitemap.xml"] = sitemap(data)
    outputs[ROOT / "robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {data['site_url']}sitemap.xml\n"
    return outputs


def write_or_check(outputs: dict[Path, str], check: bool) -> None:
    mismatches = []
    for path, content in outputs.items():
        normalized = content.rstrip() + "\n"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != normalized:
                mismatches.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(normalized, encoding="utf-8")
    if mismatches:
        raise SystemExit("Generated files are stale: " + ", ".join(mismatches))


def manifest() -> None:
    target = ROOT / "MANIFEST.sha256"
    rows = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == target or ".git" in path.parts or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  ./{path.relative_to(ROOT).as_posix()}")
    target.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()
    data = load_data()
    outputs = build_outputs(data)
    write_or_check(outputs, args.check)
    if args.manifest and not args.check:
        manifest()


if __name__ == "__main__":
    main()
