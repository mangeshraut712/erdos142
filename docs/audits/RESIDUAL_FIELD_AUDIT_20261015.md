# Residual-field amplification: audit and a sparse arithmetic obstruction

15 October 2026. Entirely offline. **Principal status: (D) NEW RIGOROUS
PARTIAL THEOREM.** The local target r_4(N)=o(N/log N) remains OPEN.

This note audits the pasted October 14 report against the actual source
files. It does not adopt that report's claim that every downstream theorem
has been independently verified in this run. Three legacy verifiers were
rerun in an isolated temporary directory; their finite checks passed.
The new proofs and their limitations are recorded here and in
`QUADRATIC_LOCALIZATION_20261015.md`.

## 1. Claims that survive, with their exact scope

Let Omega have density w in Z_p. On its uniform probability space let
B=1_A, g=E(B|F), u=B-g, a=E B, and c_xi=E_Omega u e_p(-xi x).
Use normalized full-group Fourier coefficients for zero-extended fields.
For an AP-free A, the actual endpoint and middle completion functions,
with d=0 subtracted, obey q_E,q_M>=0 and Bq_E=Bq_M=0.

For lambda_E,lambda_M>=0 and phi=1_Omega 1_(g>=gamma a) q_lambda,
put S=E_Omega g phi. Then

    |hat phi(xi)| <= E_p phi <= w S/(gamma a),
    sum_(xi!=0) conjugate(c_xi) hat phi(xi) = -S.          (A1)

The first assertion is the triangle inequality applied to phi>=0.
For the second, E_Omega u phi=-E_Omega g phi by Bphi=0;
Fourier inversion and E_Omega u=0 give (A1). In particular there is
no additional factor w in the second identity. Equivalently, Parseval
uses uhat=w c and E_p u phi=-w S.

If S>0 and a packet of s>=1 nonzero frequencies captures a fraction theta
of this pairing, then

    sum_Gamma |c_xi| >= theta gamma a/w,
    sum_Gamma |c_xi|^2 >= theta^2 gamma^2 a^2/(s w^2),
    max_Gamma |c_xi|^2 >= theta^2 gamma^2 a^2/(s^2 w^2).   (A2)

These follow successively from (A1), Cauchy--Schwarz, and averaging.
The exact sufficient packet bound for the SELECT threshold c a^(5/2)ell is

    s <= theta gamma/(w sqrt(c)) a^(-1/4)ell^(-1/2).       (A3)

The old proper-window exponent -1/8 was a stronger restriction than
necessary, not a counterexample to its implication. The exponent -1/4
works in both settings. A capturing packet is a hypothesis, not a proved
consequence of AP exclusion. These inequalities do not bound the old
projection denominator for an arbitrary packet or arbitrary signed lambda.
They provide a different sufficient implication for nonnegative lambda.

For phi_m=1_Omega g^m q_lambda put S_m=E_Omega g^m q_lambda.
The analogous bound is max_Gamma |c|>=theta S_(m+1)/(s w S_m),
when S_m>0. Log convexity S_(m+1)S_(m-1)>=S_m^2 follows by applying
Cauchy--Schwarz to g^((m-1)/2) and g^((m+1)/2) in the nonnegative
measure q_lambda dmu_Omega. There is no automatic lower bound a/2 for
S_2/S_1. Nor has Branch I been shown to retain a fixed fraction of its
pairing after discarding cells with g<a/2.

For conditional synthesis, psi_xi=e_xi-E(e_xi|F). It gives the exact
centered field by applying I-E(.|F) to Fourier inversion. Its Gram matrix
G_F is different from the Gram of globally mean-centered characters G_0.
On the full group G_0=I and 0<=G_F<=I, but G_F generally is not I.
The regularized refinement bound holds with either matrix: for G_F,
repeat rotation averaging after conditional centering. The diagonal
averaged squared norm is at most kappa^2 ||psi_xi||^2+1-kappa^2,
and each off-diagonal averaged covariance is kappa^2(G_F)_(xi,eta).
The variational proof then applies. In particular the full-group lower
bound kappa^2 sum_Gamma |uhat|^2 remains valid; its justification does not
require G_F=I. For one character on any window G_F,xi,xi<=1, so a large
single coefficient directly gives gain at least kappa^2 |c_xi|^2.

## 2. Cubic shell and truncation audit

For a mean-zero u on the full group, write b=uhat,

    T_u=sum_(t!=0) b(t)^2 b(-2t),
    S_u=sum_(t!=0) b(t)b(2t)b(-3t), U=E|u|^2.

