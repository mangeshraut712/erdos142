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
