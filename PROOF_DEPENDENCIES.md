## Publication dependency update — 21 October 2026

Mathematical frontier: [21 October reports](docs/audits/END_TO_END_ITERATION_CLOSURE_20261021.md).
Outcome D is maintained pending formal peer review. Publication state:
`AUTONOMOUS_CHECKPOINT_20261021.json`. Historical graphs below retain their
dated claims and corrections.

| Node | Classification | Dependencies and limitation |
| --- | --- | --- |
| HC21 | PROVED polynomial chirp generalization | Generalizes k-AP hole support B q_j = 0 and tight frame reconstruction to k >= 5; HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md |
| PB21 | PROVED phase boundary & step cap transition | Resolves H = 0 sub-critical collapse vs H >= 1 super-critical activation and p_arith ~ 4.46e5; PHASE_BOUNDARY_AND_STEP_CAP_20261021.md |
| QR21 | PROVED quantitative threshold & rate | EC21 step count + dimensionless budget cancellation R(N) ~ (loglog N)^(-2); QUANTITATIVE_RATE_AND_THRESHOLD_20261021.md |
| EC21 | PROVED iterative synthesis | QP21 divergent phase selection + direct quarter-cell tradeoff + twelve-slot terminal ceiling; END_TO_END_ITERATION_CLOSURE_20261021.md |
| QP21 | PROVED finite projection certificate | Centered tight frame QF21 + dominant phase selection n <= ceil(1/a) capturing theta >= 0.10 + spectral compression; QUADRATIC_PROJECTION_SELECTION_20261021.md |
| QF21 | PROVED canonical tight frame | Non-trivial centered chirps form exact tight frame on mean-zero functions (e = 0 identically); QUADRATIC_FRAME_CERTIFICATE_20261021.md |
| CE21 | PROVED completion resolution & W8 refutation | Pointwise hole support B q = 0 implies m >= 4 a^3 mu > 0 unconditionally; W8/P12 mathematically refuted across all branches; COMPLETION_ENERGY_RESOLUTION_20261021.md |
| PD19 finite | PROVED: uniform finite terminal bounds on T5 | Original degree bounds and FP18; first-moment PD7b suffices for the qualitative corollary |
| PD19 qualitative | PROVED using an explicit classical theorem | PD7b plus qualitative four-term Szemerédi; excludes positive-density failure tails |
| C19 | PROVED auxiliary obstruction | Cyclic 29-point mask modulo 101 refuting W8 without AP exclusion |
| W8 / P12 | REFUTED across all branches | Every AP-free set strictly violates W8 by +a^4 w mu and P12 by -1/2 a^4 w mu (CE21) |

Sources: [PD19](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md) and
[C19](docs/audits/O2_COVARIANCE_ATTACK_20261019.md). There is no proved implication
from Booleanity, a small individual chirp cap and a reduced weighted count
to W8. The new obstruction requires stronger use of actual AP exclusion.

---

## 19 October 2026 — New dependency and quantifier reduction

PD19 finite estimate (PROVED from FP18 and original T5) + classical
qualitative four-term Szemerédi theorem (explicit established input,
not reproved here) -> uniform vanishing of eligible relative density ->
exclusion of the positive-density QC17 failure branch.
The remaining a->0 branch, W8, and the target remain OPEN.
[Complete proof and finite errors](docs/audits/POSITIVE_DENSITY_BRANCH_ELIMINATION_20261019.md).

---

## Operative dependency graph — 18 October 2026

**Outcome D; target OPEN.** Historical nodes below retain their original
scope and subsequent corrections. The current nodes are:

