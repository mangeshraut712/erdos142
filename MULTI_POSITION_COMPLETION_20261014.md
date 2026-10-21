# Multi-position completion algebra, two-channel cell projection, and exact cross-overlap geometry — 14 October 2026

**Status: (D) NEW RIGOROUS PARTIAL THEOREM.** Extending completion analysis from endpoint-only anchors to the joint endpoint-plus-interior completion vector sharpens the cell projection, strictly increases the Hilbert-space residual overlap on finite and proper-window examples, and exposes new exact cross-overlap AP-forced zeros in the degree-six SOS hierarchy. It does not prove SELECT, a sufficient character budget, or the local target \(r_4(N)=o(N/\log N)\). This is an offline continuation; no literature novelty is claimed.

## 1. Endpoint and interior completion fields and their exact diagonals

Let \(p>3\) be prime, \(B=1_A\) on \(\mathbb{Z}_p\), and assume \(A\) has no nonzero-difference 4-AP. Reversing \(d\mapsto -d\) identifies the two endpoint slots \(j=0,3\) and the two interior slots \(j=1,2\). Define the normalized endpoint and interior completion averages and their diagonal-corrected counterparts:

    h_E(v) = p^-1 sum_{d in Z_p} B(v+d)B(v+2d)B(v+3d),
    h_M(v) = p^-1 sum_{d in Z_p} B(v-d)B(v+d)B(v+2d),
    q_E(v) = h_E(v) - B(v)/p,
    q_M(v) = h_M(v) - B(v)/p.

Booleanity and 4-AP exclusion give, pointwise on the whole group,

    B h_E = B/p,    B h_M = B/p,
    B q_E = 0,      B q_M = 0,
    q_E >= 0,       q_M >= 0.                               (1)

Write \(b=\widehat{B}\), \(K_E=\widehat{h_E}\), and \(K_M=\widehat{h_M}\) with \(p^{-1}\) spatial normalization. Solving the frequency equations \(\alpha+\beta+\gamma=t\) and \(-\alpha+\beta+2\gamma=0\) gives \(\alpha=(t+r)/2\), \(\beta=(t-3r)/2\), \(\gamma=r\). Thus

    K_E(t) = sum_r b(2t+r) b(-t-2r) b(r),
    K_M(t) = sum_r b((t+r)/2) b((t-3r)/2) b(r),
    hat q_E(t) = K_E(t) - b(t)/p,
    hat q_M(t) = K_M(t) - b(t)/p,
    sum_r b(r) hat q_E(t-r) = 0,
    sum_r b(r) hat q_M(t-r) = 0.                            (2)

For a proper window \(\Omega\), zero-extend \(B\) to \(\mathbb{Z}_p\) first so (1) holds pointwise, and restrict averages and factor partitions to \(\Omega\) afterward.

## 2. Joint two-channel cell decomposition and matrix Loewner bound — PROVED

Take any partition \(F\) of \(\Omega\) with uniform probability measure on \(\Omega\). On each nonempty cell \(C\in F\), put

    g = E_C B,    u = B - g,
    T_{E,C} = E_C q_E,    T_{M,C} = E_C q_M,
    k_E = q_E - T_{E,C},  k_M = q_M - T_{M,C}.

For \(0\le g<1\) define the vector \(\alpha_C = (1-g)^{-1}(T_{E,C}, T_{M,C})^T\) (and \(\alpha_C=(0,0)^T\) when \(g=1\)), and set

    z_E = q_E - T_{E,C}(1-B)/(1-g),
    z_M = q_M - T_{M,C}(1-B)/(1-g).

Because both \(q_E\) and \(q_M\) vanish on \(A\), the vector \(z=(z_E,z_M)^T\) satisfies

    k = -alpha_C u + z,
    E_C z = 0,    B z = 0,    E_C(u z) = 0.                 (3)

Let the global relative pairing vector and covariance matrices be

    S = (S_E, S_M)^T = E_Omega[g (T_{E,C}, T_{M,C})^T],
    U = E_Omega[g(1-g)],
    J = E_Omega[g(1-g) alpha_C alpha_C^T],
    Z = E_Omega[z z^T],
    W = E_Omega[k k^T].

**Theorem 1 (Two-channel covariance splitting and optimal overlap).**
1. The exact pairing with the residual \(u\) is \(\langle u, k\rangle_\Omega = -S\), and the within-cell completion covariance matrix splits orthogonally as

       W = J + Z,    Z >= 0 (PSD).                          (4)

