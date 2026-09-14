# Frontier audit: regular Bohr windows and relative fibers

Date: 2026-09-06. Offline derivation; no web search. The original files were not edited.

**Verdict.** Regularity gives explicit geometric error bounds and a same-rank smaller Bohr set. It supplies neither random pair/triple counts for A nor the missing endpoint marginal. In particular, regularity does not upgrade r_L+r_R>a to r_L+r_R>2a. Below is an actual cyclic 4AP-free counterexample family with negligible window-boundary error, and a separate abstract four-bit obstruction. Neither disproves an increment theorem at density comparable to 1/log N. No target asymptotic bound is proved.

## 1. Convention and regularity hypothesis

Let G=F_p, p>3. Use normalized ambient x-averages. For r characters Gamma and 0<rho<1/2, put

    B_rho = {x: ||xi x/p||_{R/Z} <= rho for every xi in Gamma}.

Assume a stated constant C_reg>=1 gives

    ||B_{(1+t)rho}|/|B_rho| - 1| <= C_reg r |t|

for every |t|<=1/(C_reg r). We assume r>=1; the full-group case has exact translation invariance. Write Omega=x_0+B_rho, W=1_Omega, w=|Omega|/p, A subset Omega, B=1_A, a=|A|/|Omega|, g=B-aW. This regularity is a hypothesis; no radius-selection theorem is being invoked without proof.

Let 0<eta<=min(1,1/(3 C_reg r)), D=B_{eta rho}, delta=C_reg r eta, and let nu be any probability distribution supported on D. For identities identifying left/right triple counts, require nu(d)=nu(-d). Uniform D and uniform D minus {0}, when nonempty, both qualify.

## 2. Translation invariance, with proof

For h in D and integer j with |j|eta<=1/(C_reg r), the circle triangle inequality gives

    B_{(1-|j|eta)rho} subset B_rho intersect (B_rho+jh).

It follows that each one-sided difference has size at most

    C_reg r |j|eta |B_rho|,

and therefore

    |Omega triangle (Omega+jh)| <= 2 C_reg r |j|eta |Omega|.       (1)

In particular the L1 distance between the two uniform probability measures is at most 2 C_reg r |j|eta; their total variation distance is at most C_reg r |j|eta. For any |F|<=1,

    |E_Omega F(x+jh)-E_Omega F(x)| <= 2 C_reg r |j|eta.

For 0<=F<=1, the last bound improves to C_reg r |j|eta, by equality of the two one-sided masses. These are window-measure assertions, not translation invariance of B=1_A.

If S_nu B(x)=E_{d~nu}B(x+d), then A subset Omega yields the additional one-sided estimate

    0 <= a-E_Omega S_nu B <= delta.                             (2)

Indeed the only lost A-points lie in a one-sided boundary strip. Equation (2) controls a mean; it does not control the variation of S_nu B or B-S_nu B.

## 3. Restricted-increment counts and their geometry errors

Define Lambda_nu(F0,F1,F2,F3)=E_{d~nu} E_x product_j F_j(x+jd), and define C_nu, Phi_nu, Sigma_L,nu, Sigma_R,nu, and M_nu by the definitions in RELATIVE_WINDOWS.md with Lambda replaced by Lambda_nu. Put

    P_nu=E_{d~nu} E_x B(x)B(x+d),
    T_nu=E_{d~nu} E_x B(x)B(x+d)B(x+2d).

The following estimates require no regularity of A:

    (1-6delta)w <= C_nu <= w;                                  (3)
    0 <= P_nu-Phi_nu <= 2delta w;                              (4)
    0 <= T_nu-Sigma_L,nu <= delta w;                           (5)
    0 <= T_nu-Sigma_R,nu <= delta w.                           (6)

Proof of (3): start with x in Omega; the exclusions x+jd not in Omega for j=1,2,3 have sizes at most j delta |Omega|. Union bound gives 6delta |Omega|.

Proof of (4): a middle pair y,y+d in A is discarded only if y-d or y+2d is outside Omega. Use membership of y and y+d in Omega, respectively, and the two one-step boundary strips. The count of the unrestricted middle pairs equals P_nu after translating x. For (5), a triple in A can be lost only if its last point translated once is outside Omega. For (6), translate a triple once and use the left boundary strip instead. This also proves (6) without assuming symmetry of nu. Symmetry gives Sigma_L,nu=Sigma_R,nu by (x,d)->(x+3d,-d).

For a cyclic 4AP-free A the exact endpoint expansion is

    M_nu = aw nu(0)-a(Sigma_L,nu+Sigma_R,nu)+a^2 Phi_nu.         (7)