| Node | Classification | Depends on / source |
| --- | --- | --- |
| BO17 | PROVED: exact Boolean occupancy and 2/3 terminal | Original degree/pair bounds; BOOLEAN_OCCUPANCY_TERMINAL_20261017.md |
| FP18 | PROVED: fixed-pattern ceiling, in particular7/11 | BO17 mechanism, arbitrary-slot pair theorem, elementary R_4(12)=8; FINITE_PATTERN_TERMINAL_20261018.md |
| QC17 | PROVED: exact quantifier negation and deficient cubic bound | Vandermonde/Fourier proof; O2_QUANTIFIERS_CUBIC_BOUND_20261017.md; independent O2_CUBIC_AUDIT_20261018.md |
| WQ18 | PROVED: R4=U²-E_F/2, Boolean correction, P12 iff W8 | Exact chirp orthogonality branches and row centering; WEIGHTED_QUARTIC_COVARIANCE_20261018.md |
| WC18 | PROVED: weighted completion projection and disjoint energy | Four original-weight channels, AP-excluded overlaps; WEIGHTED_COMPLETION_CERTIFICATE_20261018.md |
| CA18 | PROVED CONDITIONAL implication: atomic/Gram certificate implies adequate phase | WC18 projection and actual relative Gram; existence is OPEN |
| TA18 | PROVED domain separation at polynomial density | Distinct AP hypergraph, global good-endpoint Lipschitz bound, McShane, Bernoulli martingale; BOOLEAN_TYPICAL_ALTERATION_20261018.md |
| O1 | OPEN: DIRECT-Q-GAIN on stated domain | Not implied by BO17/FP18/WC18 alone; TA18 does not refute it |
| O2 | OPEN: W8 under failed adequate phase selection | WQ18 gives exact equivalence only, QC17 is too weak |
| TARGET | OPEN unconditionally | O1 plus proved quarter-cell tradeoff and terminal regime would suffice |

No edge is asserted from nonnegative E_F to P12: the energy is subtracted.
No edge is asserted from abstract Boolean laws or sparse ineligible sets
to a genuine counterexample. The old conditional iteration remains valid;
no unconditional replacement premise was silently inserted.

---

> **17 October 2026 recovery:** The latest operative frontier is in
> [CURRENT_STATUS.md](CURRENT_STATUS.md), [OPEN_LEMMAS.md](OPEN_LEMMAS.md),
> and [RESUME_AUDIT_20261017.md](docs/audits/RESUME_AUDIT_20261017.md). The late-16-October
> pair theorem reduces the gap to R_3^F+R_4^F; DIRECT-Q-GAIN replaces the
> stronger old threshold. The target remains OPEN. Earlier entries below
> are historical and retain their original scope and later corrections.

> **15 October 2026 audit:** The current operative status and corrections are in
> `CURRENT_STATUS.md` and `RESIDUAL_FIELD_AUDIT_20261015.md`. Earlier summaries
> below are historical; the appended audit qualifies conflicting claims.

# Proof dependency graph

2 October 2026. Exactly the five classifications requested in the brief
are used below. Principal status: **(C) COMPLETE CONDITIONAL CLOSURE**.
An implication theorem can be PROVED even though its conclusion, with the
unproved hypothesis omitted, remains CONDITIONAL.

## Nodes

