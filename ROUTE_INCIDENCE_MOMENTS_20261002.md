# Incidence, higher traces, and aggregate entropy: new offline calculations

2 October 2026. No internet used. Status: auxiliary propositions proved; the local target `r_4(N)=o(N/log N)` remains unresolved. No research novelty is claimed. Earlier notes are source material, not axioms. This document addresses routes F, G, H of the new brief.

## 1. Exact third and fourth traces

Let p>3 be prime, A subset Z_p, B=1_A, k=|A|. Raw matrices have no averaging factor. Define

    J(y,z)=1_{y!=z} B((2y+z)/3) B((y+2z)/3),
    D=diag(B), K=D+J.

Thus K is p times the normalized endpoint operator. Write d_y=(J^2)(y,y)=sum_z J(y,z). Cyclicity of trace, J(y,y)=0, D^j=D for j>=1 give EXACTLY

    tr K^3 = k + 3 sum_{y in A} d_y + tr J^3,
    tr K^4 = k + 4 sum_{y in A} d_y
                 + 2 sum_{y,z in A} J(y,z)^2
                 + 4 sum_{y in A} (J^3)(y,y) + tr J^4.       (1)

Proof: expand into words in D,J. For cube, words with one J have trace zero, words with two J contribute three tr(DJ^2). For fourth power, the six two-J words comprise four cyclic copies of D^2J^2 and two of DJDJ. The four three-J words give four tr(DJ^3); one-J words vanish. This proves both identities without any AP-free assumption.

If A is 4-AP-free, the A-by-A block of J is zero. Consequently the two-D/two-J alternating contribution in (1) vanishes. But three-J closed walks passing through A need not vanish. For example in Z_11, A={0,1,2,4,5} is 4-AP-free and J has the triangle on vertices {0,3,6}, so (J^3)(0,0)>0. This specific example can be checked directly from the displayed formula.

More generally `tr K^m` counts length-m cyclic sequences y_0,...,y_{m-1} whose indicated endpoint transitions have occupied middle pairs. A non-diagonal transition between two vertices in A is forbidden. No rule forbids consecutive transitions through unoccupied vertices or triangles with exactly one occupied endpoint. All these counts are nonnegative. Merely increasing m does not eliminate them.

## 2. A global Schur-complement inequality

For every ordered middle pair (u,v) in A^2 with u!=v make a column of R with ones at 2u-v and 2v-u. Put G=RR^T. Its off-diagonal entries are 2J(y,z). Its diagonal is the retained incidence degree, denoted h_y. Because A is AP-free,

    G[A,A]=diag(h_y:y in A).                                (2)

Rows belonging to A have mutually disjoint supports. Any zero h_y row is identically zero and can be omitted. Let A_+={y in A:h_y>0}, C=Z_p\A, and let U=G[C,A_+]. Orthogonal projection onto the span of the normalized rows indexed by A_+ gives

    G[C,C] - U diag(h_y^-1) U^T >= 0.                        (3)

This is PSD order. It is an exact global constraint, stronger than just the two-by-two minors.

Explicit proof: let r_y be row y of R and let Pi be orthogonal projection in the column space onto the mutually orthogonal r_x, x in A_+. Then

    <(I-Pi)r_y,(I-Pi)r_z>
       = G[y,z] - sum_{x in A_+}G[y,x]G[x,z]/h_x.

The residual Gram matrix is PSD. For every real vector v on C this yields

    sum_{x in A_+} (sum_{y in C}G[x,y]v_y)^2/h_x
        <= sum_{y,z in C}G[y,z]v_y v_z.                     (4)

Higher trace powers or Schatten bounds can be applied to this PSD inequality. However, all terms retain their arithmetic labels; deleting those labels loses the needed extraction information, as section 3 proves.

In a controlled window the same argument holds after restricting all endpoints and middle pairs to that window. No AP-richness hypothesis is needed for (3); a lower bound on h_y is a separate occupied-middle-pair assertion, not implied by ambient incidence supply.

