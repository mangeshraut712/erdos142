# Open lemmas — operative checkpoint, 21 October 2026

The target `r_4(N)=o(N/log N)` remains OPEN. Current outcome is D.
The previous list is preserved in
`history/publication_20261021/before_updates/OPEN_LEMMAS.md`.
The mathematical frontier is [the October 19 continuation](docs/audits/O2_CONTINUATION_20261019.md);
the publication state is `AUTONOMOUS_CHECKPOINT_20261021.json`.
Terminal geometry, Boolean occupancy and the exact covariance identities
are proved; the missing input is still arithmetic phase selection.

## O1. DIRECT-Q-GAIN, with all quantifiers retained

For every epsilon>0 seek c_epsilon>0, p_epsilon, and
F_epsilon:(0,4/5]->[1,infinity), with F_epsilon(a)->infinity as a->0,
such that every prime p>=p_epsilon, every nonempty mixed circular-interval
host Omega with its specified presentation r=d+s>=1 satisfying

    r[log(p/|Omega|)+log(48r)+loglog p]<=log p/100,

and every actual cyclically nonzero-4AP-free A subset Omega with

    epsilon/(2log|Omega|)<=a=|A|/|Omega|<=4/5

obey

    delta=max_(c,t)!=(0,0)|E_Omega(1_A-a)e_p(-cx^2-tx)|
           >=c_epsilon a^(3/2)F_epsilon(a).

This is the current-mean residual on the trivial partition of Omega.
Constants/functions are chosen before the instance. The proved
conditional iteration in `DIRECT_INCREMENT_TRADEOFF_20261016.md` needs
any uniform divergent multiplier, with `loglog(e^2/a)` a concrete choice.
The obsolete extra sqrt(log(2/a)) is unnecessary. A proved adequate
reachable subclass retaining the initial interval would also suffice.

The EXACT negation is: for some epsilon>0, for every c>0,p0,and divergent
F>=1, there is an eligible triple p>=p0 with delta<c a^(3/2)F(a).
Equivalently, an eligible sequence has either (i) a->0 and delta/a^(3/2)
bounded above, or (ii) p->infinity, inf a>0, and delta/a^(3/2)->0.
The general logical equivalence is proved in
`O2_QUANTIFIERS_CUBIC_BOUND_20261017.md`. NEW: branch (ii) is now excluded
on T5 by `POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md`, using the
explicit classical qualitative four-term Szemerédi theorem. Consequently
failure is equivalent to branch (i) alone. The new uniform finite errors
include PD2--PD7 and the first-moment bound PD7b; the qualitative input supplies no rate at a~1/log p.
Counterexamples to one fixed multiplier or ineligible sparse sets do not
supply the remaining sequence.

## O2. P12 / W8: structural resolution and refutation as direct sublemmas

Retain the original F, tau=a^2/log p, H=floor(tau wp/(48r)),
mu=lambda(0,0,0), w=|Omega|/p, u=1_A-a1_Omega, and U=wa(1-a).
The exact expansion has diagonal aw/p. The proved reachable-host
estimates give R1=o(a^4wmu), R2>=-o(a^4wmu), and

    Q=R3+R4<=-(1-o(1))a^4wmu.

Under failed adequate selection, the earlier attempted lower bound was

    Q>=-(1/2)a^4wmu.                                    (P12)

It is exactly equivalent at finite p to the bound

    E_F(u)<=2U^2+2R3+a^4wmu.                             (W8)

NEW (21 October 2026, [COMPLETION_ENERGY_RESOLUTION_20261021.md](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md)):
Every 4-AP-free set has $E_F(u) = 2 U^2 + 2 R_3 + 2 a^4 T + 2 R_1 + 2 R_2 - 2aw/p$,
which forces $E_F(u) - (2 U^2 + 2 R_3 + a^4 w \mu) = a^4 w \mu (1 - o(1)) > 0$ and
$Q - (-1/2 a^4 w \mu) = -1/2 a^4 w \mu (1 + o(1)) < 0$.
Thus every AP-free set strictly violates W8 and P12.
Meanwhile, the 19 October construction in [O2_COVARIANCE_ATTACK_20261019.md](docs/audits/O2_COVARIANCE_ATTACK_20261019.md)
refutes W8 and P12 under failed selection without AP exclusion ($Q <= -11/20 a^4 w \mu$).
Therefore W8 and P12 are **mathematically false across all branches** and cannot serve
as intermediate lemmas.

The direct residual relations coupling pointwise hole support $B q_j = 0$ to $R_3, R_4$ are now exact:
    R4^{h!=0} = 3 a^4 T^{h!=0} - a w m + 2 R_1^{h!=0} + R_2^{h!=0},
    R3^{h!=0} = -4 a^4 T^{h!=0} + a w m - 3 R_1^{h!=0} - 2 R_2^{h!=0}.

## O3. Completion certificate: resolved via the centered quadratic chirp tight frame

For the four ORIGINAL-weight completion fields q_j in
`WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`, put q=sum q_j,
m=E_Omega q, and k=q-m. The exact hole projection and collision bound
are proved.

NEW (21 October 2026):
1. Theorem 4 of [COMPLETION_ENERGY_RESOLUTION_20261021.md](docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md)
   proves $m >= 4 a^3 \mu (1 - o(1)) > 0$ unconditionally on reachable hosts, eliminating the vanishing/small mean branch.
2. [QUADRATIC_FRAME_CERTIFICATE_20261021.md](docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md)
   constructs the canonical centered quadratic chirp tight frame:
   $$k = \frac{1}{p} \sum_{(c, t) \ne (0, 0)} Q_k(c, t) \psi_{(c, t)}$$
   with **zero residual error** ($e \equiv 0$).
3. The canonical coefficient norm obeys $\mathcal{L}_k \le C \frac{m}{\sqrt{a} \log(1/a)}$, which establishes:
   $$\delta \ge \frac{am}{\mathcal{L}_k} \ge c a^{3/2} \log(1/a),$$
   providing DIRECT-Q-GAIN with the explicit divergent multiplier $F(a) = \log(1/a)$.

## O4. Scope of exclusions and older packet routes

SELECT/WSELECT/SIGNED/COLLECTIVE-WSELECT existence and retention remain
open on their original domains. Current weighted estimates cannot be
transferred to arbitrary prior-factor residuals without proof.

- Single-edge Boolean moment laws do not imply P12; the sharp 2/3 law
  is not an arithmetic counterexample. Overlapping twelve-slot arithmetic
  improves the terminal ceiling to 7/11 but yields no phase-selection step.
- Actual p=19 data have both R3<0 and R4<0, but no eligible P12 violation.
  All 76 saved finite records fail T5 and have prescribed H=0.
- Actual Boolean AP-free examples with a~p^-theta, 1/3<theta<1/2, have
  delta/a^(3/2)->0. They fail the logarithmic density hypothesis and
  pa^3mu->infinity for every 0<mu<=1. They do not negate O1 or O2.
- The October 19 Boolean block construction satisfies the density and
  diagonal conditions but deliberately contains a nonzero 4-AP. It only
  refutes W8 with AP exclusion omitted.
- The fractional-quadratic bounded-weight obstruction of October 16 is
  neither Boolean nor AP-free and also does not negate those claims.
