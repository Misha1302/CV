#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
site_path = root / "data" / "site.json"
data = json.loads(site_path.read_text(encoding="utf-8"))
for profile_key in ("general", "compiler"):
    for lang in ("ru", "en"):
        data["profiles"][profile_key][lang]["print_project_limit"] = 4
site_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

build_path = root / "tools" / "build_site.py"
text = build_path.read_text(encoding="utf-8")
old = '    for project_id in profile["project_ids"][:3]:\n'
new = '    project_limit = int(profile.get("print_project_limit", 3))\n    for project_id in profile["project_ids"][:project_limit]:\n'
if text.count(old) != 1:
    raise SystemExit("unexpected print project loop shape")
text = text.replace(old, new, 1)
build_path.write_text(text, encoding="utf-8")
