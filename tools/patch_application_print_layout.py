from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_SITE = ROOT / "tools" / "build_site.py"
STYLE = ROOT / "style.css"

NEW_PRINT_CV = r'''
def print_cv(data: dict[str, Any], lang: str, profile: dict[str, Any]) -> str:
    labels = {
        "experience": "Опыт" if lang == "ru" else "Experience",
        "projects": "Исследования и проекты" if lang == "ru" else "Selected Research & Engineering",
        "skills": "Компетенции" if lang == "ru" else "Skills",
        "education": "Образование" if lang == "ru" else "Education",
        "recognition": "Достижения" if lang == "ru" else "Recognition",
    }
    p = data["person"]
    contacts = f'<a href="mailto:{esc(p["email"])}">{esc(p["email"])}</a><br><a href="{esc(p["telegram"])}">{esc(p["telegram_label"])}</a><br><a href="{esc(p["github"])}">{esc(p["github_label"])}</a>'

    if profile.get("print_layout") == "application":
        experiences = []
        for item in profile["experience"][:3]:
            bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"][:2])
            experiences.append(
                f'<article class="pcv-app-entry"><div class="pcv-app-date">{esc(item["date"])}</div>'
                f'<div><h3>{esc(item["title"])}</h3><p class="pcv-app-org">{esc(item["org"])}</p><ul>{bullets}</ul></div></article>'
            )

        projects = []
        project_limit = int(profile.get("print_project_limit", 3))
        for project_id in profile["project_ids"][:project_limit]:
            project = data["projects"][project_id]
            target = project.get("repo") or project[f"case_{lang}"]
            projects.append(
                f'<article class="pcv-app-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>'
                f'<p>{esc(project[f"result_{lang}"])}</p></article>'
            )

        skills = "".join(
            f'<div class="pcv-app-skill"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
            for title, body in profile["skills"]
        )
        recognition_data = recognition_items(data, lang, profile)
        recognition = "".join(
            f'<div class="pcv-app-recognition"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
            for _, title, body in recognition_data[:2]
        )
        education = p[f"education_{lang}"]
        location = p[f"location_{lang}"]
        return f"""
<div class="print-cv pcv-application" aria-label="Focused one-page application CV">
  <header class="pcv-header"><div><h1>{esc(person_name(data, lang))}</h1><h2>{esc(profile['role'])}</h2></div><div class="pcv-contact">{contacts}</div></header>
  <p class="pcv-app-summary">{esc(profile['summary'])}</p>
  <section class="pcv-app-section pcv-app-education"><h2 class="pcv-section-title">{labels['education']}</h2><p><strong>{esc(education)}</strong><span>{esc(location)}</span></p></section>
  <section class="pcv-app-section"><h2 class="pcv-section-title">{labels['experience']}</h2>{''.join(experiences)}</section>
  <section class="pcv-app-section"><h2 class="pcv-section-title">{labels['projects']}</h2>{''.join(projects)}</section>
  <section class="pcv-app-section"><h2 class="pcv-section-title">{labels['skills']}</h2>{skills}</section>
  <section class="pcv-app-section"><h2 class="pcv-section-title">{labels['recognition']}</h2>{recognition}</section>
</div>"""

    is_compiler_print = profile["filename"] in {"ru-compiler.html", "en-compiler.html"}
    proofs = "".join(f'<div class="pcv-proof"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["proofs"])
    proof_block = "" if is_compiler_print else f'<div class="pcv-proofs">{proofs}</div>'
    experiences = []
    for item in profile["experience"][:3]:
        bullets = "".join(f"<li>{esc(text)}</li>" for text in item["bullets"][:2])
        experiences.append(f'<article class="pcv-entry"><div class="pcv-date">{esc(item["date"])}</div><div><h3>{esc(item["title"])}</h3><ul>{bullets}</ul></div></article>')
    projects = []
    project_limit = int(profile.get("print_project_limit", 3))
    project_summaries = profile.get("project_summaries", {})
    for project_id in profile["project_ids"][:project_limit]:
        project = data["projects"][project_id]
        target = project.get("repo") or project[f"case_{lang}"]
        summary = project_summaries.get(project_id, {}) if is_compiler_print else {}
        if is_compiler_print and summary:
            project_body = f'<p>{esc(summary.get("solution", ""))}</p><p class="pcv-project-result">{esc(summary.get("result", ""))}</p>'
        else:
            project_body = f'<p>{esc(project[f"result_{lang}"])}</p>'
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>{project_body}</article>')
    skills = "".join(f'<div class="pcv-skill"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>' for title, body in profile["skills"])
    education = p[f"education_{lang}"]
    recognition_data = recognition_items(data, lang, profile)
    if is_compiler_print:
        recognition = "".join(
            f'<div class="pcv-recognition"><strong>{esc(title)}</strong><span>{esc(body)}</span></div>'
            for _, title, body in recognition_data[:4]
        )
    else:
        recognition = f'<p>{esc(recognition_data[0][2])}</p>'
    return f"""
<div class="print-cv" aria-label="Focused one-page CV">
  <header class="pcv-header"><div><h1>{esc(person_name(data, lang))}</h1><h2>{esc(profile['role'])}</h2></div><div class="pcv-contact">{contacts}</div></header>
  <p class="pcv-summary">{esc(profile['summary'])}</p>{proof_block}
  <div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels['experience']}</h2>{''.join(experiences)}</section><section><h2 class="pcv-section-title">{labels['projects']}</h2>{''.join(projects)}</section></main>
  <aside class="pcv-side"><section><h2 class="pcv-section-title">{labels['skills']}</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['education']}</h2><p>{esc(education)}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels['recognition']}</h2>{recognition}</section><section class="pcv-compact"><p>{esc(p[f'location_{lang}'])}</p></section></aside></div>
</div>"""
'''