2. In the Loewner positive-semidefinite order on \(2\times 2\) real symmetric matrices,

       U W >= U J >= S S^T.                                 (5)

3. For every linear combination \(k_\lambda = \lambda_E k_E + \lambda_M k_M\) with \(\lambda=(\lambda_E,\lambda_M)^T\in\mathbb{R}^2\),

       <u, k_lambda> = -lambda^T S,
       ||k_lambda||_2^2 = lambda^T W lambda.                (6)

   Consequently, whenever \(U>0\), the maximum squared normalized Hilbert-space overlap of \(u\) with \(\operatorname{span}(k_E, k_M)\) is

       max_{lambda} |<u, k_lambda>|^2 / (U ||k_lambda||_2^2)
           = U^-1 S^T W^dagger S
           >= max( S_E^2/(U W_{EE}), S_M^2/(U W_{MM}) ).    (7)

   Equality between the two-channel bound and the endpoint-only bound \(S_E^2/(U W_{EE})\) holds (for nonsingular \(W\)) if and only if \(W_{EE} S_M = W_{EM} S_E\).

Proof: (3) gives \(\langle u, k\rangle_C = -g(1-g)\alpha_C = -g(T_{E,C},T_{M,C})^T\) and \(E_C[k k^T] = g(1-g)\alpha_C\alpha_C^T + E_C[z z^T]\); averaging over \(C\in F\) gives (4). For any \(\lambda\in\mathbb{R}^2\), Cauchy–Schwarz applied to \(\sqrt{g(1-g)}\) and \(\sqrt{g(1-g)}(\lambda^T\alpha_C)\) gives \((\lambda^T S)^2 \le U (\lambda^T J \lambda) \le U (\lambda^T W \lambda)\), which is (5). Optimizing the Rayleigh quotient over \(\lambda\) yields (7).

## 3. Joint relative spectral projection — PROVED

Let \(\Gamma\) be a finite set of characters and \(P_\Gamma\) be the \(\Omega\)-orthogonal projection onto \(L_\Gamma = \operatorname{span}\{(I-E(\cdot|F))e_p(tx) : t\in\Gamma\}\). For any weight vector \(\lambda\in\mathbb{R}^2\), set \(\delta(\lambda) = \|(I-P_\Gamma)k_\lambda\|_2\) and \(W_\Gamma(\lambda) = \|P_\Gamma k_\lambda\|_2^2\). Then whenever \(W_\Gamma(\lambda)>0\),

    ||P_Gamma u||_2^2 >= max(0, |lambda^T S| - sqrt(U) delta(lambda))^2 / W_Gamma(lambda).  (8)

In particular, if \(\delta(\lambda)^2 \le (\lambda^T S)^2/(4U)\), then

    ||P_Gamma u||_2^2 >= (lambda^T S)^2 / (4 W_Gamma(lambda))
                      >= (lambda^T S)^2 / (4 lambda^T W lambda).                            (9)

## 4. Exact interior and cross-overlap geometry and degree-six SOS — PROVED

For \(p>7\) prime and \(v\in\Omega\), let \(D_{E,v}=\{d\ne 0: v+d,v+2d,v+3d\in\Omega\}\) and \(D_{M,v}=\{d\ne 0: v-d,v+d,v+2d\in\Omega\}\), with sizes \(m_{E,v}\) and \(m_{M,v}\). Set \(E_d=\{v+d,v+2d,v+3d\}\) and \(M_d=\{v-d,v+d,v+2d\}\), and define the cubic completion polynomials

    H_{E,v} = sum_{d in D_{E,v}} X_{E_d},
    H_{M,v} = sum_{d in D_{M,v}} X_{M_d}.

Because \(M_{-d} = \{v+d, v-d, v-2d\}\), the unordered triples \(M_d\) and \(M_{-d}\) are distinct and share the two points \(\{v-d,v+d\}\).

