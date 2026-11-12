"""Cross-validate six public recruiting microsites against canonical CV data.

This validator makes it impossible to silently update PDF/DOCX/Markdown
while leaving the corresponding HTML websites stale or incomplete.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

from build_site import ROOT, build_outputs, load_data, write_or_check
from build_application_sites import ROLES


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def validate() -> dict[str, object]:
    data = load_data()
    release = data["application_cvs"]
    expected = build_outputs(data)
    all_pages: list[dict[str, object]] = []
    home = BeautifulSoup((ROOT / "index.html").read_text(encoding="utf-8"), "html.parser")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for kind in ROLES:
        for lang in ("ru", "en"):
            route = release["pages"][kind][lang]
            cv = release["variants"][kind][lang]
            path = ROOT / route
            require(path.exists(),f"Application site missing: {route}")
            require(path.read_text(encoding="utf-8") == expected[path],f"Stale generated application site: {route}")
            soup = BeautifulSoup(path.read_text(encoding="utf-8"),"html.parser")
            html = soup.find("html")
            require(html and html.get("lang") == lang,f"Wrong page language: {route}")
            require(len(soup.select("main h1")) == 1,f"Missing/duplicate H1: {route}")
            main = soup.find("main")
            require(main is not None,f"Missing main landmark: {route}")
            text = norm(main.get_text(" ",strip=True))
            for label in [data["person"]["name_"+lang],cv["role"],cv["summary"],cv["education"],cv["recognition"]]:
                require(norm(label) in text,f"Missing canonical CV content on {route}: {label[:85]}")
            if cv.get("recognition_link"):
                link=cv["recognition_link"]
                require(soup.select_one(f'a[href="{link["url"]}"]') is not None,f"Missing recognition video link: {route}")
            for skill in cv["skills"]:
                require(norm(skill) in text,f"Missing skill on {route}: {skill[:85]}")
            for exp in release["variants"][kind].get("experience",release["experience"])[lang]:
                for value in (exp["date"],exp["title"],exp["text"]):
                    require(norm(value) in text,f"Missing experience on {route}: {value[:85]}")
            project_rows = soup.select("article.ap-case")
            require(len(project_rows) == len(cv["projects"]),f"Wrong project count on {route}")
            for project in cv["projects"]:
                record = data["projects"][project["id"]]
                case = soup.select_one("#case-"+project["id"])
                require(case is not None,f"Missing case section on {route}: {project['id']}")
                case_text = norm(case.get_text(" ",strip=True))
                for value in (
                    project["title"],project["text"],
                    record["problem_"+lang],record["solution_"+lang],record["result_"+lang],
                ):
                    require(norm(value) in case_text,f"Missing detailed project content on {route}: {value[:85]}")
                require(case.select_one(f'a[href="{record["case_"+lang]}"]') is not None,f"Case link missing {route}: {project['id']}")
                if record.get("repo"):
                    require(case.select_one(f'a[href="{record["repo"]}"]') is not None,f"Source link missing {route}: {project['id']}")
            require(len(soup.select(".ap-roles a"))==3,f"Role switcher must offer 3 routes: {route}")
            for other in ROLES:
                other_route=release["pages"][other][lang]
                require(soup.select_one(f'.ap-roles a[href="{other_route}"]') is not None,
                        f"Role switch missing {route}->{other_route}")
            other_lang = "en" if lang=="ru" else "ru"
            require(soup.select_one(f'.ap-language[href="{release["pages"][kind][other_lang]}"]') is not None,
                    f"Language toggle missing {route}")
            filename=release["variants"][kind]["basename"][lang]
            base=release["release_dir"]+"/"+filename
            for ext in ("pdf","docx","md"):
                require(soup.select_one(f'a[href="{base}.{ext}"]') is not None,
                        f"Missing {ext} download link on {route}")
                require((ROOT/f"{base}.{ext}").is_file(),
                        f"Download artifact absent: {base}.{ext}")
            for target in ("work","projects","skills","education","contact"):
                require(soup.select_one(f'#{target}') is not None,f"Missing section {target} on {route}")
            require(soup.select_one('a.skip-link[href="#content"]') is not None,f"No skip link {route}")
            canonical=soup.select_one('link[rel="canonical"]')
            require(canonical is not None and canonical.get("href")==data["site_url"]+route,
                    f"Incorrect canonical URL {route}")
            for language in ("ru","en"):
                require(soup.select_one(f'link[hreflang="{language}"][href="{data["site_url"]+release["pages"][kind][language]}"]') is not None,
                        f"Missing hreflang on {route}")
            require(data["site_url"]+route in sitemap,f"Missing sitemap entry: {route}")
            if lang=="ru":
                require(home.select_one(f'a.cv-site-link[href="{route}"]') is not None,
                        f"Home needs direct website route {route}")
            all_pages.append({"route":route,"kind":kind,"lang":lang,"projects":len(project_rows),"format_links":3,"status":"PASS"})
    for lang in ("ru","en"):
        alias=ROOT/f"{lang}-engineering.html"
        new=ROOT/release["pages"]["lead"][lang]
        require(alias.is_file() and new.is_file(),"Old engineering alias missing")
        a=BeautifulSoup(alias.read_text(encoding="utf-8"),"html.parser")
        require(a.select_one('link[rel="canonical"]').get("href")==data["site_url"]+new.name,
                f"Engineering alias not canonicalized: {alias.name}")
        require(norm(a.select_one('main').get_text(" ",strip=True))==
                norm(BeautifulSoup(new.read_text(encoding="utf-8"),"html.parser").select_one('main').get_text(" ",strip=True)),
                f"Old engineering URL has stale content: {alias.name}")
    return {"status":"PASS","pages":all_pages,"legacy_engineering_aliases":2}


if __name__=="__main__":
    print(json.dumps(validate(),ensure_ascii=False,indent=2))
