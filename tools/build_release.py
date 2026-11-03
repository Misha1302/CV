#!/usr/bin/env python3
"""Generate RU/EN application PDF, DOCX and Markdown from data/site.json."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
import fitz
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Mm, Pt, RGBColor
from weasyprint import HTML

ROOT=Path(__file__).resolve().parents[1]
ZIP_NAME="Mikhail_Razakov_CV_Complete_Package_2026-11-03.zip"
KINDS=("ats","lead","runtime")
LANGS=("ru","en")

def load():
    return json.loads((ROOT/"data/site.json").read_text(encoding="utf-8"))

def record(site,kind,lang):
    release=site["application_cvs"]
    v=release["variants"][kind]
    return v[lang],release["experience"][lang],v["basename"][lang]

def contact(site,lang):
    p=site["person"]
    return p["name_"+lang],p["location_"+lang],p["email"],p["telegram"],p["github"]

def url_for(site,project,lang):
    p=site["projects"][project["id"]]
    return p.get("repo") or site["site_url"]+p["case_"+lang]

def words(lang):
    return (("Профиль","Технологии","Опыт","Проекты","Образование и достижения") if lang=="ru"
         else ("Profile","Technical skills","Experience","Projects","Education and recognition"))

def markdown(site,kind,lang):
    cv,experiences,_=record(site,kind,lang)
    name,loc,email,tg,gh=contact(site,lang)
    profile,skills,exp_label,project_label,education=words(lang)
    parts=[
        "# "+name,"","**"+cv["role"]+"**","",
        f"{loc} · [{email}](mailto:{email}) · [Telegram]({tg}) · [GitHub]({gh})","",
        "## "+profile,"",cv["summary"],"","## "+skills,"",
    ]
    parts.extend("- "+x for x in cv["skills"])
    parts+=["","## "+exp_label,""]
    for item in experiences:
        parts.extend([f"**{item['title']} · {item['date']}**","",item["text"],""])
    parts+=["## "+project_label,""]
    for item in cv["projects"]:
        parts.extend([f"**[{item['title']}]({url_for(site,item,lang)})**","",item["text"],""])
    parts+=["## "+education,"",cv["education"],"",cv["recognition"],""]
    return "\n".join(parts).strip()+"\n"

def add_hyperlink(paragraph,text,url):
    rid=paragraph.part.relate_to(
        url,"http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    h=OxmlElement("w:hyperlink")
    h.set(qn("r:id"),rid)
    r=OxmlElement("w:r")
    pr=OxmlElement("w:rPr")
    color=OxmlElement("w:color");color.set(qn("w:val"),"25536A");pr.append(color)
    underline=OxmlElement("w:u");underline.set(qn("w:val"),"single");pr.append(underline)
    r.append(pr)
    t=OxmlElement("w:t");t.text=text;r.append(t);h.append(r)
    paragraph._p.append(h)

def docx(site,kind,lang,path):
    cv,experiences,_=record(site,kind,lang)
    name,loc,email,tg,gh=contact(site,lang)
    profile,skills,exp_label,project_label,education=words(lang)
    d=Document();sec=d.sections[0]
    sec.page_width=Cm(21);sec.page_height=Cm(29.7)
    sec.top_margin=Mm(10);sec.bottom_margin=Mm(10)
    sec.left_margin=Mm(14);sec.right_margin=Mm(14)
    normal=d.styles["Normal"]
    normal.font.name="Arial";normal.font.size=Pt(9.0)
    normal.paragraph_format.space_after=Pt(2)
    normal.paragraph_format.line_spacing=1.10
    h2=d.styles["Heading 2"];h2.font.name="Arial";h2.font.size=Pt(10.2)
    h2.font.color.rgb=RGBColor(25,56,69)
    h2.paragraph_format.space_before=Pt(5)
    h2.paragraph_format.space_after=Pt(1.5)
    p=d.add_paragraph();p.paragraph_format.space_after=Pt(0)
    n=p.add_run(name);n.bold=True;n.font.size=Pt(16.5)
    p=d.add_paragraph();p.paragraph_format.space_after=Pt(2)
    n=p.add_run(cv["role"]);n.bold=True;n.font.size=Pt(10)
    p=d.add_paragraph(loc+" · ");p.paragraph_format.space_after=Pt(3)
    add_hyperlink(p,email,"mailto:"+email)
    p.add_run(" · ");add_hyperlink(p,"Telegram",tg)
    p.add_run(" · ");add_hyperlink(p,"GitHub",gh)
    d.add_heading(profile,2);d.add_paragraph(cv["summary"])
    d.add_heading(skills,2)
    for x in cv["skills"]:
        p=d.add_paragraph(x);p.paragraph_format.left_indent=Mm(2)
    d.add_heading(exp_label,2)
    for item in experiences:
        p=d.add_paragraph()
        p.paragraph_format.space_before=Pt(2)
        r=p.add_run(item["title"]+"  |  "+item["date"]);r.bold=True
        p=d.add_paragraph(item["text"]);p.paragraph_format.left_indent=Mm(2)
    d.add_heading(project_label,2)
    for item in cv["projects"]:
        p=d.add_paragraph();p.paragraph_format.space_before=Pt(2)
        add_hyperlink(p,item["title"],url_for(site,item,lang))
        p=d.add_paragraph(item["text"]);p.paragraph_format.left_indent=Mm(2)
    d.add_heading(education,2)
    d.add_paragraph(cv["education"])
    d.add_paragraph(cv["recognition"])
    d.core_properties.author=name
    d.core_properties.title=name+" — "+cv["role"]
    d.save(path)
    # python-docx uses noncanonical ZIP timestamps for individual entries.
    # Freeze them for stable hashes and reproducible GitHub Action outputs.
    with ZipFile(path, "r") as original:
        entries = [(i.filename, original.read(i.filename)) for i in original.infolist()]
    temp = path.with_suffix(".docx.tmp")
    with ZipFile(temp, "w") as normalized:
        for name, content in entries:
            info = ZipInfo(name, date_time=(2026, 11, 3, 12, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            normalized.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    temp.replace(path)

def pdf(site,kind,lang,path):
    cv,experiences,_=record(site,kind,lang)
    name,loc,email,tg,gh=contact(site,lang)
    profile,skills,exp_label,project_label,education=words(lang)
    e=html.escape
    rows="".join(f"<li>{e(x)}</li>" for x in cv["skills"])
    exps="".join(
        f"<article><h3>{e(item['title'])}<span>{e(item['date'])}</span></h3><p>{e(item['text'])}</p></article>"
        for item in experiences)
    projects="".join(
        f"<article><h3><a href='{e(url_for(site,item,lang),quote=True)}'>{e(item['title'])}</a></h3><p>{e(item['text'])}</p></article>"
        for item in cv["projects"])
    page=f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
    @page {{size:A4;margin:10mm 14mm;}}
    html {{font-family:'DejaVu Sans','Liberation Sans',sans-serif;font-size:8.95pt;color:#1e2931;}}
    body {{margin:0;line-height:1.25;}}
    h1 {{font-size:17pt;letter-spacing:-.025em;margin:0;}}
    .role {{font-size:10pt;font-weight:bold;margin:1mm 0 1.5mm;color:#234457;}}
    .contact {{font-size:8.35pt;margin:0 0 3mm;}}
    a {{color:#255670;text-decoration:none;}}
    h2 {{font-size:9.3pt;color:#234457;text-transform:uppercase;letter-spacing:.02em;
       border-bottom:.4pt solid #adc0c8;padding-bottom:.6mm;margin:2.6mm 0 1.1mm;}}
    p {{margin:0 0 1.4mm;}}
    ul {{margin:0 0 1.4mm;padding-left:4mm;}}
    li {{margin:0 0 .6mm;}}
    article {{break-inside:avoid;margin:0 0 1.6mm;}}
    h3 {{font-size:8.95pt;margin:0 0 .55mm;}}
    h3 span {{float:right;font-weight:normal;font-size:8.6pt;color:#64737b;}}
    article p {{margin:0;}}
    </style></head><body>
    <h1>{e(name)}</h1><p class="role">{e(cv['role'])}</p>
    <p class="contact">{e(loc)} · <a href="mailto:{e(email)}">{e(email)}</a>
    · <a href="{e(tg)}">Telegram</a> · <a href="{e(gh)}">GitHub</a></p>
    <h2>{e(profile)}</h2><p>{e(cv['summary'])}</p>
    <h2>{e(skills)}</h2><ul>{rows}</ul>
    <h2>{e(exp_label)}</h2>{exps}
    <h2>{e(project_label)}</h2>{projects}
    <h2>{e(education)}</h2><p>{e(cv['education'])}</p><p>{e(cv['recognition'])}</p>
    </body></html>"""
    HTML(string=page,base_url=str(ROOT)).write_pdf(str(path))

