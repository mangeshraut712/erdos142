# Corrected completion identity and exact cell projection — 13 October 2026

**Status: (D) NEW RIGOROUS PARTIAL THEOREM.** The exact projection removes
an avoidable error from the residual pairing. It does not prove SELECT,
a sufficient character budget, or the local target r4(N)=o(N/log N).
This is an offline continuation; no literature novelty is claimed.

## 1. Normalization and the diagonal

Let p>3 be prime, B=1_A on Z_p, and assume A has no nonzero-difference
4-AP. Use normalized averages and define

    h(v)=p^-1 sum_{d in Z_p} B(v+d)B(v+2d)B(v+3d),
    q(v)=h(v)-B(v)/p.

Then q is the nonzero-difference completion count divided by p. Booleanity
and AP exclusion give, pointwise on the whole group,

    B h=B/p,       B q=0,       q>=0.                 (1)

Thus B h=0 would be incorrect with this definition of h. If b=hat B,
K=hat h, then the exact frequency identities are

    K(t)=sum_r b(2t+r)b(-t-2r)b(r),
    hat q(t)=K(t)-b(t)/p,
    sum_r b(r)K(t-r)=b(t)/p,
    sum_r b(r)hat q(t-r)=0.                           (2)

All Fourier transforms in (2) use p^-1 normalization. For a proper window
Omega, zero-extend B first; (1) remains valid. Restrict averages and the
factor to Omega only afterward. A cell label never restricts the three
completion points; the zero extension does that.

## 2. Exact cell decomposition — PROVED

Take any partition F of Omega, with uniform probability measure on Omega.
On each nonempty cell C put

    g=E_C B,   u=B-g,   T_C=E_C q,   k=q-T_C.

For 0<=g<1 define alpha_C=T_C/(1-g) and

    z=q-T_C(1-B)/(1-g).

Then the exact identity is

    k=-alpha_C u+z,                                  (3)
    E_C z=0,    Bz=0,    E_C(uz)=0.

Proof: q vanishes at occupied points, so its mean over the complement is
T_C/(1-g). Subtract that complementary mean. The resulting z has zero
mean, vanishes on A, and hence is orthogonal to B-g. Subtracting T_C from
q gives (3). If g=1, q=k=u=z=0; take alpha_C=0. If g=0, u=0 and z=k.
These degenerate cells must be retained.

In particular,

    E_C(uk)=-g T_C,
    E_C k^2=g T_C^2/(1-g)+E_C z^2.                   (4)

The quotient term is defined as zero on g=1. Equation (4) is sharp: z=0
if and only if q is constant on the complement of A in each cell.
This assertion concerns the projection identity; such a q need not be
realizable as a completion function for every proposed B and F.

## 3. Exact overlap, and what actually improves — PROVED

With relative averages let

    S=E_Omega[g T_C],   U=E_Omega[g(1-g)],
    W=E_Omega[(q-T_C)^2],   J=E_Omega[g T_C^2/(1-g)].

Then

    <u,q>=<u,k>=-S,
    W=J+||z||_2^2,    S^2<=U J<=U W.                (5)

The stronger first inequality follows from Cauchy applied to
sqrt(g(1-g)) and sqrt(g/(1-g)) T_C. It also follows directly by pairing
u with the component alpha_C u in (3). All terms are nonnegative.
If S,U,W>0, the normalized Hilbert-space overlap is exactly

    |<u,k>|/sqrt(U W)=S/sqrt(U W).                    (6)

There is no subtraction of sqrt(Var(g) Var(q)) in the exact formula.
The older bound remains valid but can lose unnecessary information.
On the full group, writing a=E B, T=E q, v=Var(g), one has the finer identity

    S=aT+Cov(g,T_C),
    S>=aT-sqrt(v Var(T_C)).                           (7)

Indeed conditional expectation replaces q by T_C in its pairing with g.
The variance splitting is Var(q)=Var(T_C)+W. Therefore the uncertainty in
S depends only on the between-cell variance of completion means, whereas
W measures the within-cell component relevant to residual pairing.
Large within-cell completion variance does not by itself enlarge the error
in (7). This is a genuine sharpening of equation (14) in the October 12
Fourier report. It does not establish a positive lower bound for S under
SELECT: completions in g=0 cells contribute to T but not to S.

## 4. Relative spectral projection with the exact Gram — PROVED

For a finite set Gamma of characters, let

    psi_t=(I-E(.|F)) exp(2 pi i t x/p) on Omega,
    L_Gamma=span{psi_t:t in Gamma},
    P_Gamma=orthogonal projection onto L_Gamma.

Use the actual relative Gram G_{s,t}=<psi_s,psi_t> with the usual complex
Hilbert-space convention. If c_t=<psi_t,u>, then

    ||P_Gamma u||_2^2=c* G^dagger c.                 (8)

