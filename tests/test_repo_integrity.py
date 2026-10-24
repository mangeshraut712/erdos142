"""Repository structural integrity and navigation tests for Erdős 142."""
from __future__ import annotations

import ast
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestRepoIntegrity(unittest.TestCase):
    def test_all_python_files_syntax(self) -> None:
        """Every Python file in root and verification/ must parse with valid AST."""
        scripts = sorted(set(ROOT.glob("*.py")) | set((ROOT / "verification").rglob("*.py")) | set((ROOT / "tests").rglob("*.py")))
        self.assertGreater(len(scripts), 0, "No Python scripts found")
        for script in scripts:
            with self.subTest(script=str(script.relative_to(ROOT))):
                code = script.read_text(encoding="utf-8")
                try:
                    ast.parse(code, filename=str(script.relative_to(ROOT)))
                except SyntaxError as e:
                    self.fail(f"Syntax error in {script.relative_to(ROOT)}: {e}")

    def test_all_json_files_valid(self) -> None:
        """Every JSON file in root, checkpoints/, history/, and verification/ must be valid JSON."""
        reports = sorted(
            set(ROOT.glob("*.json"))
            | set((ROOT / "checkpoints").rglob("*.json"))
            | set((ROOT / "history").rglob("*.json"))
            | set((ROOT / "verification").rglob("*.json"))
        )
        self.assertGreater(len(reports), 0, "No JSON reports found")
        for report in reports:
            with self.subTest(json_file=str(report.relative_to(ROOT))):
                try:
                    data = json.loads(report.read_text(encoding="utf-8"))
                    self.assertIsInstance(data, (dict, list))
                except Exception as e:
                    self.fail(f"Invalid JSON in {report.relative_to(ROOT)}: {e}")

    def test_navigation_markdown_links(self) -> None:
        """Verify that relative links in key navigation Markdown files resolve to existing files."""
        navigation_files = [
            "README.md",
            "CURRENT_STATUS.md",
            "OPEN_LEMMAS.md",
            "VERIFYING.md",
            "NEXT_AUTONOMOUS_ACTION.md",
            "docs/README.md",
            "docs/PROGRESS.md",
            "docs/ROADMAP.md",
            "SOLUTION_LEDGER.md",
            "PROOF_DEPENDENCIES.md",
            "VERIFIED_THEOREMS.md",
            "FAILED_APPROACHES.md",
            "RESEARCH_JOURNAL.md",
            "AUTONOMOUS_RESUME_PROMPT.md",
            "docs/PEER_REVIEW_GUIDE.md",
            "docs/manuscript/README.md",
            "formalization/lean/README.md",
            "docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md",
            "docs/audits/BILINEAR_PAIR_INCIDENCE_20261024.md",
            "docs/audits/MULTISCALE_BOHR_OVERLAPS_20261024.md",
        ]
        total_links = 0
        for name in navigation_files:
            source = ROOT / name
            if not source.exists():
                continue
            for target in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
                if target.startswith(("http:", "https:", "mailto:", "#")):
                    continue
                relative = target.split("#", 1)[0].strip("<>")
                if relative:
                    resolved = (source.parent / relative).resolve()
                    self.assertTrue(
                        resolved.exists(),
                        f"Broken link in {name}: '{target}' points to non-existent '{resolved}'",
                    )
                    total_links += 1
        self.assertGreater(total_links, 100, f"Expected >100 local links checked, got {total_links}")

    def test_latest_checkpoint_structure(self) -> None:
        """Latest checkpoint file must exist, assert target is open, and specify file hashes."""
        checkpoint_paths = sorted((ROOT / "checkpoints").glob("AUTONOMOUS_CHECKPOINT_*.json"))
        self.assertGreater(len(checkpoint_paths), 0, "No checkpoint files found in checkpoints/")
        latest = checkpoint_paths[-1]
        data = json.loads(latest.read_text(encoding="utf-8"))
        self.assertIn("target_proved", data)
        self.assertFalse(data["target_proved"], "Current research target should not be falsely marked proved")
        self.assertIn("file_sha256", data)
        self.assertGreater(len(data["file_sha256"]), 800, "Checkpoint should track >800 repository files")


if __name__ == "__main__":
    unittest.main()
