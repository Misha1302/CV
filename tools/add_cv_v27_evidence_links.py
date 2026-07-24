from pathlib import Path

LAB = 'https://github.com/Misha1302/x86-64-codegen-ra-playground'
COURSE = 'https://github.com/Misha1302/Nasm-X86-Course'

for name in ('ru-compiler.html', 'ru-cpp-systems.html'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    old = f'<h3><a href="{LAB}">NASM IA-32 и x86-64 codegen</a></h3><span>Assembly / backend</span>'
    new = f'<h3><a href="{LAB}">NASM IA-32 и x86-64 codegen</a></h3><span><a href="{COURSE}">курс NASM</a></span>'
    if old not in text:
        raise RuntimeError(f'{name}: Assembly project header not found')
    path.write_text(text.replace(old, new), encoding='utf-8')

for name in ('en-compiler.html', 'en-cpp-systems.html'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    old = f'<h3><a href="{LAB}">NASM IA-32 and x86-64 codegen</a></h3><span>Assembly / backend</span>'
    new = f'<h3><a href="{LAB}">NASM IA-32 and x86-64 codegen</a></h3><span><a href="{COURSE}">NASM course</a></span>'
    if old not in text:
        raise RuntimeError(f'{name}: Assembly project header not found')
    path.write_text(text.replace(old, new), encoding='utf-8')

print('Added separate NASM course links to four focused PDFs')
