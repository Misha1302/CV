from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "site.json"
GENERATED_MARKER = "<!-- generated from data/site.json; do not edit -->"


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def load_data() -> dict[str, Any]:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 35:
        raise RuntimeError("unsupported data/site.json schema")
    return data


def canonical_sha256() -> str:
    return hashlib.sha256(DATA_PATH.read_bytes()).hexdigest()


def page_url(data: dict[str, Any], path: str) -> str:
    return data["site_url"] + path


def name(data: dict[str, Any], lang: str) -> str:
    return data["person"][f"name_{lang}"]


def other(lang: str) -> str:
    return "en" if lang == "ru" else "ru"


def format_int(value: int, lang: str) -> str:
    return f"{value:,}" if lang == "en" else f"{value:,}".replace(",", " ")


def wist_claim(data: dict[str, Any], lang: str, compact: bool = False) -> str:
    e = data["evidence"]["wist_verification"]
    count = format_int(e["passed"], lang)
    if lang == "ru":
        if compact:
            return f"Public verification manifest от {e['date_ru']}: {count} тестов, 0 падений; {e['scope_ru']}."
        return f"Public verification manifest от {e['date_ru']}: {count} тестов, 0 падений; {e['scope_ru']}. Source revision {e['source_commit'][:12]}."
    if compact:
        return f"Public verification manifest dated {e['date_en']}: {count} tests, zero failures; {e['scope_en']}."
    return f"Public verification manifest dated {e['date_en']}: {count} tests, zero failures; {e['scope_en']}. Source revision {e['source_commit'][:12]}."


def mcst_claim(data: dict[str, Any], lang: str, compact: bool = False) -> str:
    e = data["evidence"]["mcst_selection"]
    if lang == "ru":
        text = f"1-е место среди {e['submissions']} присланных решений; единственные {e['score']} и {e['official_tests']} официальных теста в отборе по направлению LLVM-компилятора."
        return text if compact else text + " " + e["boundary_ru"]
    text = f"1st among {e['submissions']} submitted solutions; the only {e['score']} score and {e['official_tests']} official tests in the LLVM compiler track selection."
    return text if compact else text + " " + e["boundary_en"]


def proof(data: dict[str, Any], key: str, lang: str) -> tuple[str, str]:
    if key == "wist":
        e = data["evidence"]["wist_verification"]
        title = f"{format_int(e['passed'], lang)} {'тестов' if lang == 'ru' else 'tests'} · 0 {'падений' if lang == 'ru' else 'failures'}"
        return title, wist_claim(data, lang, compact=True)
    if key == "mcst":
        return ("1-е место из 49" if lang == "ru" else "1st of 49", mcst_claim(data, lang, compact=True))
    if key == "verification":
        return (
            "Проверка корректности" if lang == "ru" else "Correctness verification",
            "Exact-oracle, differential и metamorphic testing, replay/reduction и консервативные fail-closed решения." if lang == "ru" else "Exact-oracle, differential, and metamorphic testing, replay/reduction, and conservative fail-closed decisions.",
        )
    if key == "psform":
        return (
            "yes / no / maybe",
            "Консервативный анализ зависимости памяти с exact affine-анализом и cost-guarded fallbacks." if lang == "ru" else "Conservative memory-dependence analysis with exact affine analysis and cost-guarded fallbacks.",
        )
    if key == "backend_state":
        return ("Явные состояния" if lang == "ru" else "Explicit state", "Подписки, платежи, роли, устройства и идемпотентные переходы." if lang == "ru" else "Subscriptions, payments, roles, devices, and idempotent transitions.")
    if key == "backend_recovery":
        return ("Recovery-гейты" if lang == "ru" else "Recovery gates", "Миграции, audit, reconciliation, backup/restore и rollback." if lang == "ru" else "Migrations, audit, reconciliation, backup/restore, and rollback.")
    raise KeyError(key)


