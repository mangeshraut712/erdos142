> **15 October 2026 audit:** The current operative status and corrections are in
> `CURRENT_STATUS.md` and `RESIDUAL_FIELD_AUDIT_20261015.md`. Earlier summaries
> below are historical; the appended audit qualifies conflicting claims.

# Quantitative solution ledger

2 October 2026. Offline. Principal status **(C) COMPLETE CONDITIONAL CLOSURE**;
the local target remains unproved. The only missing node in the completed
conditional chain is H in NEW_RESULTS_20261002.md section 1.

## 1. Budget before choosing an inverse theorem

Let t=ε/log N, ℓ=log(2/t), X=log N. Fix ε before taking N to infinity.
For a step with additive density gain at least Δ(a), added rank at most
R(a), and logarithmic domain loss at most L(a), dyadic density epochs give
the envelopes

    J ≲ 1+integral_t^(a*) 1/Δ(a) da,
    D ≲ d_0+sum_epochs [1+a/Δ(a)] sup_epoch R(a),
    S ≲ sum_epochs [1+a/Δ(a)] sup_epoch L(a).

For regular power/logarithmic functions these sums have the same dominant
orders as integrals of R/Δ and L/Δ. They are guaranteed upper envelopes;
failure of an envelope to be small does not prove a faster actual iteration
impossible. Claims of Θ require gains/costs bounded on both sides.

For persistent coordinate windows in one prime group, small size loss alone
is insufficient. The proved terminal estimate needs

    log(p-1)/D - S - log(2D) -> +infinity.                 (T)

A convenient sufficient condition is D[S+log(2D)+1]=o(log p). This also
preserves the old full cutoff. A domain class with a separately proved
rank-independent terminal criterion may have a different budget; none is
silently substituted here.

## 2. Mandatory weak gains and complexity tests

Assume for this table a usual geometric cost envelope
L(a)=O(R(a)+log(2/a)), and persistent added rank R. All exponents C,D,δ
are fixed and nonnegative, with δ>0 where stated. Set C'=max(C,1).

