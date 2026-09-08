from __future__ import annotations

import json
from pathlib import Path

from reposition_quant_profiles_20260908_v2 import main as apply_profiles

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "site.json"


def main() -> None:
    apply_profiles()
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["version"] = max(int(data.get("version", 0)), 58)
    for key in ("quantdev", "quant", "systems"):
        for lang in ("ru", "en"):
            data["profiles"][key][lang]["print_layout"] = "application"
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
