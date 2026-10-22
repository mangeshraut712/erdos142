#!/usr/bin/env python3
"""Check current navigation, Python syntax, JSON, and latest checkpoint hashes."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    if not __debug__ or os.environ.get("PYTHONOPTIMIZE"):
        raise SystemExit("Assertions must be enabled; remove -O and PYTHONOPTIMIZE.")
    scripts = sorted(set(ROOT.glob("*.py")) | set((ROOT / "verification").rglob("*.py")))
    for script in scripts:
        ast.parse(script.read_text(), filename=str(script.relative_to(ROOT)))
    reports = sorted(set(ROOT.glob("*.json")) | set((ROOT / "checkpoints").rglob("*.json"))
                     | set((ROOT / "history").rglob("*.json"))
                     | set((ROOT / "verification").rglob("*.json")))
    for report in reports:
        json.loads(report.read_text())
    navigation = ["README.md", "CURRENT_STATUS.md", "OPEN_LEMMAS.md", "VERIFYING.md",
                  "NEXT_AUTONOMOUS_ACTION.md", "docs/audits/O2_CONTINUATION_20261019.md",
                  "docs/README.md", "docs/PROGRESS.md", "docs/ROADMAP.md",
                  "SOLUTION_LEDGER.md", "PROOF_DEPENDENCIES.md", "VERIFIED_THEOREMS.md",
                  "FAILED_APPROACHES.md", "RESEARCH_JOURNAL.md", "AUTONOMOUS_RESUME_PROMPT.md",
                  "docs/PEER_REVIEW_GUIDE.md", "docs/manuscript/README.md",
                  "formalization/lean/README.md", "docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md"]
    links = 0
    for name in navigation:
        source = ROOT / name
        for target in re.findall(r"\]\(([^)]+)\)", source.read_text()):
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0].strip("<>")
            if relative:
                assert (source.parent / relative).exists(), f"Broken link in {name}: {target}"
                links += 1
    checkpoint_path = sorted((ROOT / "checkpoints").glob("AUTONOMOUS_CHECKPOINT_*.json"))[-1]
    checkpoint = json.loads(checkpoint_path.read_text())
    assert checkpoint["target_proved"] is False, "The current research target is still open."
    hashes = checkpoint["file_sha256"]
    assert hashes, "The latest checkpoint must contain source hashes."
    for name, digest in hashes.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        assert actual == digest, f"Checkpoint hash mismatch: {name}"
    print(json.dumps({"status": "passed", "python_files": len(scripts), "json_files": len(reports),
                      "local_links": links, "checkpoint": checkpoint_path.name,
                      "checkpoint_hashes": len(hashes)}, indent=2))


if __name__ == "__main__":
    main()
