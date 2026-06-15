from pathlib import Path
import subprocess

ENGLISH_NAME = 'HSE “Highest Standard” Olympiad'

path = Path('en.html')
text = path.read_text(encoding='utf-8')

proof_old = 'Vysshaya Proba prize-winner'
proof_new = f'{ENGLISH_NAME} prize-winner'
label_old = '<span>2026 · Vysshaya Proba</span>'
label_new = f'<span>2026 · {ENGLISH_NAME}</span>'

if text.count(proof_old) != 1:
    raise SystemExit(f'Expected one proof-strip occurrence, found {text.count(proof_old)}')
if text.count(label_old) != 2:
    raise SystemExit(f'Expected two recognition-label occurrences, found {text.count(label_old)}')

text = text.replace(proof_old, proof_new)
text = text.replace(label_old, label_new)

path.write_text(text, encoding='utf-8')
Path('index.html').write_text(text, encoding='utf-8')

tracked = subprocess.check_output(['git', 'ls-files'], text=True).splitlines()
for filename in tracked:
    file_path = Path(filename)
    if not file_path.is_file():
        continue
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    if 'Vysshaya Proba' in content or 'Vysshaya' in content:
        raise SystemExit(f'Old transliterated name remains in {filename}')

if text.count(ENGLISH_NAME) != 3:
    raise SystemExit(f'Expected three uses of the new name, found {text.count(ENGLISH_NAME)}')
if Path('en.html').read_bytes() != Path('index.html').read_bytes():
    raise SystemExit('en.html and index.html differ')
