"""Data-driven, bilingual recruiting microsites for the three CV editions.

Public facts, dates, projects and claims remain in data/site.json.
This module owns only layout, navigation and bilingual UI labels.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

ROLES = ("ats", "lead", "runtime")
ROLE_META = {
    "ats": {
        "id": "01", "title_ru": "Backend / ATS", "title_en": "Backend / ATS",
        "hint_ru": "ASP.NET Core · данные · надёжность",
        "hint_en": "ASP.NET Core · data · reliability",
    },
    "lead": {
        "id": "02", "title_ru": "Systems / Platform",
        "title_en": "Systems / Platform",
        "hint_ru": "Архитектура · состояния · восстановление",
        "hint_en": "Architecture · state · recovery",
    },
    "runtime": {
        "id": "03", "title_ru": "Compiler / Performance",
        "title_en": "Compiler / Performance",
        "hint_ru": "LLVM · CIL · проверки оптимизаций",
        "hint_en": "LLVM · CIL · optimization legality",
    },
}


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def loc(lang: str, ru: str, en: str) -> str:
    return ru if lang == "ru" else en


def site_paths(data: dict[str, Any], kind: str, lang: str) -> tuple[str, str]:
    release = data["application_cvs"]
    basename = release["variants"][kind]["basename"][lang]
    return (
        release["pages"][kind][lang],
        release["release_dir"] + "/" + basename,
    )


def role_tabs(data: dict[str, Any], lang: str, active: str) -> str:
    links = []
    for kind in ROLES:
        path, _ = site_paths(data, kind, lang)
        meta = ROLE_META[kind]
        current = ' aria-current="page"' if kind == active else ""
        links.append(
            f'<a href="{esc(path)}"{current}><span>{meta["id"]}</span>'
            f'{esc(meta[f"title_{lang}"])}</a>'
        )
    return "".join(links)


def page_head(data: dict[str, Any], kind: str, lang: str, filename: str, canonical: str | None) -> str:
    cv = data["application_cvs"]["variants"][kind][lang]
    person = data["person"]
    base = data["site_url"]
    name = person["name_"+lang]
    title = f'{name} — {cv["role"]} | CV & Engineering Portfolio'
    desc = cv["summary"]
    this_url = base + filename
    canonical_url = canonical or this_url
    alternate = base + data["application_cvs"]["pages"][kind]["en" if lang == "ru" else "ru"]
    ru_url = base + data["application_cvs"]["pages"][kind]["ru"]
    en_url = base + data["application_cvs"]["pages"][kind]["en"]
    schema = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "url": canonical_url,
        "inLanguage": lang,
        "mainEntity": {
            "@type": "Person",
            "name": name,
            "jobTitle": cv["role"],
            "email": person["email"],
            "url": base,
            "sameAs": [person["github"], person["telegram"]],
            "alumniOf": {"@type": "CollegeOrUniversity", "name": "HSE University"},
        },
    }
    json_ld = json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="{esc(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b1017">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical_url)}">
<meta property="og:image" content="{esc(base)}assets/og-card.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{esc(base)}assets/og-card.png">
<link rel="canonical" href="{esc(canonical_url)}">
<link rel="alternate" hreflang="ru" href="{esc(ru_url)}">
<link rel="alternate" hreflang="en" href="{esc(en_url)}">
<link rel="alternate" hreflang="x-default" href="{esc(base)}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/application-sites.css?v={esc(data['version'])}">
<script type="application/ld+json">{json_ld}</script>
</head>"""


