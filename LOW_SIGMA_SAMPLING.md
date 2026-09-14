# Low-Sigma continuation: density-weighted sampling and its exact limit

Date: 2026-09-07. Offline. All averages are normalized on Z_p, p odd.

STATUS: OPEN

This is a proved auxiliary analysis of one sampling mechanism. It is not
a density increment, no asymptotic bound follows, and novelty is not claimed.
The existing U3 and relative-window lemmas are accepted as infrastructure.

## 1. A density-weighted approximation — PROVED

Let B=1_A, alpha=E B>0, f=B-alpha, and

    G(x)=E_y B(y)B(2x-y).

Then E G=alpha^2 and Lambda_3(B)=E B G. Assume the low-cubic condition
Lambda_3(B)<=alpha^3. Introduce the probability measure whose density
relative to normalized counting is

    nu(x)=(B(x)+alpha)/(2alpha).

In particular E nu=1, nu>=1/2, and |f(x)|<=2alpha nu(x).
Choose independent Y_1,...,Y_k uniformly from A and put

    H(x)=(alpha/k) sum_{i=1}^k B(2x-Y_i).

For every x, E_Y H(x)=G(x). Since each summand is an indicator,

    Var_Y H(x)=[alpha G(x)-G(x)^2]/k.

Moreover

    E_x nu(x)G(x)
      =[Lambda_3(B)+alpha^3]/(2alpha)<=alpha^2.

Consequently

    E_Y ||H-G||_{L2(nu)}^2
      =[alpha E_nu G-E_nu G^2]/k <= alpha^3/k.               (1)

This proves that some sample satisfies ||H-G||_{L2(nu)}<=sqrt(alpha^3/k).
For every sample, the weighted Cauchy inequality gives

    |<f,H-G>|<=2alpha E_nu |H-G|
              <=2alpha ||H-G||_{L2(nu)}.

Hence some sample has correlation error at most

    2 alpha^(5/2)/sqrt(k).                                  (2)

If T=<f,G><=-c alpha^3 with 0<c<=1, choosing
k>=16/(c^2 alpha) makes that error at most c alpha^3/2.
Thus <f,H><=-c alpha^3/2. If a proportion of good tuples is needed,
Markov's inequality applied to (1) shows that at least 3/4 of tuples have
squared error at most 4alpha^3/k. Choosing k>=64/(c^2 alpha) then gives
the same correlation conclusion on at least 3/4 of tuples.

The usual unweighted L2 estimate followed by ||f||2<=sqrt(alpha) only
guarantees an error of order alpha^2/sqrt(k), requiring k of order
alpha^-2 for this precision. The weighted calculation improves that
sufficient sample count to alpha^-1. This comparison is of explicit
guarantees, not a claim of a new optimal inverse theorem.

The norm is density-dependent and is NOT translation invariant. Moving
H or G changes the effective weight from nu to a translate of nu. Window
regularity does not make 1_A translation invariant. Thus (1) is not an
almost-periodicity theorem and cannot be used as one without proving a
separate shift-control assertion.

## 2. A matching support obstruction — PROVED

Suppose in addition that 0<=G<=K alpha^2 for a fixed K>=1. Any H of the
displayed sample form is supported on a union of k sets (A+Y_i)/2,
of total normalized measure at most k alpha. In fact the following
argument applies to any H supported on such a union, regardless of its
coefficients or whether its samples were independent.

Outside this support H=0. Therefore

    ||G-H||_L1 >= E_{outside supp H} G
       >=alpha^2-K alpha^2 k alpha.

Since nu>=1/2,

    ||G-H||_{L1(nu)} >= (alpha^2/2)(1-K k alpha).             (3)

To obtain ||G-H||_{L2(nu)}<=c alpha^2/4, which is the precision used
above to guarantee correlation error <=c alpha^3/2, L1<=L2 and (3)
necessarily give

    k >= (1-c/2)/(K alpha) >= 1/(2K alpha).                 (4)

Thus reducing the number of positive-translate samples to o(alpha^-1)
cannot achieve this approximation precision in the spread-convolution
case. This is a theorem about this representation and norm, not about
every possible proof of the cubic branch or every scalar approximation.
Indeed, a scalar correlation alone can be witnessed by a single sample;
the obstacle concerns approximating the function in the required norm.

If clipping H at K alpha^2 is used while G<=K alpha^2, the L2 error cannot
increase, by the pointwise Lipschitz property of min(t,K alpha^2) on
nonnegative numbers. The support obstruction still applies.

## 2A. The exact soft increment and an arbitrary level-set increment — PROVED

