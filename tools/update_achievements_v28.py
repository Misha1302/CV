from __future__ import annotations

from pathlib import Path
import re

RU_TITLE = "Победы во всероссийских конкурсах"
RU_TEXT = (
    "1-е место по итоговому баллу в направлении «Инженерные науки» Всероссийского конкурса «Юниор» НИЯУ МИФИ в 2025 году "
    "и в секции «Информационные технологии» в 2026 году. Диплом I степени и Главная премия «Совершенство как надежда» "
    "Балтийского научно-инженерного конкурса."
)
EN_TITLE = "First-place results in national competitions"
EN_TEXT = (
    "Top total score in the Engineering Sciences track of the All-Russian MEPhI Junior competition in 2025 and in its "
    "Information Technology section in 2026. First-degree diploma and the Grand Prize “Perfection as Hope” at the Baltic "
    "Science and Engineering Competition."
)
RU_PRINT = (
    "Призёр «Высшей пробы»; 1-е место по итоговому баллу в «Юниоре» НИЯУ МИФИ "
    "(2025 — инженерные науки, 2026 — ИТ); Главная премия Балтийского конкурса."
)
EN_PRINT = (
    "HSE Olympiad prize-winner; 1st by total score in MEPhI Junior "
    "(2025 Engineering Sciences; 2026 IT); Baltic competition Grand Prize."
)

ARTICLE = re.compile(r'<article class="recognition-item">.*?</article>', re.DOTALL)


def patch_article(text: str, title: str, body: str, path: Path) -> str:
    candidates = []
    for match in ARTICLE.finditer(text):
        article = match.group(0)
        if "olymp.mephi.ru/junior/winners/2025" in article and "olymp.mephi.ru/junior/winners/2026" in article:
            candidates.append(match)
    if len(candidates) != 1:
        raise RuntimeError(f"{path}: expected one Junior 2025/2026 recognition article, found {len(candidates)}")
    match = candidates[0]
    article = match.group(0)
    article, h_count = re.subn(r"<h3>.*?</h3>", f"<h3>{title}</h3>", article, count=1, flags=re.DOTALL)
    article, p_count = re.subn(r"<p>.*?</p>", f"<p>{body}</p>", article, count=1, flags=re.DOTALL)
    if h_count != 1 or p_count != 1:
        raise RuntimeError(f"{path}: could not patch recognition title/body")
    return text[: match.start()] + article + text[match.end() :]


def patch_print(text: str, heading: str, body: str) -> str:
    pattern = re.compile(
        rf'(<section class="pcv-compact"><h2 class="pcv-section-title">{re.escape(heading)}</h2><p>).*?(</p></section>)',
        re.DOTALL,
    )
    updated, count = pattern.subn(rf"\1{body}\2", text)
    if count not in (0, 1):
        raise RuntimeError(f"Unexpected {heading} print-section count: {count}")
    return updated


html_files = sorted(Path(".").glob("*.html"))
ru_targets = [p for p in html_files if p.name == "ru.html" or p.name.startswith("ru-")]
en_targets = [p for p in html_files if p.name == "en.html" or p.name.startswith("en-")]
if len(ru_targets) != 8 or len(en_targets) != 8:
    raise RuntimeError(f"Expected 8 RU and 8 EN pages, got {len(ru_targets)} and {len(en_targets)}")

for path in ru_targets:
    text = patch_article(path.read_text(encoding="utf-8"), RU_TITLE, RU_TEXT, path)
    text = patch_print(text, "Достижения", RU_PRINT)
    text = text.replace("style.css?v=27", "style.css?v=28").replace("script.js?v=27", "script.js?v=28")
    path.write_text(text, encoding="utf-8")

for path in en_targets:
    text = patch_article(path.read_text(encoding="utf-8"), EN_TITLE, EN_TEXT, path)
    text = patch_print(text, "Recognition", EN_PRINT)
    text = text.replace("style.css?v=27", "style.css?v=28").replace("script.js?v=27", "script.js?v=28")
    path.write_text(text, encoding="utf-8")

index = Path("index.html")
index.write_text(
    index.read_text(encoding="utf-8").replace("style.css?v=27", "style.css?v=28").replace("script.js?v=27", "script.js?v=28"),
    encoding="utf-8",
)

renames = {
    Path("CONTENT-REVIEW-v27.md"): Path("CONTENT-REVIEW-v28.md"),
    Path("QA-report-targeted-cv-v27.md"): Path("QA-report-targeted-cv-v28.md"),
}
for old, new in renames.items():
    if not old.exists():
        raise RuntimeError(f"Missing expected release file: {old}")
    old.rename(new)

for path in [
    Path("README.md"), Path("RELEASE-METADATA.md"), Path("TARGETING.md"),
    Path("LANGUAGE-REVIEW.md"), Path("EXPERIENCE-AUDIT.md"), Path("FACT-RETENTION.md"),
    Path("LINK-AUDIT.md"), Path("CONTENT-REVIEW-v28.md"), Path("QA-report-targeted-cv-v28.md"),
]:
    path.write_text(path.read_text(encoding="utf-8").replace("v27", "v28"), encoding="utf-8")

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
marker = "## Изменения v28\n"
if marker not in text:
    raise RuntimeError("README v28 section not found")
text = text.replace(
    marker,
    marker
    + "\n- В блоке достижений явно указаны два первых результата по итоговому баллу во Всероссийском конкурсе «Юниор»: направление «Инженерные науки» (2025) и секция «Информационные технологии» (2026).\n"
    + "- Балтийская награда названа точно: диплом I степени и Главная премия «Совершенство как надежда».\n"
    + "- RU/EN web-версии и focused compiler/C++ systems PDF синхронизированы; формулировка «1-е место в РФ» не используется без категории.\n",
    1,
)
text = text.replace(
    "Предыдущая версия репозитория: v26, commit `6a67ea16513f08772a17c3b88dc777115`.",
    "Предыдущая версия репозитория: v27, commit `31a7c75144d1555b3c3fa8ca1eb7e14969770561`.",
)
text = text.replace(
    "Предыдущая версия репозитория: v26, commit `6a67ea16513f08772a17c3aee19c0135d437cc2b`.",
    "Предыдущая версия репозитория: v27, commit `31a7c75144d1555b3c3fa8ca1eb7e14969770561`.",
)
readme.write_text(text, encoding="utf-8")

qa = Path("QA-report-targeted-cv-v28.md")
qa.write_text(
    qa.read_text(encoding="utf-8")
    + "\n## National-achievement wording\n\n"
    + "- Official MEPhI result tables support the top total score in Engineering Sciences (2025) and Information Technology (2026).\n"
    + "- The Baltic result is stated as a first-degree diploma plus the Grand Prize, without claiming a unique nationwide rank.\n"
    + "- All 16 RU/EN role/portfolio HTML pages contain the synchronized wording.\n",
    encoding="utf-8",
)

corpus = "\n".join(p.read_text(encoding="utf-8") for p in html_files)
for marker in (RU_TEXT, EN_TEXT, RU_PRINT, EN_PRINT):
    if marker not in corpus:
        raise RuntimeError(f"Required achievement marker missing: {marker}")
for stale in ("двукратный абсолютный победитель", "two-time absolute winner"):
    if stale in corpus:
        raise RuntimeError(f"Stale wording remains: {stale}")
print("Updated national-achievement wording across 16 pages and v28 release metadata")
