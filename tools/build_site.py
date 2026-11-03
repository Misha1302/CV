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
        for key in data.get("selector_order", data["profile_order"])
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
<meta property="og:image" content="{esc(data['site_url'])}assets/og-card.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(data['site_url'])}assets/og-card.png">
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
    if profile.get("compiler_layout") or profile["filename"] in {"ru-compiler.html", "en-compiler.html"}:
        nav_labels.pop("contact", None)
    other = other_language(lang)
    alternate = data["profiles"][next(k for k, v in data["profiles"].items() if v[lang]["filename"] == profile["filename"])][other]["filename"]
    links = "".join(f'<a href="#{key}">{esc(label)}</a>' for key, label in nav_labels.items())
    is_compiler_profile = bool(profile.get("compiler_layout")) or profile["filename"] in {"ru-compiler.html", "en-compiler.html"}
    mobile_profiles = "" if is_compiler_profile else "".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in profile_links(data, lang))
    mobile_profiles_block = "" if not mobile_profiles else f'<div class="mobile-links">{mobile_profiles}</div>'
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
        <div class="mobile-panel"><nav>{links}</nav>{mobile_profiles_block}</div>
      </details>
    </div>
  </div>
</header>"""


def action_links(data: dict[str, Any], lang: str, profile: dict[str, Any], compact: bool = False) -> str:
    labels = {
        "mail": "Написать" if lang == "ru" else "Email",
        "github": "GitHub",
        "profiles": "Другие версии" if lang == "ru" else "Other profiles",
        "pdf": "Скачать PDF" if lang == "ru" else "Download PDF",
    }
    cv_application_links = ""
    if profile["filename"] in {"ru-backend.html", "en-backend.html"}:
        lang = "ru" if profile["filename"].startswith("ru") else "en"
        base = data["application_cvs"]["release_dir"]
        forms = data["application_cvs"]["variants"]
        cv_application_links = (
            f'<a class="button" href="{esc(base)}/{esc(forms["ats"]["basename"][lang])}.pdf" download>{"PDF для HR" if lang == "ru" else "ATS PDF"}</a>'
            f'<a class="button" href="{esc(base)}/{esc(forms["lead"]["basename"][lang])}.pdf" download>{"PDF для тимлида" if lang == "ru" else "Engineering PDF"}</a>'
        )
    profiles_link = "" if compact else f'\n  <a class="button" href="index.html">{labels["profiles"]}</a>'
    return f"""
<div class="hero-actions">
  <a class="button primary" href="mailto:{esc(data['person']['email'])}">{labels['mail']}</a>
  <a class="button" href="{esc(data['person']['github'])}" rel="noopener noreferrer" target="_blank">{labels['github']}</a>{profiles_link}
  <a class="button" href="pdf/{esc(profile['pdf'])}" download>{labels['pdf']}</a>{cv_application_links}
</div>"""


def identity_portrait(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    if not profile.get("show_portrait", True):
        return '<div class="identity-mark identity-monogram" aria-hidden="true">MR</div>'
    return f'<img class="identity-mark" src="{esc(profile.get("portrait_asset", "assets/portrait.jpg"))}" data-local-photo="true" alt="{esc(person_name(data, lang))}" width="460" height="460" loading="eager" decoding="async">'


def hero(data: dict[str, Any], lang: str, profile: dict[str, Any], compact: bool = False) -> str:
    person = data["person"]
    location = person[f"location_{lang}"]
    education = person[f"education_{lang}"]
    portrait = identity_portrait(data, lang, profile)
    if compact:
        compact_proofs = "".join(
            f'<div class="compact-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
            for title, body in profile["proofs"]
        )
        return f"""
<section class="shell hero hero-compact" id="top">
  <div class="hero-copy">
    <div class="hero-intro"><p class="eyebrow">{esc(profile['eyebrow'])}</p><h1>{esc(person_name(data, lang))}</h1><p class="hero-role">{esc(profile['role'])}</p></div>
    <div class="hero-detail"><p class="hero-summary">{esc(profile['summary'])}</p>{action_links(data, lang, profile, compact=True)}
      <div class="hero-context"><span>{esc(location)}</span><span>{esc(education)}</span></div>
      <div class="hero-contact-line"><a href="mailto:{esc(person['email'])}">{esc(person['email'])}</a> · <a href="{esc(person['telegram'])}" rel="noopener noreferrer" target="_blank">{esc(person['telegram_label'])}</a> · <a href="{esc(person['github'])}" rel="noopener noreferrer" target="_blank">{esc(person['github_label'])}</a> · <a href="{esc(person['linkedin'])}" rel="noopener noreferrer" target="_blank">LinkedIn</a></div>
    </div>
  </div>
  <aside class="compact-aside" aria-label="{'Профиль и ключевые факты' if lang == 'ru' else 'Profile and key evidence'}">
    <div class="identity-card compact-portrait">{portrait}</div>
    <div class="compact-proof-list">{compact_proofs}</div>
  </aside>
