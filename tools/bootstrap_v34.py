from __future__ import annotations

import base64
import io
import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNK_GLOB = ".cv-v34-source.b64.*"
LEGACY_FILES = [
    "data/cv-print-profiles.json",
    "tools/update_profiles_v33.py",
]
LEGACY_GLOBS = [
    "QA-report-targeted-cv-v*.md",
    "pdf/Mikhail_Razakov_DevTools_*.pdf",
    "pdf/Mikhail_Razakov_Algorithms_*.pdf",
    "pdf/Mikhail_Razakov_EdTech_*.pdf",
    "pdf/Mikhail_Razakov_Reliability_*.pdf",
]


def main() -> None:
    chunks = sorted((ROOT / "tools").glob(CHUNK_GLOB))
    if not chunks:
        raise RuntimeError("CV v34 source bundle chunks are missing")
    encoded = "".join(path.read_text(encoding="ascii") for path in chunks)
    payload = base64.b64decode(encoded, validate=True)
    with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as archive:
        archive.extractall(ROOT, filter="data")

    for relative in LEGACY_FILES:
        path = ROOT / relative
        if path.exists():
            path.unlink()
    for pattern in LEGACY_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file():
                path.unlink()

    for path in chunks:
        path.unlink()
    shutil.rmtree(ROOT / "tools" / "__pycache__", ignore_errors=True)
    Path(__file__).unlink()


if __name__ == "__main__":
    main()
