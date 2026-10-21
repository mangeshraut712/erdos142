# A sparse-defect degree-four Boolean moment certificate

2 October 2026. Offline. Root proposed the construction; this independent audit verifies it, improves its universal pair-degree constant from 12 to 6, and records its exact-cardinality limitation. No actual AP-free probability law or deterministic set is constructed. SELECT and the r4 target remain unresolved.

## 1. Precisely defined relaxation

Let Ω⊂Z_p, p>3 prime, n=|Ω|. Let E be the collection of DISTINCT four-point subsets of Ω that are nonzero cyclic four-term progressions. Work in the Boolean quotient X_i²=X_i, indexed by i∈Ω. For square-free monomials X_S with |S|≤4 define the linear functional

    L(X_S)=a^|S|, except L(X_S)=0 when S∈E.                (Q1)

Here 0<a<1 is an intended mean density, not a fixed realized cardinality. The empty moment is 1. This gives every true quartic AP monomial expectation exactly zero, and includes all Boolean quotient identities of total degree≤4.

Positive semidefiniteness means

    L(P conjugate(P))>=0 for every polynomial P of degree≤2. (Q2)

It does not assert existence of a full representing probability law. It does not include exact cardinality sum_i X_i=na as a quotient equation.

## 2. Complete centered Gram calculation

Put b=a(1-a), C_i=X_i-a, C_ij=C_iC_j for distinct unordered pairs {i,j}. Use the centered basis

    1, (C_i)_i, (C_ij)_(i<j).

Its moment Gram matrix is exactly block diagonal:

    [1] ⊕ b I_n ⊕ [b² I - a⁴ T],                       (Q3)

where T is the adjacency matrix on unordered pairs:

    T_(ij),(kl)=1 if {i,j}∩{k,l}=∅
                    and {i,j,k,l}∈E; otherwise0.

Proof. Q1 agrees with independent Bernoulli(a) moments up to degree3. Under that independent law the displayed centered basis is orthogonal, with respective squared norms1,b,b². In a product of two basis elements, the only possible defect from Q1 is the coefficient of a four-distinct-variable monomial. That occurs only for two disjoint pair basis elements; its coefficient is1, and its independent moment a⁴ is replaced by0 precisely when their union is an AP edge. All diagonal, repeated-variable, constant and linear-pair entries therefore remain as stated. This is the full calculation, not a principal-minor test.

The transformation from square-free monomials of degree≤2 to this centered basis is triangular with unit diagonal and hence invertible. PSD of Q3 is equivalent to Q2 in the original basis.

## 3. Pair degree is at most SIX

Fix an unordered pair {i,j}. An AP edge containing it has a representation i=x+rd,j=x+sd with r,s distinct slots in {0,1,2,3}. There are twelve ordered slot choices. For each choice the difference d=(j-i)/(s-r) and starting point x=i-rd are uniquely determined since p>3.

Reversal sends (x,d,r,s) to (x+3d,-d,3-r,3-s). It preserves the underlying four-point edge, acts freely on the twelve representations, and has orbits of size2. Thus at most SIX distinct AP edges can contain {i,j}. Every edge containing it determines exactly one complementary pair neighbor in T. Therefore

    maximum degree(T) <=6.                               (Q4)

This applies on arbitrary Ω, including the precise H-window class. It improves the safe but unoptimized twelve-representation bound.

For every complex vector v, symmetry and 2|v_i v_j|≤|v_i|²+|v_j|² give

    v*Tv <=6||v||².

Hence the pair block is PSD whenever

    b²>=6a⁴,
    equivalently a<=1/(1+sqrt6).                          (Q5)

Equations Q3–Q5 prove that Q1 is a PSD degree-four Boolean moment functional in that entire density range. The target density ε/log p lies in the range for sufficiently large p.