</section>"""
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
  <aside class="identity-card" aria-label="{'Профиль' if lang == 'ru' else 'Profile'}">{portrait}<strong>{esc(role_description)}</strong><span>{esc(profile['brand'])}</span></aside>
</section>"""


def compiler_hero(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    person = data["person"]
    location = person[f"location_{lang}"]
    education = person[f"education_{lang}"]
    proof_items = "".join(
        f'<div class="compiler-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
        for title, body in profile.get("proofs", [])[:3]
    )
    proof_row = f'<div class="compiler-proof-row">{proof_items}</div>' if proof_items and profile.get("show_web_proofs", True) else ""
    portrait = identity_portrait(data, lang, profile)
    return f"""
<section class="shell compiler-intro" id="top">
  <div class="compiler-intro-copy">
    <h1>{esc(person_name(data, lang))}</h1>
    <p class="hero-role">{esc(profile['role'])}</p>
    <p class="compiler-summary">{esc(profile['summary'])}</p>
{proof_row}
    <div class="compiler-meta"><span>{esc(location)}</span><span>{esc(education)}</span></div>
    <div class="compiler-links">
      <a href="mailto:{esc(person['email'])}">{esc(person['email'])}</a>
      <a href="{esc(person['telegram'])}" rel="noopener noreferrer" target="_blank">Telegram</a>
      <a href="{esc(person['github'])}" rel="noopener noreferrer" target="_blank">GitHub</a>
      <a href="{esc(person['linkedin'])}" rel="noopener noreferrer" target="_blank">LinkedIn</a>
      <a href="pdf/{esc(profile['pdf'])}" download>PDF</a>
    </div>
  </div>
  <aside class="compiler-portrait identity-card" aria-label="{'Фотография' if lang == 'ru' else 'Portrait'}">
    {portrait}
  </aside>
</section>"""


def proof_strip(profile: dict[str, Any]) -> str:
    items = "".join(f'<div class="proof-item"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["proofs"])
    return f'<section class="shell proof-strip" aria-label="Key evidence">{items}</section>'


def trajectory_section(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    if not profile.get("show_trajectory"):
        return ""
    items = "".join(
        f'<article class="trajectory-item"><time>{esc(item["period"])}</time><div><strong>{esc(item["label"])}</strong><span>{esc(item["detail"])}</span></div></article>'
        for item in data["trajectory"][lang]
    )
    label = "Эволюция compiler-проектов" if lang == "ru" else "Compiler project lineage"
    aria = "Эволюция compiler-проектов" if lang == "ru" else "Compiler project lineage"
    return f'<section class="shell trajectory-strip" aria-label="{aria}"><p class="trajectory-label">{label}</p><div class="trajectory-items">{items}</div></section>'


def print_trajectory(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    if not profile.get("print_show_trajectory", profile.get("show_trajectory")):
        return ""
    items = " · ".join(f'{item["period"]}: {item["label"]}' for item in data["trajectory"][lang])
    return f'<p class="pcv-trajectory">{esc(items)}</p>'


def experience_section(lang: str, profile: dict[str, Any], compact: bool = False) -> str:
    default_heading = "Опыт" if compact and lang == "ru" else ("Experience" if compact else ("Опыт и ответственность" if lang == "ru" else "Experience and ownership"))
    heading = profile.get("experience_heading", default_heading)
    intro = "" if compact else ("Роли описаны через границы ответственности и проверяемый результат." if lang == "ru" else "Roles are described through ownership boundaries and verifiable outcomes.")
    articles = []
    for item in profile["experience"]:
        bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"])
        articles.append(f'<article><time>{esc(item["date"])}</time><div><h3>{esc(item["title"])}</h3><p class="org">{esc(item["org"])}</p></div><ul class="timeline-details">{bullets}</ul></article>')
    note = profile.get("experience_note")
    note_html = "" if not note else f'<p class="experience-note"><strong>{esc(note["title"])}</strong><span>{esc(note["text"])}</span></p>'
    return f"""
<section class="shell section" id="experience"><div class="section-heading"><p class="section-label">01 · {'Опыт' if lang == 'ru' else 'Experience'}</p><div><h2>{esc(heading)}</h2>{f'<p class=\"section-intro\">{esc(intro)}</p>' if intro else ''}</div></div><div class="timeline">{''.join(articles)}</div>{note_html}</section>"""


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



def compiler_project_card(data: dict[str, Any], lang: str, profile: dict[str, Any], project_id: str) -> str:
    project = data["projects"][project_id]
    copy = profile["project_summaries"][project_id]
    case_url = project[f"case_{lang}"]
    labels = {"case": "Подробнее" if lang == "ru" else "Details", "repo": "GitHub"}
    links = [f'<a href="{esc(case_url)}">{labels["case"]} ↗</a>']
    if project.get("repo"):
        links.append(f'<a href="{esc(project["repo"])}" rel="noopener noreferrer" target="_blank">GitHub ↗</a>')
    type_label = copy.get("type", project[f"type_{lang}"])
    return f'<article class="project-row"><div><span class="project-type">{esc(type_label)}</span><h3>{esc(project["title"])}</h3></div><div><p>{esc(copy['solution'])}</p><p class="project-result">{esc(copy['result'])}</p><div class="project-links">{"".join(links)}</div></div></article>'


def compiler_projects_section(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    rows = "".join(compiler_project_card(data, lang, profile, project_id) for project_id in profile["project_ids"])
    heading = "Проекты" if lang == "ru" else "Projects"
    return f'<section class="shell section" id="work"><div class="section-heading"><p class="section-label">02 · {heading}</p><div><h2>{heading}</h2></div></div><div class="project-list">{rows}</div></section>'

def skills_section(lang: str, profile: dict[str, Any], compact: bool = False) -> str:
    rows = "".join(f'<div class="stack-line"><strong>{esc(title)}</strong><p>{esc(body)}</p></div>' for title, body in profile["skills"])
    heading = ("Технический стек" if lang == "ru" else "Technical stack") if compact else ("Ключевые технические области." if lang == "ru" else "Core technical areas.")
    return f'<section class="shell section" id="skills"><div class="section-heading"><p class="section-label">03 · {"Компетенции" if lang == "ru" else "Skills"}</p><div><h2>{heading}</h2></div></div><div class="stack-lines">{rows}</div></section>'


def recognition_section(data: dict[str, Any], lang: str, profile: dict[str, Any], compact: bool = False) -> str:
    rows = "".join(f'<article class="recognition-item"><span class="recognition-year">{esc(year)}</span><div><h3>{esc(title)}</h3><p>{esc(body)}</p></div></article>' for year, title, body in recognition_items(data, lang, profile))
    heading = ("Достижения" if lang == "ru" else "Recognition") if compact else ("Внешние результаты и техническая коммуникация." if lang == "ru" else "External results and technical communication.")
    return f'<section class="shell section" id="recognition"><div class="section-heading"><p class="section-label">04 · {"Достижения" if lang == "ru" else "Recognition"}</p><div><h2>{heading}</h2></div></div><div class="recognition-list">{rows}</div></section>'


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
        "experience": profile.get("experience_heading", "Опыт" if lang == "ru" else "Experience"),
        "projects": "Проекты" if lang == "ru" else "Projects",
        "skills": "Компетенции" if lang == "ru" else "Skills",
        "education": "Образование" if lang == "ru" else "Education",
        "recognition": "Достижения" if lang == "ru" else "Recognition",
    }
    p = data["person"]
    is_compiler_print = bool(profile.get("compiler_layout")) or profile["filename"] in {"ru-compiler.html", "en-compiler.html"}
    if is_compiler_print and lang == "en":
        contacts = f'<a href="mailto:{esc(p["email"])}">{esc(p["email"])}</a><br><a href="{esc(p["github"])}">{esc(p["github_label"])}</a><br><a href="{esc(p["linkedin"])}">LinkedIn</a>'
    else:
        contacts = f'<a href="mailto:{esc(p["email"])}">{esc(p["email"])}</a><br><a href="{esc(p["telegram"])}">{esc(p["telegram_label"])}</a><br><a href="{esc(p["github"])}">{esc(p["github_label"])}</a>'
    if profile["filename"] in {"ru-architecture.html", "en-architecture.html"}:
        contacts += f'<br><a href="{esc(data["site_url"])}">misha1302.github.io/CV</a>'
    proofs = "".join(f'<div class="pcv-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["proofs"])
    proof_block = "" if is_compiler_print else f'<div class="pcv-proofs">{proofs}</div>'
    experiences = []
    for item in profile["experience"][:int(profile.get("print_experience_limit", 3))]:
        bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"][:2])
        experiences.append(f'<article class="pcv-entry"><div class="pcv-date">{esc(item["date"])}</div><div><h3>{esc(item["title"])}</h3><ul>{bullets}</ul></div></article>')
    experience_note = profile.get("experience_note")
    experience_note_html = "" if not experience_note else f'<p class="pcv-experience-note"><strong>{esc(experience_note["title"])}</strong> — {esc(experience_note["text"])}</p>'
    projects = []
    project_limit = int(profile.get("print_project_limit", 3))
    project_summaries = profile.get("project_summaries", {})
    for project_id in profile["project_ids"][:project_limit]:
        project = data["projects"][project_id]
        target = project.get("repo") or project[f"case_{lang}"]
        summary = project_summaries.get(project_id, {})
        if summary:
            project_body = f'<p>{esc(summary.get("solution", ""))}</p><p class="pcv-project-result">{esc(summary.get("result", ""))}</p>'
        else:
            project_body = f'<p>{esc(project[f"result_{lang}"])}</p>'
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>{project_body}</article>')
    skills = "".join(f'<div class="pcv-skill"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["skills"])
    education = p[f"education_{lang}"]
    recognition_data = recognition_items(data, lang, profile)
    recognition_limit = int(profile.get("print_recognition_limit", 4 if is_compiler_print else 1))
    if recognition_limit > 1:
        recognition = "".join(
            f'<div class="pcv-recognition"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
            for _, title, body in recognition_data[:recognition_limit]
        )
    else:
        recognition = f'<p>{esc(recognition_data[0][2])}</p>'
    return f"""
<div class="print-cv" aria-label="Focused one-page CV">
  <header class="pcv-header"><div><h1>{esc(person_name(data, lang))}</h1><h2>{esc(profile['role'])}</h2></div><div class="pcv-contact">{contacts}</div></header>
  <p class="pcv-summary">{esc(profile['summary'])}</p>{print_trajectory(data, lang, profile)}{proof_block}
  <div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels['experience']}</h2>{''.join(experiences)}{experience_note_html}</section><section><h2 class="pcv-section-title">{labels['projects']}</h2>{''.join(projects)}</section></main>
  <aside class="pcv-side"><section><h2 class="pcv-section-title">{labels['skills']}</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['education']}</h2><p>{esc(education)}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['recognition']}</h2>{recognition}</section><section class="pcv-compact"><p>{esc(p[f'location_{lang}'])}</p></section></aside></div>
</div>"""

def profile_page(data: dict[str, Any], profile_key: str, lang: str) -> str:
    profile = data["profiles"][profile_key][lang]
    head = common_head(data, lang, profile["filename"], profile["title"], profile["description"], profile["role"])
    footer_label = "Обновлено" if lang == "ru" else "Updated"
    if profile.get("compiler_layout") or profile_key == "compiler":
        if profile_key == "compiler":
            main_content = f"{compiler_hero(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{trajectory_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"
        else:
            main_content = f"{compiler_hero(data, lang, profile)}{trajectory_section(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"
    else:
        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}"
    body_class = f"profile-{esc(profile_key)}"
    if profile.get("print_spacious"):
        body_class += " profile-print-spacious"
    if profile.get("compiler_layout") and profile_key != "compiler":
        body_class += " profile-compiler"
    if profile_key == "compiler":
        body_class += " profile-primary-compiler"
    return f"""{head}
<body class="{body_class}">{print_cv(data, lang, profile)}{header(data, lang, profile)}<main id="main">{main_content}</main><footer class="shell site-footer"><span>{esc(person_name(data, lang))} · {esc(profile['footer'])}</span><span>{footer_label} {esc(profile.get('updated_at', data['updated_at']))}</span></footer><script src="script.js?v={esc(data['version'])}" defer></script></body></html>
"""


def application_cv_links(data: dict[str, Any], lang: str) -> str:
    directory = data["application_cvs"]["release_dir"]
    rows = []
    for key in ("ats", "lead", "runtime"):
        entry = data["application_cvs"]["variants"][key]
        basename = entry["basename"][lang]
        label = entry[f"audience_{lang}"]
        base = f"{directory}/{basename}"
        rows.append(
            f'<article class="cv-option"><div><span class="cv-option-num">{("01" if key == "ats" else "02" if key == "lead" else "03")}</span>'
            f'<h3>{esc(label)}</h3></div>'
            f'<p><a href="{esc(base)}.pdf" download>PDF</a>'
            f'<a href="{esc(base)}.docx" download>DOCX</a>'
            f'<a href="{esc(base)}.md" download>Markdown</a></p></article>'
        )
    return "".join(rows)


def engineering_page(data: dict[str, Any], lang: str) -> str:
    cv = data["application_cvs"]["variants"]["lead"][lang]
    experience = data["application_cvs"]["experience"][lang]
    other = other_language(lang)
    filename = f"{lang}-engineering.html"
    name = person_name(data, lang)
    title = f"{name} — C#/.NET Backend Engineering"
    description = cv["summary"]
    head = common_head(data, lang, filename, title, description, cv["role"])
    title_experience = "Коммерческая практика и инженерная работа" if lang == "ru" else "Experience and engineering work"
    title_cases = "Четыре инженерных кейса" if lang == "ru" else "Four engineering cases"
    own = "Область ответственности и границы" if lang == "ru" else "Ownership and boundaries"
    back = "Все профили" if lang == "ru" else "All profiles"
    detailed = "Расширенная версия для тимлида" if lang == "ru" else "Extended CV for engineering leads"
    rows = "".join(
        f'<article class="engineering-entry"><p class="micro-label">{esc(item["date"])}</p><h3>{esc(item["title"])}</h3><p>{esc(item["text"])}</p></article>'
        for item in experience
    )
    cases = "".join(
        f'<article class="engineering-case"><p class="micro-label">0{idx}</p>'
        f'<h3><a href="{esc(data["projects"][entry["id"]].get("repo") or data["projects"][entry["id"]][f"case_{lang}"])}">{esc(entry["title"])}</a></h3>'
        f'<p>{esc(entry["text"])}</p></article>'
        for idx,entry in enumerate(cv["projects"],1)
    )
    download = data["application_cvs"]["release_dir"] + "/" + data["application_cvs"]["variants"]["lead"]["basename"][lang]
    return f"""{head}
<body class="engineering-page"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(name)}</strong><span>Backend Engineering</span></span></a><nav class="primary-nav"><a href="#experience">{"Опыт" if lang=="ru" else "Experience"}</a><a href="#cases">{"Кейсы" if lang=="ru" else "Cases"}</a><a href="#contact">{"Контакты" if lang=="ru" else "Contact"}</a></nav><div class="header-actions"><a class="button compact" href="{other}-engineering.html">{other.upper()}</a><a class="button compact" href="index.html">{back}</a></div></div></header>
<main class="shell engineering-main" id="main">
<section class="engineering-hero"><p class="eyebrow">{detailed}</p><h1>{esc(name)}</h1><p class="engineering-role">{esc(cv["role"])}</p><p class="engineering-summary">{esc(cv["summary"])}</p><div class="hero-actions"><a class="button primary" href="{esc(download)}.pdf" download>PDF</a><a class="button" href="{esc(download)}.docx" download>DOCX</a><a class="button" href="{lang}-backend.html" >{"Backend-профиль" if lang=="ru" else "Backend profile"}</a></div></section>
<section class="engineering-section" id="experience"><h2>{title_experience}</h2><div class="engineering-grid">{rows}</div></section>
<section class="engineering-section" id="cases"><h2>{title_cases}</h2><div class="engineering-grid">{cases}</div></section>
<section class="engineering-section engineering-boundary"><h2>{own}</h2><p>{"В LMS отвечаю за требования, архитектурные инварианты и ревью; реализация частично выполнена AI-агентами, платежи только в sandbox. Около года коммерческого опыта — оценка кандидата, а не проверенная непрерывная занятость." if lang=="ru" else "For LMS I define requirements, architectural invariants and review contributions; some implementation was agent-generated and payments are sandbox only. Approx. one year of commercial experience is candidate-reported, not verified continuous employment."}</p></section>
<section id="contact" class="contact-section"><div class="contact-panel"><div><h2>{"Связаться" if lang=="ru" else "Get in touch"}</h2><p>{esc(data["person"][f"location_{lang}"])}</p></div><div class="contact-links"><a class="button primary" href="mailto:{esc(data["person"]["email"])}">Email</a><a class="button" href="{esc(data["person"]["telegram"])}">Telegram</a><a class="button" href="{esc(data["person"]["github"])}">GitHub</a></div></div></section>
</main><footer class="shell site-footer"><span>{esc(name)}</span><span>{esc(data["updated_at"])}</span></footer></body></html>"""


def landing_page(data: dict[str, Any]) -> str:
    lang = "ru"
    canonical_key = data.get("canonical_profile", "compiler")
    primary = data["profiles"][canonical_key][lang]
    primary_en = data["profiles"][canonical_key]["en"]
    landing = data.get("landing", {})
    title = "Михаил Разаков — C#/.NET Backend Developer | Systems & Compilers"
    description = "C#/.NET backend, ASP.NET Core, payment recovery, SharpChecker at ISP RAS, LLVM at MCST, UniversalToolchain and hands-on engineering projects."
    head = common_head(data, lang, "index.html", title, description, data["profiles"]["backend"][lang]["role"], data["site_url"])
    cards = []
    for key in (profile_key for profile_key in data.get("selector_order", data["profile_order"]) if profile_key != canonical_key):
        ru = data["profiles"][key]["ru"]
        en = data["profiles"][key]["en"]
        ui = data["profile_ui"][key]
        heading = ui["landing_title"]
        body = ui["landing_description_ru"]
        cards.append(f'<article class="selector-card"><span>RU / EN</span><h2>{esc(heading)}</h2><p>{esc(body)}</p><div class="selector-links"><a href="{esc(ru["filename"])}">Русская версия</a><a href="{esc(en["filename"])}">English version</a></div><div class="selector-pdf-links"><a href="pdf/{esc(ru["pdf"])}" download>PDF RU</a><a href="pdf/{esc(en["pdf"])}" download>PDF EN</a></div></article>')
    project_ids = landing.get("project_ids", ["globaliv", "deref", "wist"])
    case_items = []
    for number, project_id in enumerate(project_ids, 1):
        project = data["projects"][project_id]
        code_link = (
            f'<a href="{esc(project["repo"])}" target="_blank" rel="noopener noreferrer">Исходники</a>'
            if project.get("repo") else ""
        )
        case_items.append(
            f'<article class="landing-case"><span class="micro-label">{number:02d} / {esc(project["type_ru"])}</span>'
            f'<h3>{esc(project["title"])}</h3>'
            f'<p>{esc(project["problem_ru"])}</p>'
            f'<div class="landing-case-actions"><a href="{esc(project["case_ru"])}">Читать инженерный разбор</a>{code_link}</div>'
            f'</article>'
        )
    project_cases = "".join(case_items)
    evidence = "".join(f"<span>{esc(item)}</span>" for item in landing.get("hero_evidence_ru", []))
    evidence_block = f'<div class="landing-evidence">{evidence}</div>' if evidence else ""
    profiles_intro = landing.get(
        "profiles_intro_ru",
        f'Основной профиль — {primary["role"]}. Специализированные версии меняют приоритет доказательств, но сохраняют единый набор проверенных фактов.',
    )
    p = data["person"]
    return f"""{head}
<body class="selector-page">
<header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(p['name_ru'])}</strong><span>{esc(data['profiles']['backend']['ru']['role'])}</span></span></a><nav class="primary-nav"><a href="#download">Резюме</a><a href="#profiles">Профили</a><a href="#cases">Кейсы</a><a href="#contact">Контакты</a></nav><div class="header-actions"><a class="button compact" href="{esc(primary_en['filename'])}" aria-label="English version of the universal CV">EN</a><a class="button compact" href="#contact">Связаться</a><details class="mobile-menu"><summary>Меню</summary><div class="mobile-panel"><nav><a href="#download">Резюме</a><a href="#profiles">Профили</a><a href="#cases">Кейсы</a><a href="#contact">Контакты</a><a href="{esc(primary_en['filename'])}">English CV</a></nav></div></details></div></div></header>
<main id="main" class="shell landing-main"><section class="selector-intro landing-hero"><p class="eyebrow">{esc(landing.get('eyebrow_ru', primary['eyebrow']))}</p><h1><span class="landing-name">Михаил Разаков</span><span class="landing-role">C#/.NET Backend Developer</span></h1><p>{esc(data['profiles']['backend']['ru']['summary'])}</p><div class="hero-actions"><a class="button primary" href="releases/2026-11-03/01_Backend_ATS.pdf" download>Скачать резюме Backend</a><a class="button" href="ru-backend.html">Профиль C#/.NET</a><a class="button" href="#cases">Посмотреть проекты</a></div>{evidence_block}</section>
<section class="landing-section application-section" id="download"><div class="section-heading"><p class="section-label">00 · Резюме</p><div><h2>Выберите версию под вакансию.</h2><p class="section-intro">Одностраничные PDF, редактируемые DOCX и Markdown. Для HR — backend, для тимлида — инженерные решения, для runtime-команд — компиляторы и CLR.</p></div></div><div class="cv-options">{application_cv_links(data,"ru")}</div><p class="cv-alt-langs"><a href="en-engineering.html">English engineering profile</a> · <a href="releases/2026-11-03/README.md">Все форматы RU / EN</a></p></section>
<section id="profiles" class="landing-section"><div class="section-heading"><p class="section-label">01 · Профили</p><div><h2>Четыре инженерных направления.</h2><p class="section-intro">{esc(profiles_intro)}</p></div></div><div class="selector-grid">{''.join(cards)}</div></section>
<section id="cases" class="landing-section"><div class="section-heading"><p class="section-label">02 · Кейсы</p><div><h2>Что спроектировал, реализовал и проверил.</h2><p class="section-intro">Открытые проекты ведут к коду и документации; закрытые — к публичному архитектурному разбору без секретов и пользовательских данных.</p></div></div><div class="project-grid">{project_cases}</div></section>
<section class="contact-section" id="contact"><div class="contact-panel"><div><h2>Связаться по инженерной роли или проекту.</h2><p>{esc(p['location_ru'])}</p></div><div class="contact-links"><a class="button primary" href="mailto:{esc(p['email'])}">Почта</a><a class="button" href="{esc(p['telegram'])}" target="_blank" rel="noopener noreferrer">Telegram</a><a class="button" href="{esc(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a></div></div></section></main>
<footer class="shell site-footer"><span>{esc(p['name_ru'])} · C#/.NET Backend Developer</span><span>Обновлено {esc(data['updated_at'])}</span></footer><script src="script.js?v={esc(data['version'])}" defer></script></body></html>
"""


def case_page(data: dict[str, Any], project_id: str, lang: str) -> str:
    project = data["projects"][project_id]
    filename = project[f"case_{lang}"]
    title = f"{project['title']} — {'архитектурный кейс' if lang == 'ru' else 'architecture case study'}"
    description = project[f"result_{lang}"]
    canonical_key = data.get("canonical_profile", "compiler")
    role = data["profiles"][canonical_key][lang]["role"]
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
        "botay": "Офлайн-клиенты могут повторять операции после перезапуска; внешние события, локальное состояние и предложения модели нельзя считать равноправными источниками истины." if lang == "ru" else "Offline clients replay commands after restarts; external observations, local state and model proposals must not share mutation authority.",
        "planfuzz": "Нестабильные исполнения, инфраструктурные сбои и необходимость сохранять точный тип расхождения." if lang == "ru" else "Flaky executions, infrastructure failures, and preserving the exact mismatch category.",
        "vpn": "Повторные webhooks, сетевые таймауты, перезапуски, миграции и невозможность раскрывать production-данные." if lang == "ru" else "Duplicate webhooks, network timeouts, restarts, migrations, and private production data.",
         "lms": "Роли и course entitlements, повторные заказы и проверка T-Bank; один платеж не даёт доступа без подтверждения провайдера." if lang == "ru" else "Roles, course entitlements, duplicate orders and T-Bank verification; payment intent alone does not grant access.",
        "psform": "Анализ должен быть консервативным, быстрым на больших диапазонах и проверяемым на малых областях." if lang == "ru" else "The analysis must be conservative, fast on large domains, and checkable on small domains.",
        "codegen": "Нужно сравнивать высокоуровневую семантику и машинный код в изолированном процессе с ограничениями ресурсов." if lang == "ru" else "High-level semantics and machine code must be compared in an isolated, resource-limited process.",
        "globaliv": "Transform допустим только при доказанной affine evolution и legality; unsupported CFG/calls должны приводить к отказу, а не к небезопасной оптимизации." if lang == "ru" else "The transform is allowed only when affine evolution and legality are established; unsupported CFG/calls must be rejected rather than optimized unsafely.",
        "quark2": "Внутренние API CLR нестабильны; микробенчмарки не доказывают общий выигрыш в production." if lang == "ru" else "CLR internals are unstable; microbenchmarks do not prove general production speedups.",
        "deref": "Анализ должен корректно сходиться на ветвлениях, циклах и join points без path explosion." if lang == "ru" else "The analysis must converge correctly across branches, loops, and join points without path explosion.",
    }[project_id]
    verification = {
        "wist": "Canonical test gate, clean-consumer projects, interpreter/CIL parity, deterministic manifests and replayable failures." if lang == "en" else "Канонический тестовый gate, clean-consumer проекты, parity интерпретатора/CIL, детерминированные манифесты и воспроизводимые падения.",
        "botay": "Operation IDs and atomic server records, explicit lifecycle conflicts, witness validation, emulator/device checks and signed APK provenance." if lang == "en" else "Идентификаторы операций и атомарные серверные записи, явные конфликты, проверка witness, эмулятор/device-тесты и происхождение подписанного APK.",
        "planfuzz": "Fresh-process confirmation, exact fingerprints, typed outcomes, and deterministic reduction." if lang == "en" else "Подтверждение в свежем процессе, exact fingerprints, типизированные исходы и детерминированное сокращение.",
        "vpn": "State-transition checks, negative webhook cases, audit records, backup/restore rehearsal, health gates, and rollback verification." if lang == "en" else "Проверки переходов состояния, негативные webhook-сценарии, audit records, репетиция backup/restore, health gates и проверка rollback.",
         "lms": "Review of role and entitlement checks, T-Bank sandbox payment verification, migrations and critical flows; no production launch." if lang == "en" else "Ревью ролей и доступов, перепроверки T-Bank sandbox, миграций и критических flows; без заявления о production-запуске.",
        "psform": "Exact brute-force oracle on small domains, metamorphic generation, sanitizers, and reproducible WA/TL examples." if lang == "en" else "Точный brute-force oracle на малых областях, метаморфная генерация, sanitizers и воспроизводимые WA/TL-примеры.",
        "codegen": "Differential comparison with an IR interpreter, isolated execution, disassembly, and spill/reload metrics." if lang == "en" else "Дифференциальное сравнение с IR-интерпретатором, изолированный запуск, дизассемблирование и метрики spill/reload.",
        "globaliv": "29 positive/negative IR regressions, LLVM verifier checks, idempotence, and before/after execution comparison." if lang == "en" else "29 positive/negative IR regression cases, LLVM verifier, idempotence и сравнение исполнения до/после преобразования.",
        "quark2": "BenchmarkDotNet harness and reproducible invocation modes; no production claim." if lang == "en" else "BenchmarkDotNet и воспроизводимые режимы вызова; без production-утверждений.",
        "deref": "Analyzer tests plus fixed-point worklist convergence over the Roslyn CFG, including branches and loops." if lang == "en" else "Analyzer tests и сходимость fixed-point worklist по Roslyn CFG, включая ветвления и циклы.",
    }[project_id]
    ownership = {
        "wist": "Архитектура, ключевые контракты, runtime, SSA, тестовая стратегия и публичная документация." if lang == "ru" else "Architecture, core contracts, runtime, SSA, verification strategy, and public documentation.",
        "botay": "Canonical/evidence/projection boundaries, offline command replay, feasibility witnesses, LLM intent limits and native Android release path." if lang == "en" else "Границы канонических данных, внешних наблюдений и проекций; replay офлайн-команд, проверка выполнимости, серверная авторизация LLM-действий и выпуск Android.",
        "planfuzz": "Модель исходов, ядро оракулов, replay, fingerprinting и reducers." if lang == "ru" else "Outcome model, oracle core, replay, fingerprinting, and reducers.",
        "vpn": "Backend-архитектура, состояния, платежные интеграции, recovery, миграции и эксплуатационные gates." if lang == "ru" else "Backend architecture, state transitions, payment integrations, recovery, migrations, and operational gates.",
         "lms": "Архитектура и критерии приёмки, ревью агентной реализации ролей, прав доступа и T-Bank sandbox." if lang == "ru" else "Architecture and acceptance criteria; review of agent-generated roles, entitlements and T-Bank sandbox payments.",
        "psform": "Алгоритм анализа, точный оракул, stress infrastructure и разбор контрпримеров." if lang == "ru" else "Analysis algorithm, exact oracle, stress infrastructure, and counterexample analysis.",
        "codegen": "IR, liveness, register allocation, code emission и differential harness." if lang == "ru" else "IR, liveness, register allocation, code emission, and the differential harness.",
        "globaliv": "Модель affine evolution, interprocedural effects, legality analysis, LLVM IR transform и regression harness." if lang == "ru" else "Affine-evolution model, interprocedural effects, legality analysis, LLVM IR transform, and regression harness.",
        "quark2": "Эксперименты с CIL, DynamicMethod и вызовами; результаты интерпретируются как исследовательские." if lang == "ru" else "CIL/DynamicMethod invocation experiments; results remain research-only.",
        "deref": "CFG/data-flow реализация, merge logic, diagnostics и analyzer tests." if lang == "ru" else "CFG/data-flow implementation, merge logic, diagnostics, and analyzer tests.",
    }[project_id]
    links = []
    if project.get("repo"):
        links.append(f'<a class="button" href="{esc(project["repo"])}" target="_blank" rel="noopener noreferrer">GitHub</a>')
    if project.get("docs"):
        links.append(f'<a class="button" href="{esc(project["docs"])}" target="_blank" rel="noopener noreferrer">Documentation</a>')
    return f"""{head}
<body class="case-page"><header class="site-header"><div class="shell header-inner"><a class="brand" href="../index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{esc(person_name(data, lang))}</strong><span>{'инженерный кейс' if lang == 'ru' else 'engineering case'}</span></span></a><div></div><div class="header-actions"><a class="button compact" href="../{esc(data['profiles'][canonical_key][lang]['filename'])}">{labels['back']}</a></div></div></header>
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
    urls.extend(page_url(data, f"{lang}-engineering.html") for lang in ("ru", "en"))
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
    for lang in ("ru", "en"):
        outputs[ROOT / f"{lang}-engineering.html"] = engineering_page(data, lang)
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
