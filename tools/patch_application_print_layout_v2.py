from __future__ import annotations

from pathlib import Path

from patch_application_print_layout import main as apply_layout

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "style.css"


def main() -> None:
    apply_layout()
    raw = STYLE.read_text(encoding="utf-8")
    STYLE.write_text(raw.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