| ID | Statement | Classification | Evidence / dependencies |
| --- | --- | --- | --- |
| P1 | AP-free diagonal Λ4(1_A)=a/p and balanced expansion | PROVED | Algebra; prior checkpoint and NEW_RESULTS §7 |
| P2 | Mixed Cauchy-Schwarz and ||f||U3>=a^(3/2)/2 at pa³>=2 | PROVED | PHASE2_AUDIT §2; briefly reverified, not counted as new |
| P3 | A factor with energy ηa² has an increment atom with retained mass >=ηa/(2M) | PROVED | NEW_RESULTS §2, independent elementary proof |
| P4 | Quarter-refinement atoms remain narrow windows in the same group | PROVED | NEW_RESULTS §§1-2; retained separate constraints |
| P5 | Critical-rank sum Σceil(K/[sqrt(a)log(2/a)])<=U_* | PROVED | NEW_RESULTS §3; multiplicative growth, split at sqrt(t) |
| P6 | Exact retained-mass size telescope and bounds D_*,S_* | PROVED | NEW_RESULTS §4; P3-P5 |
| P7 | Restricted eligibility and original cutoff persist for every partial iteration | PROVED | NEW_RESULTS §4; P5-P6, t=ε/log N |
| P8 | Terminal density <=3/4+3d floor(p/R)/(4n) | PROVED | NEW_RESULTS §5; pigeonhole, one cyclic translation and runs |
| P9 | Comparable prime 3N<p<6N for sufficiently large N | PROVED | NEW_RESULTS §6; elementary primorial/binomial proof |
| P10 | One-time [N] embedding preserves AP-freeness | PROVED | NEW_RESULTS §4; p>3N bounds integer second differences |
| H | Restricted near-full-size-window energy at rank ceil(K/[sqrt(a)log(2/a)]) | CONJECTURED | NEW_RESULTS §1; no proof, no eligible counterexample |
| I1 | H implies r4(N)=o(N/log N), with all localization, cutoff, terminal and transfer steps | PROVED | P3-P10; NEW_RESULTS §§1-6 |
| T1 | Unconditional r4(N)=o(N/log N) through this chain | CONDITIONAL | Requires H; no unconditional proof claimed |
| P11 | Fourier parameterization, cubic bound and counting sufficient condition (7.1) | PROVED | NEW_RESULTS §7; frequency constraints, Parseval |
| P12 | Quarter-arc Fourier series and exact character-refinement energy identities | PROVED | NEW_RESULTS §8; full-group scope |
| P13 | Robust quadratic-host deletion inequality including 5/p error | PROVED | ROUTE_QUADRATIC_BOOLEAN §2 |
| P14 | Boolean pair derivative negative angular mass and angular-margin bounds | PROVED | ROUTE_QUADRATIC_BOOLEAN §3 |
| P15 | Third/fourth endpoint traces and global residual Gram/Schur PSD inequality | PROVED | ROUTE_INCIDENCE_MOMENTS §§1-2 |
| P16 | Unlabeled spectral data can coexist with arbitrarily small low-rank character-factor energy after relabeling | PROVED | ROUTE_INCIDENCE_MOMENTS §3; simultaneous permutations, concentration |
| P17 | Global AP-exclusion entropy D(Q||Bern(a)^p)>=-(p/4)log(1-a⁴) | PROVED | ROUTE_INCIDENCE_MOMENTS §4; uniform overlap chain rule |
| P18 | Full-product Freiman quadratic-shell density obstruction | PROVED | ROUTE_CONSTRUCTIONS §1; difference injection and convex slices |
| P19 | Ternary full-product and polylog-seed CRT density obstructions | PROVED | ROUTE_CONSTRUCTIONS §§2-3 |
| X1 | Character structure follows from unlabeled eigenvalues/trace powers/PSD and a distinguished independent set alone | REFUTED | P16; not a counterexample to an arithmetic-labeled theorem |
| X2 | A pure quadratic interval host at target density becomes AP-free after deleting o(|B|) points | REFUTED | P13 and explicit interval resonance |
| X3 | Arbitrary dissociated sets have size <=log_3 p | REFUTED | {1,2} in Z_5 is dissociated, but 2>log_3(5); use subset sums and log_2 p |
| X4 | The project's sparse symmetric window candidate has cyclic density >=c/log p | REFUTED | ROUTE_CONSTRUCTIONS §4; explicit prime-padding density |
| C1 | New finite scalar, Fourier, atom and terminal checks | COMPUTATIONALLY CHECKED ONLY | research_program_verification_20261002.json |
| C2 | Finite quadratic and Boolean checks | COMPUTATIONALLY CHECKED ONLY | route_quadratic_boolean_verification_20261002.json |
| C3 | Finite incidence and trace checks | COMPUTATIONALLY CHECKED ONLY | route_incidence_moments_verification_20261002.json |
| C4 | Finite construction checks | COMPUTATIONALLY CHECKED ONLY | route_constructions_verification_20261002.json |

## The complete conditional path

    P9 + P10 -> initial proper rank-one AP-free window
    H + P3 + P4 -> successor with controlled gain and occupied mass
    P5 + P6 + P7 -> every partial successor remains eligible for H
    repeated successor -> terminal density >4/5
    P8 + P5 + P6 -> terminal density <=3/4+o(1)
    contradiction -> I1 (the implication from H)

The only CONJECTURED node on that path is H. There is no other hidden
inverse theorem, geometry-of-numbers input, regularity tower, cyclic reset,
or asymptotic inference from finite examples. T1 cannot be relabeled PROVED
until H is proved or a fully rigorous alternate route bypasses it.

