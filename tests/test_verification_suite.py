"""Tests for the Erdős 142 finite verification suite."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestVerificationSuite(unittest.TestCase):
    def test_current_scripts_exist_on_disk(self) -> None:
        """All scripts registered in CURRENT in run_current.py must exist."""
        from verification import run_current
        self.assertGreater(len(run_current.CURRENT), 20, "Expected at least 20 current scripts")
        for rel in run_current.CURRENT:
            script_path = ROOT / rel
            self.assertTrue(script_path.exists(), f"Registered script does not exist: {rel}")

    def test_legacy_scripts_exist_on_disk(self) -> None:
        """All legacy scripts registered in LEGACY in run_current.py must exist."""
        from verification import run_current
        self.assertGreater(len(run_current.LEGACY), 10, "Expected at least 10 legacy scripts")
        for rel in run_current.LEGACY:
            script_path = ROOT / rel
            self.assertTrue(script_path.exists(), f"Registered legacy script does not exist: {rel}")

    def test_recent_results_json_schema(self) -> None:
        """Results files must include status=passed and target_proved=False."""
        results = [
            "MULTISCALE_BOHR_OVERLAP_20261024.json",
            "BILINEAR_PAIR_INCIDENCE_20261024.json",
            "GROWING_OVERLAP_SYSTEMS_20261024.json",
            "OVERLAP_CONSTRAINTS_20261023.json",
            "LOW_MEAN_MOMENTS_20261023.json",
        ]
        for fname in results:
            path = ROOT / "verification/results" / fname
            if not path.exists():
                continue
            with self.subTest(file=fname):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data.get("status"), "passed")
                self.assertFalse(data.get("target_proved", False))


if __name__ == "__main__":
    unittest.main()
