from __future__ import annotations

import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))

ru = data["recognition"]["ru"]
en = data["recognition"]["en"]
if len(ru) != 3 or len(en) != 3 or ru[0][1] != "Олимпиадное программирование" or en[0][1] != "Programming competitions":
    raise SystemExit("Recognition structure differs from reviewed baseline")
if "Первые результаты конкурса «Юниор»" not in ru[1][2] or "Top MEPhI Junior results" not in en[1][2]:
    raise SystemExit("Junior wording differs from reviewed baseline")

data["recognition"]["ru"] = [
    ["2026", "LangDev 2026 — доклад принят", "Доклад об архитектуре UniversalToolchain/Wist2 принят программным комитетом LangDev 2026 для выступления; Торремолинос, Испания."],
    ru[0],
    ["2025–2026", "Всероссийские конкурсы", ru[1][2].replace("Первые результаты конкурса «Юниор» НИЯУ МИФИ в 2025 и 2026 годах", "Абсолютный победитель конкурса «Юниор» НИЯУ МИФИ в 2025 и 2026 годах")],
    ru[2],
]
data["recognition"]["en"] = [
    ["2026", "LangDev 2026 — accepted talk", "The LangDev 2026 Program Committee accepted a talk on the architecture of UniversalToolchain/Wist2 for presentation in Torremolinos, Spain."],
    en[0],
    ["2025–2026", "National competitions", en[1][2].replace("Top MEPhI Junior results in 2025 and 2026", "Overall winner of the MEPhI Junior competition in 2025 and 2026")],
    en[2],
]
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