## 3. A rigorous obstruction to unlabeled spectral extraction

**Proposition (all spectral data versus character-factor energy).** Fix any graph/matrix pair on p vertices with a distinguished independent set of k vertices. Simultaneously permuting rows and columns preserves every eigenvalue, every trace power (even m growing with p), Schatten norms, PSD constraints, ranks, and all interlacing statements relative to the distinguished set. If

    a=k/p, 4^d [d log p + log p] = o(a^2 p),                 (5)

there is such a permutation for which the permuted distinguished set A' has

    sup_F Var(E(1_A'|F)) = o(a^2),                           (6)

where F ranges over all factors of at most d cyclic characters, each quantized into four equal rotated half-open arcs.

This is a statement about an unlabeled graph and its distinguished set. The permuted graph generally DOES NOT equal the arithmetic endpoint graph of A'. It is therefore not an AP-free construction and not a counterexample to the actual structural theorem.

Here is a quantitative proof. Choose A' uniformly among all k-subsets of Z_p. For a fixed character and rotating its four arcs, the partition changes only when a point meets an arc boundary. There are at most 4p distinct rotations as partitions; there are p characters. Thus d-tuples of partitions number at most (4p^2)^d, and each has at most 4^d cells. Include shorter tuples by padding with the zero-character partition. The total number of cells to check, counted with multiplicity, is at most (16p^2)^d.

Generate independent Bernoulli(a) variables first, then condition on their sum being k. The binomial distribution has k as a mode when a=k/p, so its mass at k is at least 1/(p+1). For a cell S of size s>0, Hoeffding's inequality for independent Bernoulli variables gives

    P(| |A' intersect S|-as | > sqrt(s L/2))
           <= 2(p+1) exp(-L)                               (7)

after conditioning. For completeness the independent bound follows from
`log E exp(t(X-EX)) <= t^2/8`: the second derivative of the log-mgf is the variance of a tilted Bernoulli variable, at most 1/4; integrate twice from zero and optimize t. Summing the two tails proves (7). Conditioning multiplies probability by at most p+1.

Take

    L=log(2(p+1)) + d log(16p^2) + 2 log p.

A union bound gives probability at least 1-p^-2 that EVERY cell of EVERY admissible factor satisfies the bound. On this event, the exact conditional energy is

    Var(E(1_A'|F))
      = (1/p) sum_{S in F, s>0} (|A' intersect S|-as)^2/s
      <= 4^d L/(2p).                                      (8)

This proves (6) under (5). A bijection mapping the original distinguished set onto any such A' exists, and simultaneous conjugation preserves all listed matrix data. This completes the proof.

At a >= epsilon/log p, ranks d=O((log(1/a))^C) with fixed C satisfy (5), because `4^d=p^{o(1)}` and a^-2=O(log^2 p). Even arbitrary precision in all trace powers cannot, by itself, replace a theorem exploiting the exact arithmetic form of J. The escape from this obstruction must retain the map `(y,z) -> ((2y+z)/3,(y+2z)/3)` throughout spectral extraction.

## 4. Aggregate AP-exclusion entropy

Let P_a be the independent Bernoulli(a) law on all p cyclic coordinates. Let Q be ANY Boolean law supported on cyclic 4-AP-free subsets. Its coordinate marginals are not assumed equal to a. Natural logarithms are used. For each ordered (x,d), d!=0, let e_{x,d}={x,x+d,x+2d,x+3d}. There are p(p-1) edges with multiplicity, each of four distinct vertices; every vertex has multiplicity-degree exactly 4(p-1).

**Proposition.** For 0<a<1,

    D(Q||P_a) >= -(p/4) log(1-a^4) >= p a^4/4.             (9)

Proof of the entropy-cover step: order the vertices. Chain rule and monotonicity of conditional entropy imply

    H_Q(X_e) >= sum_{i in e} H_Q(X_i | X_1,...,X_{i-1}).

Summing over all edge occurrences gives `sum_e H_Q(X_e) >= 4(p-1) H_Q(X)`. Because P_a is a product law, its log-density terms sum with the same uniform multiplicity. Therefore

    sum_e D(Q_e || (P_a)_e) <= 4(p-1)D(Q||P_a).

Each Q_e gives probability zero to the all-ones assignment. Among all laws with that support restriction, the smallest divergence from (P_a)_e is `-log(1-a^4)`: decompose divergence relative to `(P_a)_e` conditioned on avoiding all ones. There are p(p-1) edge occurrences. Division proves (9). This counts overlap exactly; no independence between AP constraints was assumed.

At a=epsilon/log p, (9) grows as `epsilon^4 p/(4 log^4 p)`, but its PER-COORDINATE size is only `epsilon^4/(4 log^4 p)`. Neither total growth nor this inequality supplies correlation with a character factor.

If Q has all one-coordinate marginals equal to a, then

    D(Q||P_a) = p h(a)-H_Q(X),

so (9) is a genuine global entropy deficit at fixed marginals. It still says nothing about where the deficit lies arithmetically.

### Why summing occupied stars does not multiply information freely

For vertex x write q_x=Q(X_x=1). The exact divergence chain rule is

    D(Q||P_a) = D(Bern(q_x)||Bern(a))
       + q_x D(Q_{-x}|X_x=1 || (P_a)_{-x})
       + (1-q_x)D(Q_{-x}|X_x=0 || (P_a)_{-x}).              (10)

Thus every individual weighted occupied-star cost is bounded by the SAME global divergence. Summing gives only

    sum_x q_x D(Q_{-x}|X_x=1 || (P_a)_{-x})
        <= p D(Q||P_a).                                   (11)

Each star observes essentially all the other coordinates, so dividing by its overlap multiplicity loses the apparent extra p. One cannot infer that global divergence is the sum of p nearly disjoint star costs. Equation (9) is a valid aggregate replacement, but no entropy-to-arithmetic inverse statement has been proved here.

## 5. Exact bottleneck left by these attempts

The new global PSD inequality (4), higher trace identities (1), and entropy-cover inequality (9) hold rigorously. Their missing implication is not another local positivity check. One would need an arithmetic extraction theorem using the explicitly labeled endpoint kernel, for example:

    If A is cyclic 4-AP-free, a >= epsilon/log p, and
    J(y,z)=B((2y+z)/3)B((y+2z)/3) for y!=z,
    then for some d with 4^d(d log p)=o(a^2p),
    sup_{rank(F)<=d} Var(E(B|F)) >= a^2/(log(2/a))^C,

with fixed C and a parameter range that fits the parent iteration ledger. This is CONJECTURED, not proved; the exact sufficient complexity must come from the parent's quantitative closure, not be inferred from (5).

The permutation proposition proves that this statement cannot follow from unlabeled eigenvalues, trace powers, PSD completion data, and independence of the distinguished vertex set alone. The entropy calculation also requires a new arithmetic localization step. No complete closure is claimed in this document.

## 6. Verification and classification

Run `python3 verify_route_incidence_moments_20261002.py`; saved output is `route_incidence_moments_verification_20261002.json`. The checks use exact integers and rational arithmetic on all nonempty subsets for p=5,7,11. They verify both trace formulas for all those subsets and the projected incidence Gram/Schur identity for all AP-free subsets. Finite checks support the algebra; they are not the proof of the asymptotic permutation proposition or the entropy theorem, whose proofs appear above.

- Trace identities (1): PROVED.
- Global Schur identity and inequality (3)-(4): PROVED.
- Uniform low factor energy after vertex permutation (5)-(8): PROVED.
- Aggregate entropy deficit (9), chain accounting (10)-(11): PROVED.
- Character extraction from higher traces without arithmetic labels: REFUTED as an implication from unlabeled data alone.
- Arithmetic extraction from the actual endpoint kernel: CONJECTURED.
- Local r4 target: unresolved.
