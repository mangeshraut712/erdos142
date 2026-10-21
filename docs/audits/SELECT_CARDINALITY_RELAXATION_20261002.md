# Degree-four AP moments with exact cardinality

2 October 2026. Offline. **PROVED moment-relaxation theorem**, not a
probability distribution, an AP-free construction, or a refutation of SELECT.
No literature novelty is claimed. This repairs the cardinality defect of
the simpler quartic certificate in SELECT_QUARTIC_RELAXATION_20261002.md.

## 1. Exact statement and limitations

Let Ω⊂Z_p have n≥200 points, p>3 prime, and let E be its distinct unordered
nonzero 4AP four-sets. For 4≤k≤n−2 put a=k/n and

    ρ_j=(k)_j/(n)_j,  B_n=800+16log n.

If

    (n−k)(n−k−1)≥B_n(k−2)(k−3),                         (C1)

there is a real linear functional L on multilinear Boolean polynomials of
degree at most four such that:

1. L(1)=1 and L(X_S)=ρ_|S| for |S|≤3.
2. L(X_e)=0 for every e∈E (the actual quartic AP equation).
3. L(q²)≥0 for every real polynomial q of degree at most two, with squares
   reduced using X_i²=X_i.
4. L[(Σ_iX_i−k)X_T]=0 for |T|≤3: exact cardinality through degree four.

For any relative character, the spatially centered polynomial residual
u_i=X_i−a has zero spatial mean in this quotient, and its Fourier square has

    L|E_Ω u_i e_p(−ξi)|²
       =a(1−a)/(n−1)·[1−|E_Ω e_p(ξi)|²]≤a/(n−1).      (C2)

At n≥p exp(−sqrt(log p)) and a≈ε/log p, C1 holds for each fixed ε and
sufficiently large p, while C2 is o(a^{5/2}log(2/a)).

This proves feasibility of the explicitly listed degree-four moment
relaxation, even with the quartic AP equations and cardinality included.
It does NOT prove feasibility of all SELECT constraints. In particular,
the per-frequency bounds in C2 are expectations; higher localizing
constraints for pointwise Fourier caps, all nonnegative four-literal
cylinder probabilities, and an actual representing law are not established.
Nor does max_ξ L|c_ξ|² control L(max_ξ|c_ξ|²). These distinctions prevent
mistaking the theorem for an AP-free Fourier-invisible counterexample.

## 2. AP hypergraph bounds

A fixed pair of distinct vertices belongs to at most twelve AP four-sets:
assign the two specified vertices to distinct positions i,j∈{0,1,2,3}.
Each of twelve assignments determines the difference and start uniquely,
because j−i is invertible modulo p. Reversal can improve twelve to six,
but twelve suffices here. Summing pair degrees shows every vertex has
degree at most 4(n−1), and |E|≤n(n−1)≤n².

## 3. Balanced trades with no extra AP roots

For each root edge e={x_1,x_2,x_3,x_4}, independently choose four distinct
alternatives y_1,...,y_4 outside e. For σ∈{0,1}⁴ let e_σ contain x_i if
σ_i=0 and y_i if σ_i=1. Condition the choice on every e_σ with σ≠0
being NON-AP. This condition has probability at least 1/2 for n≥200.

Indeed the union bound over the number q of alternatives gives at most

    48/(n−7)+144/(n−7)²+96n/(n−7)³+24n²/(n−7)⁴<1/2.

For q=1, an AP containing three fixed roots has at most twelve possible
completions. For q=2, twelve edges contain the fixed pair and there are
two alternative orderings. For q=3 use vertex degree≤4n and six orderings;
for q=4 use |E|≤n² and twenty-four orderings. The denominators n−7
conservatively bound all without-replacement probabilities. The displayed
bound decreases with n and is below .256 at n=200.

Define an integer signed trade

    t_e(S)=−Σ_σ (−1)^|σ| 1_{S=e_σ}.

