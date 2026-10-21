# Full-group energy at the target density: exact identities and budgets

14 September 2026. Offline. **(E) OPEN — ONE EXACT OBSTRUCTION.**

No proof or counterexample to the target-scale AP-free energy theorem is
obtained here. No new bound for r_4(N) is claimed. The auxiliary deductions
below address the requested Fourier expansion, conditional increments,
quadratic example, and weaker iteration budgets. Novelty is not claimed.
All logarithms are natural unless a base is specified.

## 1. What small factor energy actually says

Write B=1_A, a=E B, f=B-a on Z_p, with normalized averages and Fourier
transform fhat(t)=E_x f(x)e_p(-tx). Let F be a partition into joint
quarter-arc character cells. If ||E(f|F)||_2^2<eta a^2, then for every
real F-measurable h,

    |E_A h-E h| <=sqrt(eta)*sqrt(Var(h)).                    (1)

Indeed E_A h-E h=<E(f|F),h-Eh>/a; apply Cauchy-Schwarz.
For an F-measurable set U of mass q this gives discrepancy at most
sqrt(eta q(1-q)). The total variation distance between the two cell-label
distributions is at most sqrt(eta)/2, by the exact chi-squared identity
in FULL_GROUP_HOSTILE_AUDIT_20260914.md.

These are absolute discrepancy bounds. They do not give small relative
error on arbitrarily small cells: the relative bound is
sqrt(eta(1-q)/q).

For arbitrary circular intervals in d character coordinates, choose an
integer t>=1 and refine each coordinate by frequencies xi,4xi,...,4^(t-1)xi.
This uses at most dt characters and gives the base-four grid of mesh 4^-t.
Inner and outer unions of grid cells bracket the desired torus box, with
uniform mass difference at most 2d(4^-t+1/p). If dt is within the assumed
rank limit, applying (1) to the brackets gives absolute discrepancy at most

    sqrt(eta)/2 + 2d(4^-t+1/p).                              (2)

Fine resolution costs additional rank. It is not available for free.

## 2. Exact Fourier expansion of the four-term count

For p>3,

    Lambda_4(B)=sum_{u,v} Bhat(u+2v) Bhat(-2u-3v) Bhat(u) Bhat(v).
                                                                  (3)

This follows by imposing sum_i xi_i=0 and sum_i i xi_i=0 in the
Fourier expansion and setting xi_2=u, xi_3=v. Put

    T=sum_{t!=0} fhat(t)^2 fhat(-2t),
    S=sum_{t!=0} fhat(t) fhat(2t) fhat(-3t),
    Q=sum_{u,v} fhat(u+2v) fhat(-2u-3v) fhat(u) fhat(v).

The four lines on which one of these arguments is zero meet only at
(0,0). Their contributions are two copies of aT and two copies of aS.
Therefore, exactly,

    Lambda_4(B)=a^4+2aT+2aS+Q.                              (4)

For a 4-AP-free set the diagonal gives Lambda_4(B)=a/p, so

    Q+2a(T+S)=a/p-a^4.                                    (5)

At a=epsilon/log p the right side is -(1-o(1))a^4. We have not proved
that (1) prevents this cancellation. It would be incorrect to infer that
from U2-uniformity or to reverse the checkpoint Fourier upper bound.

Booleanity gives the exact extra constraints

    sum_t fhat(t)fhat(xi-t)
      =(1-2a)fhat(xi)+a(1-a)1_{xi=0}.                      (6)

This is the transform of f^2=(1-2a)f+a(1-a). It is an unweighted
convolution constraint; (3) has two additional frequency-dependent factors.
No estimate converting (6) into a bound strong enough for (5) is proved.

## 3. Exact conditional energy increment

Let g=E(B|F), u=B-g. Refine F by quarter cells I_0,...,I_3 for a new
character and rotation. If V runs over F and W=V intersect I_j, then

    Delta=||E(B|F join P)||_2^2-||g||_2^2
         =sum_{V,j:mu(W)>0} |E u1_W|^2/mu(W).              (7)

