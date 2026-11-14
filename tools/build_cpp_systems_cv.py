"""Canonical one-column ATS exports for selected specialized CV profiles.

The separate website retains its editorial layout. PDF, DOCX and Markdown
are rendered from data/site.json -> specialized profile copy.
Do not copy/edit completed artifacts in place.
"""
from __future__ import annotations

import html
from io import BytesIO
from zipfile import ZipFile, ZipInfo
from pathlib import Path
from typing import Any

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Mm, Pt, RGBColor
from weasyprint import HTML

PROFILE_KEY = "systems"
SUPPORTED_PROFILES = {
    "systems": (["globaliv", "psform", "codegen"], "systems_project_copy"),
    "program_analysis": (["deref", "globaliv", "psform"], "project_summaries"),
    "general": (["wist", "globaliv", "codegen"], "project_summaries"),
    "compiler_backend": (["codegen", "globaliv", "wist"], "project_summaries"),
    "quantdev": (["psform", "parallel_channel_tracker", "globaliv"], "project_summaries"),
    "quant": (["parallel_channel_tracker", "wist", "psform"], "project_summaries"),
}


def h(value: Any) -> str:
    return html.escape(str(value), quote=True)


def snapshot(data: dict[str, Any], lang: str, profile_key: str = PROFILE_KEY) -> dict[str, Any]:
    if lang not in ("ru", "en"):
        raise ValueError(lang)
    if profile_key not in SUPPORTED_PROFILES:
        raise ValueError(f"Unsupported ATS specialist: {profile_key}")
    profile = data["profiles"][profile_key][lang]
    expected_ids, copy_key = SUPPORTED_PROFILES[profile_key]
    project_copy = profile[copy_key]
    ids = profile["project_ids"]
    if ids != expected_ids:
        raise ValueError(f"{profile_key} project selection changed unexpectedly: {ids}")
    for project_id in ids:
        item = project_copy[project_id]
        if not all(item.get(key) for key in ("solution", "result")):
            raise ValueError(f"Unclear project proof in {lang}: {project_id}")
        if project_id not in data["projects"]:
            entry = profile.get("project_entries", {}).get(project_id, {})
            if (entry.get("privacy_status") != "private_unpublished"
                    or item.get("source_url") or item.get("privacy_status") != "private_unpublished"
                    or not entry.get("title")):
                raise ValueError(f"Unpublished private case needs no URL and explicit privacy boundaries: {project_id}")
        elif not item.get("source_url"):
            raise ValueError(f"Public case needs evidence URL: {project_id}")
    expected_recognition = 4 if profile_key == "general" else 3
    if len(profile["experience"]) != 2 or len(profile["recognition"]) != expected_recognition:
        raise ValueError(f"Missing owned experience/recognition for {profile_key} CV")
    return {
        "profile_key": profile_key,
        "lang": lang,
        "person": data["person"],
        "name": data["person"]["name_" + lang],
        "location": data["person"]["location_" + lang],
        "education": data["person"]["education_" + lang],
        "profile": profile,
        "projects": [
            {
                "id": pid,
                "name": (data["projects"][pid]["title"] if pid in data["projects"]
                         else profile["project_entries"][pid]["title"]),
                **project_copy[pid],
            }
            for pid in ids
        ],
    }


def sections(lang: str) -> dict[str, str]:
    return ({
        "summary": "Профиль", "skills": "Технологии",
        "experience": "Опыт", "projects": "Инженерные проекты",
        "education": "Образование", "recognition": "Достижения",
        "recording": "Запись доклада",
    } if lang == "ru" else {
        "summary": "Profile", "skills": "Technical skills",
        "experience": "Experience", "projects": "Engineering projects",
        "education": "Education", "recognition": "Recognition",
        "recording": "Talk recording",
    })


def markdown(data: dict[str, Any], lang: str, profile_key: str = PROFILE_KEY) -> str:
    m = snapshot(data, lang, profile_key)
    p = m["profile"]
    person = m["person"]
    labels = sections(lang)
    lines = [
        "# " + m["name"], "", "**" + p["role"] + "**", "",
        f'{m["location"]} · [{person["email"]}](mailto:{person["email"]}) · '
        f'[Telegram]({person["telegram"]}) · [GitHub]({person["github"]})',
        "", "## " + labels["summary"], "", p["summary"], "",
        "## " + labels["skills"], "",
    ]
    lines.extend(f'- **{title}:** {body}' for title, body in p["skills"])
    lines += ["", "## " + labels["experience"], ""]
    for item in p["experience"]:
        lines += [f'**{item["title"]} · {item["date"]}**', ""]
        lines.extend("- " + bullet for bullet in item["bullets"])
        lines.append("")
    lines += ["## " + labels["projects"], ""]
    for project in m["projects"]:
        url = project.get("source_url")
        project_title = f'[{project["name"]}]({url})' if url else project["name"]
        lines += [
            f'**{project_title}**', "",
            project["solution"] + " " + project["result"], "",
        ]
    lines += ["## " + labels["education"], "", m["education"], "",
              "## " + labels["recognition"], ""]
    for item in p["recognition"]:
        year, title, body = item[:3]
        suffix = f' [{labels["recording"]}]({item[3]})' if len(item) == 4 else ""
        lines.append(f'- **{year} — {title}:** {body}{suffix}')
    return "\n".join(lines).rstrip() + "\n"


