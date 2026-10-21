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