def profile_lookup(data: dict[str, Any], filename: str) -> tuple[str, str, dict[str, Any]]:
    for profile_id, variants in data["profiles"].items():
        for lang in ("ru", "en"):
            if variants[lang]["filename"] == filename:
                return profile_id, lang, variants[lang]
    raise KeyError(filename)


def alternates(data: dict[str, Any], profile_id: str, lang: str) -> tuple[str, str]:
    current = data["profiles"][profile_id][lang]["filename"]
    alternate = data["profiles"][profile_id][other(lang)]["filename"]
    return page_url(data, current), page_url(data, alternate)


def head(data: dict[str, Any], profile_id: str, lang: str, profile: dict[str, Any]) -> str:
    canonical, alternate = alternates(data, profile_id, lang)
    source_sha = canonical_sha256()
    schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name(data, lang),
        "jobTitle": profile["role"],
        "description": profile["description"],
        "email": f"mailto:{data['person']['email']}",
        "url": canonical,
        "sameAs": [data["person"]["github_url"], data["person"]["telegram_url"]],
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "HSE University"},
        "identifier": {"@type": "PropertyValue", "propertyID": "canonical-source-sha256", "value": source_sha},
    }
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f4f1eb">
<meta name="cv:source-sha256" content="{source_sha}">
<title>{esc(profile['title'])}</title>
<meta name="description" content="{esc(profile['description'])}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{esc(profile['title'])}">
<meta property="og:description" content="{esc(profile['description'])}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(page_url(data, 'assets/og-card.svg'))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(profile['title'])}">
<meta name="twitter:description" content="{esc(profile['description'])}">
<meta name="twitter:image" content="{esc(page_url(data, 'assets/og-card.svg'))}">
<link rel="canonical" href="{esc(canonical)}">
<link rel="alternate" hreflang="{lang}" href="{esc(canonical)}">
<link rel="alternate" hreflang="{other(lang)}" href="{esc(alternate)}">
<link rel="alternate" hreflang="x-default" href="{esc(data['site_url'])}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css?v={esc(data['release_version'])}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')}</script>
</head>"""


def nav(data: dict[str, Any], profile_id: str, lang: str) -> str:
    labels = {
        "profile": "Профиль" if lang == "ru" else "Profile",
        "evidence": "Доказательства" if lang == "ru" else "Evidence",
        "experience": "Опыт" if lang == "ru" else "Experience",
        "projects": "Проекты" if lang == "ru" else "Projects",
        "skills": "Навыки" if lang == "ru" else "Skills",
        "education": "Образование" if lang == "ru" else "Education",
    }
    links = "".join(f'<a href="#{key}">{esc(label)}</a>' for key, label in labels.items())
    alt = data["profiles"][profile_id][other(lang)]["filename"]
    return f"""<a class="skip-link" href="#main">{'К содержанию' if lang == 'ru' else 'Skip to content'}</a>
<header class="site-header"><div class="shell header-inner">
<a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">MR</span><span>{esc(name(data, lang))}</span></a>
<nav class="primary-nav" aria-label="{'Разделы резюме' if lang == 'ru' else 'Resume sections'}">{links}</nav>
<div class="header-actions"><a href="{esc(alt)}" hreflang="{other(lang)}">{other(lang).upper()}</a><a class="button" href="mailto:{esc(data['person']['email'])}">{'Написать' if lang == 'ru' else 'Email'}</a></div>
</div></header>"""


def link_list(links: Iterable[dict[str, str]]) -> str:
    return "".join(f'<a href="{esc(item["url"])}" rel="noopener noreferrer">{esc(item["label"])} ↗</a>' for item in links)


def hero(data: dict[str, Any], profile: dict[str, Any], lang: str) -> str:
    p = data["person"]
    location = p[f"location_{lang}"]
    portrait_alt = "Абстрактный монограмный портрет Михаила Разакова" if lang == "ru" else "Abstract monogram portrait of Mikhail Razakov"
    return f"""<section class="hero shell" id="profile">
