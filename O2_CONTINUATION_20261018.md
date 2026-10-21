# O2 continuation: the original weighted quartic obstruction and verified partial results

18 October 2026, continuing the requested October 17 direct attack. Offline.

**Outcome (D): rigorous partial results.** The target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, O2, and inequality (P12) remain **OPEN**. This cycle proves a stronger mixed-window terminal ceiling, an exact formula for the original weighted quartic residual, a weighted completion certificate, and an actual Boolean domain-separation construction. It provides neither a proof of (P12) nor a counterexample satisfying all its hypotheses. No literature novelty is asserted.

## 1. The recovered framework and the exact unresolved inequality

The definitions are taken from the original [mixed-window proof](MIXED_QUADRATIC_TERMINAL_20261016.md), [weighted pair theorem](WEIGHTED_PAIR_REDUCTION_20261016.md), and [direct increment tradeoff](DIRECT_INCREMENT_TRADEOFF_20261016.md). Let `p>3` be prime, `Omega` a nonempty intersection of `d` nonzero linear and `s` nonconstant quadratic circular-interval constraints, `r=d+s>=1`, and `w=|Omega|/p`. Let `B=1_A`, where `A subset Omega` is cyclically 4-AP-free for nonzero differences, and `a=|A|/|Omega|`.

The factor in this attack is the trivial partition of the current host: `g=aP`, `P=1_Omega`, and `u=B-aP`, zero-extended to the full field. Thus

    E_p u=0,
    u^2=(1-2a)u+a(1-a)P,
    U=E_p u^2=wa(1-a).

The progression weight `F` is distinct from a conditional-expectation factor. For the original tent `f` of radius H,

    F(x,h)=product_l f(xi_l h)
           product_j f((2c_jx+b_j)h) f(c_jh^2),
    F(x,0)=1.

All two-variable averages have normalization `p^-2`; the persistent Fourier mass is `mu`, as defined in the original proofs. Put `T=E_(x,h) F product_i P(x+ih)`. For `1<=j<=4`, `R_j^F` is the sum of the terms with j copies of u and `4-j` copies of `aP` in the expansion of the weighted four-point count. Then

    Lambda_F(B)=a^4T+R_1^F+R_2^F+R_3^F+R_4^F=aw/p,
    Q:=R_3^F+R_4^F=aw/p-a^4T-R_1^F-R_2^F.            (1)

The last equality is exact; the AP-free count is `aw/p`, not zero. On the specified reachable hosts, with the original `tau=a^2/log p`, the proved estimates give `T=(1+o(1))wmu`, `R_1^F=o(a^4wmu)`, `R_2^F>=-o(a^4wmu)`, and negligible Boolean diagonal. Therefore

    Q<=-(1-o(1))a^4wmu.

The required incompatible inequality under adequate failed phase selection is still

    Q>=-(1/2)a^4wmu.                                  (P12)

Using AP exclusion to substitute (1) does not establish this lower bound.

## 2. Boolean occupancy improves the terminal ceiling, not selection

The [October 17 Boolean occupancy theorem](BOOLEAN_OCCUPANCY_TERMINAL_20261017.md) proved `a<=2/3+o(1)` in the original terminal regime. Its essential new inequality is `M_2<=M_1+2aw/p`, since a nonzero four-slot progression contains at most three occupied vertices. The diagonal is retained exactly. A single abstract four-bit law attains the 2/3 ceiling with zero pair covariances, so that one-edge argument cannot improve its constant by itself.

The [October 18 finite-pattern theorem](FINITE_PATTERN_TERMINAL_20261018.md) uses overlapping AP constraints inside a fixed twelve-slot progression. Every 4-AP-free subset of `{0,...,11}` has at most eight elements; a complete elementary proof and an attaining set are supplied in that note. The original pair near-positivity extends to every pair of distinct slots. Eroding each interval by `m(m-1)H` at each end gives explicit finite errors for an m-slot count and the general ceiling

    a<=(R-1)/(m-1)+o(1),

when every AP-free subset of m slots has size at most R. At `(m,R)=(12,8)`,

    a<=7/11+o(1).                                     (2)