The universal constant6 cannot be improved for this construction: in full Z_7 the pair graph is regular of degree6. This finite assertion is checked exactly by enumerating all AP edges, and can also be checked from the six completions of one pair and affine transitivity on pairs. The all-ones pair vector is then an eigenvector of T with eigenvalue6. For a>1/(1+sqrt6), the pair Gram has a negative quadratic form on that vector; at a=1/3 its Rayleigh coefficient is -2/81. This demonstrates sharpness of Q5 as a UNIVERSAL sufficient threshold for the specific construction, not necessity in every Ω.

## 4. Relative Fourier second moments are small

The raw centered variables C_i have L(C_i)=0 and L(C_iC_j)=0 for i!=j, with L(C_i²)=b. Therefore

    L(|n^-1 sum_i C_i e_p(-ξi)|²)=b/n                     (Q6)

for every frequency, including zero. This is a small second-moment Fourier objective, but its zero-frequency is not zero as a polynomial: the construction's realized density is not fixed.

To impose residual spatial mean-zero algebraically, define instead

    barX=n^-1 sum_i X_i,
    u_i=X_i-barX.

Then sum_i u_i=0 as an exact polynomial identity. For trivial F, its conditional mean is the scalar barX, which has zero spatial factor variance relative to barX on every Boolean assignment. The corrected relative Fourier moment is

    L(|n^-1 sum_i u_i e_p(-ξi)|²)
       =(b/n)[1-|E_Ωe_p(ξi)|²] <=b/n.                   (Q7)

This follows by projecting the character vector off the constant vector in the covariance bI_n. No orthogonality of characters inside Ω is assumed.

At intended a≈ε/log p and n≥p exp(-sqrt(log p)), both Q6 and Q7 are

    o(a^(5/2)log(2/a)),                                  (Q8)

because their threshold ratio is bounded by a constant times

    exp(sqrt(log p))(log p)^(3/2)/(p log log p) ->0.

These are feasible moment-level Fourier bounds, not uniform pointwise bounds for one actual set. No interchange of max_ξ with expectation is used.

## 5. Exact-cardinality limitation: an indispensable qualification

For Q1,

    L((sum_i X_i-na)²)=n b>0,
    L((barX-a)²)=b/n.                                   (Q9)

Consequently the construction does NOT satisfy the exact cardinality quotient equation. If one insists on trivial-factor residual u_i=X_i-a, it also fails the exact residual spatial mean-zero equation, despite having zero first moment. The repair u_i=X_i-barX in Q7 makes mean-zero exact but leaves barX random: intended a is not the fixed deterministic density required by SELECT.

Thus this construction establishes:

    Boolean degree-four PSD + exact quartic AP moments0
       + intended density + small Fourier-square moments

are jointly feasible at the target scale, in the relaxation defined above.

It does NOT establish feasibility of failure of SELECT with ALL its exact constraints. In particular exact cardinality, fixed nonlinear density thresholds, and representation by one deterministic Boolean set are absent. A cardinality-preserving repair would be an additional theorem, not a consequence of Q1.

Even existence of a full representing law is not asserted. For a genuine law, zero nonnegative AP monomial expectations would imply AP-freeness almost surely. The truncated PSD functional alone does not yield that law. Nor is an adaptive maximum Fourier coefficient controlled by the maximum of these separate Fourier-square moments.

## 6. Independent verification

Run `python3 verify_select_quartic_relaxation_20261002.py`. Its JSON output is `select_quartic_relaxation_verification_20261002.json`.

The checker expands every centered basis product in the Boolean quotient, reconstructs the Gram entries directly from Q1, checks every entry against Q3, verifies pair degree≤6, and checks the exact density-variance qualification Q9. It uses fractions for all moments. It covers full groups Z_5,Z_7,Z_11 and proper interval windows in Z_13,Z_19, at a=1/20,1/10,1/5,2/7. All four densities satisfy Q5. It also verifies the negative full-Z_7 direction at a=1/3.

The proof of PSD is the symbolic block calculation and maximum-degree inequality above; finite checks do not substitute for it. No new package was used or installed.

Classification: Q1–Q9 and the sufficiency/sharpness assertions are PROVED; finite execution is COMPUTATIONALLY CHECKED ONLY; an exact-cardinality or deterministic SELECT counterexample remains unproved.
