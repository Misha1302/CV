#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["version"] = int(data.get("version", 0)) + 1
data["updated_at"] = "2026-08-29"

ru_title_old = "«Высшая проба» / ВсОШ по информатике"
ru_title_new = "«Высшая проба» — олимпиадное и промышленное программирование"
ru_desc_old = "Призёр «Высшей пробы» по олимпиадному и промышленному программированию; призёр регионального этапа ВсОШ по информатике."
ru_desc_new = "Призёр «Высшей пробы» по олимпиадному и промышленному программированию."
en_title_old = "HSE Vysshaya Proba / Russian National Olympiad in Informatics"
en_title_new = "HSE Vysshaya Proba — Competitive & Industrial Programming"
en_desc_old = "Prize-winner in Vysshaya Proba olympiad and industrial programming; regional-stage prize-winner in the Russian National Olympiad in Informatics."
en_desc_new = "Prize-winner in HSE Vysshaya Proba in competitive and industrial programming."
shared_en_desc_old = "HSE Vysshaya Proba prize-winner in competitive and industrial programming; regional Russian informatics olympiad prize-winner."

for profile_key in ("general", "compiler"):
    ru_items = data["profiles"][profile_key]["ru"]["recognition"]
    en_items = data["profiles"][profile_key]["en"]["recognition"]

    ru_matches = [row for row in ru_items if row[1] == ru_title_old and row[2] == ru_desc_old]
    en_matches = [row for row in en_items if row[1] == en_title_old and row[2] == en_desc_old]
    if len(ru_matches) != 1 or len(en_matches) != 1:
        raise SystemExit(f"unexpected profile recognition shape for {profile_key}")

    ru_matches[0][1] = ru_title_new
    ru_matches[0][2] = ru_desc_new
    en_matches[0][1] = en_title_new
    en_matches[0][2] = en_desc_new

shared_ru = data["recognition"]["ru"]
shared_en = data["recognition"]["en"]
ru_shared_matches = [row for row in shared_ru if row[2] == ru_desc_old]
en_shared_matches = [row for row in shared_en if row[2] == shared_en_desc_old]
if len(ru_shared_matches) != 1 or len(en_shared_matches) != 1:
    raise SystemExit("unexpected shared recognition shape")

ru_shared_matches[0][1] = "«Высшая проба»"
ru_shared_matches[0][2] = ru_desc_new
en_shared_matches[0][1] = "HSE Vysshaya Proba"
en_shared_matches[0][2] = en_desc_new

serialized = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
for forbidden in (
    "регионального этапа ВсОШ",
    "regional-stage prize-winner",
    "regional Russian informatics olympiad",
    "Russian National Olympiad in Informatics",
):
    if forbidden in serialized:
        raise SystemExit(f"forbidden stale recognition wording remains: {forbidden}")

path.write_text(serialized, encoding="utf-8")