This applies to the same original terminal regime and reachable mixed hosts. The four-slot weight F and H are retained; the auxiliary twelve-slot host count and larger erosion are explicitly distinguished from T. The ceiling improves 2/3 by `1/33`. It supplies no additional phase correlation and does not change the unresolved `a^(3/2)` divergence threshold.

## 3. Exact quantifiers and the cubic estimate's remaining deficit

The [quantifier/cubic note](O2_QUANTIFIERS_CUBIC_BOUND_20261017.md) and [independent audit](O2_CUBIC_AUDIT_20261018.md) preserve the full DIRECT-Q-GAIN domain. For each fixed epsilon, eligibility includes

    r[log(1/w)+log(48r)+loglog p]<=log p/100,
    epsilon/(2log|Omega|)<=a<=4/5,

and actual Boolean cyclic AP exclusion. Correlation is relative:

    delta=max_(c,t)!=(0,0) |E_Omega(B-a)e_p(-cx^2-tx)|.

The proposed lower bound is `delta>=c_epsilon a^(3/2)F_epsilon(a)`, where `c_epsilon>0`, the large-prime threshold, and the function `F_epsilon>=1` with `F_epsilon(a)->infinity` are chosen before the eligible instance. Its negation quantifies over **every** such constant, threshold, and divergent function. Failure for the concrete multiplier `R(a)=loglog(e^2/a)` alone is not failure of the existential divergent-multiplier assertion.

Equivalently, failure for some epsilon supplies either an eligible sequence with `a->0` and `delta/a^(3/2)` bounded above, or one with `p->infinity`, density bounded away from zero, and that ratio tending to zero. The second branch cannot be omitted.

Direct Vandermonde absorption and Fourier Cauchy-Schwarz prove, for the original weight,

    |R_3^F|<=4w^2a^2(1-a)delta+4a beta,
    beta=(mu+p^-1/2)b+1/p.                            (3)

At the failed cap `delta<c_epsilon a^(3/2)R(a)`, the first term divided by `a^4wmu` is at most

    4c_epsilon(1-a)(w/mu)a^-1/2 R(a),

which is not small. The original boundary envelope also has leading normalized cost `2/(a log p)`, only bounded rather than vanishing at logarithmic density. The alternative `tau=a^3/log p` removes that boundary deficit but changes the weight and leaves the larger spectral deficit. Neither fact is a proof of the original (P12).

## 4. Exact weighted quartic covariance: a precise next target

The [weighted quartic theorem](WEIGHTED_QUARTIC_COVARIANCE_20261018.md) extends the earlier unweighted identity to the ORIGINAL mixed weight, retaining all coefficient resonances and the proper host. Write

    F(x,h)=sum_(C,beta,N) lambda(C,beta,N)
                                  e_p(2Cxh+Nh^2+beta h),
    lambda>=0, sum lambda=1,
    Q_u(c,t)=E_p u(y)e_p(-cy^2-ty),
    m_s=E_p u(y)^2 e_p(sy^2),
    D_s(c,t)=Q_u(c,t)conjugate(Q_u(c+s,t))-m_s/p.

For each mode put `s=(N-3C)/2`, `gamma=(N-5C)/2`, and `phi(c,t)=(3c+gamma,3t-beta)`. Chirp-index sums below are unnormalized. Then

    sum_(c,t)|D_s(c,t)|^2=U^2-(E_p u^4)/p,
    E_F(u)=sum lambda sum_(c,t)|D_s(c,t)-D_s(phi(c,t))|^2,
    R_4^F=U^2-(1/2)E_F(u).                           (4)

The proof separates the AP and pairing branches of chirp orthogonality and subtracts the pairing contribution exactly. Booleanity gives

    E_p u^4=wa(1-a)(1-3a+3a^2),
    m_s=(1-2a)Q_u(-s,0)+a(1-a)Q_P(-s,0).

Thus the proper-host transform is retained, and the quartic diagonal `(E_p u^4)/p` is distinguished from the Boolean diagonal `aw/p`.

Most importantly, (P12) is EXACTLY equivalent at finite p to

    E_F(u)<=2U^2+2R_3^F+a^4wmu.                       (W8)

