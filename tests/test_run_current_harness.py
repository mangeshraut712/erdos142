"""Pin verification/run_current.py's evidence guard and summary contract.

The --output guard keeps runs away from saved evidence, and the
reported_checks key order is what generate_dashboard.py reads. Both are one
refactor away from silently overwriting results or corrupting metrics, and
no verifier exercises them. Nothing is written inside this checkout.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from verification import run_current

ROOT = Path(__file__).resolve().parents[1]
RUN_CURRENT = ROOT / "verification" / "run_current.py"


def run_cli(script: Path, cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(script), *args],
                          cwd=str(cwd), capture_output=True, text=True, check=False)


class TestOutputGuard(unittest.TestCase):
    def test_relative_output_inside_checkout_is_refused(self) -> None:
        # Only refused because the path is resolve()d before the check.
        result = run_cli(RUN_CURRENT, ROOT, "--suite", "legacy", "--output", "verification/results")
        self.assertEqual(result.returncode, 2)
        self.assertIn("saved evidence", result.stderr)

    def test_prefix_sibling_of_runs_dir_is_refused_without_mkdir(self) -> None:
        # A string-prefix check would accept this; is_relative_to must not.
        result = run_cli(RUN_CURRENT, ROOT, "--suite", "legacy", "--output", ".verification-runs-backup")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((ROOT / ".verification-runs-backup").exists())

    def test_symlink_into_saved_evidence_is_refused(self) -> None:
        with tempfile.TemporaryDirectory(prefix="erdos142-guard-") as tmp:
            link = Path(tmp) / "alias"
            try:
                link.symlink_to(ROOT / "verification" / "results")
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = run_cli(RUN_CURRENT, ROOT, "--suite", "legacy", "--output", str(link / "probe"))
            self.assertEqual(result.returncode, 2)
            self.assertIn("saved evidence", result.stderr)
            self.assertFalse((ROOT / "verification" / "results" / "probe").exists())


class TestSummaryContract(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix="erdos142-harness-")
        self.base = Path(self._tmp.name)
        self.fake = self.base / "repo"
        (self.fake / "verification" / "scripts").mkdir(parents=True)
        shutil.copyfile(RUN_CURRENT, self.fake / "verification" / "run_current.py")
        self.cli = self.fake / "verification" / "run_current.py"
        shapes = {
            0: '{"total_checks": 7, "checks": 3}',  # total_checks outranks checks
            1: '{"checks": 3}',
            2: '{"counts": 11}',
            3: "not json at all",                   # tolerated, count missing
            4: '{"status": "passed"}',              # no recognised count key
        }
        for index, rel in enumerate(run_current.LEGACY):
            body = shapes.get(index, '{"checks": 1}')
            (self.fake / rel).write_text(f"print({body!r})\nraise SystemExit(0)\n")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_all_pass_summary(self) -> None:
        self.assertGreaterEqual(len(run_current.LEGACY), 5)
        out = self.base / "out"
        result = run_cli(self.cli, self.fake, "--suite", "legacy", "--output", str(out))
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads((out / "summary.json").read_text())
        self.assertIs(summary["passed"], True)
        self.assertIs(summary["isolated"], True)
        self.assertIs(summary["saved_reports_overwritten"], False)
        self.assertEqual([r["script"] for r in summary["results"]], run_current.LEGACY)
        self.assertEqual([r.get("reported_checks") for r in summary["results"]],
                         [7, 3, 11, None, None] + [1] * (len(run_current.LEGACY) - 5))
        self.assertTrue((out / (Path(run_current.LEGACY[0]).name + ".stdout")).exists())

    def test_first_failure_stops_the_run(self) -> None:
        (self.fake / run_current.LEGACY[3]).write_text("print('{\"checks\": 0}')\nraise SystemExit(1)\n")
        out = self.base / "out2"
        result = run_cli(self.cli, self.fake, "--suite", "legacy", "--output", str(out))
        self.assertEqual(result.returncode, 1)
        summary = json.loads((out / "summary.json").read_text())
        self.assertIs(summary["passed"], False)
        self.assertEqual(len(summary["results"]), 4)
        self.assertEqual(summary["results"][3]["exit_code"], 1)


if __name__ == "__main__":
    unittest.main()