Assume K>1, G<=K alpha^2, and T=<f,G><=-c alpha^3 with 0<c<=1.
Define u=1-G/(K alpha^2). Then 0<=u<=1 and

    E u=(K-1)/K,
    E B u>=alpha(K-1+c)/K.

The second identity follows from E BG=alpha^3+T<=(1-c)alpha^3.
Thus the density of A under the soft probability weight u is at least

    alpha[1+c/(K-1)].                                       (5)

There is also an actual level set E_t={x:u(x)>=t} satisfying

    density_E_t(A)>=alpha[1+c/(2(K-1))],
    |A intersect E_t|/|A|>=c/(2K).                          (6)

Proof: by layer cake, integral_0^1 |E_t|/p dt=E u and the corresponding
integral of |A intersect E_t|/p is E B u. Call a level good when its
density is at least the first quantity in (6). The total A-mass integral
over good levels is at least

    E B u-alpha[1+c/(2(K-1))]E u >= c alpha/(2K).

Since the parameter interval has length one, some good level has at least
this much normalized A-mass, proving (6).

This has attractive scalar economics: the density grows by a fixed
multiplicative factor and a fixed fraction of A is retained. The domain
E_t is, however, the sublevel set

    {x:G(x)<=K alpha^2(1-t)}.

It is an A-dependent convolution level set. It is not proved to be a
long progression, a bounded-rank Bohr set, or a controlled relative
window. Iterating relative density on arbitrary subsets gives no terminal
contradiction: the process may end with the ambient set equal to A.
Therefore (5)-(6) do not close the local target.

## 3. What the sample count does and does not buy

H is a sum of translates of the unknown set A. These supports are not
automatically intervals, controlled Bohr windows, or quadratic cells.
No rank, radius, or length guarantee has been obtained from (1).

If a proposed localization construction pays the ambient tuple density
alpha^k, its logarithmic loss is k log(1/alpha). Equation (4) makes this
at least a constant times alpha^-1 log(1/alpha) for that construction.
At alpha_0=epsilon/log N this exceeds a constant times

    (log N/epsilon) log(log N/epsilon),

already too large before iteration. This is a conditional accounting
statement about a method that actually pays alpha^k; it is not a lower
bound on every possible arithmetic localization of the samples.

Even if that cost were improved to a constant times k, the reciprocal
density scale alpha^-1 is the endpoint, not a little-o saving. A new
argument would still have to improve mass retention, amplify the gain,
recycle the samples across steps, or bound the total charge by a smaller
potential. None of those implications is supplied by the sampling lemma.

## 4. A linear signal alone does not guarantee near-full-mass phase refinement — PROVED

This is an explicitly outside-class model; it is not AP-free and not a
prime cyclic set. It tests only inferences from one linear coefficient.

On [0,1)^2 with uniform measure, let

    A={(t,u): 0<=u<=a+2c a^2 cos(2pi t)},

where 0<a<=min(1/4,1/(4c)) and c>0 is fixed. Then A is Boolean, has
measure a, and its balanced function has first t-Fourier coefficient
c a^2. Consider any refinement E=S times [0,1), of measure mu>0;
it can be any measurable S, not just an interval.

The mean-zero integral of the cosine gives

    density_E(A)-a
      =-(2c a^2/mu) integral_{S complement} cos(2pi t) dt
      <=2c a^2(1-mu)/mu.

If this gain is at least lambda a^2 with fixed lambda>0, then

    mu<=2c/(2c+lambda),
    retained_A_mass <=1-(1-2ca)lambda/(2c+lambda).            (7)

The mass bound follows because the excluded first-coordinate fibers
each have density at least a-2ca^2. It is bounded away from one as a
tends to zero, contradicting any exp(-K a) retention guarantee for such
refinements and fixed K. This does not rule out using other coordinates,
additional arithmetic hypotheses, or AP-freeness. It isolates the extra
content needed beyond the size of one Fourier coefficient.

## 5. Exact recurrence remains the completion test

For increments satisfying only mu_j Delta a_j>=kappa a_j^2, the sharp
scalar bound and its attaining path are in GLOBAL_COMPATIBILITY.md (11)-(13).
For native progression conversion, the checkpoint guarantee is

    log N_j >= 2^-j log N_0
      -[2log(128pi)+log(1/(c a_0))](1-2^-j).

The actual endpoint-density path a_{j+1}=a_j+k a_j^2 obeys exactly

    1/a_j-1/a_{j+1}=k/(1+k a_j).

It can take order 1/a_0 steps, while the displayed length guarantee only
supports order log log N_0 steps. The weighted sampling calculation does
not alter that recurrence until a valid arithmetic localization theorem
is proved. The local target remains OPEN.