This is equation (W8) of the linked quartic note. It is **OPEN**, not a proved energy bound. The energy in (4) is nonnegative but is subtracted; its positivity has the opposite orientation from a lower bound on Q. A failed individual chirp cap controls the entries of D_s, not their signed covariance with the affine permutation phi. The unconditional consequence is only `-U^2+2(E_p u^4)/p<=R_4^F<=U^2`, far too coarse at the `a^4wmu` scale. The cubic term in W8 cannot be dropped.

## 5. Weighted completion energy and the missing certificate

The [completion note](WEIGHTED_COMPLETION_CERTIFICATE_20261018.md) uses four hole-supported nonzero-difference fields

    q_j(v)=P(v) E_h 1_(h!=0)F(v-jh,h)
                              product_(i!=j)B(v+(i-j)h).

They satisfy `Bq_j=0` and restore exactly `B/p` when h=0 is included. The original weight need not be invariant under reversal, so there are four channels, not an automatic endpoint/interior identification. An actual p=11 example verifies this distinction.

Put `q=sum q_j`, `m=E_Omega q`, and `k=q-m`. The inherited hole projection gives

    <B-a,k>_Omega=-am,
    E_Omega k^2=a m^2/(1-a)+E_Omega z^2,

with a mean-zero hole-supported z orthogonal to B-a. Separating pairs of completion triples that intersect, and using AP-forced overlap zeros, proves the finite arithmetic bound

    E_Omega(disjoint weighted completion energy)
                      >=m^2/(1-a)-26m/p.             (5)

The sharper collision loss is `(24m_E+26m_M)/p`. This is a quantified extension of the earlier hole projection and degree-six overlap geometry, not a new selection theorem.

A direct sufficient phase certificate is now explicit. Assume m>0 and approximate k on the proper host by centered nonconstant quadratic/linear phases with coefficient l1 sum L and relative L2 error e. Then

    am<=delta L+sqrt(a(1-a)) e.

Consequently `e<=(m/2)sqrt(a/(1-a))` and `L<=m/(2sqrt(a)R)` force `delta>=a^(3/2)R`. An exact relative-Gram variant is also proved, without assuming phase orthogonality. No existence theorem for that approximation, its coefficient budget, or its error is known. In particular m can vanish or be too small. The available low-completion alternative gives only the deficient scale `a^2mu/w` under further small-error conditions. A complete completion-based proof must resolve both branches.

## 6. Actual Boolean examples and what they do not refute

The [finite diagnostic data](BOOLEAN_O2_DIAGNOSTICS_20261017.json) contain exact modular AP exclusion and exact rational residuals, together with floating sweeps over every quadratic phase. A concrete witness has

    p=19, Omega=F_19, H=9,
    A={2,3,4,6,7,9,10,11},
    a=8/19, w=1, mu=10/19,
    R_1=0,
    R_2=158656/12380495,
    R_3=-50624/12380495,
    R_4=-38472/12380495,
    Q=-89096/12380495,
    a^4wmu=40960/2476099,
    Q/(a^4wmu)=-0.4350390625.

Both cubic and quartic residuals are negative here. The all-phase sweep gives `delta=0.2521589733765169`, attained at `(c,t)=(16,1)` under the recorded convention. The concrete failed-cap condition would require `c_epsilon>0.8768391060544218`; this finite value does not select a universal constant.

This witness does **not** violate even the bare numerical half-main lower bound, and it is not eligible for the theorem. Its T5 left/right sides are about `4.95111931043` and `0.02944438979`, its prescribed original H is zero, and the Boolean diagonal divided by the main scale is `1.3396484375`. All 76 saved finite records fail the product budget and have prescribed H=0. None is a genuine eligible (P12) counterexample; negative residuals alone do not provide one.

There is also a rigorous asymptotic **actual Boolean** construction in the [full alteration-range theorem](BOOLEAN_TYPICAL_ALTERATION_20261018.md). For every fixed `1/3<theta<1/2`, it produces

    a=(1+o(1))p^-theta,
    delta/a^(3/2)->0.

