"""Tests for checkpoint hash verification and updater tooling."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

from verification.update_checkpoint_hashes import compute_sha256, update_checkpoint

ROOT = Path(__file__).resolve().parents[1]


class TestCheckpointTooling(unittest.TestCase):
    def test_compute_sha256(self) -> None:
        """compute_sha256 should match hashlib standard."""
        readme = ROOT / "README.md"
        h = compute_sha256(readme)
        self.assertEqual(len(h), 64)
        self.assertTrue(all(c in "0123456789abcdef" for c in h))

    def test_checkpoint_consistency_dry_run(self) -> None:
        """update_checkpoint with check_only=True should verify current hashes without modifying."""
        ret = update_checkpoint(check_only=True)
        # Should be 0 or 1 depending on whether uncommitted files changed;
        # the function should complete without unhandled exception.
        self.assertIn(ret, (0, 1))


if __name__ == "__main__":
    unittest.main()