Holder and the invertibility of 2 and 3 give
sum |b|^3>=|T_u+S_u|/2. Set M=|T_u+S_u|>0, tau=M/(4U), and
J=floor(log_2(rho/tau)), where rho=max |b|. The bound M<=2rho U
ensures rho/tau>=2; U=0 or M=0 has no signal and is excluded here.
The coefficients below tau contribute at most tau U=M/4.
The remaining J+1 dyadic shells contain cubic mass at least M/4.
Some shell with s entries in [b_0,2b_0) therefore satisfies

    s b_0^3 >= M/[32(J+1)].                              (A4)

When M>=c_1 a^3, U<=a and J+1<=C_J ell(a), the sufficient small-shell
condition for b_0^2>=c a^(5/2)ell(a) is

    s <= c_1/[32 C_J c^(3/2)] a^(-3/4)ell(a)^(-5/2).     (A5)

For example rho<=sqrt(a), tau>=c_1 a^2/4 give the stated logarithmic
bound on J. The old exponent -7/2 is sufficient but unnecessarily small.
At the corrected cutoff the shell-energy lower bound is of order
a^(7/4)ell(a)^(-3/2). Large total Fourier energy does not imply a
large energy gain per character. Also Branch II can be supplied by
<u/2+h,K_u^(3)> even when M is small. (A4) leaves that case open.

The full-group truncated D_3 bound also survives. Put h_-=(a-g)_+ and
g_+=g 1_(g>=a/2). Then g_+>=max(0,a-2h_-). For three coordinates,
the product is at least a^3-2a^2 times the sum of their h_- values:
first truncate each deficit at a, and use product(1-z_j)>=1-sum z_j
for z_j in [0,1]. Multiply by the remaining B. Two distinct AP slots
are uniformly independent on Z_p, so each mixed average E B_i h_-,j
equals a E h_-. Summing the 12 ordered pairs gives

    D_3(g_+) >=4a^4-24a^3 E h_- >=4a^4-12a^3 sqrt(v).

Here E h_-=(1/2)E|g-a|<=sqrt(v)/2. This does not prove positivity
of the thresholded completion pairing, and this independence argument
cannot be transferred unchanged to a proper window.

## 3. Finite quadratic-host audit and stronger replacement

The discrete Z_I and Phi bounds in the October 14 report survive direct
tuple-count verification. Their common no-wrap condition is 4(L-1)<p.
For Phi_M the integer maximum is
L(2M+1)-3M(M+1), M=floor((L-1)/3): at a central integer y all distances
1,...,M fit on both sides; for every other y terms are only omitted.
For Phi_E, its exact integer sum is over
-floor((L-1-y)/3)<=u<=floor(y/3) of L-|u|; summing the two triangular
sums gives L(1+A+B)-[A(A+1)+B(B+1)]/2, where A=floor(y/3)
and B=floor((L-1-y)/3). Set m=A+B<=(L-1)/3. Since
A^2+B^2>=m^2/2, this is at most L(1+m)-m^2/4-m/2.
That expression increases over the stated range of m, so it is at most
(11L^2+20L+5)/36, which is no larger than the reported upper bound.
Thus the continuum limits 8/27,
1/3, 11/36 and 23/18 are consistent with the discrete counts.

But interval density beta=L/p and host density w=|{x:q(x) in I}|/p
are not identical. They differ by at most K/sqrt(p). The finite hitting
inequality uses w. The conclusion 53/69+o(1)<4/5 requires, for example,
beta^(-3)p^(-1/2)(2+log p)^4 ->0; it is not uniform over all L>=1.
For p=7, q(x)=x^2, I={0}, Omega=A={0} is AP-free and has relative
density 1. This refutes only the unqualified finite-p claim, not its
asymptotic version or the original r_4 target.

`QUADRATIC_LOCALIZATION_20261015.md` proves a stronger replacement:

    a <= 3/4 + 20(2+log p)/(beta p^(1/6))

under explicit finite size conditions, and hence a<=3/4+o(1) when
beta p^(1/6)/(2+log p) tends to infinity. It restricts to progressions
with small first and second quadratic increments and uses their almost
constant completion degrees. It does not use translation invariance of
the host, independence of several quadratic coordinates, or an inverse
theorem. A finite-pattern extension is proved there as well.

## 4. An actual AP-free obstruction outside the target density range

**Theorem.** For every sufficiently large prime p there is a cyclically
4-AP-free set A subset Z_p such that, writing a=|A|/p,

    (1/2)p^(-3/5)<=a<=2p^(-3/5),
    max_(xi!=0)|hat 1_A(xi)|<=6p^(-4/5)sqrt(log p),       (A6)

and q_E is nonzero. For the trivial factor g=a, v=0, the actual completion
field q=q_E+q_M has positive pairing S=a E q. Nevertheless, for every
packet with s<=C a^(-1/4)/ell(a),

    |sum_Gamma conjugate(uhat) hat q|/S
          <=s rho/a=O_C(p^(-1/20)/sqrt(log p)) ->0.       (A7)