<div class="hero-main"><p class="level">{esc(profile['level'])}</p><h1>{esc(name(data, lang))}</h1><p class="role">{esc(profile['role'])}</p><p class="tagline">{esc(profile['tagline'])}</p><p class="summary">{esc(profile['summary'])}</p>
<div class="hero-actions"><a class="button primary" href="mailto:{esc(p['email'])}">{'Написать' if lang == 'ru' else 'Email'}</a><a class="button" href="pdf/{esc(profile['pdf'])}">{'PDF'}</a><a class="button" href="ats/{esc(profile['ats'])}">{'ATS text'}</a></div></div>
<aside class="contact-card" aria-label="{'Контакты' if lang == 'ru' else 'Contact details'}"><img src="assets/portrait.svg" width="320" height="320" alt="{esc(portrait_alt)}"><dl><div><dt>{'Локация' if lang == 'ru' else 'Location'}</dt><dd>{esc(location)}</dd></div><div><dt>Email</dt><dd><a href="mailto:{esc(p['email'])}">{esc(p['email'])}</a></dd></div><div><dt>Telegram</dt><dd><a href="{esc(p['telegram_url'])}" rel="noopener noreferrer">{esc(p['telegram_label'])}</a></dd></div><div><dt>GitHub</dt><dd><a href="{esc(p['github_url'])}" rel="noopener noreferrer">{esc(p['github_label'])}</a></dd></div></dl></aside>
</section>"""


def evidence_section(data: dict[str, Any], profile: dict[str, Any], lang: str) -> str:
    cards = []
    for key in profile["proof_keys"]:
        title, body = proof(data, key, lang)
        cards.append(f'<article class="evidence-card"><h3>{esc(title)}</h3><p>{esc(body)}</p></article>')
    return f"""<section class="section shell" id="evidence"><div class="section-head"><p>01</p><h2>{'Ключевые доказательства' if lang == 'ru' else 'Key evidence'}</h2></div><div class="evidence-grid">{''.join(cards)}</div></section>"""


def experience_section(data: dict[str, Any], profile: dict[str, Any], lang: str) -> str:
    rows = []
    for exp_id in profile["experience_ids"]:
        exp = data["experiences"][exp_id]
        bullets = list(exp[f"bullets_{lang}"])
        if exp.get("claim_key") == "wist":
            bullets.append(wist_claim(data, lang, compact=True))
        elif exp.get("claim_key") == "mcst":
            bullets.append(mcst_claim(data, lang, compact=True))
        links = link_list(exp.get("links", []))
        rows.append(f"""<article class="timeline-item"><div class="timeline-meta"><time>{esc(exp[f'date_{lang}'])}</time><p>{esc(exp[f'org_{lang}'])}</p></div><div><h3>{esc(exp[f'title_{lang}'])}</h3><ul>{''.join(f'<li>{esc(b)}</li>' for b in bullets)}</ul><div class="inline-links">{links}</div></div></article>""")
    return f"""<section class="section shell" id="experience"><div class="section-head"><p>02</p><h2>{'Опыт' if lang == 'ru' else 'Experience'}</h2></div><div class="timeline">{''.join(rows)}</div></section>"""


def projects_section(data: dict[str, Any], profile: dict[str, Any], lang: str) -> str:
    cards = []
    for project_id in profile["project_ids"]:
        project = data["projects"][project_id]
        case = project[f"case_{lang}"]
        links = [f'<a href="{esc(case)}">{"Кейс" if lang == "ru" else "Case"} ↗</a>']
        if project.get("repo"):
            links.append(f'<a href="{esc(project["repo"])}" rel="noopener noreferrer">GitHub ↗</a>')
        if project.get("docs"):
            links.append(f'<a href="{esc(project["docs"])}" rel="noopener noreferrer">{"Документация" if lang == "ru" else "Documentation"} ↗</a>')
        cards.append(f"""<article class="project-card"><p class="project-type">{esc(project[f'type_{lang}'])}</p><h3>{esc(project['title'])}</h3><ul>{''.join(f'<li>{esc(b)}</li>' for b in project[f'bullets_{lang}'])}</ul><div class="inline-links">{''.join(links)}</div></article>""")
    return f"""<section class="section shell" id="projects"><div class="section-head"><p>03</p><h2>{'Избранные проекты' if lang == 'ru' else 'Selected projects'}</h2></div><div class="projects-grid">{''.join(cards)}</div></section>"""


def skills_section(profile: dict[str, Any], lang: str) -> str:
    rows = "".join(f'<div class="skill-row"><h3>{esc(title)}</h3><p>{esc(body)}</p></div>' for title, body in profile["skills"])
    return f"""<section class="section shell" id="skills"><div class="section-head"><p>04</p><h2>{'Навыки' if lang == 'ru' else 'Skills'}</h2></div><div class="skills-list">{rows}</div></section>"""


def education_section(data: dict[str, Any], lang: str) -> str:
    p = data["person"]
    return f"""<section class="section shell" id="education"><div class="section-head"><p>05</p><h2>{'Образование и достижения' if lang == 'ru' else 'Education and recognition'}</h2></div><div class="education-grid"><article><h3>{'Образование' if lang == 'ru' else 'Education'}</h3><p>{esc(p[f'education_{lang}'])}</p></article><article><h3>{'Достижения' if lang == 'ru' else 'Recognition'}</h3><p>{esc(p[f'achievement_{lang}'])}</p></article></div></section>"""


def profile_page(data: dict[str, Any], profile_id: str, lang: str) -> str:
    profile = data["profiles"][profile_id][lang]
    return "\n".join([
        GENERATED_MARKER,
        head(data, profile_id, lang, profile),
        "<body>",
        nav(data, profile_id, lang),
        '<main id="main">',
        hero(data, profile, lang),
        evidence_section(data, profile, lang),
        experience_section(data, profile, lang),
        projects_section(data, profile, lang),
        skills_section(profile, lang),
        education_section(data, lang),
        "</main>",
        f'<footer class="shell site-footer"><span>{esc(name(data, lang))}</span><span>source {canonical_sha256()[:12]} · {esc(data["release_version"])}</span></footer>',
        '<script src="script.js" defer></script>',
        "</body></html>",
    ]) + "\n"


def index_page(data: dict[str, Any]) -> str:
    cards = []
    labels = {"compiler": "Compiler / Language Platforms", "backend": ".NET Backend", "systems": "C++ / LLVM", "general": "General"}
    for profile_id in data["profile_order"]:
        ru = data["profiles"][profile_id]["ru"]
        en = data["profiles"][profile_id]["en"]
        cards.append(f"""<article class="selector-card"><p>{esc(labels[profile_id])}</p><h2>{esc(ru['role'])}</h2><span>{esc(ru['level'])}</span><p>{esc(ru['tagline'])}</p><div class="inline-links"><a href="{esc(ru['filename'])}">RU</a><a href="{esc(en['filename'])}">EN</a><a href="pdf/{esc(ru['pdf'])}">PDF RU</a><a href="pdf/{esc(en['pdf'])}">PDF EN</a></div></article>""")
    title = "Михаил Разаков — резюме"
    description = "Role-specific CV profiles for compiler, .NET backend, C++/LLVM, and general software development."
    return f"""{GENERATED_MARKER}
