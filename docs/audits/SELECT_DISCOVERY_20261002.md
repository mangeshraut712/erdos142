# SELECT discovery and explicit low-order duality barrier

2 October 2026. Offline. No dependency installed. Principal conclusion of this lane: no proof or asymptotic refutation of SELECT; an exact degree-two relaxation barrier and finite genuine-AP-free search were obtained. No novelty claim is made.

Scope: new directive d2d994a5 and its exact SELECT target. Prior CURRENT_STATUS, STRUCTURAL_HYPOTHESIS_ATTACK, NEW_RESULTS, SOLUTION_LEDGER, PROOF_DEPENDENCIES, AGENTS and directly used derivative/quarter-conversion notes were inspected in this and the preceding continuous research turn. Old files are preserved. Root handles downstream thresholds and geometry; this lane concentrates on computational discovery and dual certificates.

## 1. Exact residual Parseval certificate

Let Ω⊂Z_p have n points, B=1_A, a=|A|/n, F any partition, g=E_Ω(B|F), u=B-g, and V=E_Ω|g-a|². Orthogonal decomposition and Booleanity give

    E_Ω|u|²=a(1-a)-V.

Extend u by zero outside Ω. For relative coefficients c_ξ=n^-1 sum_(x∈Ω)u(x)e_p(-ξx), full-group character orthogonality gives

    sum_(ξ∈Z_p)|c_ξ|²=(p/n)[a(1-a)-V].

Since c_0=0,

    max_(ξ!=0)|c_ξ|² >= p[a(1-a)-V]/[n(p-1)].             (D1)

This is valid on every relative window and every existing factor; no relative orthogonality was assumed. Under V<ζa^(9/4), it gives

    max |c_ξ|² >= p a[1-a-ζa^(5/4)]/[n(p-1)].             (D2)

For a≤4/5, ζ≤1/4, the bracket is positive: its minimum occurs at 4/5 and exceeds 0.01. This is an unconditional finite certificate, but at the target density it only has size a/n. Its SELECT-normalized scale is

    O(1/[n a^(3/2) log(2/a)]),                           (D3)

which tends to zero uniformly for n≥p exp(-sqrt(log p)), a≈ε/log p. Thus D1 is inadequate for the target by an exponentially large-in-log-p factor.

The Z_13 AP-free difference set {0,1,3,9}, with trivial F, saturates D1 exactly: all nonzero squared coefficients are 3/169. This is a sharpness example for that universal Parseval argument, not a target-density asymptotic counterexample.

## 2. A strengthened degree-two PSD relaxation cannot prove SELECT

The first-moment LP relaxation is already insufficient. Replacing Boolean B_x by b_x∈[0,1], retaining fixed mean a, and imposing each AP inequality sum_(x∈e)b_x≤3 admits b_x=a whenever a≤3/4. It has u=0 for every partition F and zero residual coefficients. Therefore its minimum Fourier objective is zero. A first-moment dual cannot separate these constraints.

One can strengthen the relaxation considerably and it still fails at the target scale.

**Proposition.** Let Ω be ANY n-point ground set, choose integer 1≤k≤n/3, a=k/n, and assign first and second Boolean moments

    L(B_x)=a,
    L(B_x²)=a,
    L(B_xB_y)=ρ=k(k-1)/[n(n-1)] for x!=y.               (D4)

These satisfy:

1. PSD of the full degree-one moment matrix indexed by 1,B_x;
2. Boolean diagonal identities B_x²=B_x;
3. exact cardinality in moments: L(sum B_x)=k and L(B_x sum B_y)=kL(B_x);
4. L(sum_(x∈e)B_x)≤3 for every four-point AP edge e;
5. the same AP inequality multiplied by EVERY B_i or 1-B_i, for every i in Ω, including vertices outside e.

Yet every relative Fourier square has moment

    L(|n^-1 sum_(x∈Ω)(B_x-a)e_p(-ξx)|²)
       =a(1-a)/(n-1) · [1-|E_Ωe_p(ξx)|²]
       <=a/(n-1).                                      (D5)

With trivial F, low-factor-energy is exactly zero. For an H-window and k/n≈ε/log p, the right side in D5 is o(a^(5/2)log(2/a)), uniformly over every frequency. Hence this entire listed moment/PSD system admits failure of the desired Fourier lower bound.

### Proof

The covariance matrix from D4 is

    X-aa^T=(a-ρ)(I-J/n).

Its constant eigenvalue is zero, and every other eigenvalue is a-ρ>0. The moment matrix is PSD by its Schur complement. Its row sum is

    a+(n-1)ρ=ka,

so exact cardinality holds.

For an AP edge of four distinct points, its expected occupancy sum is 4a≤3. For the multiplier B_i, its expectation is a+3ρ if i∈e, and 4ρ otherwise. Since ρ≤a² and a≤1/3,

    a+3ρ≤2a≤3a,
    4ρ≤(4/3)a≤3a.

For the multiplier 1-B_i, the expectation is 3a-3ρ if i∈e, and 4a-4ρ otherwise. The inequalities

    3a-3ρ≤3a≤3(1-a),
    4a-4ρ≤4a≤3(1-a)

