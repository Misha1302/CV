from pathlib import Path

path = Path('style.css')
text = path.read_text(encoding='utf-8')
replacements = {
    'font-size: 9pt;\n    line-height: 1.27;': 'font-size: 10pt;\n    line-height: 1.32;',
    'font-size: 23pt;': 'font-size: 25pt;',
    'font-size: 11.5pt;': 'font-size: 13pt;',
    'font-size: 8.4pt; line-height: 1.38;': 'font-size: 9.2pt; line-height: 1.42;',
    'margin: 3mm 0 2.7mm; font-size: 9.2pt; line-height: 1.32;': 'margin: 4mm 0 3.5mm; font-size: 10.2pt; line-height: 1.38;',
    'gap: 2mm; margin-bottom: 3.2mm;': 'gap: 2.8mm; margin-bottom: 4.2mm;',
    'min-height: 16mm; padding: 2.4mm 2.7mm;': 'min-height: 20mm; padding: 3.2mm 3.3mm;',
    'font-size: 10.2pt; line-height: 1.12;': 'font-size: 11.4pt; line-height: 1.14;',
    'margin-top: 1mm; font-size: 7.8pt; line-height: 1.2;': 'margin-top: 1.3mm; font-size: 8.7pt; line-height: 1.25;',
    'gap: 5mm;': 'gap: 6.5mm;',
    'margin-top: 3mm;': 'margin-top: 4.5mm;',
    'margin: 0 0 1.7mm; padding-bottom: .8mm;': 'margin: 0 0 2.2mm; padding-bottom: 1.1mm;',
    'font-size: 10.5pt; line-height: 1.15;': 'font-size: 11.5pt; line-height: 1.16;',
    'grid-template-columns: 26mm minmax(0, 1fr); gap: 2.5mm; padding: 1.5mm 0 2mm;': 'grid-template-columns: 28mm minmax(0, 1fr); gap: 3mm; padding: 2.2mm 0 3mm;',
    'font-size: 7.5pt; font-weight: 700;': 'font-size: 8.2pt; font-weight: 700;',
    'font-size: 9.2pt; line-height: 1.18;': 'font-size: 10.2pt; line-height: 1.2;',
    'margin: 1mm 0 0; padding-left: 3.6mm;': 'margin: 1.4mm 0 0; padding-left: 4.2mm;',
    'margin: 0 0 .75mm; font-size: 8.25pt; line-height: 1.23;': 'margin: 0 0 1mm; font-size: 9.15pt; line-height: 1.28;',
    'padding: 1.5mm 0 1.7mm;': 'padding: 2.2mm 0 2.5mm;',
    'font-size: 7.2pt;': 'font-size: 8pt;',
    'margin: .8mm 0 0; font-size: 8.15pt; line-height: 1.24;': 'margin: 1.2mm 0 0; font-size: 9.05pt; line-height: 1.3;',
    'padding: 1.25mm 0;': 'padding: 1.8mm 0;',
    'font-size: 8.3pt; line-height: 1.15;': 'font-size: 9.1pt; line-height: 1.18;',
    'margin-top: .55mm; font-size: 7.75pt; line-height: 1.22;': 'margin-top: .8mm; font-size: 8.55pt; line-height: 1.28;',
    'font-size: 8pt; line-height: 1.27;': 'font-size: 8.9pt; line-height: 1.34;',
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f'Missing CSS fragment: {old}')
    text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
print('Increased v27 print typography and spacing')