<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{esc(data['site_url'])}"><link rel="stylesheet" href="style.css?v={esc(data['release_version'])}"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head><body><main class="shell selector"><p class="level">Junior / internship</p><h1>{esc(name(data, 'ru'))}</h1><p class="selector-lead">Выберите профиль под конкретную роль. Compiler-версия — основная; backend остаётся отдельной целевой историей.</p><div class="selector-grid">{''.join(cards)}</div></main></body></html>\n"""


def case_page(data: dict[str, Any], project_id: str, lang: str) -> str:
    project = data["projects"][project_id]
    title = f"{project['title']} — {'инженерный кейс' if lang == 'ru' else 'engineering case'}"
    back = "../ru-compiler.html" if lang == "ru" else "../en-compiler.html"
    if project_id in {"vpn", "lms"}:
        back = "../ru-backend.html" if lang == "ru" else "../en-backend.html"
    source_links = []
    for key, label in (("repo", "GitHub"), ("docs", "Documentation" if lang == "en" else "Документация")):
        if project.get(key):
            source_links.append(f'<a href="{esc(project[key])}" rel="noopener noreferrer">{esc(label)} ↗</a>')
    planfuzz = ""
    if project_id == "wist":
        planfuzz = f"""<section id="planfuzz"><h2>PlanFuzz</h2><p>{'Экспериментальный компонент Wist2: отдельная устойчивая страница больше не заявляется; ссылка ведёт к canonical Wist2 case и публичной документации.' if lang == 'ru' else 'Experimental Wist2 component: it is no longer presented as a separate canonical case; links resolve to this stable Wist2 case and public documentation.'}</p></section>"""
    source_sha = canonical_sha256()
    return f"""{GENERATED_MARKER}
<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(project[f'bullets_{lang}'][0])}"><link rel="canonical" href="{esc(page_url(data, project[f'case_{lang}']))}"><link rel="stylesheet" href="../style.css?v={esc(data['release_version'])}"></head><body><main class="case shell"><a class="back-link" href="{esc(back)}">← {'Назад к резюме' if lang == 'ru' else 'Back to CV'}</a><p class="project-type">{esc(project[f'type_{lang}'])}</p><h1>{esc(project['title'])}</h1><section><h2>{'Граница утверждения' if lang == 'ru' else 'Claim boundary'}</h2><ul>{''.join(f'<li>{esc(b)}</li>' for b in project[f'bullets_{lang}'])}</ul></section>{planfuzz}<div class="inline-links">{''.join(source_links)}</div><p class="source-note">source {source_sha[:12]}</p></main></body></html>\n"""