The constants are uniform over packets. This is a counterexample to
removing the density-range hypothesis from a small-packet theorem.
It is NOT a counterexample to SELECT, which requires a logarithmic
lower density in large admissible windows, or to the target theorem.

*Proof.* Include each residue independently with probability t=p^(-3/5).
The expected number of ordered nonzero-difference four-term progressions
is at most p^2 t^4=p^(-2/5), so the probability that any exists tends to zero.

For completeness the needed Fourier deviation estimate follows from the
elementary Bernstein bound

    Pr(|sum X_i|>=z)<=2 exp(-z^2/[2(V+z/3)]),

for independent centered real |X_i|<=1 and sum E X_i^2<=V. One obtains
it by expanding the exponential: E exp(lambda X_i) is at most
exp(lambda^2 E X_i^2/[2(1-lambda/3)]) for 0<lambda<3, using
k!>=2*3^(k-2) for k>=2; multiply these estimates and minimize the
Chernoff bound with lambda=z/(V+z/3). Apply the same argument to -X_i.

Take X_i to be the centered Bernoulli variables multiplied by the real
or imaginary part of e_p(-xi i); V<=pt. For z=4sqrt(pt log p),
eventually z<=pt, so each real tail costs at most 2p^(-6).
A union bound over both parts and all nonzero frequencies proves the
second bound of (A6), with failure probability at most 4p^(-5).
The same estimate with z=pt/2 bounds the failure of the first assertion
by 2 exp(-pt/12).

Let Z count ordered nonzero-difference three-term progressions in A.
Then E Z=p(p-1)t^3. For any fixed ordered triple, at most 9p ordered
triples share a point, at most 36 share at least two, and at most 6
have the same three-point support. Disjoint indicators are independent;
the remaining covariance is at most t^(6-k) for overlap k. Consequently

    Var Z <=9p^3 t^5+36p^2 t^4+6p^2 t^3,
    Pr(Z=0)<=36/(pt)+144/(p^2 t^2)+24/(p^2 t^3) ->0.

All three desired events therefore occur together for all sufficiently
large p. Every ordered three-term progression gives an endpoint completion
at its preceding point. AP exclusion puts that point outside A, so q_E
is nonzero, and S>0. Since q>=0, |hat q|<=E q. With g=a the complete
pairing is -S and every packet satisfies (A7). Substituting (A6),
a asymptotic to p^(-3/5), and ell(a) asymptotic to log p proves the limit.
Also rho^2/[a^(5/2)ell(a)]=O(p^(-1/10)) ->0. This completes the proof.

The mechanism uses actual completion triples and actual Boolean AP-free
sets, not arbitrary nonnegative fields or pseudo-moment distributions.
Its density is polynomially smaller than epsilon/log p. That limitation
is essential, and it provides no evidence that an eligible counterexample
exists at the target density.

## 5. Quantitative ledger and exact remaining tasks

At a=epsilon/log N, write ell=log(2/a). The previously available squared
signal a^4 and the SELECT threshold a^(5/2)ell still differ by
epsilon^(-3/2)(log N)^(3/2)ell. The weaker collective threshold replaces
ell by R(a)=log log(e^2/a); it still needs a divergent amplification.

If the packet hypothesis of (A2) holds, the implied coefficient is at
least theta^2 gamma^2 a^2/(s^2 w^2). With s<=C a^(-1/4)/ell, this is
at least theta^2 gamma^2 a^(5/2)ell^2/(C^2 w^2), so one character would
suffice for the original SELECT threshold once
theta^2 gamma^2 ell>=c C^2 w^2. Finding that packet remains unproved.
Searching over a packet does not require adding all its characters when
the conclusion is a single large coefficient.

No new density-increment step, cumulative-rank bound, or cumulative
window-loss estimate follows unconditionally from this audit. The existing
conditional iteration remains a separate implication with unproved
structural premises; it was not completely re-audited here. The new
quadratic terminal theorem covers one interval host, not arbitrary
intersections produced by repeated refinements.

Precise continuation:

1. In the original admissible logarithmic-density windows, prove positive
   retention S_gamma after thresholding and find Gamma with S_gamma>0,
   |sum_Gamma conjugate(c)hat phi|>=theta S_gamma, and size satisfying
   (A3), or produce a different quantified refinement. Keep the actual
   residual Gram matrix and the single-character conversion explicit.
   A proof using only positivity and AP exclusion without the density/size
   restriction is ruled out by (A6)--(A7).
2. For the quadratic alternative, extend the weighted count/degree argument
   to the actual class of intersections produced by a specified increment,
   then prove the increment and its full complexity/size ledger. A terminal
   theorem for one quadratic interval alone does not close that iteration.
3. Branch II still requires either a bound on the winning shell size with
   cutoff (A5), or control of the cubic-field pairing when |T_u+S_u| is small.

Do not repeat the numerical checks as an asymptotic proof, and do not
label these remaining existence assertions as established amplification.
