Continue the OFFLINE Erdős #142 research in
/Users/mangeshraut/Downloads/erdos142-offline-20260906.

The unconditional target r_4(N)=o(N/log N) remains OPEN. Current outcome D.
Read AUTONOMOUS_CHECKPOINT_20261018.json, CURRENT_STATUS.md,
O2_CONTINUATION_20261018.md and OPEN_LEMMAS.md. Preserve historical files.
Nine verifiers passed isolated reruns; current evidence is under
history/continuation_20261018/verification/. Do not restart from older
October 17 recovery notes or repeat unchanged verification routinely.

Use the ORIGINAL mixed-window and weighted-pair proofs, not summaries
alone: MIXED_QUADRATIC_TERMINAL_20261016.md,
WEIGHTED_PAIR_REDUCTION_20261016.md and
DIRECT_INCREMENT_TRADEOFF_20261016.md. On the current trivial partition,
P=1_Omega, B=1_A, u=B-aP, w=|Omega|/p, a=|A|/|Omega|.
Original F(x,0)=1, tau=a²/log p, H=floor(tau wp/(48r)), mu=lambda(0,0,0).
The actual AP-free expansion is a^4T+R1+R2+R3+R4=aw/p, not zero.
On reachable hosts R1=o(main), R2>=-o(main), so R3+R4<=-(1-o(1))main.
The pair theorem is near-positivity, not exact PSD or two-sided smallness.

NEW proved results: Boolean occupancy2/3 terminal, twelve-slot7/11 terminal
under unchanged M13, exact DIRECT-Q-GAIN negation, direct cubic bound with
an explicit insufficient spectral/boundary envelope, original-weight
quartic covariance, four weighted completion channels and conditional
atomic/Gram certificate, and actual Boolean AP-free small-chirp sets at
polynomial density 1/3<theta<1/2. See dated notes in the checkpoint.
The polynomial-density sets fail the required density and diagonal
regimes and do not refute P12. All76 finite diagnostic records also fail
eligibility. No genuine P12 counterexample has been found.

PRIMARY NEXT ATTACK: WEIGHTED_QUARTIC_COVARIANCE_20261018.md W8.
Let U=wa(1-a), Q_u(c,t)=E_p u e_p(-cy²-ty),
s=(N-3C)/2, gamma=(N-5C)/2, m_s=E_p u² e_p(sy²),
D_s(c,t)=Q_u(c,t)conj(Q_u(c+s,t))-m_s/p,
phi(c,t)=(3c+gamma,3t-beta), and
E_F=sum lambda sum_(c,t)|D_s-D_s o phi|² (inner sums unnormalized).
PROVED: R4=U²-E_F/2. Under failed adequate selection, prove

    E_F<=2U²+2R3+a^4wmu.

This is exactly OPEN P12: R3+R4>=-a^4wmu/2. Keep R3 and proper-host
corrections. Nonnegative energy is subtracted and cannot give the desired
lower bound without a new upper estimate. The existing direct cubic
estimate has the wrong quantitative scale. Do not call W8 proved.

ALTERNATIVE: prove the completion certificate in
WEIGHTED_COMPLETION_CERTIFICATE_20261018.md and handle small/zero mean.
Its conditional implication and disjoint-six-point lower bound are
proved; certificate existence and low-completion closure are OPEN.

DIRECT-Q-GAIN needs, for every epsilon, constants and a uniform divergent
F_epsilon(a)>=1 such that delta>=c_epsilon a^(3/2)F_epsilon(a), on
r[log(1/w)+log(48r)+loglog p]<=logp/100 and
epsilon/(2log|Omega|)<=a<=4/5. Constants precede the instance.
The concrete R(a)=loglog(e²/a) suffices by the unchanged quarter-cell
tradeoff mu_C gamma>=kappa delta/(8a); extra sqrtlog is unnecessary.
Exact negation has both eligible-sequence branches in the Oct17 note.

Prioritize theorem/proof work; audit exact exponents, normalization,
Booleanity, AP exclusion, all finite-p errors and domain restrictions.
Finite computation supports proofs, never substitutes for asymptotics.
Do not use a generic real weight or pseudo-moment law as an actual set.
Do not claim a complete sufficient replacement when its existence
premise is missing. Update all nine requested status/ledger files and
save an exact dated checkpoint before ending. No background work is
running merely because this resume prompt exists.
