---
name: Mathematical Audit or Countercheck
about: Report a gap, counterexample, or precision issue in an audit or identity.
title: "[Audit]: "
labels: ["audit", "mathematics"]
assignees: ["mangeshraut712"]
---

### Target Audit / Identity

Specify the document or theorem (e.g., `BILINEAR_PAIR_INCIDENCE_20261024.md`, `MULTISCALE_BOHR_OVERLAPS_20261024.md`, BP24, MS24, OD23, CL23, etc.).

### Observed Issue or Obstruction

Explain clearly:
1. Exact hypothesis or parameter regime where the gap occurs.
2. Analytic failure, reversed inequality, or missing cross-term.
3. Finite counterexample configuration (prime $p$, subset $A$, host $\Omega$).

### Verifier Script or Minimal Reproducer

```python
# Minimal Python reproducer
```

### Proposed Resolution

- [ ] Modify theorem statement to restrict hypothesis.
- [ ] Add explicit countercheck to `verification/scripts/`.
- [ ] Update `FAILED_APPROACHES.md` and ledger.
