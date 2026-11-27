"""Regression test: _probe_terminal.max_block_gain must not crash and must match brute force."""
from __future__ import annotations

from fractions import Fraction as F
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "verification" / "scripts"


def _load():
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location("_probe_terminal", SCRIPTS / "_probe_terminal.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _brute_force(bits, min_len):
    n, m = len(bits), sum(bits)
    a = F(m, n)
    best, best_len = F(0), 0
    for i in range(n):
        for j in range(i + min_len, n + 1):
            gain = F(sum(bits[i:j]), j - i) - a
            if gain > best:
                best, best_len = gain, j - i
    return best, best_len


class TestProbeTerminal(unittest.TestCase):
    def test_max_block_gain_matches_brute_force(self) -> None:
        probe = _load()
        for bits, min_len in (
            ([1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 2),
            ([0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1], 3),
            ([int(x in (0, 20, 22, 25, 30, 32)) for x in range(40)], 4),
        ):
            self.assertEqual(probe.max_block_gain(list(bits), min_len), _brute_force(list(bits), min_len))


if __name__ == "__main__":
    unittest.main()