The identity follows from orthogonality of the old conditional expectation
and the new residual projection. It is exact for empty and tiny cells.
For each j, Cauchy-Schwarz over V shows

    Delta >=sum_j |E u1_{I_j}|^2/mu(I_j)
           =||E(u|P)||_2^2.

The checkpoint rotation argument applies to the real mean-zero function u,
giving a rotation with

    Delta >=(4/pi^2)|uhat(xi)|^2.                          (8)

Thus if every candidate quarter refinement has gain at most kappa, then

    max_{xi!=0}|uhat(xi)| <=(pi/2)sqrt(kappa),
    ||u||_U2^4 <=(pi^2/4) kappa a.                        (9)

The last step uses Parseval and ||u||_2^2<=a. This is a U2 estimate,
not a U3 or 4-AP counting estimate.

Conditional Booleanity is also exact:

    u^2=(1-2g)u+g(1-g),
    E(u^2|F)=g(1-g).                                      (10)

A hypothetical gain c a^2/log(2/a) would reach eta a^2 in order
log(2/a) refinements. It would NOT exceed the total variance, which is
of order a. Reaching the structural energy threshold is the appropriate
stopping condition. No AP-free implication producing that gain is proved.

## 4. The correct generic dissociated-spectrum estimate

A set D of nonzero frequencies is dissociated when no nonzero choice of
coefficients in {-1,0,1} sums to zero. Its subset sums are distinct, so

    |D|<=log_2 p.                                         (11)

The assertion 3^|D|<=p does not follow: differences of two signed sums
have coefficients in {-2,-1,0,1,2}.

For 0<tau<=a, a dissociated subset D of Spec_tau(f) satisfies

    |D| <=4(a/tau)^2 log(1/a).                            (12)

Here is a self-contained proof. Choose phases phi_xi so that
E_A cos(2pi xi x/p+phi_xi)>=tau/a. For 0<t<=1/2 put
P(x)=product_{xi in D}(1+t cos(2pi xi x/p+phi_xi)).
Dissociation and Fourier expansion give E P=1. Positivity and Jensen give
E_A log P<=log E_A P<=log(1/a). Since log(1+z)>=z-z^2 for |z|<=1/2,

    log(1/a)>=|D|(t tau/a-t^2).

Take t=tau/(2a). This proves (12). A maximal dissociated subset spans
Spec_tau(f) with coefficients {-1,0,1}, since adjoining any other element
would create such a relation involving that element.

At tau=a^2 the generic bound is 4a^-2 log(1/a), far above the desired
polylogarithmic rank. At tau comparable to a it gives logarithmic rank,
but AP-freeness has not been shown to force coefficients of that size.
For M individual frequencies with total squared mass W, (8) at least
gives energy >=4W/(pi^2 M) from one of them. Replacing M by dissociated
dimension without controlling its whole span would not be justified.

## 5. The quadratic example has many progressions, not merely one

Let L=floor(p/log p), b=L/p, I={0,...,L-1}, and B(x)=1_I(x^2).
The checkpoint Gauss estimate gives |a-b|<=(1+log p)/sqrt(p), where a=E B.
Expanding the four interval indicators in Fourier gives quadratic forms

    sum_{j=0}^3 k_j (x+jh)^2.

Their 2-by-2 symmetric matrix is zero exactly when
sum k_j=sum j k_j=sum j^2 k_j=0, equivalently

    (k_0,k_1,k_2,k_3)=t(-1,3,-3,1).

For a symmetric matrix M over Z_p, direct squaring of the normalized
quadratic sum gives

    |E_z e_p(z^T M z)|^2=p^(-rank M).

To check this, write the difference of two arguments as h. Averaging
the remaining argument vanishes unless Mh=0; for such h, h^T M h=0.
There are p^(2-rank M) kernel vectors. Every nonzero matrix therefore
contributes at most p^-1/2 in magnitude.

