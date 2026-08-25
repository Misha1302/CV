from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "style.css"
text = STYLE.read_text(encoding="utf-8")
marker = "/* v46 mobile timeline containment */"
if marker not in text:
    text += """

/* v46 mobile timeline containment */
@media (max-width: 760px) {
  .timeline,
  .timeline article,
  .timeline article > *,
  .timeline-details,
  .timeline-details li {
    min-width: 0;
    max-width: 100%;
  }
  .timeline time,
  .timeline h3,
  .timeline .org,
  .timeline-details li {
    overflow-wrap: anywhere;
    word-break: break-word;
  }
}
"""
STYLE.write_text(text, encoding="utf-8")