def redirect_page(data: dict[str, Any], source: str, target: str) -> str:
    # Redirect targets are expressed relative to the source file directory.
    canonical_path = (source.rsplit("/", 1)[0] + "/" + target) if "/" in source else target
    canonical = page_url(data, canonical_path)
    return f"""{GENERATED_MARKER}
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url={esc(target)}"><link rel="canonical" href="{esc(canonical)}"><title>Moved</title></head><body><main><h1>Moved</h1><p><a href="{esc(target)}">Continue</a></p></main></body></html>\n"""


def ats_text(data: dict[str, Any], profile_id: str, lang: str) -> str:
    profile = data["profiles"][profile_id][lang]
    p = data["person"]
    h = {
        "profile": "ПРОФИЛЬ" if lang == "ru" else "PROFILE",
        "evidence": "КЛЮЧЕВЫЕ ДОКАЗАТЕЛЬСТВА" if lang == "ru" else "KEY EVIDENCE",
        "experience": "ОПЫТ" if lang == "ru" else "EXPERIENCE",
        "projects": "ИЗБРАННЫЕ ПРОЕКТЫ" if lang == "ru" else "SELECTED PROJECTS",
        "skills": "НАВЫКИ" if lang == "ru" else "SKILLS",
        "education": "ОБРАЗОВАНИЕ И ДОСТИЖЕНИЯ" if lang == "ru" else "EDUCATION AND RECOGNITION",
    }
    lines = [name(data, lang), profile["role"], profile["level"], profile["tagline"], p[f"location_{lang}"], p["email"], p["telegram_label"], p["github_label"], "", h["profile"], profile["summary"], "", h["evidence"]]
    for key in profile["proof_keys"]:
        title, body = proof(data, key, lang)
        lines += [title, body]
    lines += ["", h["experience"]]
    for exp_id in profile["experience_ids"]:
        exp = data["experiences"][exp_id]
        lines += [f"{exp[f'date_{lang}']} — {exp[f'title_{lang}']}", exp[f"org_{lang}"]]
        lines += [f"• {b}" for b in exp[f"bullets_{lang}"]]
        if exp.get("claim_key") == "wist":
            lines.append("• " + wist_claim(data, lang, compact=True))
        elif exp.get("claim_key") == "mcst":
            lines.append("• " + mcst_claim(data, lang, compact=True))
        lines += [item["url"] for item in exp.get("links", [])]
    lines += ["", h["projects"]]
    for project_id in profile["project_ids"]:
        project = data["projects"][project_id]
        lines.append(project["title"])
        lines += [f"• {b}" for b in project[f"bullets_{lang}"]]
        if project.get("repo"):
            lines.append(project["repo"])
    lines += ["", h["skills"]]
    for title, body in profile["skills"]:
        lines.append(f"{title}: {body}")
    lines += ["", h["education"], p[f"education_{lang}"], p[f"achievement_{lang}"], "", f"canonical-source-sha256: {canonical_sha256()}", f"release-version: {data['release_version']}"]
    return "\n".join(lines) + "\n"