Thus, with E_nu=aw nu(0)-2a T_nu+a^2 P_nu,

    |M_nu-E_nu| <= 2delta(a+a^2)w.                             (8)

The diagonal for uniform D is aw/|D|, not aw/p. For nu uniform on D minus {0}, the diagonal is exactly zero.

These estimates do NOT show P_nu is close to a^2 w or T_nu is close to a^3 w. Such statements concern A and are independent hypotheses or new theorems. They also do NOT compare Lambda_nu to the original full uniform-d Lambda: replacing the distribution of d is a change of counting problem, not a window-boundary perturbation. If one uses the unnormalized restriction E_d 1_D(d), all displayed restricted counts are multiplied by |D|/p.

## 4. Errors versus the a^4 baseline and explicit costs

Suppose delta<=a^3/128. Then (8) is at most a^4 w/32, since a<=1. Also (4) is at most a^2 w/64, and (5)-(6) are at most a^3 w/128. Equation (3) makes C_nu comparable to w. Therefore radius

    eta <= a^3/(128 C_reg r)                                  (9)

is sufficient to make these particular geometric errors small relative to the pair, triple, and mixed baselines simultaneously. For an arbitrary bounded four-linear test with no exposed a factors, the crude geometry error is order delta w and would instead require delta much smaller than a^4. One must use the actual weights in (7), not silently interchange these two requirements.

For uniform D, a sufficient diagonal condition at delta<=1/12 is

    |D| >= 16 a^(-3),

which implies aw/|D| <= a^4 C_nu/8. Omitting this condition is especially dangerous when D contains only a few increments.

Elementary size bounds are

    |D| >= (eta/3)^r |B_rho|,
    |D| >= p (eta rho/2)^r.                                   (10)

Proof of the first: lift each coordinate of B_rho to [-rho,rho], partition it into at most ceil(2/eta)<=3/eta intervals of length at most eta rho, and take a largest common cell S. For fixed s_0 in S, the injection s->s-s_0 maps S into D. For the second, partition the whole r-torus into ceil(1/(eta rho))^r boxes, choose a largest cell among the p image points, and take differences in that cell; ceil(1/(eta rho))<=2/(eta rho).

The rank remains r but the guaranteed logarithmic loss from B_rho to D is at most

    r log(3/eta)=r[3 log(1/a)+log(384 C_reg r)]                  (11)

when using equality in (9). The absolute lower bound and diagonal cutoff are guaranteed, for example, by

    log p >= r[log(256 C_reg r/rho)+3 log(1/a)]
             +log 16+3 log(1/a).                              (12)

At a comparable to 1/log N, one step costs O(r(log log N+log r)) in the relative size guarantee. The absolute cutoff additionally sees r log(1/rho). Repeated shrinkage accumulates in rho; growing ranks cannot be treated as fixed. These costs are quantified geometry, not an iteration that solves the low-signal or mixed branch.

## 5. Actual regular-window counterexample to the 2a upgrade

There is a family of cyclic 4AP-free sets in rank-one, 2-regular narrow windows with delta/a^3 tending to zero, such that a<r_L+r_R<2a. For the nonzero increment law supported on {-1,1}, its pair/triple counts moreover satisfy

    Phi_nu/(a^2 C_nu)->1,
    Sigma_nu/(a^3 C_nu)->1,
    M_nu/(a^4 C_nu)->-1.                                      (13)

This refutes a threshold upgrade based on regularity, negligible boundary error, or the corresponding restricted-increment mixed counts alone.

Construction and proof: let m tend to infinity. Among vectors v in {0,...,m-1}^9 choose a most populous level of sum_i v_i^2. Encode these vectors as integers in base 2m and call the resulting set S. Put H=(2m)^9 and K=|S|. Pigeonholing the at most 9(m-1)^2+1 levels, and then fixing eight coordinates for an upper bound, gives

    m^9/[9(m-1)^2+1] <= K <= m^8.                              (14)

The set S is 3AP-free in the integers. In an equation s_0+s_2=2s_1 there are no carries in base 2m, so the digit vectors satisfy v_0+v_2=2v_1. Equal Euclidean squared norms imply v_0=v_1=v_2: expand the norm of their midpoint, or use ||v_0-v_2||^2=0.

Set N=10H+1, Omega=[0,N-1], s=K/N,

    P=floor(K^2/N),  T=floor(KP/N).

Choose any P members of S and then any T of those P members. At each z in S put 10z+3 into A; add 10z+4 for the P selected members; add 10z+5 for the T doubly selected members. Thus |A|=K+P+T and a=(K+P+T)/N.