def html_for_pdf(data: dict[str, Any], lang: str, profile_key: str = PROFILE_KEY) -> str:
    m = snapshot(data, lang, profile_key)
    p = m["profile"]
    person = m["person"]
    labels = sections(lang)

    skills = "".join(
        f'<p class="skill"><strong>{h(title)}:</strong> {h(body)}</p>'
        for title, body in p["skills"]
    )
    experience = "".join(
        '<article class="experience"><h3>'
        + h(item["title"]) + f' <span class="date">· {h(item["date"])}</span></h3>'
        + "".join(f'<p class="bullet">• {h(bullet)}</p>' for bullet in item["bullets"])
        + "</article>"
        for item in p["experience"]
    )
    project_html = []
    for item in m["projects"]:
        url = item.get("source_url")
        heading = (f'<a href="{h(url)}">{h(item["name"])}</a>'
                   if url else h(item["name"]))
        project_html.append(
            f'<article class="project"><h3>{heading}</h3>'
            f'<p>{h(item["solution"])} {h(item["result"])}</p></article>'
        )
    projects = "".join(project_html)
    recognition = "".join(
        f'<p><strong>{h(item[0])} · {h(item[1])}:</strong> {h(item[2])}'
        + (f' — <a href="{h(item[3])}">{h(labels["recording"])}</a>' if len(item) == 4 else "")
        + "</p>"
        for item in p["recognition"]
    )

    # Flat, reading-order-preserving structure; no CSS columns/floats/tables.
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 12mm 14mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif;
  font-size: 9.65pt; line-height: 1.27; color: #202932; }}