The zero-matrix terms, in contrast, sum to the NONNEGATIVE quantity

    Z_I=sum_t |Ihat(t)|^2 |Ihat(3t)|^2.

Using sum_k |Ihat(k)|<=1+log p, valid here once L/p<=1/2, gives

    |Lambda_4(B)-Z_I| <=(1+log p)^4/sqrt(p).                (13)

For each integer 0<=t<=floor(1/(12b)), the interval formula gives
|Ihat(t)|,|Ihat(3t)|>=2b/pi. These indices are distinct modulo p,
and there are at least 1/(12b) of them. Hence

    Z_I >=4b^3/(3pi^4).                                   (14)

Consequently, for all sufficiently large primes,

    Lambda_4(B) >=a^3/(12pi^4),
    Lambda_4(B)-a/p >=a^3/(24pi^4).                        (15)

An explicit sufficient threshold is p>=exp(200). Indeed b>=1/(2log p),
and sqrt(p)>=12pi^4(1+log p)^7 ensures that the error in (13) is at most
half the bound (14) and that b/2<=a<=2b. This inequality holds for log p>=200:
the ratio exp(v/2)/(1+v)^7 increases there, and at v=200 it follows already
from exp(100)>2^100, pi^4<100, and 201<256. The same threshold gives
p a^2>=24pi^4, allowing subtraction of the diagonal in (15).

Thus this linearly invisible Boolean example has progression density of
order at least a^3, exceeding a^4 by a factor of order 1/a. Its quadratic
resonance has a positive sign because the four Fourier factors pair into
absolute squares. We have NOT shown that every Boolean set with low linear
factor energy has this positivity. This family is not AP-free and is not
a counterexample to the proposed AP-free theorem.

## 6. Which weaker structural bounds would actually fit iteration?

This is conditional bookkeeping for a hypothetical HEREDITARY input.
It does not establish or attempt a general-window extension.

Suppose at density a<=4/5 a factor adds at most R(a) characters and has
energy at least kappa(a)a^2, where 0<kappa(a)<=1. The accepted cell lemma
gives a successor with

    a' >=a(1+kappa(a)/2),
    retained A fraction >=kappa(a)a/(2*4^R(a)).             (16)

Let a_0 be the initial density, L_0=log(2/a_0). Suppose throughout that
kappa(a)>=kappa_0 and R(a)<=R_0. Since log(1+kappa_0/2)>=kappa_0/4,
one may take the following explicit upper bounds through density 4/5:

    J_*=ceil(4L_0/kappa_0)+1,
    D_*=d_0+J_* R_0,
    S_*=L_0+J_*[log(2/kappa_0)+L_0+R_0 log 4].             (17)

Here D_* bounds rank and S_* bounds log(n_0/n_j). The last estimate uses
the exact telescope log(n_0/n_j)=log(a_j/a_0)+sum log(1/retained_i).
No number of refinements of order a/DeltaE is required if the assumed
structural input already supplies a completed factor.

The checkpoint terminal lemma succeeds whenever, with n_0 comparable to p,

    log(p-1)/D_* - S_* - log(2D_*) -> +infinity,             (18)

and the full size cutoff persists. A convenient sufficient condition is

    D_*[S_*+log(2D_*)+1]=o(log p).                         (19)

It implies both S_*=o(log p) and D_*=o(log p); at a_0=epsilon/log N,
the cutoff logarithm O(D_*+log D_*+log(1/a_0)) is therefore negligible
relative to log n_j=log n_0-O(S_*). For the terminal bound use
R_terminal>= (p-1)^(1/d_j)/2 in the checkpoint, which gives (18).

For fixed nonnegative C,D and positive constants K,c, take

    R(a)<=K log^C(2/a),
    kappa(a)>=c/log^D(2/a),

with c reduced if necessary so kappa<=1. Then

    J_*=O(L_0^(D+1)),
    D_*=O(L_0^(C+D+1)),
    S_*=O(L_0^(D+1+max(C,1))).                             (20)

