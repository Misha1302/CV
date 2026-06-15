from pathlib import Path

MCST_URL = "https://www.mcst.ru/student"

ru_path = Path("ru.html")
en_path = Path("en.html")
index_path = Path("index.html")
readme_path = Path("README.md")

ru = ru_path.read_text(encoding="utf-8")
en = en_path.read_text(encoding="utf-8")

for anchor in (
    '<a href="cv.html">Открыть CV на английском</a>',
    '<a class="sidebar-download" href="cv.html">Открыть CV на английском · HTML</a>',
):
    ru = ru.replace(anchor, "")

ru_old = '<article><span>2026 · МЦСТ</span><h3>Отбор по направлению LLVM-компилятора</h3><p>Первое место среди 49 присланных решений; единственное решение, получившее 5,0/5,0 и прошедшее все 104 теста.</p></article>'
ru_new = '<article><span>2026 · МЦСТ</span><h3>Отбор по направлению LLVM-компилятора</h3><p>Первое место среди 49 присланных решений; единственное решение, получившее 5,0/5,0 и прошедшее все 104 теста.</p><div class="evidence-links"><a href="https://www.mcst.ru/student" rel="noopener noreferrer" target="_blank">Официальная программа стажировки ↗</a></div></article>'
assert ru.count(ru_old) == 1
ru = ru.replace(ru_old, ru_new, 1)

for anchor in (
    '<a href="cv.html">Open CV</a>',
    '<a class="sidebar-download" href="cv.html">Open CV · printable HTML</a>',
):
    en = en.replace(anchor, "")

en_old = '<article><span>2026 · MCST</span><h3>LLVM Compiler Selection</h3><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p></article>'
en_new = '<article><span>2026 · MCST</span><h3>LLVM Compiler Selection</h3><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p><div class="evidence-links"><a href="https://www.mcst.ru/student" rel="noopener noreferrer" target="_blank">Official internship program ↗</a></div></article>'
assert en.count(en_old) == 1
en = en.replace(en_old, en_new, 1)

ru_path.write_text(ru, encoding="utf-8")
en_path.write_text(en, encoding="utf-8")
index_path.write_text(en, encoding="utf-8")
readme_path.write_text(
    "# Mikhail Razakov — professional profile\n\n"
    "Static bilingual professional profile.\n\n"
    "- `index.html` / `en.html` — English profile\n"
    "- `ru.html` — Russian profile\n"
    "- `style.css`, `script.js` — presentation and navigation\n\n"
    "The site is published through GitHub Pages at `https://misha1302.github.io/CV/`.\n",
    encoding="utf-8",
)

assert not Path("cv.html").exists()
assert not Path("cv.css").exists()
assert "cv.html" not in ru
assert "cv.html" not in en
assert ru.count(MCST_URL) == 1
assert en.count(MCST_URL) == 1
assert index_path.read_bytes() == en_path.read_bytes()