def sitemap(data: dict[str, Any]) -> str:
    urls = [data["site_url"]]
    for profile_id in data["profile_order"]:
        for lang in ("ru", "en"):
            urls.append(page_url(data, data["profiles"][profile_id][lang]["filename"]))
    for project in data["projects"].values():
        urls.append(page_url(data, project["case_ru"]))
        urls.append(page_url(data, project["case_en"]))
    body = "".join(f"<url><loc>{esc(url)}</loc><lastmod>{data['updated_at']}</lastmod></url>" for url in sorted(set(urls)))
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def build_outputs(data: dict[str, Any]) -> dict[Path, str]:
    outputs: dict[Path, str] = {ROOT / "index.html": index_page(data)}
    for profile_id in data["profile_order"]:
        for lang in ("ru", "en"):
            profile = data["profiles"][profile_id][lang]
            outputs[ROOT / profile["filename"]] = profile_page(data, profile_id, lang)
            outputs[ROOT / "ats" / profile["ats"]] = ats_text(data, profile_id, lang)
    for project_id, project in data["projects"].items():
        outputs[ROOT / project["case_ru"]] = case_page(data, project_id, "ru")
        outputs[ROOT / project["case_en"]] = case_page(data, project_id, "en")
    for source, target in data["redirects"].items():
        outputs[ROOT / source] = redirect_page(data, source, target)
    outputs[ROOT / "sitemap.xml"] = sitemap(data)
    outputs[ROOT / "robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {data['site_url']}sitemap.xml\n"
    meta = {
        "schema_version": data["schema_version"],
        "release_version": data["release_version"],
        "updated_at": data["updated_at"],
        "baseline_commit": data["baseline_commit"],
        "canonical_source": "data/site.json",
        "canonical_source_sha256": canonical_sha256(),
        "wist_evidence_source_commit": data["evidence"]["wist_verification"]["source_commit"],
        "wist_evidence_source_blob_sha": data["evidence"]["wist_verification"]["source_blob_sha"],
    }
    outputs[ROOT / "data" / "build-meta.json"] = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
    return outputs


def write_or_check(outputs: dict[Path, str], check: bool) -> None:
    failures = []
    for path, content in outputs.items():
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                failures.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if failures:
        raise RuntimeError("generated files are stale: " + ", ".join(failures[:20]))


def manifest() -> None:
    target = ROOT / "MANIFEST.sha256"
    lines = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == target or ".git" in path.parts or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  ./{path.relative_to(ROOT).as_posix()}")
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()
    data = load_data()
    write_or_check(build_outputs(data), check=args.check)
    if args.manifest:
        manifest()
    if not args.check:
        print(json.dumps({"generated": len(build_outputs(data)), "source_sha256": canonical_sha256()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