P11-P19 are separate proved auxiliary results; none is connected to H by
a proved implication. In particular derivative angular mass is not original
Fourier mass, and the entropy deficit is not an arithmetic energy increment.

The recent mixed-factor window argument remains a proof sketch in its own
notes. It is not a dependency of I1, P13-P19, or a claimed target disproof.

## Later October 2 structural continuation

Current principal status: **(D) NEW RIGOROUS THEOREM**. Earlier status and
nodes above are historical and remain valid with their stated conditions.

| ID | Statement | Classification | Evidence / dependencies |
| --- | --- | --- | --- |
| P20 | Relative single-character refinement gain ≥(8/π²)|E_Ωu conjugate(eξ)|² | PROVED | STRUCTURAL_SAMPLING §2; midpoint rotation averaging, projection |
| P21 | Relative many-character gain ≥κ²c*[κ²G+(1−κ²)I]^{-1}c | PROVED | STRUCTURAL_SAMPLING §3; independent rotations and Gram optimization |
| P22 | Exact sampling mean/covariance and Paley bound | PROVED | STRUCTURAL_SAMPLING §4; occupancy probabilities |
| P23 | Derivative double transform, convolution degrees, codegrees and signed coupling | PROVED | STRUCTURAL_GRAPH §1; normalized difference-variable Fourier transform |
| P24 | Support-weighted Boolean cocycle and quantitative triangle consistency criterion | PROVED | STRUCTURAL_GRAPH §3; explicit support and phase-error hypotheses |
| P25 | Uniform quadratic-phase and Boolean-host invisibility on all H-windows at expanded rank | PROVED | STRUCTURAL_GEOMETRY §§2–3; Gauss sums, interval l1 norms, tiny-cell bound |
| P26 | Relative positive quadratic resonance and nonzero APs in every H-window host | PROVED | STRUCTURAL_GEOMETRY §4A; exact lift labels, resonance, error and diagonal comparison |
| P27 | Many short shifts with quantified relative window boundary | PROVED | STRUCTURAL_GEOMETRY §1; box pigeonhole; not translation invariance of B |
| P28 | Variable-energy dyadic budget and sufficient power/log region | PROVED | STRUCTURAL_HYPOTHESIS_ATTACK §2; P3,P8,P9,P10 for its conditional target implication |
| P29 | SG implies the local target with energy goal ζa^{9/4} and rank O(a^{-1/4}/ell) | PROVED | STRUCTURAL_HYPOTHESIS_ATTACK §§2–3,6; P20,P28 plus earlier elementary terminal/transfer |
| SG | Uniform AP-free residual selection: squared relative coefficient ≥c a^{5/2}ell below the lower stopping energy | CONJECTURED | STRUCTURAL_HYPOTHESIS_ATTACK §6; precise sufficient alternative, not equivalent to H |
| SAMP | AP-free lower bound for the expected regularized-Gram sampling statistic | CONJECTURED | STRUCTURAL_SAMPLING (18); no derivative-to-residual transfer proved |
| DC | Low factor energy implies an adequate direct relative/full-group AP count | CONJECTURED | STRUCTURAL_HYPOTHESIS_ATTACK §4; only the asymptotic comparison is proved |
| X5 | Row angular mass, positivity and exact fiber exclusion force a small compressed right support | REFUTED | STRUCTURAL_GRAPH §2 diffuse abstract graph; not a Boolean H counterexample |
| X6 | Saturated Boolean pair coefficients force arbitrary selected frequencies to be additive | REFUTED | STRUCTURAL_GRAPH §4, actual AP-free Z_13 witness |
| X7 | Expanded H linear-quarter budget approximates every genuine quadratic phase on H-windows | REFUTED | P25; best squared L2 approximation error is 1−o(1) |
| C5 | Finite structural/rotation/Gram/graph/geometry/adversarial check executions | COMPUTATIONALLY CHECKED ONLY | structural_*_verification_20261002.json; exact and floating scopes in notes |
| T2 | Unconditional local target through SG/SAMP/DC | CONDITIONAL | Their structural premises remain unproved |

