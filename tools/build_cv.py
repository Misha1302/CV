from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import fitz
from weasyprint import HTML

from build_site import (
    ROOT,
    canonical_sha256,
    esc,
    format_int,
    load_data,
    mcst_claim,
    name,
    proof,
    wist_claim,
)

ALLOWED_SCHEMES = {"https", "mailto"}
A4 = (595.28, 841.89)


def absolute_profile_url(data: dict, profile: dict) -> str:
    return data["site_url"] + profile["filename"]


def abs_link(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in ALLOWED_SCHEMES:
        raise RuntimeError(f"print link must be absolute: {url}")
    return url


def contacts_html(data: dict, lang: str) -> str:
    p = data["person"]
    location = p[f"location_{lang}"]
    return f"""<address class="contacts">
<span>{esc(location)}</span>
<a href="mailto:{esc(p['email'])}">{esc(p['email'])}</a>
<a href="{esc(abs_link(p['telegram_url']))}">{esc(p['telegram_label'])}</a>
<a href="{esc(abs_link(p['github_url']))}">{esc(p['github_label'])}</a>
</address>"""


def evidence_html(data: dict, profile: dict, lang: str) -> str:
    cards = []
    for key in profile["proof_keys"]:
        title, body = proof(data, key, lang)
        cards.append(f'<article class="proof"><h3>{esc(title)}</h3><p>{esc(body)}</p></article>')
    return f'<section aria-labelledby="evidence-heading"><h2 id="evidence-heading">{"КЛЮЧЕВЫЕ ДОКАЗАТЕЛЬСТВА" if lang == "ru" else "KEY EVIDENCE"}</h2><div class="proof-grid">{"".join(cards)}</div></section>'


def experience_html(data: dict, profile: dict, lang: str, ids: list[str] | None = None, continuation: bool = False) -> str:
    rows = []
    selected_ids = ids if ids is not None else profile["experience_ids"]
    for exp_id in selected_ids:
        exp = data["experiences"][exp_id]
        bullets = list(exp[f"bullets_{lang}"])
        if exp.get("claim_key") == "wist":
            bullets.append(wist_claim(data, lang, compact=True))
        elif exp.get("claim_key") == "mcst":
            bullets.append(mcst_claim(data, lang, compact=True))
        links = "".join(f'<a href="{esc(abs_link(item["url"]))}">{esc(item["label"])}</a>' for item in exp.get("links", []))
        rows.append(f"""<article class="entry"><div class="entry-head"><div><h3>{esc(exp[f'title_{lang}'])}</h3><p class="org">{esc(exp[f'org_{lang}'])}</p></div><time>{esc(exp[f'date_{lang}'])}</time></div><ul>{''.join(f'<li>{esc(b)}</li>' for b in bullets)}</ul>{f'<p class="links">{links}</p>' if links else ''}</article>""")
    if continuation:
        heading = "ОПЫТ — ПРОДОЛЖЕНИЕ" if lang == "ru" else "EXPERIENCE — CONTINUED"
        return f'<section class="experience-continuation" aria-labelledby="experience-cont-heading"><h2 id="experience-cont-heading">{heading}</h2>{"".join(rows)}</section>'
    return f'<section aria-labelledby="experience-heading"><h2 id="experience-heading">{"ОПЫТ" if lang == "ru" else "EXPERIENCE"}</h2>{"".join(rows)}</section>'


def projects_html(data: dict, profile: dict, lang: str) -> str:
    cards = []
    for project_id in profile["project_ids"]:
        project = data["projects"][project_id]
        links = []
        if project.get("repo"):
            links.append(f'<a href="{esc(abs_link(project["repo"]))}">GitHub</a>')
        if project.get("docs"):
            links.append(f'<a href="{esc(abs_link(project["docs"]))}">{"Документация" if lang == "ru" else "Documentation"}</a>')
        cards.append(f"""<article class="project"><h3>{esc(project['title'])}</h3><p class="org">{esc(project[f'type_{lang}'])}</p><ul>{''.join(f'<li>{esc(b)}</li>' for b in project[f'bullets_{lang}'])}</ul>{f'<p class="links">{" · ".join(links)}</p>' if links else ''}</article>""")
    return f'<section class="projects-section" aria-labelledby="projects-heading"><h2 id="projects-heading">{"ИЗБРАННЫЕ ПРОЕКТЫ" if lang == "ru" else "SELECTED PROJECTS"}</h2>{"".join(cards)}</section>'


def skills_html(profile: dict, lang: str) -> str:
    rows = "".join(f'<div class="skill"><h3>{esc(title)}</h3><p>{esc(body)}</p></div>' for title, body in profile["skills"])
    return f'<section aria-labelledby="skills-heading"><h2 id="skills-heading">{"НАВЫКИ" if lang == "ru" else "SKILLS"}</h2><div class="skills">{rows}</div></section>'


def education_html(data: dict, lang: str) -> str:
    p = data["person"]
    return f"""<section aria-labelledby="education-heading"><h2 id="education-heading">{'ОБРАЗОВАНИЕ И ДОСТИЖЕНИЯ' if lang == 'ru' else 'EDUCATION AND RECOGNITION'}</h2><div class="education"><p>{esc(p[f'education_{lang}'])}</p><p>{esc(p[f'achievement_{lang}'])}</p></div></section>"""


def source_note(data: dict, lang: str) -> str:
    e = data["evidence"]["wist_verification"]
    label = "Источник Wist evidence" if lang == "ru" else "Wist evidence source"
    return f'<footer><p>{label}: <a href="{esc(abs_link(e["source_url"]))}">{esc(e["source_commit"][:12])}</a> · canonical {canonical_sha256()[:12]} · {esc(data["release_version"])}</p></footer>'


def print_html(data: dict, profile_id: str, lang: str) -> str:
    profile = data["profiles"][profile_id][lang]
    two_pages = data["profiles"][profile_id]["pdf_pages"] == 2
    page_break_class = " page-two" if two_pages else ""
    source = canonical_sha256()
    compact_body = "9.5pt" if profile_id == "backend" else "9.35pt"
    compact_css = "" if two_pages else """
body { font-size: %s; line-height: 1.24; }
header { padding-bottom: 2.8mm; margin-bottom: 2.6mm; }
h1 { font-size: 21pt; margin-bottom: 1.3mm; }
.role { font-size: 11.8pt; }
.level { margin: .8mm 0 .6mm; font-size: 8.7pt; }
.tagline { margin-bottom: 1.2mm; font-size: 8.9pt; }
.contacts { font-size: 8.55pt; gap: .8mm 3mm; }
section { margin-top: 2.35mm; }
h2 { margin-bottom: 1.25mm; padding-bottom: .55mm; font-size: 9.25pt; }
h3 { font-size: 9.55pt; }
ul { margin-top: .8mm; }
li { margin-bottom: .45mm; }
.proof-grid { gap: 1.6mm; }
.proof { padding: 1.6mm 1.8mm; }
.proof h3 { font-size: 9.05pt; }
.proof p { margin-top: .55mm; font-size: 8.55pt; line-height: 1.22; }
.entry, .project { padding: .8mm 0 1mm; }
.org, time, .links { font-size: 8.5pt; }
.skill { grid-template-columns: 35mm 1fr; gap: 2mm; padding: .7mm 0; }
.skill h3, .skill p { font-size: 9.05pt; }
.education { gap: 3mm; }
footer { margin-top: 1.7mm; padding-top: .8mm; }
""" % compact_body
    css = f"""
@page {{ size: A4 portrait; margin: 10mm 13mm 10mm 13mm; @bottom-right {{ content: counter(page) " / " counter(pages); font: 8.5pt 'DejaVu Sans'; color: #666; }} }}
* {{ box-sizing: border-box; }}
html {{ font-family: 'DejaVu Sans', sans-serif; color: #161616; background: white; }}
body {{ margin: 0; font-size: {'10pt' if two_pages else '9.35pt'}; line-height: 1.34; }}
a {{ color: #163d73; text-decoration: none; }}
header {{ border-bottom: 1.2pt solid #252525; padding-bottom: 4.2mm; margin-bottom: 4mm; }}
h1 {{ font-size: 22pt; line-height: 1; margin: 0 0 2mm; letter-spacing: -.35pt; }}
.role {{ font-size: 12.5pt; line-height: 1.15; font-weight: 700; margin: 0; }}
.level {{ display: inline-block; margin: 1.2mm 0 1mm; font-size: 9pt; font-weight: 700; letter-spacing: .25pt; text-transform: uppercase; }}
.tagline {{ margin: 0 0 2.2mm; font-size: 9.4pt; font-weight: 600; }}
.contacts {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4mm; font-style: normal; font-size: 8.8pt; }}
.contacts span, .contacts a {{ white-space: nowrap; }}
.summary {{ margin: 3.1mm 0 0; font-size: 10pt; line-height: 1.38; }}
section {{ margin-top: 3.4mm; break-inside: auto; }}
h2 {{ margin: 0 0 2mm; padding-bottom: .9mm; border-bottom: .7pt solid #7e8791; font-size: 9.7pt; line-height: 1.1; letter-spacing: .65pt; color: #2c3641; }}
h3 {{ margin: 0; font-size: 10pt; line-height: 1.22; }}
p {{ margin: 0; }}
ul {{ margin: 1.2mm 0 0; padding-left: 4.4mm; }}
li {{ margin: 0 0 .85mm; }}
.proof-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm; }}
.proof {{ border: .7pt solid #9ca5ae; border-radius: 2mm; padding: 2.5mm 2.6mm; break-inside: avoid; }}
.proof h3 {{ font-size: 9.5pt; }}
.proof p {{ margin-top: 1mm; font-size: 8.8pt; line-height: 1.3; }}
.entry, .project {{ break-inside: avoid; padding: 1.5mm 0 1.8mm; border-bottom: .45pt solid #d0d3d6; }}
.entry-head {{ display: flex; justify-content: space-between; gap: 4mm; align-items: baseline; }}
time {{ font-size: 8.7pt; white-space: nowrap; font-weight: 600; }}
.org {{ margin-top: .5mm; color: #4d5660; font-size: 8.7pt; }}
.links {{ margin-top: 1mm; font-size: 8.7pt; }}
.project h3 {{ font-size: 10.1pt; }}
.skills {{ border-top: .45pt solid #d0d3d6; }}
.skill {{ display: grid; grid-template-columns: 40mm 1fr; gap: 3mm; padding: 1.2mm 0; border-bottom: .45pt solid #d0d3d6; break-inside: avoid; }}
.skill h3 {{ font-size: 9pt; }}
.skill p {{ font-size: 9pt; }}
.education {{ display: grid; grid-template-columns: 1fr 1.35fr; gap: 5mm; }}
.education p {{ break-inside: avoid; }}
.page-two {{ break-before: page; padding-top: 0; }}
footer {{ margin-top: 3mm; padding-top: 1.5mm; border-top: .45pt solid #b8bec5; font-size: 8.5pt; color: #555; }}
footer p {{ margin: 0; }}
{compact_css}
"""
    if two_pages:
        first_experience = experience_html(data, profile, lang, profile["experience_ids"][:2])
        continued_experience = experience_html(data, profile, lang, profile["experience_ids"][2:], continuation=True)
    else:
        first_experience = experience_html(data, profile, lang)
        continued_experience = ""
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{esc(profile['title'])}</title><meta name="author" content="{esc(name(data, lang))}"><meta name="description" content="{esc(profile['description'])}"><meta name="keywords" content="{esc(profile['tagline'])}"><meta name="dcterms.created" content="2026-08-03"><meta name="cv:source-sha256" content="{source}"><style>{css}</style></head><body><main>
<header><h1>{esc(name(data, lang))}</h1><p class="role">{esc(profile['role'])}</p><p class="level">{esc(profile['level'])}</p><p class="tagline">{esc(profile['tagline'])}</p>{contacts_html(data, lang)}</header>
<section aria-labelledby="profile-heading"><h2 id="profile-heading">{'ПРОФИЛЬ' if lang == 'ru' else 'PROFILE'}</h2><p>{esc(profile['summary'])}</p></section>
{evidence_html(data, profile, lang)}
{first_experience}
<div class="continuation{page_break_class}">{continued_experience}{projects_html(data, profile, lang)}{skills_html(profile, lang)}{education_html(data, lang)}{source_note(data, lang) if two_pages else ''}</div>
</main></body></html>"""


def font_sizes(page: fitz.Page) -> list[float]:
    return [
        float(span["size"])
        for block in page.get_text("dict").get("blocks", [])
        for line in block.get("lines", [])
        for span in line.get("spans", [])
        if span.get("text", "").strip()
    ]


def basic_metrics(path: Path, expected_pages: int) -> dict[str, object]:
    with fitz.open(path) as doc:
        if doc.page_count != expected_pages:
            raise RuntimeError(f"{path.name}: expected {expected_pages} pages, got {doc.page_count}")
        page_metrics = []
        all_sizes: list[float] = []
        links = []
        for number, page in enumerate(doc, start=1):
            if abs(page.rect.width - A4[0]) > 3 or abs(page.rect.height - A4[1]) > 3:
                raise RuntimeError(f"{path.name}: page {number}: not A4")
            text = page.get_text("text")
            sizes = font_sizes(page)
            all_sizes += sizes
            blocks = [b for b in page.get_text("blocks") if str(b[4]).strip()]
            bottom = max((float(b[3]) for b in blocks), default=0.0)
            page_metrics.append({"page": number, "text_chars": len(text), "last_text_y": round(bottom, 2), "bottom_whitespace": round(page.rect.height - bottom, 2)})
            for annotation in page.get_links():
                uri = annotation.get("uri")
                if not uri:
                    raise RuntimeError(f"{path.name}: page {number}: non-URI link: {annotation}")
                if urlparse(uri).scheme not in ALLOWED_SCHEMES:
                    raise RuntimeError(f"{path.name}: page {number}: invalid link: {uri}")
                links.append({"page": number, "uri": uri})
        if not all_sizes or min(all_sizes) < 8.45:
            raise RuntimeError(f"{path.name}: min font too small: {min(all_sizes) if all_sizes else None}")
        return {
            "file": path.name,
            "pages": doc.page_count,
            "page_metrics": page_metrics,
            "min_font_pt": round(min(all_sizes), 2),
            "median_font_pt": round(statistics.median(all_sizes), 2),
            "links": links,
            "sha256": __import__("hashlib").sha256(path.read_bytes()).hexdigest(),
        }


def render_evidence(path: Path, evidence_dir: Path) -> None:
    with fitz.open(path) as doc:
        for index, page in enumerate(doc):
            pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
            png = evidence_dir / f"{path.stem}-page-{index + 1}.png"
            pix.save(png)
            # Grayscale copy is a real independent render surface.
            gray = fitz.Pixmap(fitz.csGRAY, pix)
            gray.save(evidence_dir / f"{path.stem}-page-{index + 1}-gray.png")
        thumb = doc[0].get_pixmap(matrix=fitz.Matrix(.45, .45), alpha=False)
        thumb.save(evidence_dir / f"{path.stem}-thumbnail.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "pdf")
    parser.add_argument("--evidence-dir", type=Path, default=ROOT / "evidence" / "pdf")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    data = load_data()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.evidence_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("SOURCE_DATE_EPOCH", "1785715200")  # 2026-08-03T00:00:00Z
    report = []
    for profile_id in data["profile_order"]:
        expected_pages = int(data["profiles"][profile_id]["pdf_pages"])
        for lang in ("ru", "en"):
            profile = data["profiles"][profile_id][lang]
            path = args.output_dir / profile["pdf"]
            html = print_html(data, profile_id, lang)
            (args.evidence_dir / f"{path.stem}.print.html").write_text(html, encoding="utf-8")
            HTML(string=html, base_url=data["site_url"]).write_pdf(
                path,
                pdf_variant="pdf/ua-1",
                pdf_tags=True,
                full_fonts=True,
                srgb=True,
                custom_metadata=True,
                pdf_identifier=canonical_sha256(),
            )
            metrics = basic_metrics(path, expected_pages)
            render_evidence(path, args.evidence_dir)
            text_path = args.evidence_dir / f"{path.stem}.pdftotext.txt"
            layout_path = args.evidence_dir / f"{path.stem}.pdftotext-layout.txt"
            subprocess.run(["pdftotext", str(path), str(text_path)], check=True)
            subprocess.run(["pdftotext", "-layout", str(path), str(layout_path)], check=True)
            report.append(metrics | {"profile": profile_id, "lang": lang})
    output = {"canonical_source_sha256": canonical_sha256(), "pdfs": report}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
