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

NEW 21 October results (COMPLETION_ENERGY_RESOLUTION_20261021.md):
1. Exact cyclic AP-free chirp energy identity: sum |Q_B|^2 |Q_B o 3|^2 = alpha^2,
   forcing sum_{(c,t)!=0} |Q_B|^4 >= alpha^2 (1 - alpha^2).
2. Exact completion-residual dual system:
   R4^{h!=0} = 3 a^4 T^{h!=0} - a w m + 2 R1^{h!=0} + R2^{h!=0},
   R3^{h!=0} = -4 a^4 T^{h!=0} + a w m - 3 R1^{h!=0} - 2 R2^{h!=0}.
3. Structural impossibility of W8 / P12 as direct sublemmas: every AP-free set
   violates W8 by +a^4 w mu and P12 by -1/2 a^4 w mu, while the Oct 19 block set
   violates them without AP exclusion. W8 and P12 cannot serve as intermediate steps.
4. Elimination of the small/zero-mean completion branch in O3:
   m >= 4 a^3 mu (1 - o(1)) > 0 unconditionally on reachable hosts.
5. Geometric alignment: correlation between u and -k approaches 1 - a -> 1.

PRIMARY NEXT ATTACK: Open Lemma O3 (WEIGHTED_COMPLETION_CERTIFICATE_20261018.md).
With m > 0 unconditionally guaranteed, prove existence of a quadratic phase representation
for the centered completion field k = q - m:
    k = sum c_chi (chi - E_Omega chi) + e,
    sum |c_chi| <= m / (2 sqrt(a) R(a)),
    ||e||_{L2(Omega)} <= (m/2) sqrt(a / (1-a)),
or use the cubic non-linear integral alignment u ~ -(1-a)/m * k to extract phase correlation
directly without full spectral expansion.

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
