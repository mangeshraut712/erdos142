"""Tests for status and research dashboard generation."""
from __future__ import annotations

import io
from pathlib import Path
import sys
import unittest

from scripts.generate_dashboard import build_dashboard_html as build_rich_dashboard
import scripts.research_status
from verification.generate_dashboard import build_dashboard_html as build_status_dashboard

ROOT = Path(__file__).resolve().parents[1]


class TestDashboard(unittest.TestCase):
    def test_status_dashboard_html_generation(self) -> None:
        """Status dashboard HTML must generate and contain expected key badges, metrics, and scripts."""
        html = build_status_dashboard()
        self.assertIn("Erdős 142 — Research Pack Status Dashboard", html)
        self.assertIn("MS24", html)
        self.assertIn("BP24", html)
        self.assertIn("IE24", html)
        self.assertIn("CL23", html)
        self.assertIn("verify_multiscale_bohr_overlap_20261024.py", html)
        self.assertIn("verify_bilinear_pair_incidence_20261024.py", html)
        self.assertIn("research pack status dashboard", html.lower())

    def test_status_dashboard_reads_checks_from_result_artifacts(self) -> None:
        """GO24/OC23 counts come from the artifacts' "checks" field, not hard-coded defaults."""
        import json
        import tempfile
        from unittest import mock

        import verification.generate_dashboard as status_dashboard

        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp) / "verification/results"
            results.mkdir(parents=True)
            (results / "GROWING_OVERLAP_20261024.json").write_text(json.dumps({"checks": 12345}), encoding="utf-8")
            (results / "OVERLAP_CONSTRAINTS_20261023.json").write_text(json.dumps({"checks": 67890}), encoding="utf-8")
            with mock.patch.object(status_dashboard, "ROOT", Path(tmp)):
                html = status_dashboard.build_dashboard_html()
        self.assertIn("<strong>12,345</strong>", html)
        self.assertIn("<strong>67,890</strong>", html)

    def test_status_file_matches_generator(self) -> None:
        """docs/status.html must match the status generator output."""
        status_file = ROOT / "docs/status.html"
        self.assertTrue(status_file.exists(), "docs/status.html does not exist")
        generated = build_status_dashboard()
        actual = status_file.read_text(encoding="utf-8")
        self.assertEqual(generated, actual, "docs/status.html is out of sync with verification/generate_dashboard.py")

    def test_rich_dashboard_html_generation(self) -> None:
        """Rich dashboard HTML must generate and contain interactive tools."""
        html = build_rich_dashboard()
        self.assertIn("Erdős 142 — Research Program", html)
        self.assertIn("BP24", html)
        self.assertIn("Bilinear Ceiling", html)
        self.assertIn("val-ceiling", html)

    def test_research_status_cli(self) -> None:
        """CLI research status runner must execute cleanly and print status."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            ret = scripts.research_status.main()
            self.assertEqual(ret, 0)
        finally:
            sys.stdout = old_stdout
        output = captured.getvalue()
        self.assertIn("RESEARCH PROGRAM STATUS DASHBOARD", output)
        self.assertIn("Target:", output)
        self.assertIn("MS24", output)


if __name__ == "__main__":
    unittest.main()