hold for a≤1/3. Thus every listed multiplied AP inequality holds.

For D5 use the covariance matrix above and the character vector on Ω. Its squared norm is n and its constant projection has squared norm n|E_Ωe_ξ|². Thus the quadratic form divided by n² is

    (a-ρ)/n · [1-|E_Ωe_ξ|²]
       =a(1-a)/(n-1) · [1-|E_Ωe_ξ|²].

At a≈ε/log p and n≥p exp(-sqrt(log p)), its ratio to the SELECT threshold is at most

    O_ε(exp(sqrt(log p))(log p)^(3/2)
                      /[p log log p]) ->0.              (D6)

This proves the proposition and its quantitative consequence.

### Exactly what this does and does not rule out

D4 are actual moments of the uniform k-subset ensemble. That ensemble is NOT supported on AP-free sets: for k≥4 its AP-edge occupancy moment is

    L(product_(x∈e)B_x)=(k)_4/(n)_4>0.

The genuine quartic equation product_e B_x=0 is absent from the degree-two relaxation. The proposition therefore refutes an attempted SELECT proof from the enumerated low-order constraints; it does not refute SELECT, higher-degree SOS, or a relaxation incorporating the exact quartic exclusions and their consistency.

The squared Fourier inequalities in this relaxation are inequalities on moments, not a guarantee about every individual sampled k-subset. This distinction is essential. The certificate is an exact feasible point for the lifted moment optimization problem.

## 3. Genuine AP-free finite discovery

The script discover_select_20261002.py enumerates every subset in the following domains, discarding any subset containing a nonzero cyclic AP:

- full groups Z_p, p=5,7,11,13,17 (full-group diagnostics, not H-windows);
- proper rank-one narrow windows Ω={0,...,floor(p/3)-1}, p=13,17,19,23,29,31,43.

It then tests F trivial and six rank-one quarter factors: characters ξ=1,2,3 and rotations θ=0,1/8. For each factor it computes V, the exact-in-form residual, every nonzero relative coefficient, and

    ratio=max |c_ξ|²/[a^(5/2)log(2/a)].

It records minima only when V<ζa^(9/4), for ζ=1/32,1/8,1/4. Proper-window examples also meet the recorded lower density threshold ε/(2log n) with ε=0.1, upper density≤4/5, rank≤floor sqrt(log p), size≥p exp(-sqrt(log p)), and narrow diameter. No statement that these primes exceed unknown p0(ε) is made.

The factor family is intentionally explicit and small. This is not enumeration of all intermediate factors. A rank-one tested factor is an intermediate factor in the greedy premise only when M(a)≥2. For the stated greedy stopping threshold this is guaranteed if

    c < ζa^(-1/4)/[(8/π²)log(2/a)].                      (D7)

Each nontrivial witness records this requirement numerically, rather than assuming an unspecified c or rank budget. The trivial factor has no such restriction.

There were 174,538 subset/factor residual cases. The smallest recorded proper-window ratio at ζ=1/8 or 1/4 was approximately 0.047398, at

    p=43, Ω={0,...,13}, A={0,2,3,5,6,7,11,12,13},
    F=quarter partition of character1, rotation0.

For ζ=1/32, the smallest proper-window ratio was approximately 0.066394 at p=31. The lowest full-group diagnostic ratio was approximately 0.086843 at p=11. These observations neither prove a positive asymptotic lower bound nor refute constants smaller than the observed ratios. They also show why removing an intermediate factor cannot be ignored: some minima occur after a genuine low-energy quarter conditioning.

The search validates D1 on every evaluated residual. It used floating Fourier arithmetic with tolerance 1e-10. AP-free detection is exact bitmask enumeration of all cyclic progression edges.

## 4. LP evidence and available dependencies

The environment already has NumPy and SciPy; cvxpy, pulp and ortools were absent. No package was installed. SciPy HiGHS first-moment LPs were solved for a full-group p=13,density4/13 instance and a proper p=43,n=14,density1/2 instance. Both attain objective zero, as certified analytically by b_x=a. The proper-window LP bounds residual real/imaginary Fourier components after subtracting a; it does not mistakenly bound the original window-supported coefficients.

The checker verify_select_duality_20261002.py independently verifies the moment PSD eigenvalues, cardinality identities and all AP multiplier cases using exact fractions for 62 parameter instances. Its output also includes numerical asymptotic samples of D6; the limit is established by the symbolic exponent, not those samples.

## 5. Remaining exact attack after this lane

A dual certificate for SELECT must use information absent from D4, namely the exact quartic AP-edge moment zero AND compatible higher moments from one deterministic Boolean set. A certificate using only degree-two PSD, Boolean diagonal, exact size, AP occupancy-sum constraints and their one-Boolean-variable multipliers cannot work, even on the permitted relative geometry.

The next genuinely new dual search should add the quartic AP zero constraints and study their interaction with the Fourier square objective. This note does not assert that a fixed SOS degree suffices. No unconditional SELECT inequality, valid asymptotic counterexample, or target proof was found.

Files: discover_select_20261002.py; select_discovery_verification_20261002.json; verify_select_duality_20261002.py; select_duality_verification_20261002.json. All earlier files were retained.
