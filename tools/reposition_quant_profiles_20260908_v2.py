from __future__ import annotations

import json
from pathlib import Path

from reposition_quant_profiles_20260908 import main as apply_base

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "site.json"


def main() -> None:
    apply_base()
    data = json.loads(PATH.read_text(encoding="utf-8"))

    ru = data["profiles"]["quant"]["ru"]
    ru["title"] = "Михаил Разаков — Quantitative Research Candidate | C++ · Python"
    ru["role"] = "Quantitative Research Candidate | C++ · Python"
    ru["footer"] = "Quantitative Research Candidate · C++ · Python"

    en = data["profiles"]["quant"]["en"]
    en["title"] = "Mikhail Razakov — Quantitative Research Candidate | C++ · Python"
    en["role"] = "Quantitative Research Candidate | C++ · Python"
    en["footer"] = "Quantitative Research Candidate · C++ · Python"

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