CSS_BLOCK = r'''

/* application CV layout v58: linear reading order for ATS and fast human scan */
@media print {
  .profile-quantdev .pcv-application,
  .profile-quant .pcv-application,
  .profile-systems .pcv-application {
    padding: 10.5mm 12mm 10mm;
  }
  .pcv-application .pcv-header {
    padding-bottom: 3.2mm;
  }
  .pcv-application .pcv-header h1 {
    font-size: 22pt;
    line-height: 1.02;
  }
  .pcv-application .pcv-header h2 {
    margin-top: 1.4mm;
    font-size: 11.5pt;
    line-height: 1.2;
  }
  .pcv-application .pcv-contact {
    font-size: 8.6pt;
    line-height: 1.34;
  }
  .pcv-app-summary {
    margin: 3.1mm 0 3.4mm;
    font-size: 9.4pt;
    line-height: 1.36;
  }
  .pcv-app-section + .pcv-app-section {
    margin-top: 3.2mm;
  }
  .pcv-application .pcv-section-title {
    margin: 0 0 1.7mm;
    padding-bottom: .7mm;
    border-bottom: 1px solid #9b2438;
    font-size: 9.8pt;
    line-height: 1.1;
    letter-spacing: .02em;
    text-transform: uppercase;
  }
  .pcv-app-education p {
    display: flex;
    justify-content: space-between;
    gap: 5mm;
    margin: 0;
    font-size: 9pt;
    line-height: 1.25;
  }
  .pcv-app-education span {
    color: #4e4547;
    white-space: nowrap;
  }
  .pcv-app-entry {
    display: grid;
    grid-template-columns: 29mm 1fr;
    gap: 3mm;
    margin-bottom: 2.3mm;
    break-inside: avoid;
  }
  .pcv-app-date {
    color: #8d2638;
    font-size: 8.4pt;
    font-weight: 650;
    line-height: 1.25;
  }
  .pcv-app-entry h3,
  .pcv-app-project h3 {
    margin: 0;
    font-size: 9.5pt;
    line-height: 1.2;
  }
  .pcv-app-org {
    margin: .4mm 0 .7mm;
    color: #4e4547;
    font-size: 8.3pt;
    line-height: 1.2;
  }
  .pcv-app-entry ul {
    margin: .4mm 0 0 3.6mm;
    padding: 0;
  }
  .pcv-app-entry li {
    margin: 0 0 .45mm;
    font-size: 8.7pt;
    line-height: 1.28;
  }
  .pcv-app-project {
    margin-bottom: 1.9mm;
    break-inside: avoid;
  }
  .pcv-app-project p {
    margin: .55mm 0 0;
    color: #4e4547;
    font-size: 8.7pt;
    line-height: 1.28;
  }
  .pcv-app-project a {
    color: inherit;
    text-decoration: none;
  }
  .pcv-app-skill {
    display: grid;
    grid-template-columns: 34mm 1fr;
    gap: 3mm;
    margin-bottom: 1.1mm;
    font-size: 8.65pt;
    line-height: 1.27;
    break-inside: avoid;
  }
  .pcv-app-skill strong {
    font-size: 8.7pt;
  }
  .pcv-app-skill span {
    color: #4e4547;
  }
  .pcv-app-recognition {
    display: grid;
    grid-template-columns: 42mm 1fr;
    gap: 3mm;
    margin-bottom: 1.2mm;
    font-size: 8.55pt;
    line-height: 1.25;
    break-inside: avoid;
  }
  .pcv-app-recognition strong {
    font-size: 8.6pt;
  }
  .pcv-app-recognition span {
    color: #4e4547;
  }
}
'''


def patch_build_site() -> None:
    raw = BUILD_SITE.read_text(encoding="utf-8")
    start = raw.index("def print_cv(")
    end = raw.index("\ndef profile_page", start)
    updated = raw[:start] + NEW_PRINT_CV.strip() + "\n" + raw[end:]
    BUILD_SITE.write_text(updated, encoding="utf-8")


def patch_style() -> None:
    raw = STYLE.read_text(encoding="utf-8")
    marker = "/* application CV layout v58: linear reading order for ATS and fast human scan */"
    if marker in raw:
        start = raw.index(marker)
        # Keep the file deterministic on retries by replacing from the marker onward.
        raw = raw[:start].rstrip() + "\n"
    updated = (raw.rstrip() + CSS_BLOCK).rstrip() + "\n"
    STYLE.write_text(updated, encoding="utf-8")


def main() -> None:
    patch_build_site()
    patch_style()


if __name__ == "__main__":
    main()