P20–P28 are new proved tools or obstructions. No arrow P20–P28 => H, SG,
SAMP or DC is proved. P29 proves an implication, not its premise. The H
proof and an eligible AP-free counterexample both remain absent.

## SELECT attack dependency update — 2 October 2026

Unconditional new branches:
- Pairwise AP-coordinate independence -> full-group main-term positivity
  (SELECT_ALGEBRA_20261002.md); no relative independence inferred.
- Exact AP-slot marginals + Cauchy-Schwarz -> relative main-term bound
  (SELECT_ATTACK_20261002.md); all H ranks not settled by this bound.
- AP pair codegree -> triple-balanced trades -> pair-load bound -> harmonic
  PSD perturbation -> exact-cardinality quartic moment theorem
  (SELECT_CARDINALITY_RELAXATION_20261002.md). No representing law inferred.
- Hitting identity + quadratic Fourier expansion -> quadratic bias or
  quarter deletion (SELECT_DELETION_20261002.md); no linear-bias conclusion.

Conditional branch only: WSELECT -> unchanged greedy ceiling ->
O(t^-1/2/R(t)) rank/size -> prior packing/interval transfer -> local target.
WSELECT is UNPROVED. Its proof cannot use expected Fourier squares as
pointwise caps. Full-group SIGNED is also UNPROVED and still needs window
transfer. Combined finite rerun evidence: select_reverification_20261002.json.

## Positive-moment continuation — 12 October 2026

AP codegrees + admissible-trade probability -> exact averaged balanced
trades -> bounds on each fourth-moment perturbation -> positive four-vertex
probability laws. Pair-load expectation -> constant 400ρ_4 perturbation
-> moment PSD. Zero-sum fixed-cardinality fourth-moment identity + pair
perturbation norm -> all linear-square Fourier-cap localizers. Triple-load
expectation -> conditional pair-literal PSD. Conditional sampling and
quadratic-square positivity -> cap/literal and cap/cap products. Together
these prove the specified degree-four preordering obstruction.

See SELECT_POSITIVE_MOMENTS_20261012.md for assumptions and proof. No edge
from truncated-moment feasibility to a global distribution, genuine
AP-free set, SELECT refutation, or target proof is asserted. The earlier
full-group main-term bound remains proved; signed cancellation remains open.

## Degree-six dependency update — 12 October 2026

Triple-balanced fourth moments -> exact up/down identities -> canonical
extension plus the full harmonic correction parametrization. Two
overlapping AP edges on five vertices -> negative canonical fifth moment
-> failure of the AP multiplier equation. AP exclusion X_v H_v=0 + cubic
PSD -> completion-square lower bound. Bounded overlap of completing
triples -> sixth-moment enhancement >=a^7/8. These exclude the canonical
lift but supply no exclusion of all z_5,z_6 corrections.

Boolean/cardinality/AP identities -> degree-eight global completion SOS.
Actual AP exclusion + factor projection + Fourier inversion -> relative
completion-to-residual bound; its needed spectral l1 estimate is UNPROVED.
Nonnegative top moments + cardinality -> global representation at degree k;
cap products at k+2 -> pointwise cap support, with prohibitive growing degree.

See DEGREE_SIX_ATTACK_20261012.md. No arrow from these results to SELECT,
SIGNED, an actual counterexample, or the unconditional local target is proved.

Finite p=23 branch: exhaustive root-trade averaging + affine invariance
-> exact fourth-moment orbit values -> positive rational orbit weights
-> global AP-free five-set law -> all-degree extension at these finite
parameters. No arrow to the growing-p target regime is established.

## Sixth-order Fourier dependency update — 12 October 2026

Ratio geometry + AP multipliers + cubic PSD -> sharpened localized
sixth-order enhancement. Fourier inversion -> cubic completion spectrum
and exact diagonal subtraction. Neither gives a residual coefficient.
Quadratic resonance + Gauss sums -> failure of correlation-size-only
linear inversion for bounded weights (AP exclusion absent).