All fixed C,D satisfy (19), since L_0=O(log log N). Thus such a weaker
energy theorem WOULD suffice if hereditary, with the necessary density
quantifiers. In particular rank K L^2 and energy c a^2/L fit comfortably:
J_*=O(L_0^2), D_*=O(L_0^4), S_*=O(L_0^4).

For R(a)<=K a^-delta L^C and kappa(a)>=c a^delta'/L^D, with all exponents
nonnegative, the same ledger gives a sufficient power region

    delta+delta' < 1/2.                                   (21)

Indeed D_*,S_* are bounded by a_0^(-(delta+delta')) times fixed powers
of L_0. At a_0=epsilon/log N their product is o(log N) under (21).
The boundary and larger exponents are not guaranteed by these bounds.
This is a sufficient region for this ledger, not a proof that no improved
iteration or stronger cell-selection estimate can do better. Equation
(18), rather than the coarse exponent test, is the more precise criterion.

## 7. Density quantifiers and the remaining obstruction

A hypothesis stated only for a>=c_0/log p with ONE fixed c_0>0 does not
by itself cover every initial epsilon/log N needed for a little-o result.
For this pipeline the appropriate coverage is every fixed epsilon>0,
allowing the structural constants and starting threshold to depend on it.
In a hypothetical later hereditary version, coverage down to
epsilon/(2log n) would persist: (19) gives log n>=log n_0/2 while
a_j>=epsilon/log n_0. This is a conditional coverage check, not an extension.

No eligible target-density counterexample was constructed. The available
no-wrap sphere hosts satisfy the energy conclusion and lie below this
density scale; their thinnings cannot increase density. Affine maps retain
supremal energy. A union of individually AP-free blocks can have cross-block
APs, and random projection needs an additional global relation estimate.
No construction with verified density, AP-freeness, and simultaneous
factor discrepancy was obtained by those methods. Their failure is not
a proof that such a family is impossible.

The next precise FULL-GROUP obstruction, weaker than constant ENERGY, is:

For every epsilon>0, do there exist c_epsilon,K_epsilon>0 and p_epsilon
such that every prime p>=p_epsilon and every nonempty 4-AP-free A subset
Z_p with epsilon/log p<=a<=4/5 admits a rotated-quarter factor with

    rank <=ceil(K_epsilon log^2(2/a)),
    Var(E(B|F)) >=c_epsilon a^2/log(2/a)?                  (OPEN)

This one statement remains unproved and unrefuted. Proving its full-group
form would still require a hereditary extension before the conditional
budget above could yield the target. No actual iteration has been run on
an unproved structural input.

## 8. Checks and continuation

Run `python3 verify_target_scale_20260914.py`. Exact rational checks test
conditional energy increments and conditional Booleanity. Fourier/Gauss
comparisons use floating point and explicitly labelled tolerances. These
support the algebra; they do not verify (OPEN) or the asymptotic target.

Next prompt:

> Work offline at a>=epsilon/log p, for every fixed epsilon>0. Address (OPEN)
> in TARGET_SCALE_ENERGY_BUDGET_20260914.md: quarter-factor rank at most
> K_epsilon log^2(2/a), energy at least c_epsilon a^2/log(2/a).
> The exact residual refinement gain is (7), with a one-character lower
> bound (8); small gains currently give only U2 control (9). The exact
> 4-AP cancellation is (5), and Boolean convolution is (6). Find an AP-free
> mechanism preventing that cancellation under low factor energy, or an
> actual target-density counterexample. The quadratic interval example
> has a positive resonance and at least a^3/(24pi^4) nontrivial progression
> density; it is not an AP-free example. Generic dissociated-spectrum
> dimension is bounded by min(log_2 p,4(a/tau)^2 log(1/a)), not log_3 p.
> Polylogarithmic rank and inverse-polylogarithmic relative energy fit the
> conditional iteration budget, but no hereditary extension is yet proved.
> Resolve the full-group statement before attempting that extension.
