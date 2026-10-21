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

## O2. P12, now an exact original-weight covariance bound

Retain the original F, tau=a^2/log p, H=floor(tau wp/(48r)),
mu=lambda(0,0,0), w=|Omega|/p, u=1_A-a1_Omega, and U=wa(1-a).
The exact expansion has diagonal aw/p. The proved reachable-host
estimates give R1=o(a^4wmu), R2>=-o(a^4wmu), and

    Q=R3+R4<=-(1-o(1))a^4wmu.

Under failed adequate selection, prove

    Q>=-(1/2)a^4wmu.                                    (P12)

For the precise Fourier probability measure lambda(C,beta,N), set

    Q_u(c,t)=E_p u(y)e_p(-cy^2-ty),
    s=(N-3C)/2, gamma=(N-5C)/2,
    m_s=E_p u(y)^2 e_p(sy^2),
    D_s(c,t)=Q_u(c,t)conjugate(Q_u(c+s,t))-m_s/p,
    phi(c,t)=(3c+gamma,3t-beta),
    E_F(u)=sum lambda sum_(c,t)|D_s(c,t)-D_s(phi(c,t))|^2.

The inner sums are unnormalized. The PROVED identity R4=U^2-E_F/2
makes P12 exactly equivalent to the OPEN finite bound

    E_F(u)<=2U^2+2R3+a^4wmu.                             (W8)

Do not discard R3. Do not infer a lower bound on Q from nonnegative E_F.
Use `WEIGHTED_QUARTIC_COVARIANCE_20261018.md` for the proof, proper-host
Boolean correction, norms and both distinct diagonals. The general
Cauchy-Schwarz bound has scale U^2, which is insufficient.

The direct cubic bound is proved but deficient:

    |R3|<=4w^2a^2(1-a)delta+4a[(mu+p^-1/2)b+1/p].

At failed delta<c a^(3/2)R, its spectral envelope divided by a^4wmu is
4c(1-a)(w/mu)a^-1/2 R. Its original boundary envelope includes
2/(a log p), not o(1) at logarithmic density. Shrinking tau changes
the weight and fixes only that boundary envelope. It does not prove W8.

The October 19 construction in `O2_COVARIANCE_ATTACK_20261019.md`
refutes W8 with AP exclusion removed even when all the other listed
conditions hold. It has `a~1/log p`, `delta=o(a^(3/2))`, original H,
`pa^3mu->infinity`, and `Q<=(-11/20+o(1))a^4wmu`, but includes
`{0,1,2,3}`. It is not a counterexample to O1 or O2. Any proposed
covariance proof must use actual AP exclusion more strongly than a
weighted-count deficit; the pointwise identities `Bq_j=0` are available.

## O3. Completion-certificate existence, including the small-mean branch

For the four ORIGINAL-weight completion fields q_j in
`WEIGHTED_COMPLETION_CERTIFICATE_20261018.md`, put q=sum q_j,
m=E_Omega q, and k=q-m. The exact hole projection and collision bound
are proved. If m>0, a sufficient approximation by centered nonconstant
quadratic phases is

    k=sum c_chi(chi-E_Omega chi)+e,
    sum|c_chi|<=m/(2sqrt(a)R(a)),
    ||e||_(L2(Omega))<=(m/2)sqrt(a/(1-a)).

This implies delta>=a^(3/2)R(a). Existence of this approximation is
OPEN; the relative-Gram formulation cannot assume orthogonal phases.
A complete argument must ALSO treat vanishing or small m. The current
low-completion implication has only scale a^2mu/w when its bracket is
positive and errors are sufficiently small. No complete replacement
selection theorem has been proved.

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
