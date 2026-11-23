#!/usr/bin/env python3
"""Regression tests for the artifact-versus-source checks in validate_cv.

These checks exist because a session edited data/site.json, rebuilt the HTML and
left the PDFs at the previous revision: the site and the PDFs described
different CVs and nothing failed. Every test here must fail when the
corresponding check is removed, so the tests are paired with a mutation run.

Run: python3 tools/test_validate_cv.py -v
"""
from __future__ import annotations

import copy
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import fitz

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_cv  # noqa: E402


def _build_pdf(path: Path, text: str) -> None:
    """Render `text` into a one-page PDF that actually contains a Cyrillic text layer.

    PyMuPDF's built-in Helvetica has no Cyrillic glyphs and silently extracts as
    a row of dots, so the font must be embedded explicitly.
    """
    font_path = Path("/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf")
    if not font_path.is_file():
        raise unittest.SkipTest(f"Cyrillic-capable font missing: {font_path}")
    document = fitz.open()
    page = document.new_page()
    page.insert_font(fontname="dejavu", fontfile=str(font_path))
    # insert_text does not wrap: anything past the page edge is clipped and lost
    # from the text layer. A textbox keeps the whole string extractable.
    page.insert_textbox(fitz.Rect(36, 36, 559, 806), text, fontsize=9, fontname="dejavu")
    document.save(path)
    document.close()


class PdfFlowTextTests(unittest.TestCase):
    """Text extracted from a PDF must be comparable with the data source."""

    def test_hyphenated_line_break_is_joined(self):
        # PDF engines wrap "LLVM-анализ" as "LLVM-\nанализ"; a naive substring
        # check then reports a mismatch on a correct artifact.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "wrapped.pdf"
            _build_pdf(path, "межпроцедурный LLVM-\nанализ и release/\nrecovery-процедуры")
            with fitz.open(path) as document:
                text = validate_cv.pdf_flow_text(document[0])
        self.assertIn("LLVM-анализ", text)
        self.assertIn("release/recovery-процедуры", text)

    def test_distinguish_whitespace_is_normalised(self):
        # Generator HTML wraps paragraphs at arbitrary points; only whitespace
        # differences must not count as a mismatch.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "wrapped.pdf"
            _build_pdf(path, "одна    строка\nвторая строка")
            with fitz.open(path) as document:
                text = validate_cv.pdf_flow_text(document[0])
        self.assertEqual(text, "одна строка вторая строка")


class RequireFragmentTests(unittest.TestCase):
    def test_matching_fragment_passes(self):
        validate_cv.require_fragment("до и после", "до и  после", "test")

    def test_stale_fragment_is_rejected_with_locator(self):
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.require_fragment("вывел LMS в production, 90+ учеников",
                                         "вывел LMS в production, 120+ учеников", "note.pdf")
        message = str(caught.exception)
        self.assertIn("note.pdf", message)
        self.assertIn("not rebuilt", message)

    def test_empty_fragment_is_a_source_bug(self):
        # An empty expected string would make `in` vacuously true and silently
        # disable the check; that must fail loudly instead.
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.require_fragment("любой текст", "   ", "empty.pdf")
        self.assertIn("empty expected fragment", str(caught.exception))


class PdfSetCompletenessTests(unittest.TestCase):
    def setUp(self):
        self.data = validate_cv.load_data()
        self.tmp = tempfile.TemporaryDirectory()
        self.pdf_dir = Path(self.tmp.name)
        for key in self.data["profile_order"]:
            for lang in ("ru", "en"):
                _build_pdf(self.pdf_dir / self.data["profiles"][key][lang]["pdf"], "pdf")

    def tearDown(self):
        self.tmp.cleanup()

    def test_complete_set_passes(self):
        validate_cv.validate_pdf_set_completeness(self.data, self.pdf_dir)

    def test_orphaned_pdf_is_rejected(self):
        # A renamed or dropped profile leaves an old PDF that keeps shipping.
        _build_pdf(self.pdf_dir / "Mikhail_Razakov_Removed_Profile_RU.pdf", "old")
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.validate_pdf_set_completeness(self.data, self.pdf_dir)
        self.assertIn("Removed_Profile", str(caught.exception))

    def test_missing_pdf_is_rejected(self):
        (self.pdf_dir / self.data["profiles"]["backend"]["ru"]["pdf"]).unlink()
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.validate_pdf_set_completeness(self.data, self.pdf_dir)
        self.assertIn("missing=", str(caught.exception))


