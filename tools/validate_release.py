#!/usr/bin/env python3
"""Check synchronization, attribution and document integrity of the CV edition."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from zipfile import ZipFile
import fitz
from docx import Document
from build_release import ROOT, KINDS, LANGS, ZIP_NAME, load, markdown, record

def require(ok,message):
    if not ok:
        raise RuntimeError(message)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-dir",type=Path)
    args=parser.parse_args()
    site=load()
    out=args.output_dir or ROOT/site["application_cvs"]["release_dir"]
    kb=json.loads((ROOT/"knowledge/resume-evidence.json").read_text(encoding="utf-8"))
    ids={a["id"] for a in kb["assets"]}
    report=[]
    for lang in LANGS:
        for ex in site["application_cvs"]["experience"][lang]:
            require(bool(ex.get("evidence_refs")),f"missing experience evidence: {ex['id']}")
            require(set(ex["evidence_refs"])<=ids,f"unknown experience evidence: {ex['id']}")
    for kind in KINDS:
        for lang in LANGS:
            cv,experiences,stem=record(site,kind,lang)
            for proj in cv["projects"]:
                require(proj["id"] in site["projects"],f"unknown project {proj['id']}")
                require(bool(proj.get("evidence_refs")),f"missing project evidence {proj['id']}")
                require(set(proj["evidence_refs"])<=ids,f"unknown project evidence {proj['id']}")
            md=out/(stem+".md")
            docx=out/(stem+".docx")
            pdf=out/(stem+".pdf")
            require(md.exists() and docx.exists() and pdf.exists(),f"missing formats {stem}")
            require(md.read_text(encoding="utf-8")==markdown(site,kind,lang),f"stale Markdown {stem}")
            with ZipFile(docx) as z:
                require(z.testzip() is None,f"corrupt DOCX ZIP {stem}")
                xml=z.read("word/document.xml").decode("utf-8")
                rel=z.read("word/_rels/document.xml.rels").decode("utf-8")
                require(__import__('html').escape(cv["role"]) in xml,f"missing DOCX role {stem}")
                for proj in cv["projects"]:
                    require(proj["text"] in xml or proj["text"][:48] in xml,f"missing DOCX project text {stem}:{proj['id']}")
                require(rel.count('Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"')>=5,f"few DOCX hyperlinks {stem}")
            Document(docx)
            d=fitz.open(pdf)
            require(d.page_count==1,f"{stem}: {d.page_count} PDF pages")
            page=d[0]
            require(abs(page.rect.width-595.28)<3 and abs(page.rect.height-841.89)<3,f"not A4 {stem}")
            text=" ".join(page.get_text().split())
            require(len(text)>1350 and cv["role"] in text,f"weak PDF text/role {stem}")
            for proj in cv["projects"]:
                name=proj["title"].split(" · ")[0].split(" / ")[0].strip()
                require(name in text,f"PDF missing {name} ({stem})")
            sizes=[s["size"] for b in page.get_text("dict")["blocks"] if "lines" in b
               for ln in b["lines"] for s in ln["spans"] if s["text"].strip()]
            require(sizes and min(sizes)>=8.3,f"PDF small fonts {stem}: {min(sizes) if sizes else '-'}")
            links=[x.get("uri") for x in page.get_links() if x.get("uri")]
            require(len(links)>=5,f"PDF clickable links missing {stem}")
            fonts=d.get_page_fonts(0)
            require(fonts and any("DejaVu" in str(f) for f in fonts),f"Cyrillic-capable font not seen {stem}")
            report.append({"name":stem,"lang":lang,"pages":1,"chars":len(text),"min_font":round(min(sizes),2),"pdf_links":len(links),"docx":"valid","md":"synced"})
            d.close()
    arc=out/ZIP_NAME
    require(arc.exists(),"CV ZIP missing")
    with ZipFile(arc) as z:
        require(z.testzip() is None,"invalid CV ZIP")
        names=set(z.namelist())
        for variant in report:
            for suffix in (".md",".docx",".pdf"):
                require(variant["name"]+suffix in names,f"ZIP missing {variant['name']+suffix}")
        require("04_Evidence_Research_and_Review.md" not in names,"private research exposed in ZIP")
        require("MANIFEST.sha256" in names,"internal manifest not packaged")
    print(json.dumps({"status":"PASS","variants":report,"zip_entries":len(names),"evidence_assets":len(ids)},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