AP exclusion + completion mean/variance + small spectral tail -> collective
Fourier energy lemma; the mean/variance/tail and admissible character
budget hypotheses are not proved throughout the SELECT window class.
Completion support + degree-nine literal positivity / degree-twelve PSD
-> third/fourth completion-moment bounds, without Fourier closure.
Exact rational p=29,k=6 orbit law -> finite all-degree consistency only.
No new unconditional path to SELECT or r4(N)=o(N/log N) is established.

## Two-channel completion and spectral dependency update — 14 October 2026

Pointwise AP exclusion B q_E = B q_M = 0 -> joint 2x2 cell projection
k = -alpha_C u + z -> 2x2 Loewner inequality UW >= UJ >= SS^T -> optimal
two-channel Hilbert-space overlap U^-1 S^T W^dagger S (strictly improving
endpoint-only overlap and rescuing S_E=0 proper windows).

Full-group Fourier inversion of zero-extended B + cell centering on Omega
-> unwindowed cubic Fourier synthesis k_lambda = sum_{xi!=0} hat(q_lambda)(xi) psi_xi
on proper windows -> direct regularized relative Gram bridge to quarter-arc
refinement gain Delta E. Matrix decomposition W = W_Gamma + W_tail -> exact
2x2 matrix pencil optimization ((1-mu)W_Gamma + mu W_tail)^dagger S.

Ratio geometry of E_d, M_e -> 6 interior ratios, 8 cross-ratios, AP-forced
cross-zero at r=2, and affine collapse of the 14 five-term unions ->
2x2 degree-six matrix SOS certificate.

