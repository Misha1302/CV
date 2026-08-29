#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["version"] = int(data.get("version", 0)) + 1
data["updated_at"] = "2026-08-29"

recognition_ru = [
    [
        "2026",
        "UniversalToolchain — Балтийский научно-инженерный конкурс",
        "Диплом I степени и Главная премия «Совершенство как надежда» за UniversalToolchain."
    ],
    [
        "2025–2026",
        "НИЯУ МИФИ «Юниор»",
        "Абсолютный победитель конкурса в 2025 и 2026 годах; в 2026 — диплом I степени, 96/100 за UniversalToolchain."
    ],
    [
        "2025–2026",
        "«Высшая проба» / ВсОШ по информатике",
        "Призёр «Высшей пробы» по олимпиадному и промышленному программированию; призёр регионального этапа ВсОШ по информатике."
    ],
    [
        "2026",
        "LangDev'26 — Extensible Programming on .NET",
        "Доклад принят к устному выступлению на LangDev'26."
    ]
]

recognition_en = [
    [
        "2026",
        "UniversalToolchain — Baltic Science and Engineering Competition",
        "First Degree Diploma and Grand Prize “Perfection as Hope” for UniversalToolchain."
    ],
    [
        "2025–2026",
        "MEPhI Junior",
        "Absolute winner in 2025 and 2026; in 2026, First Degree Diploma, 96/100 for UniversalToolchain."
    ],
    [
        "2025–2026",
        "HSE Vysshaya Proba / Russian National Olympiad in Informatics",
        "Prize-winner in Vysshaya Proba olympiad and industrial programming; regional-stage prize-winner in the Russian National Olympiad in Informatics."
    ],
    [
        "2026",
        "LangDev'26 — Extensible Programming on .NET",
        "Accepted for an oral presentation at LangDev'26."
    ]
]

for profile_key in ("general", "compiler"):
    data["profiles"][profile_key]["ru"]["recognition"] = recognition_ru
    data["profiles"][profile_key]["en"]["recognition"] = recognition_en

# Keep the shared recognition data complete for profiles that inherit it.
for lang, item in (("ru", recognition_ru[-1]), ("en", recognition_en[-1])):
    shared = data["recognition"][lang]
    if not any("LangDev" in row[1] for row in shared):
        shared.append(item)

path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
