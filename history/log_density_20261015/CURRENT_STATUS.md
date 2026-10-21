# Current research status — 15 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM.**
The local target `r_4(N)=o(N/log N)` remains **OPEN**. No unconditional
SELECT, WSELECT, SIGNED, or COLLECTIVE-WSELECT theorem is claimed.

The latest audit is `RESIDUAL_FIELD_AUDIT_20261015.md`. The new terminal
counting theorem is `QUADRATIC_LOCALIZATION_20261015.md`.

- **PROVED:** For a single quadratic interval host of phase density beta,
  a 4-AP-free subset has relative density at most
  `3/4 + 20(2+log p)/(beta p^(1/6))` under the explicit size conditions
  in (Q1)–(Q4). Hence the bound is `3/4+o(1)` when
  `beta p^(1/6)/(2+log p) -> infinity`. Weighted progression counts,
  rather than translation packing, prove this result.
- **PROVED:** There exist actual cyclic AP-free sets at density comparable
  to `p^(-3/5)` with nonzero completion pairing but with every packet of
  `O(a^(-1/4)/ell(a))` frequencies capturing a vanishing fraction of it.
  This is outside SELECT's logarithmic-density hypotheses; it is not a
  counterexample to SELECT or the target.
- **AUDITED CONDITIONAL IMPLICATION:** A packet capturing a theta-fraction
  of the nonnegative thresholded completion pairing forces
  `max |c_xi|^2 >= theta^2 gamma^2 a^2/(s^2 w^2)`.
  The largest sufficient packet scale from this inequality is
  `s <= theta gamma/(w sqrt(c)) a^(-1/4)ell(a)^(-1/2)`.
  Existence of such a packet and retention after thresholding remain open.
- **CORRECTIONS:** The dyadic-shell sufficient cutoff improves from
  `a^(-3/4)ell^(-7/2)` to `a^(-3/4)ell^(-5/2)`. The earlier stronger
  restrictions were sufficient, not sharp. Conditional and globally
  centered Gram matrices must be distinguished. The old quadratic
  terminal claim needs an asymptotic size condition and distinct phase
  and host densities.

Verification: the residual-field, quadratic-to-linear, and core legacy
scripts passed their finite checks in a temporary directory. The independent
new script separates integer/rational checks from floating Fourier checks:
`python3 verify_residual_field_audit_20261015.py`.
See `RESIDUAL_FIELD_AUDIT_VERIFICATION_20261015.json` for actual coverage.
The entire October 2 conditional chain was not re-audited in this run.

The unresolved structural dependency is still a density increment with
adequate energy per character in the original admissible windows, or a
separate quadratic increment architecture with proved cumulative losses.
The single quadratic-host terminal theorem does not establish either.

Historical checkpoint files were saved before editing under
`history/audit_20261015_residual_field/`. No historical research note or
legacy verifier was overwritten. Resume from `AUTONOMOUS_RESUME_PROMPT.md`.