Binomial expansion B = g + u inside nonnegative directional completion
derivatives D_k = sum_{|I|=k} Lambda_4(g on I, B on I^c) >= 0 -> exact
boundary-free identities D_1 = 4R_0+3R_1+2R_2+R_3 = 2w(S_E+S_M)+4w(a^2+v)/p,
4D_0 - D_1 = R_1+2R_2+3R_3+4R_4 = -2w(S_E+S_M)+4wU/p, and 10-block
two-channel inversion -> unconditional scale-a^4 lower bounds R_1 >= -4R_0,
3R_1+R_2 >= -6R_0, 3R_1+2R_2+R_3 >= -4R_0 -> finite-dimensional LP dual
proof that R_4 = Lambda_4(u) is unconstrained from below by D_1..D_4 and
bounds on R_1,R_2,R_3 alone (verified across all 10 reflection-symmetric
blocks). Exact Collapse Theorem: F_SIGNED := w(S_E+S_M) + R_3/2 + R_4 =
R_0 + R_1/2 + w(U-a^2-v)/p identically -> repaired R_1-free conservation law
w(S_E+S_M) + (R_3/2 + R_4 - R_1/2) = R_0 + w(U-a^2-v)/p and three-way
dichotomy. Operator block decomposition <u,(K_B+R_B)u>_p = DIAG + CROSS + COMPLEMENT
-> exact cancellation of 2<g_A,K u_C>_p in CROSS + COMPLEMENT and dual Schur
complement bounds on A^c. Exact Branch II identification: w(S_E+S_M) <= theta R_0
forces R_3 <= -2(2-theta)R_0 - 3R_1 - 2R_2 + 4w(a^2+v)/p and
R_4 >= (3-2theta)R_0 + 2R_1 + R_2 + w(a-4a^2-4v)/p. Exact linear-residual
pairing: R_1 = 2<u,h_{E,g}+h_{M,g}>_p = R_{1,(2)} + R_{1,(3)} with
|R_{1,(2)}| <= 12a rho v = o(a^4) under SELECT failure and ||H_g^{(3)}||_2 <= 2v^(3/2)
-> Branch III variance floor v >= c_1 a^(7/3) and collective capture
>= (1-2c_0)^2 R_0^2/(64v^3) >= c' a^(5/4) conditional on H_g^{(3)} tail bound.
Trilinear L2 stability ||C_{E/M}(f_1,f_2,f_3)||_2 <= ||f_1||_2||f_2||_2||f_3||_2
-> cubic approximation stability ||H_h^{(3)} - H_{h_L}^{(3)}||_2 <= 6v||h-h_L||_2,
1D cubic harmonic decay O(log|t|/t^2), and l^1-Fourier bounds
|R_1| <= 4 rho v(3a + ||hat(h)||_1), |R_{2,(1)}| <= 12a rho^2 ||hat(h)||_1,
and |R_{2,(2)}| <= 6 rho^2 ||hat(h)||_1^2 (via the single-variable Fourier
formula for R_{2,(1)}). Weight-k ANOVA decomposition on T^d -> Fourier cap
|hat(G_S)(m)|^2 <= (8/pi^2)^k ||G_S||_2^2 and continuum Walsh cubic norm 4/27.
One-sided physical truncation g >= W(a-h_-) inside D_3 + Z_p^2 pairwise
bijection -> D_3 >= a^3 sum_i Lambda_4(B at i, W at != i) - 6w^2 a^3 sqrt(v)
on Omega, and on Z_p proves D_3 >= 4a^4 - 6a^3 sqrt(v),
R_1 >= -6a^3 sqrt(v) - 16a v^(3/2) - 4v^2 = -O(a^(33/8)), and
T >= a^4 - 3a^3 sqrt(v) - 4a v^(3/2) - v^2 + (U-a^2-v)/p -> unconditional
elimination of Branch III on Z_p for all v <= zeta a^(9/4) and strict
two-branch positive dichotomy (Branch I: S_E+S_M >= a^4/2 - O(a^(33/8));
Branch II: R_3/2 + R_4 >= a^4/2 - O(a^(33/8))). Spectral splitting
hat(q_E)+hat(q_M) = K^(2)+K^(3)-2hat(f)/p -> ||K^(2)||_2^2 <= 36a^3 rho^2 = O(a^(11/2)ell(a));
clipped completion tilde{q} = min(q_E+q_M, tau_q) -> L^2 projection energy
>= tilde{S}^2/(tau_q E[tilde{q}]) and peak-set projection E_peak(tau_q) >= tau_q S_{>tau_q}^2/(4w^2 a^2 E[q]);
proper-window marginal l^1 bound |sum_i Lambda_4(u at i, W at != i)| <= 4w^2 rho_Omega ||hat(W)||_1
(resolving Sublemma 2C); Fourier operator splitting Q_0 K_B Q_0 = a L_{E,f} + Q_0 K_f Q_0
and tr(K_u^4) = tr(R_u^4) <= ||u||_{U^3}^8 -> ||K_u^(3)||_2^2 <= 4U||u||_{U^3}^4 and
universal Branch II identity Y = a(T_u+S_u) + <u/2+h, K_u^(3)>_p <= 2a sqrt(U)||u||_{U^2}^2 + sqrt(U(U+4v))||u||_{U^3}^2;
bilateral multiplier set Gamma_alpha^*(tau) -> sum_{xi in Gamma_alpha^*}|hat(u)(xi)|^2 >= |T_u+S_u|/(8 rho);
exact validity polynomial a^2 - U(U+4v) = a^3(2-a) - 2a(1-a)v + 3v^2 -> |Y| <= a(1+2sqrt(U))||u||_{U^3}^2 for v <= a^2;
diagonal-free Branch I and zero-baseline Branch II all-chirp identities -> c=0 linear part of <h,K_u^(3)>_p is <= 2 rho^2 sqrt(vU) = o(a^4);
quadratic window translation mixing | |Omega_quad cap (Omega_quad+h)|/p - w^2 | <= (||hat(1_I)||_1^2 - w)/sqrt(p) -> pure quadratic-arc windows lose >= 1-w-o(1) under every h != 0;
exact continuum hitting-degree evaluation Z_I = (8/27)w^3 and max_I H = (23/18)w^2 (0 < w <= 1/4) -> single quadratic window has analytic terminal density <= 53/69 + o(1) < 4/5, while s >= 2 quadratic coordinates decay as (16/69)^s;
per-slope r-mean subtraction in chirp space -> centered baseline-free chirp identities for S_E, S_M, M_E, M_M, R_4 and universal fourth-moment norm sum_{c!=0,r} W_tilde_u(c,r)^2 = U^2 - ||u||_{U^2}^4 - (E[u^4]-U^2)/p;
4(L-1) < p zero-wraparound integer congruence -> exact finite-p bounds Z_I >= (8/27)w^3 + w/(3p^2) and max_I H <= (23/18)w^2 + 4w/(3p) + 2/p^2;
pointwise nonnegativity of phi_lambda^(m) = 1_Omega g^m q_lambda and phi_lambda^(>= gamma a) -> pointwise Fourier caps |hat(phi_lambda^(>= gamma a))(xi)| <= (w/(gamma a))S_{>= gamma a}(lambda) -> elimination of W_Gamma denominator barrier (sum_Gamma |c_xi|^2 >= theta^2 gamma^2 a^2/(|Gamma|w^2));
Holder (3,3,3) on T_u, S_u -> sum_{xi!=0}|hat(u)(xi)|^3 >= |T_u+S_u|/2 -> dyadic shell dichotomy (single-character SELECT holds whenever winning shell has size <= c_2 a^(-3/4)ell(a)^(-7/2)).

