#!/usr/bin/env python3
"""Update SHA-256 digests in the latest autonomous checkpoint file.

This tool recomputes hashes for all files currently tracked in the latest
checkpoint's `file_sha256` dictionary. It can also optionally track new files
passed as arguments.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def compute_sha256(path: Path) -> str:
    """Compute hex-encoded SHA-256 for a file."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_checkpoint(add_files: list[str] | None = None, check_only: bool = False) -> int:
    checkpoint_paths = sorted((ROOT / "checkpoints").glob("AUTONOMOUS_CHECKPOINT_*.json"))
    if not checkpoint_paths:
        sys.stderr.write("No checkpoint file found in checkpoints/\n")
        return 1

    latest_cp_path = checkpoint_paths[-1]
    data = json.loads(latest_cp_path.read_text(encoding="utf-8"))
    file_hashes: dict[str, str] = data.get("file_sha256", {})

    if add_files:
        for f in add_files:
            rel = str(Path(f).resolve().relative_to(ROOT))
            if rel not in file_hashes:
                file_hashes[rel] = ""

    mismatches: list[tuple[str, str, str]] = []
    missing_files: list[str] = []
    new_hashes: dict[str, str] = {}

    for rel_path in sorted(file_hashes.keys()):
        full_path = ROOT / rel_path
        if not full_path.exists():
            missing_files.append(rel_path)
            continue
        actual = compute_sha256(full_path)
        new_hashes[rel_path] = actual
        expected = file_hashes.get(rel_path, "")
        if actual != expected:
            mismatches.append((rel_path, expected, actual))

    if missing_files:
        sys.stderr.write(f"Warning: {len(missing_files)} tracked files missing on disk:\n")
        for m in missing_files[:5]:
            sys.stderr.write(f"  {m}\n")

    if check_only:
        if mismatches:
            print(f"FAILED: {len(mismatches)} hash mismatches found.")
            for rel, exp, act in mismatches[:10]:
                print(f"  {rel}: expected {exp[:12]}..., got {act[:12]}...")
            return 1
        print(f"PASSED: All {len(new_hashes)} tracked file hashes match {latest_cp_path.name}.")
        return 0

    data["file_sha256"] = new_hashes
    latest_cp_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {len(new_hashes)} file hashes in {latest_cp_path.name} ({len(mismatches)} changed).")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Update or check SHA-256 hashes in latest checkpoint.")
    parser.add_argument("--add", nargs="*", default=[], help="Additional file paths relative to root to track.")
    parser.add_argument("--check", action="store_true", help="Check hashes without updating the checkpoint.")
    args = parser.parse_args()

    sys.exit(update_checkpoint(add_files=args.add, check_only=args.check))


if __name__ == "__main__":
    main()