The Moore-Penrose inverse handles dependent or zero characters. Equation
(8) is projection energy, not an unqualified sum of relative Fourier
squares. Relative characters need not be orthogonal. A factor refinement
which resolves these characters contains their real and imaginary parts,
and captures at least this projection energy. A quarter-quantized
refinement requires the separate regularized Gram conversion already in
the October 12 report; it must not be replaced by (8) without proof.

Let delta=||(I-P_Gamma)k||_2 and W_Gamma=||P_Gamma k||_2^2. Orthogonality
and (5) imply

    ||P_Gamma u||_2^2 >=
      (max(0,S-sqrt(U) delta))^2/W_Gamma,             (9)

when W_Gamma>0. Proof: split <u,k> into its projection and tail pairings,
bound the tail by sqrt(U) delta, then use Cauchy on the projection.
If S>0 and

    delta^2<=S^2/(4U),

then W_Gamma>0 and

    ||P_Gamma u||_2^2>=S^2/(4W_Gamma)>=S^2/(4W).     (10)

This eliminates the factor-variance premise from the old sufficient
concentration statement when S itself is available. It replaces total
variance by W and uses the exact relative Gram. It is still conditional
on a small enough set Gamma with the stated tail. No such character
budget has been proved here.

Cellwise orthogonality does not survive a chosen spectral projection:

    ||P_Gamma k||^2=||P_Gamma(alpha u)||^2
                   +||P_Gamma z||^2
                   -2 Re<P_Gamma(alpha u),P_Gamma z>.

Thus the explicit negative residual component can be cancelled in selected
frequencies. When alpha varies across cells it also multiplies u, mixing
frequencies. The verifier exhibits positive projected cross terms even
for the trivial factor, where alpha is constant. This finite numerical
diagnostic prevents an unjustified inference from global orthogonality
to frequency-by-frequency orthogonality; it is not a SELECT counterexample.

For a trivial full-group factor, S=aT and W=Var(q), so the sharpening does
not supply a new density exponent in that case. At T of order a^3 and
U of order a, the sufficient tail remains of order a^7. Completion size
and the exact projection alone do not give a small character budget.

## 5. The zero-completion branch — PROVED, with scope distinctions

If q is identically zero on the whole group, A is 3-AP-free. Conversely,
every 3-AP-free set has q=0: any triple y,y+d,y+2d contributes to the
completion at y-d, and every completion arises this way. Here d!=0 and
p>3 ensure the points are distinct.

Put a=|A|/p and rho=max_{t!=0}|b(t)|. The mean identity from (2) gives

    0=a^3-a/p+sum_{r!=0} b(r)^2 b(-2r).

Parseval and the triangle inequality give, for 0<a<1,

    rho>=max(0,(a^2-1/p)/(1-a)).                     (11)

Thus q=0 does not mean there is no arithmetic signal. On the full group
it gives an explicit linear Fourier branch. But when pa^2 tends to
infinity its guaranteed squared signal is only of order a^4. Compared
with SELECT's a^(5/2) log(2/a), the ratio is of order

    a^(3/2)/log(2/a) -> 0.

At a=epsilon/log N this ratio is of order

    epsilon^(3/2)/[(log N)^(3/2) log(2 log N/epsilon)].

This guarantee is insufficient at the required scale. Equation (11) is
for B's full-group coefficients, not arbitrary nontrivial-factor residual
coefficients or properly normalized relative coefficients.

If q is zero only on Omega, the 3-AP-free equivalence and the zero global
mean do not follow. For example in Z_11 take A=Omega={0,1,2}. It contains
a 3-AP but its completion anchors are 3 and 10, outside Omega. This is a
finite diagnostic, outside the claimed asymptotic regime. The earlier
ternary-cube and digit-product examples are also retained as finite
checks, not target-density asymptotic counterexamples.

If q=0 on Omega then S=W=0, so (9)-(10) provide no signal. A completion-only
proof must supply a separate relative-window zero/low-completion branch.
Full-group (11) cannot simply be transplanted into that branch.

## 6. Verification and remaining lemma

Run `python3 verify_completion_projection_20261013.py`.
The run checked all AP-free subsets of Z_7 and Z_11 and four proper-window
diagnostics: 743 set/window cases, 5,189 exact cell identities, 2,229 exact
pairing/variance checks, 4,458 numerical relative Gram projection checks,
and 276 nonempty full-group zero-completion Fourier branches. The pointwise
identities and the global zero-completion/3-AP equivalence use integers
and Fractions. Fourier/Gram inequalities use tolerance 1e-10; symbolic
proofs above establish the stated inequalities independently of testing.
Results are in COMPLETION_PROJECTION_VERIFICATION_20261013.json.

The remaining lemma is precise: under the permitted relative-window and
low-factor-energy hypotheses, obtain either a direct residual/refinement
gain at the required scale, including the S=0 branch, or S>0 plus a
character set Gamma satisfying delta^2<=S^2/(4U), with S^2/(4W_Gamma)
and the added rank meeting the established SELECT or collective dyadic
ledger. The exact projection has reduced the uncertainty to these inputs;
it has not proved them.