PUBLIC_NOTE="""# Public claim boundaries / Открытые границы доказательств

This is a sanitized public research summary. It intentionally excludes internal project paths, private employers' documents, operational hosts and application credentials.

- Employment: ISP RAS / SharpChecker and MCST / LLVM dates and responsibility are recorded from the candidate and available evidence.
- Commercial experience: approximately one year in aggregate is candidate-attested, not independently verified as a single continuous .NET position.
- VpnMediator: current operation and user numbers are candidate-reported. Architecture is described from source inspection. Python Telegram bot is distinct from the ASP.NET Core service.
- UniversalToolchain: a repository test manifest is not proof that all tests were executed again during resume preparation.
- TuringSquare-LMS: ongoing work, partly AI-agent implemented; payments evaluated in sandbox, not production.
- Quark2: experimental CLR internals and microbenchmarks, not general production speedup.
- Competition results and conference claims have mixed public and author-supplied evidence, recorded in the knowledge layer.
"""

def write_readmes(site,out):
    rows=["# Mikhail Razakov — CV / Резюме","",
          "Три специализации, русская и английская версии, три синхронизированных формата.","",
          "| Аудитория | PDF RU | PDF EN | DOCX RU | DOCX EN | Markdown RU | Markdown EN |",
          "|---|---|---|---|---|---|---|"]
    for key in KINDS:
        v=site["application_cvs"]["variants"][key]
        ru=v["basename"]["ru"];en=v["basename"]["en"]
        rows.append(f"| {v['audience_ru']} | [PDF]({ru}.pdf) | [PDF]({en}.pdf) | [DOCX]({ru}.docx) | [DOCX]({en}.docx) | [MD]({ru}.md) | [MD]({en}.md) |")
    rows+=["","Для первичного отклика — Backend ATS; для руководителя разработки — Tech Lead; для CLR/LLVM-команд — Runtime/Compiler.",
          "Кандидат подтверждает суммарный коммерческий стаж и эксплуатацию VpnMediator. Часть архитектурных утверждений подтверждена исходниками; детали и границы приведены в открытой сводке.",
          "[Evidence boundaries](04_Public_Evidence_Boundaries.md) · [CV website](https://misha1302.github.io/CV/) · [Engineering profile](https://misha1302.github.io/CV/ru-engineering.html)","",
          "[Complete CV ZIP]("+ZIP_NAME+")",""]
    (out/"README.md").write_text("\n".join(rows),encoding="utf-8")
    (out/"00_README_Choose_Version.md").write_text(
        "# Выбор версии CV / Choosing a version\n\n"
        "01_Backend_ATS — основной CV для HR и ATS.\n\n"
        "02_Tech_Lead — инженерные решения, платежные состояния и границы ответственности.\n\n"
        "03_Runtime_Compiler — CLR, CIL, LLVM, static analysis и производительность.\n\n"
        "Суффикс _EN обозначает английский перевод с тем же набором проверяемых фактов.\n",encoding="utf-8")
    (out/"04_Public_Evidence_Boundaries.md").write_text(PUBLIC_NOTE,encoding="utf-8")

