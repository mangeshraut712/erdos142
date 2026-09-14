# Endpoint incidence: entropy and overlap audit

14 September 2026. Offline. **(E) OPEN — SINGLE FINAL OBSTRUCTION.**

The target r_4(N)=o(N/log N) is neither proved nor disproved here.
The calculations below are auxiliary deductions, with no novelty claim.
No new ambient counterexample is offered. In particular, the earlier
AP-richness construction does not satisfy the full cutoff and does not
refute the remaining lemma.

## 1. Conventions and the cutoff

Let p>3 be prime, A subset Omega subset Z_p, n=|Omega|, a=|A|/n>0.
Retain the checkpoint definition of a rank-r controlled window: intersect
inverse images of consecutive integer lift intervals of diameter <p/3.
Assume

    n >= max(256 r 3^r, 8 3^r a^(-3)).

For fixed x in Omega define

    H_x={h!=0: x+h,x+2h,x+3h are in Omega}, m_x=|H_x|.

The incidence count in the request counts both orientations: its d_A(x)
is exactly 2m_x. A progression with x as its last endpoint corresponds
bijectively to one starting at x by reversing h. Each geometric progression
through x as an endpoint is counted once by H_x.

The checkpoint residue-class argument gives m_x >=4a^(-2)-1 for at
least half of A, hence the stronger convention-adjusted statement
d_A(x)>=8a^(-2)-2. This does not require all endpoints to be in A.
Indeed, a label class of size s supplies s-1 distinct opposite endpoints,
and therefore s-1 distinct members of H_x. Classes of size below
an/(2*3^r) contain fewer than |A|/2 points altogether.

## 2. A growing star has bounded vertex degree

For h in H_x put e_h={x+h,x+2h,x+3h}. These are three distinct points,
none equal to x. The edges e_h are distinct: their element sum is
3x+6h, and 6 is invertible modulo p. Each y!=x belongs to at most
three edges, because y=x+jh uniquely determines h for each j=1,2,3.
Consequently each edge meets at most six other edges. Greedily choosing
an edge and removing it and its neighbors constructs a disjoint matching
of size at least ceil(m_x/7).

Now introduce a LOCAL AUXILIARY probability law: independent Bernoulli(a)
variables on Omega minus {x}. Let E_x mean that no edge e_h is fully
occupied. Write P for this product law and Q=P(.|E_x). For 0<a<1,

    (1-a^3)^m_x <= P(E_x) <= (1-a^3)^ceil(m_x/7).             (1)

For the upper bound, E_x implies avoidance on the disjoint matching,
where the events are independent. For the lower bound, the individual
avoidance events are decreasing and positively correlated under a
product law. Here is a direct justification of the latter fact.
For two decreasing functions, induct on the number of coordinates.
Condition on the final coordinate. The conditional covariance is
nonnegative by induction; the covariance of the two conditional means
is nonnegative since both means decrease with that coordinate. The
total covariance identity proves the assertion. Apply it successively
to the indicators of avoidance and of their intersections.

The relative entropy, using natural logarithms, is exactly

    D(Q||P)=-log P(E_x),

because Q/P is the constant 1/P(E_x) on E_x. Hence for 0<a<=1/2,

    m_x a^3/7 <= D(Q||P) <= (8/7)m_x a^3.                  (2)

The inequalities follow from t<=-log(1-t)<=t/(1-t), with t=a^3<=1/8.
When m_x=0 all quantities vanish. The law at a=0 also has zero cost;
a=1 with m_x>0 has P(E_x)=0 and cannot be conditioned this way.

At the lower-cutoff scale m_x=O(a^(-2)), (2) has size O(a), not an
absolute positive entropy cost. **The cutoff supplies a lower bound
on m_x, not an upper bound.** Thus this statement does not assert small
entropy for every eligible window. For much larger stars, (2) permits
large entropy. Neither case converts entropy into a character factor.

Q is not an actual deterministic AP-free set of fixed density a, its
marginals need not remain a, and the laws for different x are not shown
to be compatible. This calculation is not a counterexample to the
requested energy lemma. It identifies what a single-star entropy
argument proves and what it does not prove.

## 3. Exact overlap of middle-pair columns

Use raw counting matrices in this section, with no 1/p normalization.
Make a column for each ordered pair (u,v), u!=v, whose completion

    (2u-v, u, v, 2v-u)

lies in Omega. Let R have rows indexed by Omega, and put ones at the
two endpoints of this column. A middle pair has exactly two endpoints;
it cannot have an arbitrarily large endpoint codegree.

Let J(y,z), for y!=z in Omega, be the indicator that both
(2y+z)/3 and (y+2z)/3 lie in Omega, and set J(y,y)=0. Then

    RR^T = diag(2m_y) + 2J.                                (3)