This A is 4AP-free in the integers. A second-difference equation for points 10z+e, e in {3,4,5}, has digit error of absolute value at most 4, so divisibility by 10 forces z_0-2z_1+z_2=0. Since S is 3AP-free, the first three macro-coordinates coincide, and applying the argument to the last three makes all four coincide. Each cluster has at most three points, so a nontrivial four-term AP is impossible.

Take any prime p>3N. Then A is also cyclic 4AP-free: every second difference of representatives in [0,N-1] has absolute value below p, so modular second differences must be integer zero. This Omega is in the narrow-window class of RELATIVE_WINDOWS.md, because its coordinate diameter N-1 is below p/3.

It is also a translate of the rank-one Bohr set with rho=N/(2p). It is 2-regular for |t|<=1/2. To check this explicitly, write N=2M+1, so rho p=M+1/2. The size change when multiplying rho by 1+t is at most N|t|+1. If a change occurs at all then |t|>=1/N; therefore the size change is at most 2N|t|. The radii in this range are below 1/2, so no saturation issue occurs.

Take eta=2/N, so D=B_{eta rho}={-1,0,1}, and delta=4/N. For each d=1 or -1 all the chosen cluster endpoints and their one-step completions stay inside Omega. Direct counting gives

    q_d=(P+T)/p,  t_L,d=t_R,d=T/p,
    r_L=r_R=T/(P+T),  C_nu=(N-3)/p.                            (15)

Here nu is uniform on {-1,1}. The inequality NT<=KP proves exactly

    r_L <= K/N < a,

when P>0. Thus r_L+r_R<2a. On the other hand (14) gives s->0 and Ns^3->infinity: the latter grows at least as a positive constant times m^3. Hence

    P~Ns^2, T~Ns^3, a~s, r_L/a->1.

It follows that r_L+r_R>a for all sufficiently large m, and (13) follows by substituting (15). Also

    delta/a^3 = 4/(Na^3) -> 0.

The window is almost unchanged by translation by 1, but

    |A triangle (A+1)|=2K,
    |A triangle (A+1)|/|A| -> 2.

Thus even maximal relative translation irregularity of A coexists with negligible geometric boundary error and actual AP-freeness.

Scope limits: this family has polynomially small density (between constant multiples of m^-2 and m^-1), so a log N tends to zero. It is outside the target-density regime a comparable to 1/log N. Equation (13) concerns the explicitly nonzero increment law; uniform D includes a large diagonal because |D|=3 and fails the diagonal-size cutoff. Nor does (13) assert the original full-uniform-d mixed alternative. These limitations prevent this counterexample from being misreported as a disproof of the desired theorem.

## 6. Abstract perfect-marginal obstruction (outside the cyclic-set class)

For 0<a<=1/2 and e in {0,1}^4 with k=sum e_i, define

    P(e)=a^k(1-a)^(4-k)-a^4(-1)^k.

For even k, nonnegativity follows from 1-a>=a; for odd k the correction is positive. Summing the alternating correction over any omitted coordinate gives zero. Thus this is a probability distribution whose every proper marginal is exactly independent Bernoulli(a), but P(1111)=0.

Conditioned on e_1=e_2=1, the two endpoint marginals are each exactly a, their joint probability is zero, and

    E[(e_0-a)e_1e_2(e_3-a)]=-a^4.

Consequently even perfect proper marginals and a negative mixed signal do not imply an endpoint conditional mean greater than a. This is an abstract local law, not an asserted realization by one cyclic set simultaneously for all differences. The missing global arithmetic compatibility is exactly what a further theorem would have to use.

## 7. Finite verification and remaining gap

As a small actual narrow-window check, take p=307, Omega=[0,100], and

    A={1,2,3,8,11,12,13,16,19,23,24,29,31,37,41,47,48,
       54,56,58,61,63,67,69,73,76,78,81,87,88,92,94,95,99,100}.

Exhaustive integer AP enumeration verifies 4AP-freeness; the no-wrap argument gives cyclic 4AP-freeness. For d=1 the exact counts are q*p=8 and t_L*p=t_R*p=2. Thus a=35/101 and r_L+r_R=1/2 lies strictly between a and 2a. The window is 2-regular by the preceding interval proof. This small example is not claimed to satisfy a theorem's large local-size cutoff or stable-Phi condition.

The proved frontier is therefore: geometry can be made harmless at explicit rank/radius cost; the all-d arithmetic compatibility of A remains necessary. No mixed-branch density increment, no cheap repeated smoothing, and no r_4(N)=o(N/log N) conclusion follows from these estimates.