def archive(out):
    files=sorted(p for p in out.iterdir() if p.is_file()
       and p.name not in {ZIP_NAME,"MANIFEST.sha256","04_Evidence_Research_and_Review.md","05_Outreach_Messages.md"})
    (out/"MANIFEST.sha256").write_text(
       "".join(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name+"\n" for p in files),
       encoding="utf-8")
    with ZipFile(out/ZIP_NAME,"w") as z:
        for p in files+[out/"MANIFEST.sha256"]:
            inf=ZipInfo(p.name,date_time=(2026,11,3,12,0,0))
            inf.external_attr=0o644<<16
            inf.compress_type=ZIP_DEFLATED
            z.writestr(inf,p.read_bytes(),compress_type=ZIP_DEFLATED,compresslevel=9)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output-dir",type=Path)
    ap.add_argument("--skip-archive",action="store_true")
    args=ap.parse_args()
    site=load()
    out=args.output_dir or ROOT/site["application_cvs"]["release_dir"]
    out.mkdir(parents=True,exist_ok=True)
    for kind in KINDS:
        for lang in LANGS:
            _,_,stem=record(site,kind,lang)
            (out/(stem+".md")).write_text(markdown(site,kind,lang),encoding="utf-8")
            docx(site,kind,lang,out/(stem+".docx"))
            pdf(site,kind,lang,out/(stem+".pdf"))
    write_readmes(site,out)
    if not args.skip_archive:
        archive(out)
    print(json.dumps({"status":"built","formats":["md","docx","pdf"],"variants":6,"dir":str(out)}))

if __name__=="__main__":
    main()