**Proposition 2 (Exact interior and cross-overlap classification).** For \(p>7\):
1. **Interior overlaps:** Let \(R_M = \{i/j \bmod p : i,j\in\{-1,1,2\}\} = \{1, -1, 2, 1/2, -2, -1/2\}\), which has 6 distinct elements. For \(d,e\in\mathbb{F}_p^\times\) with \(r=e/d\):
   - \(|M_d\cap M_e| = 3\) if \(r=1\);
   - \(|M_d\cap M_e| = 2\) if \(r=-1\), with \(M_d\cup M_{-d} = \{v-2d,v-d,v+d,v+2d\}\);
   - \(|M_d\cap M_e| = 1\) if \(r\in\{2, 1/2, -2, -1/2\}\);
   - \(|M_d\cap M_e| = 0\) otherwise.
   None of the unions \(M_d\cup M_e\) for \(r\in R_M\setminus\{1\}\) contains a 4-AP for \(p>7\).

2. **Cross overlaps:** Let \(R_{EM} = \{i/j \bmod p : i\in\{1,2,3\}, j\in\{-1,1,2\}\} = \{1, 2, 3, -1, -2, -3, 1/2, 3/2\}\), which has 8 distinct elements for \(p>7\). For \(d,e\in\mathbb{F}_p^\times\) with \(r=e/d\):
   - \(|E_d\cap M_e| = 2\) if \(r=1\), where \(E_d\cup M_d = \{v-d,v+d,v+2d,v+3d\}\);
   - \(|E_d\cap M_e| = 1\) if \(r\in R_{EM}\setminus\{1\}\), so \(|E_d\cup M_e| = 5\);
   - \(|E_d\cap M_e| = 0\) otherwise.

3. **AP-forced cross-overlap zeros:** Among the seven 5-element cross-unions \(E_d\cup M_{rd}\) (\(r\in R_{EM}\setminus\{1\}\)), the ratio \(r=2\) gives

       E_d union M_{2d} = {v-2d, v+d, v+2d, v+3d, v+4d},

   which contains the 4-AP \(\{v+d,v+2d,v+3d,v+4d\}\) for every \(p>7\) (and for \(p=13\), \(r=3\) additionally contains a wrapped 4-AP). Thus \(M(E_d\cup M_{2d})=0\) under degree-five AP multipliers.

**Theorem 3 (Degree-six joint completion matrix SOS certificate).**
For any real weights \(\alpha,\beta\) and scalar \(s\), Booleanity and the degree-four AP equations \(X_v H_{E,v}=0\) and \(X_v H_{M,v}=0\) give the degree-six SOS certificate

    [alpha H_{E,v} + beta H_{M,v} - s(1-X_v)]^2
      - 2 s X_v (alpha H_{E,v} + beta H_{M,v})
      = (alpha H_{E,v} + beta H_{M,v})^2
        - 2 s (alpha H_{E,v} + beta H_{M,v}) + s^2(1-X_v) >= 0.   (10)

Consequently, any degree-six PSD extension \(L\) with \(L(X_v)=a\) must satisfy the \(2\times 2\) matrix inequality

    [ L(H_{E,v}^2)         L(H_{E,v} H_{M,v}) ]
    [ L(H_{E,v} H_{M,v})   L(H_{M,v}^2)       ]
      >= (1-a)^-1 [ L(H_{E,v}) ] [ L(H_{E,v})  L(H_{M,v}) ].     (11)
                  [ L(H_{M,v}) ]

Under uniform third moments \(L(X_T)=\rho_3\), the right-hand side is \((1-a)^{-1}\rho_3^2 (m_{E,v}, m_{M,v})^T (m_{E,v}, m_{M,v})\), forcing joint sixth-moment correlations across endpoint-endpoint, endpoint-interior, and interior-interior disjoint triple pairs simultaneously.

## 5. What changes in the zero-completion branch — PROVED