The deletion rule removes every sampled vertex participating in a cyclic 4-AP. A bounded-local-incidence good family, a global Lipschitz extension, and Bernoulli martingale concentration control the FINAL altered set in all p^2 phases simultaneously. Translation invariance and the constant phase control actual centering and density. The proof has two independent mathematical audits, including the conditional variance and the global good-endpoint Lipschitz step. The simpler [elementary alteration proof](BOOLEAN_ALTERATION_CHIRP_20261018.md), valid for `2/5<theta<1/2`, is preserved as an alternative proof on that smaller range.

This construction refutes an unrestricted assertion that Boolean cyclic AP exclusion forces an `a^(3/2)` correlation at every small density. It does not refute DIRECT-Q-GAIN: polynomial density lies below `epsilon/(2log p)`. The diagonal obstruction is robust to the choice of a weight with the prescribed baseline normalization: since `mu<=1` and `theta>1/3`,

    p a^3 mu<=p a^3->0.

Thus the condition `p a^3mu->infinity` required for P11 fails for every such weight. For the original full-host tent, H is eventually positive and the sharper diagonal/main ratio is asymptotic to `48log p/(pa^5)`, which diverges. The construction supplies no eligible P12 counterexample and does not change outcome D.

## 7. Verification record and the precise continuation point

The following verifiers passed. Counts describe the respective finite checks and are not counts of independent theorems.

| Artifact | Verified scope | Count |
|---|---|---:|
| [Boolean occupancy](BOOLEAN_OCCUPANCY_VERIFICATION_20261017.json) | Exact Boolean expansion, diagonals, occupancy, finite errors | 14,041 checks |
| [Actual finite diagnostics](BOOLEAN_O2_DIAGNOSTICS_20261017.json) | Exact residual/AP recounts and all-phase sweeps | 3,382 checks; 76 saved records |
| [Original cubic verifier](verify_o2_cubic_quantifiers_20261017.py) | Cubic absorption, host correction, unweighted quartic identity | 468 checks |
| [Independent cubic audit](O2_CUBIC_AUDIT_20261018.json) | Nonempty eroded hosts with nonzero omitted-host corrections | 48 checks |
| [Finite-pattern terminal](FINITE_PATTERN_TERMINAL_VERIFICATION_20261018.json) | Twelve-point certificate and three hosts with nonempty interiors | 51,971 checks |
| [Weighted quartic](WEIGHTED_QUARTIC_VERIFICATION_20261018.json) | Exact modular branches and numerical weighted covariance identities | 15,102 checks |
| [Weighted completion](WEIGHTED_COMPLETION_VERIFICATION_20261018.json) | Geometry, rational completion/projection identities, atomic/Gram checks | 144 geometry + 366 + 366 rational cases + 145 numerical cases |
| [Elementary Boolean alteration](BOOLEAN_ALTERATION_CHIRP_VERIFICATION_20261018.json) | Exact deletion/AP recounts and floating all-phase sweeps | 440 checks |
| [Full-range Boolean alteration](BOOLEAN_TYPICAL_ALTERATION_VERIFICATION_20261018.json) | Exact finite-cube geometry, Lipschitz/extension/martingale identities, and all-phase sweeps | 525,186 checks; 707,238 chirp coefficients |

The finite-pattern audit adds genuinely nonempty eroded hosts; the older October 17 occupancy configurations had empty eroded interiors. Fourier, Gram, and square-root-envelope checks use floating arithmetic where documented. The full-range alteration verifier's largest FFT/direct-sum discrepancy is `2.0888836804026048e-17`. None of these finite cases verifies the full asymptotic target domain. The quantifier theorem and asymptotic conclusions rest on their written proofs, not extrapolation of samples.

The next mathematical task is to prove W8 from the actual Boolean/AP-free arithmetic and the precisely quantified failed phase-selection cap, with the original weight and cubic term retained. An alternative is to prove adequate phase selection directly, for example by establishing the completion certificate together with its missing low-completion branch. The terminal ceiling is now stronger, but further changes to that constant do not resolve this selection problem. No sufficient control of the signed quartic covariance, complete completion certificate, or genuine eligible counterexample has been obtained.
