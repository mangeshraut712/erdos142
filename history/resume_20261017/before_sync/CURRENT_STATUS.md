# Current research status — 16 October 2026

**Principal status: (D) NEW RIGOROUS PARTIAL THEOREM.**
The local target `r_4(N)=o(N/log N)` remains **OPEN**.
No unconditional selection or density-increment theorem is claimed.

The latest proofs are `MIXED_QUADRATIC_TERMINAL_20261016.md` and
`LOG_DENSITY_ATTACK_20261016.md`. They supersede the claim that stable
mixed-window terminal geometry is still an unresolved dependency.

- **PROVED:** A terminal counting theorem for intersections of arbitrary
  linear and quadratic intervals, including repeated and resonant phases.
  AP-free relative density is at most `3/4+o(1)` when rank and logarithmic
  size loss are both `o(sqrt(log p))`. Equations (M1), (M12), and (L14)
  give explicit finite errors and a broader product-budget regime.
- **PROVED:** Direct extraction of one quarter-arc cell from a relative
  phase correlation delta: density gain at least `kappa delta/8`, and
  retained occupied mass at least `kappa delta/(8a)`, on the same cell.
  Here kappa=2sqrt(2)/pi; the residual is B-a on the current window.
- **PROVED CONDITIONAL IMPLICATION:** DIRECT-Q-P implies the local target.
  Its required correlation is `c_epsilon a^(3/2)sqrt(ell(a))R(a)`, where
  ell=log(2/a), R=loglog(e^2/a). Its explicit host domain is (L10).
  At initial density epsilon/log N, writing L=log N, cumulative rank is
  `O(sqrt(L)/(sqrt(log L)loglog L)+log L)` and logarithmic size loss is
  `O(sqrt(L)sqrt(log L)/loglog L+(log L)^2)`. Their product is o(L).
  The structural hypothesis DIRECT-Q-P is **OPEN**.
- **PROVED:** For the new weighted count on reachable hosts, the linear
  residual is `o(a^4 w mu)` with the finite bound (M16). The remaining
  signed residual involves degrees 2--4, not a first-order boundary error.
- **PROVED:** The sparse diffuse-completion construction extends to every
  fixed `a` comparable to `p^(-theta)`, 1/2<theta<2/3. This is outside the
  logarithmic-density regime and does not refute the local target.
- **REFUTED AUXILIARY CLAIM:** Positive-Fourier tent weights do not make
  the actual arithmetic pair kernel PSD. An exact p=53 witness is given.
  It is a bounded weighted function, not a Boolean AP-free counterexample.

The remaining squared-signal gap for DIRECT-Q-P is
`a^(-1)ell(a)R(a)^2` relative to an available squared signal a^4.
This diverges at a=epsilon/log N; constant improvements cannot close it.
Neither a U^3 signal nor the new terminal theorem proves phase correlation.
The old SELECT, WSELECT, SIGNED and COLLECTIVE-WSELECT inputs remain OPEN.

Verification: the October 15 independent verifier passed its 21,465 checks
again in an isolated directory. The new verifier passes 1,642 finite checks,
separating exact weights, diagonals and rational witnesses from floating
Fourier identities. See `LOG_DENSITY_VERIFICATION_20261016.json`.
Finite checks support the proofs; they do not establish selection for all p.

Before-change checkpoint copies are in `history/log_density_20261015/`;
new diagnostic evidence is in `history/log_density_20261016/`.
No historical research note or verification output was overwritten.
Resume using `AUTONOMOUS_RESUME_PROMPT.md` and the machine checkpoint
`AUTONOMOUS_CHECKPOINT_20261016.json`. No background computation is running.