1. **Full group:** On the full group,
   - \(\sum_{v\in\mathbb{Z}_p} q_E(v) = p\Lambda_3(B) - a\) counts ordered 3-APs \((y,y+d,y+2d)\) in \(A\) with \(d\ne 0\) (each has completion anchor \(v=y-d\)). Thus \(q_E\equiv 0\) on \(\mathbb{Z}_p\) if and only if \(A\) is 3-AP-free.
   - \(\sum_{v\in\mathbb{Z}_p} q_M(v) = p\mathbb{E}_{v,d} B(v-d)B(v+d)B(v+2d) - a\) counts configurations \((y, y+2d, y+3d)\) in \(A\) with \(d\ne 0\) (i.e., 4-APs missing one interior point \(v=y+d\)). These two global sums need not be equal on a general 4-AP-free set: for instance, \(A=\{0,1,2\}\subset\mathbb{Z}_{11}\) has one 3-AP (\(\sum H_E=2\)) but no \((y,y+2d,y+3d)\) triple (\(\sum H_M=0\)), whereas \(A=\{0,2,3\}\subset\mathbb{Z}_{11}\) has \(\sum H_M=2\) and \(\sum H_E=0\).
   - However, under the bijection \((y,d)\mapsto (y'=y+3d, d'=-2d)\) in \(\mathbb{Z}_p\) (\(p>3\)), the triple \((y, y+2d, y+3d)\) equals \((y'+3d'/2, y'+d'/2, y')\), which is a 3-AP if and only if \(d=0\). Wait: a configuration \((y, y+2d, y+3d)\) has difference \(2d\) and \(d\), not equal differences! Its Fourier expansion is

         E_v q_M(v) = a^3 - a/p + sum_{r!=0} b(r) b(2r) b(-3r),

     which is precisely the **second cubic Fourier invariant** \(S = \sum_{r\ne 0} \widehat{f}(r)\widehat{f}(2r)\widehat{f}(-3r)\) from the 4-AP expansion \(\Lambda_4(B) = a^4 + 2a(T+S) + Q\), whereas \(\mathbb{E}_v q_E(v) = a^3 - a/p + T\) with \(T = \sum_{r\ne 0} \widehat{f}(r)^2\widehat{f}(-2r)\) is the **first cubic Fourier invariant**!
   - Consequently, if \(q_M\equiv 0\) on \(\mathbb{Z}_p\) (or even if \(\mathbb{E} q_E + \mathbb{E} q_M = 0\)), Cauchy–Schwarz and Parseval give the same linear Fourier lower bound

         rho = max_{r!=0} |b(r)| >= max(0, (a^2 - 1/p)/(1 - a)),    (12)

     because \(|S| \le \rho \sum_{r\ne 0} |b(2r)||b(-3r)| \le \rho a(1-a)\). Thus \(q_E\) and \(q_M\) are the exact physical-space duals of the two cubic Fourier terms \(T\) and \(S\) in \(\Lambda_4(B)\)!
2. **Proper windows:** On a proper window \(\Omega\), \(q_E\) can vanish identically on \(\Omega\) while \(q_M\) is nonzero on \(\Omega\) (and vice versa).
   - For the earlier proper-window diagnostic \(p=101, \Omega=\{0,\dots,24\}, A=\{0,1,3\}\), \(q_E\equiv 0\) on \(\Omega\), so the endpoint-only overlap is \(S_E=0\). However, for \(v=2\in\Omega\) and \(d=-1\), \(v-d=3\in A, v+d=1\in A, v+2d=0\in A\), so \(H_M(2)=1>0\). Thus \(S_M>0\) and the two-channel projection extracts a strictly positive signal on \(\Omega\) where the endpoint projection was identically zero.
   - Similarly, for the ternary cube \(A\subset\Omega=\{0,\dots,13\}\) in \(\mathbb{Z}_{59}\), \(H_E\equiv 0\) on \(\Omega\), whereas \(\sum_{v\in\Omega} H_M(v)=10>0\), so \(S_M>0\).
   - Only when all \((1,2,3)\) and \((-1,1,2)\) triples in \(A\) have completion anchors outside \(\Omega\) (or when both \(q_E\) and \(q_M\) vanish globally, as in the Sidon-like digit product \(\{0,1,4\}+16\{0,1,4\}\subset\mathbb{Z}_{277}\)) do both \(q_E\) and \(q_M\) vanish on \(\Omega\).

## 6. Verification

Run `python3 verify_multi_position_completion_20261014.py`.
It verifies (1)–(11), exact interior and cross-overlap ratios, exact \(2\times 2\) cell covariance splittings and Loewner inequalities on all 743 AP-free subset/window cases in \(\mathbb{Z}_7,\mathbb{Z}_{11}\) and the proper-window diagnostics, confirms strict two-channel overlap improvements over endpoint-only projection on 2,017 nontrivial cases across \(\mathbb{Z}_7,\mathbb{Z}_{11},\mathbb{Z}_{13}\), and checks the proper-window rescues on `{0,1,3}` and the ternary cube. Output is saved to `MULTI_POSITION_COMPLETION_VERIFICATION_20261014.json`.
