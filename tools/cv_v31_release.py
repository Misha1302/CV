from pathlib import Path
import base64
import zlib

base = Path(__file__).resolve().parent / ".cv_v31_payload"
ordered = [base / "part00a.txt", base / "part00b.txt"] + [base / f"part{i:02d}.txt" for i in range(1, 8)]
encoded = "".join(path.read_text(encoding="utf-8").strip() for path in ordered)
source = zlib.decompress(base64.b64decode(encoded)).decode("utf-8")

source = source.replace(
    '    common_ru = {\n        "education": COMMON_RU_EDU,',
    '    common_ru = {\n        "lang": "ru",\n        "education": COMMON_RU_EDU,',
)
source = source.replace(
    '    common_en = {\n        "education": COMMON_EN_EDU,',
    '    common_en = {\n        "lang": "en",\n        "education": COMMON_EN_EDU,',
)

old = '''    def build_block(profile: dict) -> str:\n        contact = "<br>".join(esc(x) for x in profile["contact"])\n        proofs = "".join(f'<div class="pcv-proof"><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in profile["proofs"])\n'''
new = '''    def build_block(profile: dict) -> str:\n        contact_values = profile["contact"]\n        contact_links = [\n            f'<a href="mailto:{esc(contact_values[0])}">{esc(contact_values[0])}</a>',\n            f'<a href="https://{esc(contact_values[1])}">{esc(contact_values[1])}</a>',\n            f'<a href="https://{esc(contact_values[2])}">{esc(contact_values[2])}</a>',\n        ]\n        contact = "<br>".join(contact_links)\n        ru = profile.get("lang") == "ru"\n        labels = {\n            "experience": "Опыт" if ru else "Experience",\n            "projects": "Избранные проекты" if ru else "Selected projects",\n            "skills": "Компетенции" if ru else "Skills",\n            "education": "Образование" if ru else "Education",\n            "recognition": "Достижения" if ru else "Recognition",\n            "communication": "Техническая коммуникация" if ru else "Technical communication",\n            "availability": "Доступность" if ru else "Availability",\n        }\n        proofs = "".join(f'<div class="pcv-proof"><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in profile["proofs"])\n'''
if old not in source:
    raise RuntimeError("v31 bootstrap: build_block source marker not found")
source = source.replace(old, new)

old_return = '''        return f"""<div class="print-cv" aria-label="Focused one-page CV"><header class="pcv-header"><div><h1>{esc(profile["name"])}</h1><h2>{esc(profile["role"])}</h2></div><div class="pcv-contact">{contact}</div></header><p class="pcv-summary">{esc(profile["summary"])}</p><div class="pcv-proofs">{proofs}</div><div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">Experience</h2>{''.join(experience)}</section><section><h2 class="pcv-section-title">Selected projects</h2>{projects}</section></main><aside class="pcv-side"><section><h2 class="pcv-section-title">Skills</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">Education</h2><p>{esc(profile["education"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">Recognition</h2><p>{esc(profile["recognition"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">Communication</h2><p>{esc(profile["communication"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">Availability</h2><p>{esc(profile["availability"])}</p></section></aside></div></div>"""\n'''
new_return = '''        return f"""<div class="print-cv" aria-label="Focused one-page CV"><header class="pcv-header"><div><h1>{esc(profile["name"])}</h1><h2>{esc(profile["role"])}</h2></div><div class="pcv-contact">{contact}</div></header><p class="pcv-summary">{esc(profile["summary"])}</p><div class="pcv-proofs">{proofs}</div><div class="pcv-columns"><main class="pcv-main"><section><h2 class="pcv-section-title">{labels["experience"]}</h2>{''.join(experience)}</section><section><h2 class="pcv-section-title">{labels["projects"]}</h2>{projects}</section></main><aside class="pcv-side"><section><h2 class="pcv-section-title">{labels["skills"]}</h2>{skills}</section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["education"]}</h2><p>{esc(profile["education"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["recognition"]}</h2><p>{esc(profile["recognition"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["communication"]}</h2><p>{esc(profile["communication"])}</p></section><section class="pcv-compact"><h2 class="pcv-section-title">{labels["availability"]}</h2><p>{esc(profile["availability"])}</p></section></aside></div></div>"""\n'''
if old_return not in source:
    raise RuntimeError("v31 bootstrap: print return source marker not found")
source = source.replace(old_return, new_return)
source = source.replace("span[3] for block in page.get_text(\"dict\")[\"blocks\"]", "span[\"size\"] for block in page.get_text(\"dict\")[\"blocks\"]")

exec(compile(source, "cv_v31_release.py", "exec"))