| Additive gain Δ | Added rank R | Steps J | Cumulative rank envelope | Cumulative log-loss envelope | Target test |
| --- | --- | --- | --- | --- | --- |
| ca² | log^C(2/a) | O(t^-1) | O(t^-1ℓ^C) | O(t^-1ℓ^C') | Does not guarantee S=o(X), or (T) |
| ca²/log^D(2/a) | log^C(2/a) | O(t^-1ℓ^D) | O(t^-1ℓ^(C+D)) | O(t^-1ℓ^(C'+D)) | Same failure, with additional logarithms |
| ca^(2+δ) | log^C(2/a) | O(t^(-1-δ)) | O(t^(-1-δ)ℓ^C) | O(t^(-1-δ)ℓ^C') | Envelope grows faster than X |
| ca² | a^-δ | O(t^-1) | O(t^(-1-δ)) | O(t^(-1-δ)) | Envelope grows faster than X |
| ca²/log^D(2/a) | a^-δ | O(t^-1ℓ^D) | O(t^(-1-δ)ℓ^D) | O(t^(-1-δ)ℓ^D) | No guaranteed closure |
| ca^(2+δ) | a^-θ, θ>=0 | O(t^(-1-δ)) | O(t^(-1-δ-θ)) | Same power, with possible log factor when θ=0 | No guaranteed closure |
| ca² | exp(Csqrt(log(2/a))) | O(t^-1) | t^-1 exp(Csqrt(ℓ)) times bounded factors | Same dominant order | At t=ε/X this is X^(1+o(1)), not o(X) |
| ca²/log^D(2/a) | exp(Csqrt(log(2/a))) | O(t^-1ℓ^D) | t^-1ℓ^D exp(Csqrt(ℓ)) | Same dominant order | No guaranteed closure |
| ca^(2+δ) | exp(Csqrt(log(2/a))) | O(t^(-1-δ)) | t^(-1-δ) exp(Csqrt(ℓ)) | Same dominant order | X^(1+δ+o(1)) |

These tests explain the distinction in the brief: exp(O(ℓ^C)) may describe
a harmless ONE-TIME complexity, while multiplying it by order 1/t steps
may destroy the required budget. In the exp(Csqrt(ℓ)) cases, each factor is
indeed X^o(1); the number of steps is still material.

For a gain ca^(2-σ), 0<σ<1, and R,L=exp(Csqrt(log(2/a))) times fixed
logarithms, the SIZE envelope is X^(1-σ+o(1))=o(X). For the present
persistent-window terminal bound, D and S have that same power, so the
sufficient PRODUCT test requires σ>1/2. Passing a size-only ledger must
not be reported as a complete quadratic localization theorem.

## 3. Constant-relative energy and the improved endpoint

For quarter-factor energy η(a)a², the proved atom lemma gives

    Δ(a)>=η(a)a/2,
    r_A>=η(a)a/(2·4^R(a)),
    log(n/n')=log(a'/a)-log r_A.

For fixed η>0, J=O(ℓ). The old worst-density bound J max R loses a
logarithm. The new density-sensitive sum with

    R(a)<=ceil(K/[sqrt(a)log(2/a)])

instead gives

    U=ΣR(a_j)=O(t^-1/2/ℓ+ℓ),
    D=O(t^-1/2/ℓ+ℓ),
    S=O(t^-1/2/ℓ+ℓ²),
    D(S+log(2D)+1)=O_ε(X/(log X)²+sqrt(X)(log X)^C)
                    =o(X)                               (fixed C).

The proof and explicit constants are in NEW_RESULTS sections 3-5. Any
fixed positive logarithmic saving log^-γ(2/a), γ>0, in the critical rank
a^-1/2 also passes after the same sharpened summation. We state just γ=1
in the single remaining hypothesis H.

For another useful parameterization, take energy η(a)≳a^β/log^D(2/a)
and added rank R(a)≲a^-δ/log^C(2/a), δ>0. Rank dominates the logarithmic
mass-retention terms. Dyadic sums give D,S=O(t^(-(β+δ))ℓ^(D-C)).
Hence β+δ<1/2 suffices for (T). At β+δ=1/2 a logarithmic saving C>D
also suffices. This endpoint statement refers to the recorded geometric
conversion, not a proof of the underlying energy theorem.

## 4. Quadratic inverse substitutions actually performed

The accepted ||f||U3>=ca^(3/2) gives no localization by itself.
If a hypothetical inverse theorem yielded correlation ρ>=c||f||U3^C
and localization loss a^-t, then the naive gain exponent would be
s=3C/2 and size loss envelope a_0^(-(s+t-1)). Even t=0 needs C<4/3
for the strict size test. PHASE2's actual-norm obstruction rules out the
overstrong C<2 formulation already; it does not rule out density-sensitive
inverse statements of a different form.

If the only guaranteed gain is ρ(a)=exp(-Ca^-k), k>0, the initial epoch
step bound involves exp(C_ε X^k) times powers of X. For every fixed k>0,
exp(C_ε X^k)/X grows faster than X. This GUARANTEE cannot close a ledger
with a positive constant per-step cost. It is not a lower bound on the
actual steps of an unknown improved inverse theorem.

No unproved known-style inverse theorem or unspecified constant was used
as an input to the completed conditional chain.

## 5. Ledger for the completed conditional chain

| Item | Explicit value or proved bound |
| --- | --- |
| Starting density | a_0>=t=ε/log N |
| Starting domain | Ω_0=[N] in a single prime 3N<p<6N; rank one |
| Structural signal | H alone: Var_Ω(E(B|F))>=ηa² |
| Density gain | a'>=a(1+η/2) |
| Per-step added rank | ceil(K/[sqrt(a)log(2/a)]) |
| Retained occupied fraction | >=ηa/(2·4^R) |
| Exact per-step size loss | log(a'/a)-log r_A |
| Step count | <=ceil(log(2/t)/log(1+η/2))+1 |
| Total rank | <=1+U_* from NEW_RESULTS (3.2) |
| Cumulative logarithmic size loss | <=S_* from NEW_RESULTS (4.3) |
| Restricted rank eligibility | D_*=o(sqrt(log p)) |
| Restricted size eligibility | log(p/n)<=log6+S_*=o(sqrt(log p)) |
| Lower density eligibility | a>=ε/(2log n) since log n>=log N/2 |
| Old full cutoff | log threshold=O(D_*+log D_*+ℓ)=o(log N) |
| Terminal density | >4/5 |
| Terminal contradiction | density<=3/4+9D_*exp(S_*-log(p-1)/D_*)<=4/5 eventually |
| Integer/cyclic transfer | two integer second differences bounded by 2(N-1)<p |
| Remaining unproved statement | H, and only H, in this conditional chain |

## 6. Failed route ledger

Fourier: cubic cancellation is bounded by 4abρ, but generic dissociation at
ρ of order a² allows O(a^-2log(1/a)) generators. No acceptable quartic
lower bound follows from this. Character selection produces U2 control
only; it does not supply the AP-free selection gain.

Quadratic: the new constant-fraction hole theorem excludes negligible
deletion of a pure quadratic interval host. Arbitrary localized quadratic
inverse/localization remains unproved.

Boolean: forced derivative angular mass is ~a⁴ at a=ε/log p, only an
order-a² fraction of total derivative energy, and the selected frequencies
depend on the difference. Coherent assembly remains unproved.

Incidence: higher traces and the global Schur PSD constraint were derived.
An unlabeled-spectrum-to-character implication is ruled out by relabeling;
the actual arithmetically labeled endpoint matrix is still essential.

Entropy: the global deficit is >=pa⁴/4, but no theorem locates it in the
admissible arithmetic factors. Overlapping star costs cannot be freely added.

Construction: full-product quadratic shells, ternary coding hosts and CRT
products of polylog-size seeds do not reach c/log p. No disproof was obtained.

## 7. Later structural attack: exact variable-energy budget

The current continuation has principal status (D) NEW RIGOROUS THEOREM.
Earlier conditional bookkeeping is retained, not promoted to an unconditional
proof. Full proofs of the following envelopes are in STRUCTURAL_HYPOTHESIS_ATTACK.

For dyadic density epochs e_k=2^k t, let m_k be the infimum of guaranteed
relative energy η(a), R_k the supremum of added rank, and
M_k=1+4log(2)/m_k. Then every partial iteration satisfies

    D_t=1+Σ M_kR_k,
    S_t=log(1/t)+Σ M_k[log(2/(m_ke_k))+log4 R_k].

The sufficient conditions for the unchanged H class are D_t,S_t=o(sqrt X)
AND D_t(S_t+log(2D_t)+1)=o(X), X=log N. The separate eligibility bounds
are needed for asymmetric general functions; a product test alone need
not keep the size inside H's range.

For η(a)≳a^β/ell(a)^C, s(a)≲ceil(a^{-γ}/ell(a)^D), β≥0,γ>0,
the leading cumulative D,S are O(t^{−(β+γ)}ell(t)^{C−D}). Thus
β+γ<1/2 suffices; β+γ=1/2 with D>C also suffices. Ceiling and mass
overhead are lower order for positive γ. These are sufficient bounds,
not impossibility claims outside this region.

Relative quarter conversion now has constant κ²=8/π², with no w loss.
If each residual of low factor energy has squared relative coefficient
≥c a^λell(a)^q, a stopping goal ζa^{2+β}/ell(a)^C requires rank
O(a^{−(λ−2−β)}/ell(a)^{C+q}), for β<λ−2 and fixed constants.
Leading cumulative rank/log-loss is O(t^{−(λ−2)}/ell(t)^q): the weak
energy exponent β cancels from this cost, while mass overhead requires
β<1/2. Critical λ=5/2 therefore still needs q>0.

Specific unproved SG: β=1/4, λ=5/2, q=1, C=0. Stopping energy is
ζa^{9/4}, per-factor rank O(a^{-1/4}/ell), cumulative D,S=O(t^{-1/2}/ell).
At a≈ε/log p the coefficient magnitude must be ≳a^{5/4}sqrt(ell),
not merely a². Conversion/iteration are proved; selection is not.

For direct counting with α=wa, an actual full-group lower bound
Λ4(B)≥cα⁴/ell(a)^C would contradict α/p even at w=e^{-sqrt(log p)},
because pα³/ell(a)^C→∞. A window-relative baseline ca⁴Λ4(1_Ω)/ell(a)^C
would be stronger. Neither lower bound is deduced from small factor energy.

## SELECT follow-up ledger — 2 October 2026

PROVED: full-group Λ4(g) positivity from factor variance; exact-cardinality
degree-four PSD functional with actual AP fourth moments zero; relative
AP-marginal main-term lower bound; quadratic-host hitting certificate.
See SELECT_ATTACK_20261002.md and its linked route filenames.

CONDITIONAL/UNPROVED: SELECT and its weaker R(a)=log log(e²/a) replacement.
The replacement keeps M=ceil[ζa^-1/4/(κ²c log(2/a))]; matched energy/gain
factors yield cumulative rank and size O(t^-1/2/R(t)) and close the
existing downstream geometry. It does not supply the missing hypothesis.

OPEN: signed cancellation of the nonempty residual terms; uniform relative
main-term geometry at full H rank; stronger arithmetic/Fourier localizers
beyond the feasible basic moment relaxation. No actual SELECT-refuting
sequence was produced. Principal status D, unconditional target unresolved.

## SELECT continuation — 12 October 2026

PROVED: exact averaged trades repair negative four-variable probabilities,
preserve AP zeros and exact cardinality, and reduce the PSD perturbation
bound to 400ρ_4. All linear-square Fourier-cap localizers hold for τ>=120a/n.
With n-k>=32(k-3), every literal-product localizer through degree four and
all permitted cap products also hold. Thus the specified full degree-four
preordering cannot certify infeasibility at SELECT density.

Proof: SELECT_POSITIVE_MOMENTS_20261012.md. Theorem constraints and proof
system scope are explicit; this is not a representing probability law or
an AP-free counterexample. SELECT, WSELECT, SIGNED and the target remain
unproved. Status D. New exact/numerical checks are saved separately.

## Degree-six attack — 12 October 2026

PROVED: exact harmonic parametrization of fifth/sixth cardinality
extensions; negative fifth moments in the canonical lift on five-point
APs; degree-six completion-square certificate; forced disjoint-completion
sixth-moment enhancement >=a^7/8; degree-eight global completion identity;
relative residual/completion Fourier inequality. A degree-k/k+2 global
realizability endpoint is proved but is not quantitatively efficient.

AUDITED: prior degree-four theorem remains valid. The canonical extension
is refuted, not all degree-six extensions. New corrections z_5,z_6 and
their PSD/localizing feasibility remain open. No new character increment
budget is proved, so the conditional target chain remains conditional.

Evidence: DEGREE_SIX_ATTACK_20261012.md and
DEGREE_SIX_VERIFICATION_20261012.json. Status D; target unresolved.

Finite extension continuation: at p=23, k=5 the exact averaged-trade
fourth moments have a global AP-free representing law with 19 positive
rational affine-orbit weights. All moments through degree four are
independently checked by expanding this law. This is below the n>=200
theorem range and proves no asymptotic feasibility or SELECT failure.

## Sixth-order Fourier continuation — 12 October 2026

PROVED: exact ratio decomposition of completion overlaps (no two-point
intersections for p>7); AP-forced zeros at ratios 2 and 1/2; sharpened
localized enhancement under m_v a^4>=20; exact normalized completion
Fourier transform with all diagonals removed; multiplicative incidence
spectrum; higher-moment certificates at degrees nine and twelve.

PROVED OBSTRUCTION, LIMITED SCOPE: bounded quadratic weights can have
sixth-order excess >=a^7/8 and arbitrarily diffuse additive Fourier mass.
They fail AP exclusion and do not refute SELECT. The exact collective
completion-tail lemma is proved as an implication; its spectral and
variance premises remain unproved for the required AP-free residuals.

EXACT FINITE CERTIFICATE: p=29,k=6 has a global representing law with
32 positive rational orbit weights, verified on 24,360 AP-free six-sets.
It does not establish target-regime degree-six feasibility. No density-
increment closure is claimed. See SIXTH_ORDER_FOURIER_ATTACK_20261012.md
and SIXTH_ORDER_VERIFICATION_20261012.json. Principal status D.

## Two-channel completion & spectral continuation — 14 October 2026

PROVED: exact dual completion channels q_E, q_M with B q_E = B q_M = 0 and
physical-Fourier duality E[q_E] = a^3 - a/p + T, E[q_M] = a^3 - a/p + S;
2x2 cell covariance splitting W = J + Z and Loewner order UW >= UJ >= SS^T;
unwindowed cubic Fourier synthesis k_lambda = sum_{xi!=0} hat(q_lambda)(xi) psi_xi
on proper windows Omega and direct regularized relative Gram bridge to
quarter-arc refinement gain Delta E; exact 2x2 matrix pencil optimization
((1-mu)W_Gamma + mu W_tail)^dagger S rescuing S_E=0 proper-window cases;
complete cross-channel sixth-order overlap decomposition and affine collapse
of the 14 five-term unions; boundary-free binomial-derivative identities
D_1 = 4R_0+3R_1+2R_2+R_3 = 2w(S_E+S_M)+4w(a^2+v)/p and
4D_0 - D_1 = R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p, plus 10-block
reflection-symmetric inversion and unconditional scale-a^4 lower bounds
R_1 >= -4R_0, 3R_1+R_2 >= -6R_0, 3R_1+2R_2+R_3 >= -4R_0 (bypassing the
a^(31/8), a^(13/4), a^(21/8) Cauchy-Schwarz losses on those lower bounds);
finite-dimensional LP dual proof that R_4 = Lambda_4(u) is a free slack
variable in D_1..D_4 (verified on all 10 reflection-symmetric blocks);
the Exact Collapse Theorem F_SIGNED := w(S_E+S_M) + R_3/2 + R_4 =
R_0 + R_1/2 + w(U-a^2-v)/p (proving the exact R_1-free conservation law
w(S_E+S_M) + (R_3/2 + R_4 - R_1/2) = R_0 + w(U-a^2-v)/p and the repaired
Unconditional Two-Channel Dichotomy); exact operator block decomposition
<u,(K_B+R_B)u>_p = DIAG + CROSS + COMPLEMENT with DIAG = (2/p)||u_A||_p^2,
CROSS = -2w(S_E+S_M) - 2<g_A,K u_C>_p <= 0, COMPLEMENT = D_{2,E}+D_{2,M} +
2<g_A,K u_C>_p - (2/p)||g_A||_p^2 >= 0, and dual Schur complement bounds on A^c;
exact identification of Branch II (w(S_E+S_M) <= theta R_0) as the
Negative Cubic / Positive Quartic Residual Branch R_3 <= -2(2-theta)R_0 - 3R_1 - 2R_2 + 4w(a^2+v)/p
and R_4 >= (3-2theta)R_0 + 2R_1 + R_2 + w(a-4a^2-4v)/p; exact linear-residual
pairing R_1 = 2<u,h_{E,g}+h_{M,g}>_p = 2w sum_{xi!=0} conj(c_xi)(K_{E,g}(xi)+K_{M,g}(xi))
with quadratic/cubic-in-h splitting R_1 = R_{1,(2)} + R_{1,(3)}, proving
|R_{1,(2)}| <= 12a rho v = o(a^4) under SELECT failure, ||H_g^{(3)}||_2 <= 2v^(3/2),
a variance floor v >= c_1 a^(7/3) for Branch III, and collective energy
>= (1-2c_0)^2 R_0^2/(64v^3) >= c' a^(5/4) on any character set capturing H_g^{(3)};
trilinear L2 stability ||C_{E/M}(f_1,f_2,f_3)||_2 <= ||f_1||_2||f_2||_2||f_3||_2,
1D cubic averaging harmonic decay |K_{E,Phi}(t)| <= O(log|t|/t^2) (l^2 tail O(L^-3 log^2 L)),
and exact l^1-Fourier bounds |R_1| <= 4 rho v (3a + ||hat(h)||_1),
|R_{2,(1)}| <= 12a rho^2 ||hat(h)||_1, and |R_{2,(2)}| <= 6 rho^2 ||hat(h)||_1^2
(via the single-variable Fourier formula for R_{2,(1)}), proving that
||hat(h)||_1 = o(a^(1/2)/ell(a)) makes both |R_1| = o(a^4) and |R_2| = o(a^4)
under SELECT failure; weight-k ANOVA Fourier cap |hat(G_S)(m)|^2 <= (8/pi^2)^k ||G_S||_2^2
and exact continuum Walsh cubic norm 4/27;
unconditional one-sided physical truncation of D_3 proving
D_3 >= a^3 sum_i Lambda_4(B at i, W at != i) - 6w^2 a^3 sqrt(v) on every window Omega
and D_3 >= 4a^4 - 6a^3 sqrt(v), R_1 >= -6a^3 sqrt(v) - 16a v^(3/2) - 4v^2 = -O(a^(33/8)) = -o(a^4),
and T >= a^4 - 3a^3 sqrt(v) - 4a v^(3/2) - v^2 + (U-a^2-v)/p on Z_p (eliminating
Branch III unconditionally on Z_p for all v <= zeta a^(9/4) without any Fourier-cap
or l^1-norm assumption, and establishing the strict two-branch positive dichotomy
S_E+S_M >= a^4/2 - O(a^(33/8)) or R_3/2 + R_4 >= a^4/2 - O(a^(33/8)));
exact spectral splitting hat(q_E)+hat(q_M) = K^(2) + K^(3) - 2 hat(f)/p with
||K^(2)||_2^2 <= 36a^3 rho^2 = O(a^(11/2)ell(a)), clipped completion projection
tilde{q} = min(q_E+q_M, tau_q) and peak-set projection p_{tau_q} = 1_{P_{tau_q}} - E_F[1_{P_{tau_q}}]
with E_diffuse(tau_q) >= S_clip^2/(tau_q E[q_clip]) and E_peak(tau_q) >= tau_q S_{>tau_q}^2/(4w^2 a^2 E[q]);
proper-window two-branch reduction with l^1 window-marginal bound
|sum_i Lambda_4(u at i, W at != i)| <= 4w^2 rho_Omega ||hat(W)||_1 (resolving Sublemma 2C);
exact Fourier operator decomposition Q_0 K_B Q_0 = a L_{E,f} + Q_0 K_f Q_0,
fourth-power trace bound tr(K_u^4) = tr(R_u^4) <= ||u||_{U^3}^8, and global U^3
cubic completion-variance bound ||K_u^(3)||_2^2 <= 4U ||u||_{U^3}^4;
universal Branch II identity Y = R_3/2 + R_4 = a(T_u+S_u) + <u/2+h, K_u^(3)>_p
<= 2a sqrt(U)||u||_{U^2}^2 + sqrt(U(U+4v))||u||_{U^3}^2 (proving ||u||_{U^3} >= a^(3/2)/2(1-o(1))
for arbitrary factors F with zero R_1, R_2 error);
bilateral multiplier set Gamma_alpha^*(tau) = Spec_{tau/sqrt(2)}(u) cap alpha^(-1) Spec_tau(u)
carrying sum_{xi in Gamma_alpha^*} |hat(u)(xi)|^2 >= |T_u+S_u|/(8 rho);
first-principles trace identity tr(K_u^4) = tr(R_u^4) = E_{h,k}[F_u(2h,k)F_u(h,2k)] <= ||u||_{U^3}^8
and exact validity polynomial a^2 - U(U+4v) = a^3(2-a) - 2a(1-a)v + 3v^2;
diagonal-free Branch I and zero-baseline Branch II all-chirp identities
(bounding the c=0 linear part of <h,K_u^(3)>_p by 2 rho^2 sqrt(vU) = O(a^(33/8)ell(a)) = o(a^4));
elementary Gauss-sum proof of quadratic window translation mixing
| |Omega_quad cap (Omega_quad+h)|/p - w^2 | <= (||hat(1_I)||_1^2 - w)/sqrt(p) for all h != 0
(excluding pure quadratic-arc windows from the terminal h-cycle packing argument),
paired with the exact continuum hitting-degree evaluation Z_I = (8/27)w^3 and
max_I H = (23/18)w^2 for 0 < w <= 1/4 (proving that a single quadratic window has
analytic terminal density <= 53/69 + o(1) < 4/5 without translation packing, while
s >= 2 quadratic coordinates decay as (16/69)^s);
centered baseline-free all-chirp covariance identities for S_E, S_M, M_E, M_M, and R_4
(eliminating all O(a^2) baselines aU and -U^2) and exact fourth-moment chirp norms
sum_{c!=0,r} W_tilde_u(c,r)^2 = U^2 - ||u||_{U^2}^4 - (E[u^4]-U^2)/p;
exact finite-p zero-wraparound polynomial bounds Z_I >= (8/27)w^3 + w/(3p^2) and
max_I H <= (23/18)w^2 + 4w/(3p) + 2/p^2 for 1 <= L <= (p+3)/4;
moment-weighted and density-thresholded completion pointwise Fourier caps
|hat(phi_lambda^(m))(xi)| <= w S^(m)(lambda) and |hat(phi_lambda^(>= gamma a))(xi)| <= (w/(gamma a))S_{>= gamma a}(lambda)
(eliminating the W_Gamma <= O(a^4) denominator barrier in Branch I, so any packet Gamma
capturing a theta-fraction of S_{>= gamma a}(lambda) has sum_Gamma |c_xi|^2 >= theta^2 gamma^2 a^2/(|Gamma|w^2)
and max_Gamma |c_xi|^2 >= theta^2 gamma^2 a^2/(|Gamma|^2 w^2));
purely diagonal l^3 bound sum_{xi!=0}|hat(u)(xi)|^3 >= |T_u+S_u|/2 and dyadic shell
dichotomy (proving single-character SELECT whenever the winning shell has size <= c_2 a^(-3/4)ell(a)^(-7/2));
and covariance sign separation between quadratic-resonant hosts (Cov > 0)
and AP-free sets (Cov <= 0).

OPEN: Sublemmas 2A'' and 2B'' in OPEN_LEMMAS.md — capturing a constant fraction theta
of the numerator pairing with phi_lambda^(>= a/2) or K_u^(3) on a packet Gamma of size
<= M(a), and ruling out flat dyadic shells of size > c_2 a^(-3/4)ell(a)^(-7/2).
See QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md, QUADRATIC_TO_LINEAR_TRANSFER_20261014.md,
RESIDUAL_FIELD_AMPLIFICATION_20261014.md, and RESIDUAL_FIELD_AMPLIFICATION_VERIFICATION_20261014.json.
Principal status D; unconditional target unresolved.


## Audit and continuation — 15 October 2026

This entry controls interpretation of conflicting older summary claims.
Principal status D; the unconditional local target remains OPEN.
See `RESIDUAL_FIELD_AUDIT_20261015.md` and
`QUADRATIC_LOCALIZATION_20261015.md` for proofs and precise hypotheses.

| ID | Statement | Status |
| --- | --- | --- |
| QL15 | Weighted localized progressions give a<=3/4+20(2+log p)/(beta p^(1/6)) in a single quadratic interval host under (Q1)–(Q4) | PROVED |
| QL15m | Finite-pattern occupancy transfer (Q11), with m<p and explicit boundary/Gauss errors | PROVED |
| SP15 | Actual AP-free examples at a comparable to p^(-3/5), v=0, nonzero completions, no O(a^(-1/4)/ell) packet with constant-fraction completion capture | PROVED outside the target regime |
| PC15 | Nonnegative completion cap plus a capturing packet implies (A2) and the packet bound (A3) | PROVED implication; packet existence OPEN |
| DS15 | Cubic winning-shell sufficient cutoff a^(-3/4)ell^(-5/2) | PROVED implication; small-shell existence OPEN |
| V15 | New deterministic finite audit, with exact and floating scopes separated | COMPUTATIONALLY CHECKED ONLY |

Corrections: the old -1/8 proper-window packet exponent and -7/2 shell
logarithm were sufficient but unnecessarily restrictive. G_F is generally
not I on the full group; G_0=I and G_F<=I. The old 53/69 terminal bound
needs a phase-width/prime-size condition and distinguishes phase density
from host density. Thresholded pairing retention was not proved.
"Denominator barrier eliminated" means only the conditional cap implication,
not an unconditional concentration theorem. The full downstream conditional
iteration was not re-audited in this run. Proper-window branch reduction
still needs uniform error bounds in the actual admissibility regime.

Dependency paths:

    elementary Gauss sums + localized progression weights + AP exclusion -> QL15
    finite-pattern occupancy bound + same weighted counting -> QL15m
    independent Bernoulli sampling + variance/Fourier bounds + AP exclusion -> SP15
    nonnegative cap + OPEN small-packet existence -> PC15 -> single-character refinement
    QL15 + OPEN stable host class + OPEN increment/loss estimates -> possible quadratic iteration

No proved arrow from QL15, SP15, PC15, or DS15 closes the unconditional target.
Historical checkpoint snapshots: `history/audit_20261015_residual_field/`.

## 16 October 2026 — Mixed-window terminal theorem and a smaller selection target

Principal status D. The local unconditional target is OPEN. This entry
supersedes the old open status of iteration-stable quadratic terminal
geometry; it does not upgrade any structural selection claim.

| ID | Exact source and conclusion | Status |
| --- | --- | --- |
| MT16 | MIXED_QUADRATIC_TERMINAL_20261016.md (M1)-(M13): terminal density <=3/4+o(1) for mixed interval windows under explicit rank/size or product budgets | PROVED |
| MR16 | Same source (M15)-(M16): weighted first residual o(a^4w mu) on reachable hosts, with finite error | PROVED |
| DA16 | LOG_DENSITY_ATTACK_20261016.md (L2): one quarter cell has gain >=kappa delta/8 and retained occupied mass >=kappa delta/(8a) | PROVED |
| DI16 | Same source (L10)-(L14): DIRECT-Q-P implies r_4(N)=o(N/log N), with complete product-budget iteration | CONDITIONALLY PROVED; hypothesis OPEN |
| SP16 | Same source section 6: diffuse-completion actual AP-free sets for every fixed exponent 1/2<theta<2/3 | PROVED outside target density |
| NP16 | Same source section 7: p=53 arithmetic pair kernel has explicit negative rational quadratic form | PROVED counterexample to generic PSD, not Boolean/AP-free selection |
| V16 | LOG_DENSITY_VERIFICATION_20261016.json: 1,642 finite checks | COMPUTATIONALLY CHECKED ONLY |

The structural threshold in DI16 is amplitude
`a^(3/2)sqrt(ell(a))R(a)`, ell=log(2/a), R=loglog(e^2/a). It is formulated
on the explicit product-budget domain (L10), not silently on the old
linear/factor domain. At initial t=epsilon/log N, L=log N, conditional
rank is O(sqrt(L)/(sqrt(log L)loglog L)+log L), size loss is
O(sqrt(L)sqrt(log L)/loglog L+(log L)^2), and their product is o(L).
Thus the terminal theorem applies. The remaining squared-signal gain over
a^4 is a^(-1)ell(a)R(a)^2, still divergent. No unconditional increment
or target-density counterexample was obtained.

The preceding independent verifier passed again in isolation (21,465
finite checks). Historical files were preserved; checkpoint copies are in
history/log_density_20261015/, and new diagnostic evidence is in
history/log_density_20261016/. The old conditional architecture remains
available; the new one avoids its arbitrary-intermediate-factor premise.
