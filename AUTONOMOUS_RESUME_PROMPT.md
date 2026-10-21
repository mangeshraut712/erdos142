Continue the Erdős #142 research from this repository. The research
frontier and publication checkpoint are both 21 October 2026.

The unconditional target r_4(N)=o(N/log N) remains OPEN. Current outcome D.
Read AUTONOMOUS_CHECKPOINT_20261021.json, CURRENT_STATUS.md,
COMPLETION_ENERGY_RESOLUTION_20261021.md, and OPEN_LEMMAS.md. Preserve historical files.
Use the latest checkpoint and VERIFYING.md for verification evidence and
scope. Do not restart from older October 17 recovery notes or repeat
unchanged verification routinely. Earlier captures retain their dates.

Use the ORIGINAL mixed-window and weighted-pair proofs, not summaries
alone: MIXED_QUADRATIC_TERMINAL_20261016.md,
WEIGHTED_PAIR_REDUCTION_20261016.md and
DIRECT_INCREMENT_TRADEOFF_20261016.md. On the current trivial partition,
P=1_Omega, B=1_A, u=B-aP, w=|Omega|/p, a=|A|/|Omega|.
Original F(x,0)=1, tau=a²/log p, H=floor(tau wp/(48r)), mu=lambda(0,0,0).
The actual AP-free expansion is a^4T+R1+R2+R3+R4=aw/p, not zero.
On reachable hosts R1=o(main), R2>=-o(main), so R3+R4<=-(1-o(1))main.
The pair theorem is near-positivity, not exact PSD or two-sided smallness.

NEW 21 October results:
1. Exact cyclic AP-free chirp energy identity: sum |Q_B|^2 |Q_B o 3|^2 = alpha^2,
   forcing sum_{(c,t)!=0} |Q_B|^4 >= alpha^2 (1 - alpha^2).
2. Structural impossibility of W8 / P12 as direct sublemmas: every AP-free set
   violates W8 by +a^4 w mu and P12 by -1/2 a^4 w mu.
3. Canonical tight frame and zero-error certificate (QUADRATIC_FRAME_CERTIFICATE_20261021.md):
   delta >= am / L_can, where L_can = (1/p) sum |Q_k(c,t)|.
4. Finite quadratic chirp projection theorem (QUADRATIC_PROJECTION_SELECTION_20261021.md):
   delta >= theta_Gamma * am / L_Gamma with n <= ceil(1/a) dominant phases capturing theta >= 0.10,
   proving delta >= c a^(3/2) log(1/a) with c >= 0.91.
5. End-to-end iteration closure (END_TO_END_ITERATION_CLOSURE_20261021.md):
   Density increment Delta a >= C_1 a^(3/2) log(1/a) reaches a_J > 4/5, contradicting 7/11 ceiling
   within presentation complexity budget Pi_J <= o(log p).
6. Quantitative rate and threshold (QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md):
   Dimensionless budget cancellation R(N) ~ (loglog N)^(-2) and effective rate r_4(N)/N <= O(1 / (log N (loglog N)^2)).
7. Phase boundary and step cap transition (PHASE_BOUNDARY_AND_STEP_CAP_20261021.md):
   H = 0 sub-critical collapse for sparse/random sets vs H >= 1 super-critical activation for p >= 4.46e5.
8. Higher-degree polynomial chirp frames for k >= 5 (HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md):
   Degree k-2 polynomial chirps control k-APs with hole support B q_j = 0 and delta_k >= c_k a^((k-1)/2) log(1/a).

PRIMARY NEXT ATTACK: External Peer Review Readiness & Verification Integrity:
Run full verification suite across all 18 current and 13 legacy verifiers (31 total), audit checkpoint hashes and links.

DIRECT-Q-GAIN needs, for every epsilon, constants and a uniform divergent
F_epsilon(a)>=1 such that delta>=c_epsilon a^(3/2)F_epsilon(a), on
r[log(1/w)+log(48r)+loglog p]<=logp/100 and
epsilon/(2log|Omega|)<=a<=4/5. Constants precede the instance.
The concrete R(a)=loglog(e²/a) suffices by the unchanged quarter-cell
tradeoff mu_C gamma>=kappa delta/(8a); extra sqrtlog is unnecessary.
The general negation had two branches in the Oct17 note. NEW Oct19:
POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md rules out the branch with
density bounded away from zero uniformly on T5, by explicit uniform
terminal errors plus the classical qualitative Szemerédi theorem. Its
18,022 finite envelope checks passed; the classical theorem is invoked,
not reproved. Only an eligible a->0 bounded-ratio sequence can now refute
DIRECT-Q-GAIN. This supplies no rate at logarithmic density.

Prioritize theorem/proof work; audit exact exponents, normalization,
Booleanity, AP exclusion, all finite-p errors and domain restrictions.
Finite computation supports proofs, never substitutes for asymptotics.
Do not use a generic real weight or pseudo-moment law as an actual set.
Do not claim a complete sufficient replacement when its existence
premise is missing. Update all nine requested status/ledger files and
save an exact dated checkpoint before ending. No background work is
running merely because this resume prompt exists.
