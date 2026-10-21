#!/usr/bin/env python3
"""Run checked-in verifiers in an isolated copy, preserving saved evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
CURRENT = [
    "verification/scripts/verify_boolean_occupancy_20261017.py",
    "verification/scripts/verify_boolean_o2_diagnostics_20261017.py",
    "verification/scripts/verify_o2_cubic_quantifiers_20261017.py",
    "verification/scripts/verify_finite_pattern_terminal_20261018.py",
    "verification/scripts/verify_o2_cubic_audit_20261018.py",
    "verification/scripts/verify_weighted_completion_20261018.py",
    "verification/scripts/verify_weighted_quartic_covariance_20261018.py",
    "verification/scripts/verify_boolean_alteration_chirp_20261018.py",
    "verification/scripts/verify_boolean_typical_alteration_20261018.py",
    "verification/scripts/verify_positive_density_branch_20261019.py",
    "verification/scripts/verify_o2_covariance_attack_20261019.py",
    "verification/scripts/verify_completion_energy_resolution_20261021.py",
    "verification/scripts/verify_quadratic_frame_certificate_20261021.py",
    "verification/scripts/verify_quadratic_projection_selection_20261021.py",
]
LEGACY = [
    f"verification/scripts/{name}.py"
    for name in (
        "verify_ap_richness", "verify_compat", "verify_compatibility",
        "verify_core", "verify_endpoint_incidence", "verify_energy_counterexample",
        "verify_full_group_energy", "verify_increment", "verify_localization",
        "verify_mixed", "verify_phase2", "verify_relative", "verify_signed",
    )
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", choices=["current", "legacy", "all"], default="current")
    parser.add_argument("--output", type=Path,
                        help="Log directory outside the checkout or under .verification-runs/")
    args = parser.parse_args()
    if not __debug__ or os.environ.get("PYTHONOPTIMIZE"):
        parser.error("Assertions must be enabled; remove -O and PYTHONOPTIMIZE.")
    paths = CURRENT.copy() if args.suite != "legacy" else []
    if args.suite != "current":
        paths += LEGACY
    if not paths or any(not (ROOT / p).is_file() for p in paths):
        parser.error("A selected verifier is missing; run from a complete checkout.")
    numpy_version = None
    if args.suite != "legacy":
        try:
            import numpy
        except ImportError:
            parser.error('Current verifiers require NumPy: python -m pip install -e ".[verification]"')
        numpy_version = numpy.__version__
    output = args.output.resolve() if args.output else None
    # Put reports outside the temporary copy; never overwrite original captures.
    if output:
        if output.is_relative_to(ROOT) and not output.is_relative_to(ROOT / ".verification-runs"):
            parser.error("Inside this checkout, output must be under .verification-runs/ to preserve saved evidence.")
        output.mkdir(parents=True, exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix="erdos142-verify-") as directory:
        copied = Path(directory) / "repo"
        ignore = shutil.ignore_patterns(".git", ".venv", "__pycache__", "*.pyc", ".verification-runs", "node_modules", ".next")
        # Copy symlink targets as ordinary files so a verifier cannot write
        # through a preserved link into the original checkout.
        shutil.copytree(ROOT, copied, ignore=ignore, symlinks=False)
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["PYTHONPATH"] = os.pathsep.join([str(copied), str(copied / "verification/scripts")])
        for path in paths:
            started = time.monotonic()
            source_hash = hashlib.sha256((copied / path).read_bytes()).hexdigest()
            process = subprocess.run([sys.executable, str(copied / path)], cwd=copied, env=env,
                                     capture_output=True, text=True)
            result = {"script": path, "exit_code": process.returncode,
                      "seconds": round(time.monotonic() - started, 3),
                      "source_sha256": source_hash}
            try:
                payload = json.loads(process.stdout)
                if isinstance(payload, dict):
                    result["reported_checks"] = next((payload[k] for k in ("total_checks", "checks", "counts") if k in payload), None)
            except json.JSONDecodeError:
                pass
            results.append(result)
            print(f"{'PASS' if process.returncode == 0 else 'FAIL'} {path}", flush=True)
            if output:
                (output / (Path(path).name + ".stdout")).write_text(process.stdout)
                (output / (Path(path).name + ".stderr")).write_text(process.stderr)
            if process.returncode:
                print(process.stderr[-5000:] or process.stdout[-5000:], file=sys.stderr)
                break
    report = {"suite": args.suite, "python": sys.version.split()[0], "numpy": numpy_version,
              "isolated": True, "saved_reports_overwritten": False,
              "passed": len(results) == len(paths) and all(x["exit_code"] == 0 for x in results),
              "results": results,
              "scope": "Selected current and/or original September verifiers, not every archived experiment; no asymptotic target proof."}
    if output:
        (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
