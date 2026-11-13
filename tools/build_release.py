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
    return v[lang],v.get("experience",release["experience"])[lang],v["basename"][lang]

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
    recognition = cv["recognition"]
    if cv.get("recognition_link"):
        link = cv["recognition_link"]
        recognition += f" — [{link['label']}]({link['url']})"
    parts+=["## "+education,"",cv["education"],"",recognition,""]
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
    spacious = kind in ("lead", "runtime")
    normal.font.name="Arial";normal.font.size=Pt(10.3 if kind=="lead" else (10.0 if spacious else 9.5))
    normal.paragraph_format.space_after=Pt(3.2 if spacious else 2)
    normal.paragraph_format.line_spacing=1.16 if spacious else 1.10
    h2=d.styles["Heading 2"];h2.font.name="Arial";h2.font.size=Pt(11.2 if kind=="lead" else (11.0 if spacious else 10.2))
    h2.font.color.rgb=RGBColor(25,56,69)
    h2.paragraph_format.space_before=Pt(6.5 if spacious else 5)
    h2.paragraph_format.space_after=Pt(2.0 if spacious else 1.5)
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
    p=d.add_paragraph(cv["recognition"])
    if cv.get("recognition_link"):
        p.add_run(" — ")
        link=cv["recognition_link"]
        add_hyperlink(p,link["label"],link["url"])
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
    spacious = kind in ("lead", "runtime")
    base_size = "10.0" if kind=="lead" else ("9.6" if spacious else "9.5")
    body_line = "1.32" if spacious else "1.25"
    heading_size = "10.4" if kind=="lead" else "10.0"
    item_size = "10.0" if kind=="lead" else ("9.6" if spacious else "9.5")
    contact_size = "8.75"
    recognition_html = e(cv["recognition"])
    if cv.get("recognition_link"):
        link = cv["recognition_link"]
        recognition_html += f' — <a href="{e(link["url"],quote=True)}">{e(link["label"])}</a>'
    page=f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
    @page {{size:A4;margin:10mm 14mm;}}
    html {{font-family:'DejaVu Sans','Liberation Sans',sans-serif;font-size:{base_size}pt;color:#1e2931;}}
    body {{margin:0;line-height:{body_line};}}
    h1 {{font-size:17pt;letter-spacing:-.025em;margin:0;}}
    .role {{font-size:10pt;font-weight:bold;margin:1mm 0 1.5mm;color:#234457;}}
    .contact {{font-size:{contact_size}pt;margin:0 0 3mm;}}
    a {{color:#255670;text-decoration:none;}}
    h2 {{font-size:{heading_size}pt;color:#234457;text-transform:uppercase;letter-spacing:.02em;
       border-bottom:.4pt solid #adc0c8;padding-bottom:.6mm;margin:2.6mm 0 1.1mm;}}
    p {{margin:0 0 1.4mm;}}
    ul {{margin:0 0 1.4mm;padding-left:4mm;}}
    li {{margin:0 0 .6mm;}}
    article {{break-inside:avoid;margin:0 0 1.6mm;}}
    h3 {{font-size:{item_size}pt;margin:0 0 .55mm;}}
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
    <h2>{e(education)}</h2><p>{e(cv['education'])}</p><p>{recognition_html}</p>
    </body></html>"""
    HTML(string=page,base_url=str(ROOT)).write_pdf(str(path))

PUBLIC_NOTE="""# Public claim boundaries / Открытые границы доказательств

This is a sanitized public research summary. It intentionally excludes internal project paths, private employers' documents, operational hosts and application credentials.

- Employment: ISP RAS / SharpChecker and MCST / LLVM dates and responsibility are recorded from the candidate and available evidence.
- Commercial experience: separate client software deliveries are documented from 2023, but exact full-time-equivalent duration is not established. Older CV variants may still contain a historical candidate estimate pending separate approval.
- VpnMediator: current operation and user numbers are candidate-reported. Architecture is described from source inspection. Python Telegram bot is distinct from the ASP.NET Core service.
- UniversalToolchain: a repository test manifest is not proof that all tests were executed again during resume preparation.
- TuringSquare-LMS: candidate reports approximately 40 platform users as of November 2026, without independent user analytics or active/paying scope; source-level materials and access controls do not prove the full production task-publication/Judge workflow. Implementation is partly AI-agent produced.
- Quark2: experimental CLR internals and microbenchmarks, not general production speedup.
- LLVM Global IV: source-backed legality gates, not verified production speedups.
- Systems/Platform: hands-on engineering, not a formal architect or Tech Lead appointment.
- Competition results and conference claims have mixed public and author-supplied evidence, recorded in the knowledge layer.
"""

def write_readmes(site,out):
    rows=["# Mikhail Razakov — CV / Резюме","",
          "Три специализации, отдельные сайты RU/EN и три синхронизированных формата для скачивания.","",
           "| Аудитория | Сайт RU | Website EN | PDF RU | PDF EN | DOCX RU | DOCX EN | Markdown RU | Markdown EN |",
          "|---|---|---|---|---|---|---|---|---|"]
    for key in KINDS:
        v=site["application_cvs"]["variants"][key]
        ru=v["basename"]["ru"];en=v["basename"]["en"]
        ru_url=site["site_url"]+site["application_cvs"]["pages"][key]["ru"]
        en_url=site["site_url"]+site["application_cvs"]["pages"][key]["en"]
        rows.append(f"| {v['audience_ru']} | [Открыть]({ru_url}) | [View]({en_url}) | [PDF]({ru}.pdf) | [PDF]({en}.pdf) | [DOCX]({ru}.docx) | [DOCX]({en}.docx) | [MD]({ru}.md) | [MD]({en}.md) |")
    rows+=["","Для обычного backend-отклика — Backend ATS; для архитектуры/platform — Systems / Platform (02); для LLVM/CLR/performance — Compiler / Performance (03).",
          "Отдельные заказные проекты датируются с 2023 года, общий FTE-стаж не подтверждён. Версия 02 обновлена отдельно; версия 03 не пересматривалась. Пользователи LMS (~40) указаны по сообщению кандидата, без независимой метрики.",
           "[Evidence boundaries](04_Public_Evidence_Boundaries.md) · [CV website](https://misha1302.github.io/CV/) · [Systems / Reliability](https://misha1302.github.io/CV/ru-systems-platform.html)","",
          "[Complete CV ZIP]("+ZIP_NAME+")",""]
    (out/"README.md").write_text("\n".join(rows),encoding="utf-8")
    (out/"00_README_Choose_Version.md").write_text(
        "# Выбор версии CV / Choosing a version\n\n"
        "01_Backend_ATS — основной CV для HR и ATS.\n\n"
        "02_Systems_Platform — Systems / Reliability: состояние, восстановление и контракты. Прежнее имя 02_Tech_Lead сохранено как совместимый alias.\n\n"
        "03_Runtime_Compiler — compiler/runtime engineering, проверка корректности оптимизаций и микробенчмарки.\n\n"
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
            if kind=="lead":
                legacy=site["application_cvs"]["variants"][kind]["legacy_basename"][lang]
                for ext in (".md",".docx",".pdf"):
                    (out/(legacy+ext)).write_bytes((out/(stem+ext)).read_bytes())
    write_readmes(site,out)
    if not args.skip_archive:
        archive(out)
    print(json.dumps({"status":"built","formats":["md","docx","pdf"],"variants":6,"dir":str(out)}))

if __name__=="__main__":
    main()