def render(data: dict[str, Any], kind: str, lang: str, filename: str | None = None) -> str:
    if kind not in ROLES or lang not in ("ru", "en"):
        raise ValueError("Unknown application CV kind or language")
    cv = data["application_cvs"]["variants"][kind][lang]
    if filename is None:
        filename = data["application_cvs"]["pages"][kind][lang]
    actual_url = data["application_cvs"]["pages"][kind][lang]
    base_url = data["site_url"] + actual_url
    head = page_head(data, kind, lang, filename, base_url)
    person = data["person"]
    name = person["name_"+lang]
    loc_name = person["location_"+lang]
    experience = data["application_cvs"]["experience"][lang]
    meta = ROLE_META[kind]
    other_lang = "en" if lang == "ru" else "ru"
    other_page = data["application_cvs"]["pages"][kind][other_lang]
    _, files = site_paths(data, kind, lang)
    header = f"""<a class="skip-link" href="#content">{loc(lang,'К содержанию','Skip to content')}</a>
<header class="ap-header">
  <div class="ap-wrap ap-header-grid">
    <a class="ap-brand" href="index.html" aria-label="{esc(name)} — CV"><span class="ap-brand-mark">MR</span>
      <span class="ap-brand-name">{esc(name)}<small>{loc(lang,'Инженерное портфолио','Engineering portfolio')}</small></span></a>
    <nav class="ap-roles" aria-label="{loc(lang,'Специализация','Specialization')}">{role_tabs(data,lang,kind)}</nav>
    <div class="ap-header-actions"><a class="ap-language" href="{esc(other_page)}" hreflang="{other_lang}">{other_lang.upper()}</a>
      <a class="ap-head-mail" href="mailto:{esc(person['email'])}">{loc(lang,'Связаться','Get in touch')} <span aria-hidden="true">↗</span></a></div>
  </div>
</header>"""

    detail = {
        "work": loc(lang, "Опыт и практика", "Experience & practice"),
        "projects": loc(lang, "Инженерные проекты", "Engineering work"),
        "skills": loc(lang, "Технологии", "Technical skills"),
        "education": loc(lang, "Образование", "Education"),
        "contact": loc(lang, "Контакты", "Contact"),
    }
    navlinks = "".join(
        f'<a href="#{anchor}">{esc(label)}</a>'
        for anchor, label in detail.items()
    )
    hero = f"""<section class="ap-hero" aria-labelledby="page-title">
      <div class="ap-hero-main">
        <p class="ap-kicker"><span class="ap-pulse" aria-hidden="true"></span>
          {loc(lang,'Профессиональный профиль','Professional profile')} <span class="ap-sep">/</span> {meta["id"]} — 03</p>
        <h1 id="page-title"><span class="ap-name">{esc(name)}</span><span class="ap-role-title">{esc(cv['role'])}</span></h1>
        <p class="ap-intro">{esc(cv['summary'])}</p>
        <div class="ap-hero-actions">
          <a class="ap-button ap-primary" href="#projects">{loc(lang,'Смотреть проекты','Explore projects')} <span aria-hidden="true">↘</span></a>
          <a class="ap-button ap-outline" href="{esc(files)}.pdf" download>{loc(lang,'Резюме PDF','Resume PDF')} <span aria-hidden="true">↓</span></a>
        </div>
        <div class="ap-download-other">
          <span>{loc(lang,'Редактируемые форматы','Editable formats')}</span>
          <a href="{esc(files)}.docx" download>DOCX</a>
          <a href="{esc(files)}.md" download>Markdown</a>
        </div>
      </div>
      <aside class="ap-hero-aside" aria-label="{loc(lang,'Основные факты','Key facts')}">
        <div class="ap-index-label">{loc(lang,'Срез профиля','Profile at a glance')} <span>2026.11</span></div>
        <div class="ap-spotlight">{esc(meta[f'hint_{lang}'])}</div>
        <div class="ap-fact-row"><span>01</span><p>{esc(experience[0]['title'])}<small>{esc(experience[0]['date'])}</small></p></div>
        <div class="ap-fact-row"><span>02</span><p>{esc(experience[1]['title'])}<small>{esc(experience[1]['date'])}</small></p></div>
        <div class="ap-fact-row"><span>03</span><p>{esc(experience[2]['title'])}<small>{esc(experience[2]['date'])}</small></p></div>
        <div class="ap-aside-end"><span>{esc(loc_name)}</span><span>{loc(lang,'Доступен для удалённой работы','Open to remote work')}</span></div>
      </aside>
    </section>"""

    intro = f"""<div class="ap-section-nav" aria-label="{loc(lang,'Навигация по разделам','Page sections')}"><div class="ap-wrap">{navlinks}</div></div>"""

    exp_rows = "".join(
        f"""<article class="ap-exp-item">
          <div class="ap-exp-date">{esc(item['date'])}</div>
          <div><h3>{esc(item['title'])}</h3><p>{esc(item['text'])}</p></div>
        </article>"""
        for item in experience
    )
    work = f"""<section class="ap-section ap-work" id="work">
      <div class="ap-section-aside"><span class="ap-number">01 / 04</span><h2>{detail['work']}</h2>
        <p>{loc(lang,'Коммерческую практику, исследования и самостоятельные проекты показываю раздельно — без искусственного завышения стажа.','Commercial work, research and independent projects are presented separately, without inflating tenure.')}</p>
      </div>
      <div class="ap-exp-list">{exp_rows}</div>
    </section>"""

    cases = []
    for n, item in enumerate(cv["projects"], 1):
        project = data["projects"][item["id"]]
        case = project[f"case_{lang}"]
        repo = project.get("repo")
        source = (
            f'<a href="{esc(repo)}" target="_blank" rel="noopener noreferrer">{loc(lang,"Исходники","Source code")} <span aria-hidden="true">↗</span></a>'
            if repo else ""
        )
        labels = [
            (loc(lang,"Задача","Problem"), project[f"problem_{lang}"]),
            (loc(lang,"Решение","Approach"), project[f"solution_{lang}"]),
            (loc(lang,"Результат и границы","Outcome & limits"), project[f"result_{lang}"]),
        ]
        tech_details = "".join(
            f'<div class="ap-case-detail"><h4>{esc(label)}</h4><p>{esc(body)}</p></div>'
            for label,body in labels
        )
        cases.append(
          f"""<article class="ap-case" id="case-{esc(item['id'])}">
            <div class="ap-case-identity"><div class="ap-case-index">{n:02d} <span>/ {len(cv['projects']):02d}</span></div>
              <p class="ap-case-type">{esc(project[f'type_{lang}'])}</p>
              <h3>{esc(item['title'])}</h3>
              <p class="ap-case-summary">{esc(item['text'])}</p>
              <div class="ap-case-links">
                <a href="{esc(case)}">{loc(lang,'Полный разбор кейса','Full case study')} <span aria-hidden="true">↗</span></a>
                {source}
              </div>
            </div>
            <div class="ap-case-technical">{tech_details}</div>
          </article>"""
        )
    projects = f"""<section class="ap-project-section" id="projects"><div class="ap-section-heading">
        <span class="ap-number">02 / 04</span>
        <div><h2>{detail['projects']}</h2>
        <p>{loc(lang,'Реальные задачи, решения и проверяемые границы результата.','Real constraints, engineering choices and verifiable outcomes.')}</p></div>
        <span class="ap-count">{len(cv['projects']):02d}</span>
      </div>{''.join(cases)}</section>"""

    skill_rows = "".join(f'<li>{esc(s)}</li>' for s in cv["skills"])
    highlights = "".join(
        f'<a class="ap-repo-ref" href="{esc(data["projects"][x["id"]].get("repo") or data["projects"][x["id"]][f"case_{lang}"])}">{esc(data["projects"][x["id"]]["title"])} <span aria-hidden="true">↗</span></a>'
        for x in cv["projects"]
    )
    skills = f"""<section class="ap-section ap-skills" id="skills">
        <div class="ap-section-aside"><span class="ap-number">03 / 04</span><h2>{detail['skills']}</h2>
          <p>{loc(lang,'Список технологий соответствует выбранному профилю CV; контекст применения — в кейсах.','Technologies are targeted to this CV edition; usage context is in the case studies.')}</p></div>
        <div class="ap-skills-content"><ul>{skill_rows}</ul>
          <h3>{loc(lang,'Верифицируемые материалы','Reference projects')}</h3>
          <div class="ap-reference-links">{highlights}</div>
        </div>
      </section>"""
    notes = loc(
        lang,
        "Совокупный коммерческий стаж указан по данным кандидата. Доступность исходников, манифест тестов и успешное прохождение тестов — разные виды доказательств. TuringSquare-LMS в разработке: реализация частично агентная, платежи — sandbox. Ни одно из этих утверждений не выдаётся за независимую проверку production.",
        "Aggregate commercial tenure is candidate-reported. Source availability, a test manifest and freshly executed tests are different evidence levels. TuringSquare-LMS is in development: parts are agent-implemented, payments are sandbox only. None of these statements claim independently verified production behavior.",
    )
    edu = f"""<section class="ap-section ap-education" id="education">
        <div class="ap-section-aside"><span class="ap-number">04 / 04</span><h2>{detail['education']}</h2></div>
        <div class="ap-education-content">
          <h3>{esc(cv['education'])}</h3>
          <p>{esc(cv['recognition'])}</p>
          <div class="ap-evidence"><strong>{loc(lang,'Границы доказательств','Evidence boundaries')}</strong>
            <p>{esc(notes)}</p>
            <a href="releases/2026-11-03/04_Public_Evidence_Boundaries.md">{loc(lang,'Подробнее о подтверждениях','Read source limitations')} <span aria-hidden="true">↗</span></a>
          </div>
        </div>
      </section>"""

    nav_footer = role_tabs(data,lang,kind)
    end = f"""<section class="ap-contact" id="contact">
      <div class="ap-contact-inner">
        <p class="ap-kicker">{loc(lang,'Открыт к диалогу','Open to conversation')} <span class="ap-sep">/</span> {meta['id']}</p>
        <h2>{loc(lang,'Обсудим инженерную задачу.','Let’s discuss an engineering problem.')}</h2>
        <p>{esc(name)} · {esc(loc_name)}</p>
        <div class="ap-contact-links">
          <a class="ap-button ap-primary" href="mailto:{esc(person['email'])}">{loc(lang,'Написать на почту','Send an email')} <span aria-hidden="true">↗</span></a>
          <a href="{esc(person['telegram'])}" target="_blank" rel="noopener noreferrer">Telegram ↗</a>
          <a href="{esc(person['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
        </div>
      </div>
      <div class="ap-bottom"><span>{esc(name)} © 2026</span><a href="index.html">{loc(lang,'Все профили','All profiles')} ↗</a></div>
    </section>"""
    return f"""{head}
<body class="ap ap-{kind}">{header}<main id="content">
<div class="ap-wrap">{hero}</div>
{intro}
<div class="ap-wrap">{work}{projects}{skills}{edu}</div>
{end}</main></body></html>
"""


def outputs(data: dict[str, Any], root: Path) -> dict[Path, str]:
    created: dict[Path, str] = {}
    for kind in ROLES:
        for lang in ("ru", "en"):
            filename = data["application_cvs"]["pages"][kind][lang]
            created[root/filename] = "\n".join(line.rstrip() for line in render(data,kind,lang).splitlines()) + "\n"
    # Previous public engineering URLs keep the current engineering edition,
    # with a canonical URL pointing at the named Tech Lead route.
    for lang in ("ru", "en"):
        filename = f"{lang}-engineering.html"
        created[root/filename] = "\n".join(line.rstrip() for line in render(data, "lead", lang, filename).splitlines()) + "\n"
    return created
