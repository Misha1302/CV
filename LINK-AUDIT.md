# Link audit - v30

- 17 HTML files and 17 sitemap entries are retained.
- All local HTML/PDF/paper/stylesheet/script/asset paths are checked by CI.
- Fragment links and duplicate IDs are checked.
- Every `target="_blank"` link must include `noopener noreferrer`.
- Compiler and C++ systems pages/PDFs include links to PS-form, AdvancedAlgorithms where relevant, Nasm-X86-Course and x86-64 codegen lab.
- PDF links are validated as clickable annotations after export.

Verdict: PASS only together with the v30 CI report.