It equals −1 on its AP root and zero on every other AP edge. For every
triple T, Σ_{S⊃T}t_e(S)=0: the two completions in the unused coordinate
cancel; a triple using both members of a coordinate pair occurs nowhere.

## 4. A uniform pair-load bound

For a fixed pair P, one trade contains either zero or four transversals
containing P. Let N_P count participating trades. Their independent
indicator means sum to at most

    12+48n/(n−4)+24n²/[(n−4)(n−5)]<100.                 (C3)

The first term covers roots containing both points. Roots containing one
point number at most 8n; the other point can occupy three allowed
alternative slots, probability≤3/(n−4), doubled by conditioning. For
roots containing neither, twelve ordered alternative placements have
probability≤12/[(n−4)(n−5)], again doubled. Thus C3 is valid uniformly.

Independence gives E exp(N_P)≤exp((e−1)EN_P)≤exp(200). Markov therefore
gives P(N_P>200+4log n)≤n^{-4}. A union bound over fewer than n² pairs
shows a positive-probability choice of all trades with

    N_P≤200+4log n  for EVERY P.                         (C4)

Fix such a choice. Put t(S)=Σ_e t_e(S), and set

    L(X_S)=ρ_4[1+t(S)] for |S|=4,

retaining uniform fixed-k moments for all lower degrees. AP moments vanish
exactly. Triple balancing preserves the fixed-cardinality identities:
for |T|=3 the only new terms are Σ_{S⊃T}ρ_4t(S)=0; lower degrees are
unchanged. Boolean reduction defines all remaining polynomial evaluations.

Some non-AP fourth moments need not be nonnegative. This is a degree-four
PSD functional, not an asserted probability law; see the limitations above.

## 5. Positive semidefiniteness

Index pair monomials by two-sets P. The change Δ in their Gram block has
entry ρ_4t(P∪Q) for disjoint pairs and zero otherwise. It is symmetric and
has absolute row sum at most 4ρ_4 N_P≤ρ_4B_n by C4. Hence ||Δ||op≤ρ_4B_n.

Let U be the pair/vertex incidence matrix. Triple balancing implies ΔU=0:
for i∉P, the relevant sum is over all four-sets containing P∪{i}; for
i∈P it vanishes because changed entries require disjoint pairs. Thus Δ
acts only on H=ker(U*) (the harmonic pair-coefficient subspace).

The uniform fixed-k pair Gram block is

    M0=λI+(ρ_3−ρ_4)UU*+ρ_4J,
    λ=ρ_2−2ρ_3+ρ_4
      =ρ_2 (n−k)(n−k−1)/[(n−2)(n−3)].                  (C5)

On H it is exactly λI. H also has zero cross-block with constant and
linear monomials: its pair coefficients have zero total and zero sum
at every vertex. The remaining blocks retain the genuine uniform fixed-k
PSD matrix. Consequently the entire degree-two moment matrix remains
PSD whenever λ≥ρ_4B_n. This is exactly C1. It proves the theorem.

## 6. Target-density comparison and meaning

For a≈ε/log p and n in the allowed window range,

    ρ_4B_n/λ=O(a²log n)=O_ε(1/log p)→0.

Since second moments are unchanged, C2 follows by expanding the character
square under uniform fixed-size sampling. Moreover

    [a/(n−1)]/[a^{5/2}log(2/a)]
      =O_ε(exp[−log p+sqrt(log p)](log p)^{3/2}/log log p)→0.

Thus a basic degree-four Boolean PSD certificate with exact AP moments,
cardinality, and per-frequency expected-square caps is feasible at the
target scale. A successful dual argument needs additional information,
such as the missing Fourier-cap localizers, nonnegative higher moments, or stronger arithmetic consistency. This is a precise limitation of the
specified relaxation, not a lower bound on the degree needed by every
possible SOS proof of SELECT.

An independent algebraic/combinatorial audit checked the trade probability,
pair load, harmonic block, and cardinality identities. Finite checks are
saved separately in verify_select_cardinality_20261002.py and its JSON.