class ReleaseArtifactTests(unittest.TestCase):
    """The packaged release must carry the current source text."""

    def setUp(self):
        self.data = copy.deepcopy(validate_cv.load_data())
        self.tmp = tempfile.TemporaryDirectory()
        self.release_dir = Path(self.tmp.name)
        for kind, variant in self.data["application_cvs"]["variants"].items():
            for lang in ("ru", "en"):
                self._write_variant(variant["basename"][lang], variant[lang])

    def _write_variant(self, stem: str, payload: dict) -> None:
        projects = "\n\n".join(project["text"] for project in payload["projects"])
        (self.release_dir / f"{stem}.md").write_text(
            f"# CV\n\n## Профиль\n\n{payload['summary']}\n\n{projects}", encoding="utf-8")
        # DOCX content is not parsed here; validate_release.py does that. This
        # check only requires the file to exist and be non-empty.
        (self.release_dir / f"{stem}.docx").write_bytes(b"PK\x03\x04placeholder")
        _build_pdf(self.release_dir / f"{stem}.pdf", payload["summary"] + "\n\n" + projects)

    def tearDown(self):
        self.tmp.cleanup()

    @property
    def stem(self) -> str:
        return self.data["application_cvs"]["variants"]["ats"]["basename"]["ru"]

    @property
    def summary(self) -> str:
        return self.data["application_cvs"]["variants"]["ats"]["ru"]["summary"]

    def test_current_release_passes(self):
        results = validate_cv.validate_release_artifacts(self.data, self.release_dir)
        self.assertTrue(any(row["stem"] == self.stem for row in results))

    def test_stale_summary_in_markdown_is_rejected(self):
        path = self.release_dir / f"{self.stem}.md"
        path.write_text(path.read_text(encoding="utf-8").replace(self.summary, "устаревший профиль"),
                        encoding="utf-8")
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.validate_release_artifacts(self.data, self.release_dir)
        self.assertIn("not rebuilt", str(caught.exception))

    def test_stale_pdf_is_rejected(self):
        # This is the exact failure that motivated the check: markdown rebuilt,
        # PDF left at the previous revision.
        _build_pdf(self.release_dir / f"{self.stem}.pdf", "старый текст без профиля")
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.validate_release_artifacts(self.data, self.release_dir)
        self.assertIn("not rebuilt", str(caught.exception))

    def test_missing_format_is_rejected(self):
        (self.release_dir / f"{self.stem}.docx").unlink()
        with self.assertRaises(RuntimeError) as caught:
            validate_cv.validate_release_artifacts(self.data, self.release_dir)
        self.assertIn("missing or empty", str(caught.exception))


class WiringTests(unittest.TestCase):
    """The checks are useless if main() never calls them.

    Direct-call tests still pass when the call is deleted from main(), so the
    wiring is asserted separately with the expensive stages stubbed out.
    """

    def _run_main(self, argv: list[str]) -> tuple[object, object]:
        data = {"profile_order": [], "profiles": {}, "projects": {}, "redirects": [],
                "application_cvs": {"release_dir": "releases/x", "variants": {}, "pages": {}}}
        with mock.patch.object(validate_cv, "load_data", return_value=data), \
             mock.patch.object(validate_cv, "validate_source_of_truth"), \
             mock.patch.object(validate_cv, "validate_universal_positioning"), \
             mock.patch.object(validate_cv, "validate_script"), \
             mock.patch.object(validate_cv, "validate_html", return_value=set()), \
             mock.patch.object(validate_cv, "validate_pdfs", return_value=[]), \
             mock.patch.object(validate_cv, "validate_manifest"), \
             mock.patch.object(validate_cv, "validate_pdf_set_completeness") as completeness, \
             mock.patch.object(validate_cv, "validate_release_artifacts", return_value=[]) as release, \
             mock.patch.object(sys, "argv", ["validate_cv.py", *argv]), \
             mock.patch("builtins.print"):
            validate_cv.main()
        return completeness, release

    def test_main_checks_pdf_set_and_release_artifacts(self):
        completeness, release = self._run_main(["--skip-manifest"])
        self.assertTrue(completeness.called, "main() no longer validates the PDF set")
        self.assertTrue(release.called, "main() no longer validates release artifacts")


if __name__ == "__main__":
    unittest.main()
