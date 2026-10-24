<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

## Description

Briefly describe the contribution: audit, new finite verifier, identity proof, or tooling improvement.

## Mathematical Claims and Boundaries

- [ ] Does **not** claim an asymptotic theorem for $r_4(N)$ or close official Erdős #142 unless formally peer-reviewed.
- [ ] Explicitly states all hypotheses (cyclic group $\mathbb{F}_p$, interval/Bohr host, relative density $a$, weight $w$).
- [ ] Any failed approaches or obstructions are documented in `FAILED_APPROACHES.md`.

## Verification and Quality Checks

- [ ] Finite verifier added or updated in `verification/scripts/`.
- [ ] Registered in `verification/run_current.py` (if part of current suite).
- [ ] `python verification/check_repository.py` passes with zero errors.
- [ ] `python verification/generate_dashboard.py --check` passes.
- [ ] `python -m unittest discover tests` passes.
- [ ] Latest checkpoint hashes updated via `python verification/update_checkpoint_hashes.py`.

## Commits & Attribution

- [ ] Signed-off commit: `Signed-off-by: Name <email>`
- [ ] No robotic co-author trailers (`Co-authored-by`).