h1 {{ font-size: 17pt; line-height: 1.12; margin: 0; letter-spacing: -.1pt; }}
.role {{ font-size: 10.2pt; line-height: 1.22; font-weight: 700;
  color: #244b5f; margin: 3pt 0 3pt; }}
.contact {{ font-size: 8.85pt; line-height: 1.18; margin: 3pt 0 8pt; }}
h2 {{ font-size: 10pt; font-weight: 750; text-transform: uppercase;
  margin: 8pt 0 3pt; color: #244b5f;
  border-bottom: .5pt solid #a4b9c4; padding-bottom: 1.3pt; }}
h3 {{ font-size: 9.65pt; margin: 4pt 0 1pt; line-height: 1.22; }}
p {{ margin: 0 0 2.2pt; }}
strong {{ font-weight: 700; }}
a {{ color: #245875; text-decoration: none; }}
.date {{ font-size: 8.8pt; font-weight: 400; color: #4b5963; }}
section {{ margin: 0; }}
article {{ break-inside: avoid; }}
.experience {{ margin-bottom: 3pt; }}
.project {{ margin-bottom: 3pt; }}
.bullet {{ padding-left: 10pt; text-indent: -10pt; }}
</style></head><body>
<header><h1>{h(m["name"])}</h1><p class="role">{h(p["role"])}</p>
<p class="contact">{h(m["location"])} ·
 <a href="mailto:{h(person["email"])}">{h(person["email"])}</a> ·
 <a href="{h(person["telegram"])}">Telegram</a> ·
 <a href="{h(person["github"])}">GitHub</a></p></header>
<section><h2>{h(labels["summary"])}</h2><p>{h(p["summary"])}</p></section>
<section><h2>{h(labels["skills"])}</h2>{skills}</section>
<section><h2>{h(labels["experience"])}</h2>{experience}</section>
<section><h2>{h(labels["projects"])}</h2>{projects}</section>
<section><h2>{h(labels["education"])}</h2><p>{h(m["education"])}</p></section>
<section><h2>{h(labels["recognition"])}</h2>{recognition}</section>
</body></html>"""


def hyperlink(paragraph, label: str, url: str) -> None:
    rid = paragraph.part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    node = OxmlElement("w:hyperlink")
    node.set(qn("r:id"), rid)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "245875")
    props.append(color)
    under = OxmlElement("w:u")
    under.set(qn("w:val"), "single")
    props.append(under)
    run.append(props)
    text = OxmlElement("w:t")
    text.text = label
    run.append(text)
    node.append(run)
    paragraph._p.append(node)


def normalize_docx_container(path: Path) -> None:
    """Pin ZIP entry timestamps without rewriting Word XML or its links.

    python-docx inserts a fresh current timestamp into every ZIP directory
    member on each save. Fixing only container metadata makes the same
    canonical data generate byte-identical DOCX in one toolchain.
    """
    memory = BytesIO()
    with ZipFile(path, "r") as src, ZipFile(memory, "w") as out:
        for item in src.infolist():
            entry = ZipInfo(item.filename, date_time=(2026, 11, 13, 12, 0, 0))
            entry.compress_type = item.compress_type
            entry.external_attr = item.external_attr
            entry.internal_attr = item.internal_attr
            entry.create_system = item.create_system
            entry.comment = item.comment
            out.writestr(entry, src.read(item.filename), compress_type=entry.compress_type)
    path.write_bytes(memory.getvalue())


def save_docx(data: dict[str, Any], lang: str, path: Path, profile_key: str = PROFILE_KEY) -> None:
    m = snapshot(data, lang, profile_key)
    p = m["profile"]
    person = m["person"]
    labels = sections(lang)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Mm(11), Mm(10)
    sec.left_margin, sec.right_margin = Mm(14), Mm(14)

    normal = doc.styles["Normal"]
    normal.font.name = "DejaVu Sans"
    normal.font.size = Pt(9.6)
    normal.font.color.rgb = RGBColor(32, 41, 50)
    normal.paragraph_format.line_spacing = 1.14
    normal.paragraph_format.space_after = Pt(2)

    heading2 = doc.styles["Heading 2"]
    heading2.font.name = "DejaVu Sans"
    heading2.font.size = Pt(10)
    heading2.font.bold = True
    heading2.font.color.rgb = RGBColor(36, 75, 95)
    heading2.paragraph_format.space_before = Pt(6)
    heading2.paragraph_format.space_after = Pt(2)
    head = doc.add_paragraph()
    head.paragraph_format.space_after = Pt(0)
    run = head.add_run(m["name"])
    run.bold = True
    run.font.size = Pt(17)
    role = doc.add_paragraph()
    role.paragraph_format.space_after = Pt(2)
    r = role.add_run(p["role"])
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(36, 75, 95)

    contact = doc.add_paragraph()
    contact.paragraph_format.space_after = Pt(3)
    contact.add_run(m["location"] + " · ")
    hyperlink(contact, person["email"], "mailto:" + person["email"])
    contact.add_run(" · ")
    hyperlink(contact, "Telegram", person["telegram"])
    contact.add_run(" · ")
    hyperlink(contact, "GitHub", person["github"])

    doc.add_heading(labels["summary"], level=2)
    doc.add_paragraph(p["summary"])
    doc.add_heading(labels["skills"], level=2)
    for title, body in p["skills"]:
        q = doc.add_paragraph()
        q.add_run(title + ": ").bold = True
        q.add_run(body)

    doc.add_heading(labels["experience"], level=2)
    for item in p["experience"]:
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(1)
        q.add_run(item["title"]).bold = True
        q.add_run(" · " + item["date"])
        for bullet in item["bullets"]:
            bullet_par = doc.add_paragraph("• " + bullet)
            bullet_par.paragraph_format.left_indent = Mm(3)
            bullet_par.paragraph_format.first_line_indent = Mm(-3)
            bullet_par.paragraph_format.space_after = Pt(1)

    doc.add_heading(labels["projects"], level=2)
    for item in m["projects"]:
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(1)
        if item.get("source_url"):
            hyperlink(q, item["name"], item["source_url"])
        else:
            q.add_run(item["name"]).bold = True
        doc.add_paragraph(item["solution"] + " " + item["result"])

    doc.add_heading(labels["education"], level=2)
    doc.add_paragraph(m["education"])
    doc.add_heading(labels["recognition"], level=2)
    for item in p["recognition"]:
        q = doc.add_paragraph()
        q.add_run(item[0] + " · " + item[1] + ": ").bold = True
        q.add_run(item[2])
        if len(item) == 4:
            q.add_run(" — ")
            hyperlink(q, labels["recording"], item[3])

    doc.core_properties.title = p["role"]
    doc.core_properties.subject = {
        "systems": "C++ / Systems Engineer CV",
        "program_analysis": "Static Analysis / Program Analysis Engineer CV",
        "general": "Compiler Infrastructure / Language Tooling Engineer CV",
        "compiler_backend": "Compiler Backend / Code Generation Engineer CV",
        "quantdev": "Quant Developer / Research Software Engineer CV",
        "quant": "Quantitative Research Candidate CV",
    }[profile_key]
    doc.core_properties.author = m["name"]
    doc.save(path)
    normalize_docx_container(path)


def render_files(data: dict[str, Any], lang: str, out_dir: Path, profile_key: str = PROFILE_KEY) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    model = snapshot(data, lang, profile_key)
    stem = Path(model["profile"]["pdf"]).stem
    pdf = out_dir / (stem + ".pdf")
    md = out_dir / (stem + ".md")
    docx = out_dir / (stem + ".docx")
    md.write_text(markdown(data, lang, profile_key), encoding="utf-8")
    save_docx(data, lang, docx, profile_key)
    HTML(string=html_for_pdf(data, lang, profile_key)).write_pdf(str(pdf))
    return {"pdf": pdf, "docx": docx, "md": md}
