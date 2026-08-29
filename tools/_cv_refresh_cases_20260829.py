#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))
for project_id in ("globaliv", "deref"):
    data["projects"][project_id]["case_ru"] = f"cases/ru-{project_id}.html"
    data["projects"][project_id]["case_en"] = f"cases/en-{project_id}.html"
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
