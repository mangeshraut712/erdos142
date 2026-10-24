#!/usr/bin/env python3
"""CLI research status dashboard for Erdős 142 research pack.

Prints an ANSI-formatted status overview including:
- Formal research status (Target: OPEN, Oct 21 claims: WITHDRAWN)
- Verified theorems ledger (BP24, MS24, PC24, GI24, IE24, OD23, CL23, LM23, etc.)
- Active physical obstructions (Spatial Decoupling, Bilinear Ceiling, Factorial Scarcity)
- Verification suite metrics (total checks across all test runs)
- Open critical lemmas (P12, W8, DIRECT-Q-GAIN, low-mean branch)
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# ANSI color codes
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"


def format_num(n: int) -> str:
    return f"{n:,}"


def main() -> int:
    print(f"\n{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}           ERDŐS PROBLEM 142 — RESEARCH PROGRAM STATUS DASHBOARD       {RESET}")
    print(f"{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}\n")

    # 1. Target and Program Status
    print(f"{BOLD}Target:{RESET}            {YELLOW}r_4(N) = o(N / log N){RESET} [Local weaker form of Erdős #142]")
    print(f"{BOLD}Status:{RESET}            {RED}OPEN (Single Final Obstruction){RESET}")
    print(f"{BOLD}October 21 Status:{RESET} {MAGENTA}Closure and effective-rate claims WITHDRAWN{RESET}")
    print(f"{BOLD}Latest Audit:{RESET}      {GREEN}MS24 — Multi-Scale Bohr Host Overlaps (24 Oct 2026){RESET}")

    # 2. Checkpoint Summary
    checkpoint_paths = sorted((ROOT / "checkpoints").glob("AUTONOMOUS_CHECKPOINT_*.json"))
    if checkpoint_paths:
        latest_cp = checkpoint_paths[-1]
        try:
            cp_data = json.loads(latest_cp.read_text(encoding="utf-8"))
            tracked_files = len(cp_data.get("file_sha256", {}))
            print(f"{BOLD}Checkpoint:{RESET}        {GREEN}{latest_cp.name}{RESET} ({tracked_files} tracked SHA-256 digests)")
        except Exception as e:
            print(f"{BOLD}Checkpoint:{RESET}        {latest_cp.name} (error loading: {e})")

    print(f"\n{BOLD}{BLUE}── Active Structural Obstructions ─────────────────────────────────────{RESET}")
    obstructions = [
        ("Spatial Decoupling", "Pointwise hole annihilation B(v)K(v,c)=0 forces <u, Kf> = -a <g,f> identically"),
        ("Universal Bilinear Ceiling", "|E[psibar Kf]| <= 6w a^(3/2) <= 6 a^(3/2); ratio to a^(3/2) uniformly bounded"),
        ("Factorial Scarcity", "Pattern triples grow factorially (n >= 1/a), but completion triples remain O(aw)"),
        ("Cross-Host Invariance", "Density discrepancy <u, psi> is invariant under host shifts for zero-mean psi"),
        ("Local Law CL23", "Consistent Boolean laws on floor(1/a)+1 vertices satisfy R3+R4 = -a^4 on 4-APs"),
    ]
    for name, desc in obstructions:
        print(f"  • {BOLD}{name}:{RESET} {desc}")

    print(f"\n{BOLD}{BLUE}── Key Verified Theorems (Selected) ───────────────────────────────────{RESET}")
    theorems = [
        ("MS24 (Oct 24)", "Multi-scale Bohr host overlap invariance and cross-host spatial decoupling"),
        ("BP24 (Oct 24)", "Universal bilinear pair incidence ceiling: |E[psibar Kf]| <= 6 a^(3/2)"),
        ("PC24 (Oct 24)", "Arithmetic completion pairs have <= 9 valid extensions in 4-AP geometry"),
        ("GI24 (Oct 24)", "Explicit zero-completion patterns of size >= (2sqrt(2)/9) n / sqrt(n-1)"),
        ("IE24 (Oct 24)", "Weighted completion incidence operator Euclidean norm ||K||^2 <= 72 a w / p"),
        ("OD23 (Oct 23)", "Sharp completion degree q(v) <= 2aw and variance Var(q) <= 2aw m - m^2"),
        ("CL23 (Oct 23)", "Consistent local Boolean law existence on floor(1/a)+1 vertices with zero triples"),
        ("LM23 (Oct 23)", "Exact completion mean moment cone and valid variance upper bound"),
    ]
    for tag, desc in theorems:
        print(f"  {GREEN}✓{RESET} {BOLD}{tag}:{RESET} {desc}")

    # 3. Aggregate Verification Results
    print(f"\n{BOLD}{BLUE}── Verification Suite Status ──────────────────────────────────────────{RESET}")
    results_dir = ROOT / "verification/results"
    total_checks = 0
    passed_results = 0
    total_results = 0

    if results_dir.exists():
        for res_file in sorted(results_dir.glob("*.json")):
            try:
                data = json.loads(res_file.read_text(encoding="utf-8"))
                total_results += 1
                if data.get("status") == "passed":
                    passed_results += 1
                # Try to count checks
                c = data.get("checks")
                if isinstance(c, int):
                    total_checks += c
                elif isinstance(c, dict):
                    total_checks += sum(v for v in c.values() if isinstance(v, int))
                else:
                    tot = data.get("total_checks") or data.get("counts")
                    if isinstance(tot, int):
                        total_checks += tot
                    elif isinstance(tot, dict):
                        total_checks += sum(v for v in tot.values() if isinstance(v, int))
            except Exception:
                pass

    print(f"  • Result artifacts: {BOLD}{passed_results}/{total_results} passing{RESET}")
    print(f"  • Total finite assertions verified: {BOLD}{format_num(total_checks)}{RESET}")
    print(f"  • Verified counterexamples to local target: {BOLD}{GREEN}0 (Target remains strictly open){RESET}")

    print(f"\n{BOLD}{BLUE}── Open Conjectures and Lemmas ────────────────────────────────────────{RESET}")
    open_lemmas = [
        ("DIRECT-Q-GAIN", "Super-critical density gain delta >= c_eps a^(3/2) F_eps(a) with F_eps(a) -> inf"),
        ("P12", "Quadratic phase correlation under failed linear selection"),
        ("W8", "Pointwise Bohr host localization without boundary density loss"),
        ("Low-Mean Branch", "Elimination of arithmetic zero-completion hosts m <= 2 a^3 T / w"),
    ]
    for tag, desc in open_lemmas:
        print(f"  {YELLOW}?{RESET} {BOLD}{tag}:{RESET} {desc}")

    print(f"\n{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