The diagonal counts the two ordered columns for each geometric
progression at y. For distinct endpoints, the middle points are unique;
the two orientations give exactly two columns.

Next keep only columns with B(u)B(v)=1, obtaining R_B. Define

    t_y=#{h!=0: x=y, x,x+h,x+2h,x+3h in Omega,
                    B(x+h)B(x+2h)=1},
    J_B(y,z)=B((2y+z)/3)B((y+2z)/3), y!=z,
    J_B(y,y)=0.

Since B vanishes off Omega, this gives

    R_B R_B^T = diag(2t_y) + 2J_B.                          (4)

If A is 4-AP-free, the off-diagonal A-by-A block J_B vanishes.
Equivalently each retained column has at most one endpoint in A.
The bound m_y >=4a^(-2)-1 does not itself give a lower bound on t_y:
that would require information on occupation of the middle pair.

Thus a large singular value of R can come from its ambient diagonal.
To use R_B instead requires control of occupied middle pairs and of the
arithmetic structure of its singular vectors. Formula (4) returns the
checkpoint endpoint kernel, together with an explicit degree diagonal;
it is not a proved new arithmetic inverse theorem.

## 4. Adversarial scope ledger

These checks are against the scope of the deductions, not claims that
the proposed global energy lemma has passed all adversarial tests.

| Checkpoint example | Consequence for this attempt |
|---|---|
| UNIFORM_ENERGY_COUNTEREXAMPLE | Fails full cutoff; no refutation of the remaining lemma. |
| AP_RICHNESS_COUNTEREXAMPLE | AP-isolated points force 3^r comparable to n in every controlled representation; fails full cutoff. |
| Affine-spread 3-AP-free family | Still a required global test; (1)-(4) make no claim of an integer-progression increment or cyclic reembedding. |
| Z_11 wrap witness | At the recorded size/density it fails the size cutoff; no reembedding is performed here. |
| Z_101 size-28 witness | Even rank zero requires n>=8(101/28)^3>101; positive rank requires n>=768. The weighted matrix identities still apply. |
| Regular-center compatibility | A local law is not asserted to be globally consistent. Growing stars alone do not settle this issue. |
| Flat Z_13 difference-set spectrum | With a=4/13, even rank-zero cutoff exceeds 13. No conversion from arbitrary singular vectors to characters is claimed. |
| Concentrated-support examples | No improved U3 inverse exponent or general exclusion by the cutoff is claimed. |
| 8192 half-density interval example | Not 4-AP-free; cannot test the forbidden-joint implication. |
| a=epsilon/log N | O(a^(-2)) edges give O(epsilon/log N) local entropy cost; no arithmetic energy lower bound follows from (2) alone. |

No eligible deterministic counterexample to the energy lemma has been
constructed. No proof of that lemma or alternative proof of the target
has been obtained.

## 5. The one remaining closing theorem

**Unproved full-cutoff arithmetic energy theorem.** There exist absolute
constants eta>0 and C>0 such that for every prime p>3, every checkpoint
controlled window Omega of rank r and size n, and every nonempty
4-AP-free A subset Omega of density 0<a<=4/5 satisfying the full cutoff,
there is a factor obtained by quantizing at most ceil(C log(2/a))
characters into four equal half-open arcs (with allowed rotations),
restricted to Omega, such that

    Var_Omega(E(1_A | F)) >= eta a^2.

This is one sufficient theorem, not a result established by this audit.
The energy-to-cell and terminal implications are already recorded in
LOCALIZATION_BRIDGE.md. With this theorem they give multiplicative
density growth, O(log(1/a_0)) steps, and O(log(1/a_0)^2) cumulative
rank and logarithmic size loss. Those are CONDITIONAL consequences.
No unconditional iteration is available from (1)-(4).

## 6. Reproduction and next research prompt

Run `python3 verify_endpoint_incidence.py`. It checks the orientation,
bounded-degree and matching assertions, exact product-law probabilities,
and both Gram matrix formulas on small cyclic examples. These are finite
diagnostics supporting the derivations above, not a test of the closing
theorem or a full-cutoff asymptotic construction.

Next prompt:

> Work offline from ENDPOINT_INCIDENCE_AUDIT.md and the accepted checkpoints.
> Address the single full-cutoff arithmetic energy theorem in section 5.
> Single-star degree is at most three and its exclusion entropy is between
> m a^3/7 and 8m a^3/7 for a<=1/2. Middle-pair overlap has the exact weighted
> Gram formula (4). Exploit consistency between different occupied endpoint
> stars to control occupation of their middle pairs and produce the stated
> logarithmic-rank factor. A large ambient degree or an arbitrary singular
> vector is not that conclusion. Alternatively construct a deterministic
> family violating the energy conclusion while satisfying the entire
> cutoff. If the energy theorem is proved, execute the checkpoint iteration
> through density 4/5 and verify every cutoff before claiming the target.