See MULTI_POSITION_COMPLETION_20261014.md, TWO_CHANNEL_SPECTRAL_ATTACK_20261014.md,
MIXED_COUNT_CLOSURE_20261014.md, SIGNED_QUARTIC_ATTACK_20261014.md,
TWO_CHANNEL_OPERATOR_BLOCKS_20261014.md, TWO_CHANNEL_DICHOTOMY_CLOSURE_20261014.md,
THREE_BRANCH_AMPLIFICATION_20261014.md, CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md,
CUBIC_RESONANCE_ATTACK_20261014.md, FINAL_STRUCTURAL_BOTTLENECK_20261014.md,
TWO_BRANCH_AUTONOMOUS_CLOSURE_20261014.md, QUADRATIC_TWO_BRANCH_CLOSURE_20261014.md,
QUADRATIC_TO_LINEAR_TRANSFER_20261014.md, and RESIDUAL_FIELD_AMPLIFICATION_20261014.md.
No arrow from these proved theorems to unconditional SELECT, SIGNED, or
r4(N)=o(N/log N) is claimed; Sublemmas 2A'' and 2B'' in OPEN_LEMMAS.md remain OPEN.


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

## Operative dependency update — 16 October 2026

The local target remains OPEN. The following new arrows have complete
written proofs in MIXED_QUADRATIC_TERMINAL_20261016.md and
LOG_DENSITY_ATTACK_20261016.md; finite tests are supplementary evidence.

    nonnegative Fourier tent coefficients + elementary quadratic Gauss sums
      -> persistent baseline mu>=eta^(d+2s)
      -> common degree baseline + exceptional mass of vertex average <=1/p
      -> erosion bound + exact weighted diagonal subtraction
      -> MT16 mixed-window terminal theorem

    relative phase correlation of B-a
      -> random quarter-midpoint averaging
      -> DA16 single cell with both density gain and retained occupied mass

    OPEN DIRECT-Q-P on domain (L10)
      -> DA16 -> exact dyadic sums (L4), optimized bounds (L12)
      -> rank times log-size loss=o(log p)
      -> MT16 terminal contradiction + elementary prime/integer transfer
      -> r_4(N)=o(N/log N) [CONDITIONAL ONLY]

    MT16 degree estimates -> MR16 weighted first-residual control
    Boolean AP exclusion + exact diagonal -> residual identity (L8)
    OPEN signed estimate (L9) under failure of DIRECT-Q-P
      -> contradiction with (L8) -> DIRECT-Q-P along reachable windows

No proved arrow supplies DIRECT-Q-P or (L9). The original SELECT/WSELECT/
COLLECTIVE-WSELECT/retention dependencies are also still OPEN. The new
first-residual estimate is for the specified weighted form and cannot
be substituted into an old unweighted identity without a separate proof.

Independent failed shortcut: NP16 is an exact arithmetic-kernel counterexample
to pair PSD under positive-Fourier weights. Its witness is non-Boolean;
Boolean/AP-free information remains potentially decisive. Sparse SP16 is
an actual AP-free family only for 1/2<theta<2/3, outside the target regime.
