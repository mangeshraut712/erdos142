# Next research action

**Status: OPEN; outcome D, partial results only.** Updated 24 October 2026.
The local target `r_4(N)=o(N/log N)`, DIRECT-Q-GAIN, P12 and W8 remain
unproved. The October 21 closure and effective-rate claims are withdrawn
because of missing proof steps, not merely pending external peer review.

Read the [authoritative proof correction](docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md) and
[current checkpoint](checkpoints/AUTONOMOUS_CHECKPOINT_20261024.json).

For genuinely eligible AP-free hosts under failed adequate phase selection,
prove `E_F(u)<=2U^2+2R3+a^4wmu`, where `U=wa(1-a)`, or prove adequate
phase selection directly. Use the pointwise completion identities `Bq_j=0`
together with T5, logarithmic density, original weight, and exact diagonals.
Retain the cubic term. Do not replace one-sided pair bounds by equalities.

A direct completion route needs a uniform cross-spectrum concentration
bound and control of the orthogonal residual, plus the small/zero completion
mean branch. The exact frame alone does not provide any of these.

Read the correction before any proof attempt. Test proposed norm and
concentration inequalities on the recorded rational counterexamples before
using them in an iteration. Preserve failed drafts and audit new analytic
steps independently; passing finite checks cannot replace a proof.

## October 23 research continuation

Attack simultaneous extendable-triple restrictions across overlapping edges of the eroded mixed host, under failed quadratic selection. First read LM23 and the explicit zero-mean law so the next attempt adds information not present in the one-edge moments. Seek the full sufficient gain throughout m<=2a^3T/w, retaining original weight and boundary errors.

[Exact statements, proofs, obstruction and dependency graph](docs/audits/LOW_MEAN_MOMENT_CONE_20261023.md).

## October 23 overlapping-progression results

**OD23:** For actual cyclic four-AP-free A and the original bounded weight,
q(v)<=2aw and Var_Omega(q)<=2aw m-m^2, improving the previous constants.
The proof uses mutually exclusive completion triples at directions h and 2h.
**CL23:** Consistent local Boolean laws on every set of at most floor(1/a)+1
vertices have marginal a, pair moments a^2, zero triples, and residual
R3+R4=-a^4 on each four-coordinate edge. These are local probability laws,
not eligible arithmetic counterexamples. OC23 provides the exact modular
overlap parameterization and finite joint occupancy polytopes.

P12, W8 and DIRECT-Q-GAIN remain OPEN. The degree improvement gives no
positive mean or sufficient phase gain. Next attack a density-dependent
family of overlaps using global consistency or failed phase selection;
a fixed finite overlap alone cannot exclude CL23.

[Proofs, exact slack identity, audit and updated dependency graph](docs/audits/OVERLAP_CONSTRAINTS_20261023.md).

## October 24 growing-system results

PC24 proves that an occupied pair has at most nine possible third vertices
in a four-AP completion triple. GI24 constructs actual zero-completion
subsets of every n-vertex pattern of size at least (2sqrt(2)/9)n/sqrt(n-1).
IE24 proves the weighted completion incidence bound ||K||^2<=72aw/p,
with counting Euclidean norms. These do not supply sufficient phase gain.

The factorial threshold beyond n~1/a forces arbitrary triples, while
completion triples form a sparse arithmetic subfamily. The missing
transfer between those quantities remains OPEN. Next apply the incidence
operator to centered occupied-pair data under failed phase selection,
retaining the contribution of triples without arithmetic extensions.
The October 21 closure remains withdrawn; no eligible counterexample exists
in these new checks and no proof of the local target is claimed.

[Precise statements, proofs, failed attacks and dependency graph](docs/audits/GROWING_OVERLAP_SYSTEMS_20261024.md).

## October 24 bilinear-pair incidence results

**BP24:** For every 4-AP-free subset A and every pair vector with ||f||_infty<=1
and test function with ||psi||_infty<=1, |E_Omega[psibar Kf]|<=6w a^(3/2)<=6 a^(3/2).
The ratio |E_Omega[psibar Kf]|/a^(3/2)<=6w is uniformly bounded and cannot
supply the diverging factor F_epsilon(a)->infinity needed by DIRECT-Q-GAIN.
Pointwise hole support B(v) K(v, c)=0 forces u(v)=-a on the entire row support
of K, spatial decoupling <u, Kf> = -a <g, f>, and the exact closed quartic
residual identity R4 = 3a^4T + 2R1 + R2 - awm + aw(1-4a)/p.
Under m=0 and failed linear selection, R4 ~ 3a^4T > 0, but Gowers U^3 transfer
yields an exponent gap delta >= a^(4C) (4C >= 2 > 3/2).

P12, W8 and DIRECT-Q-GAIN remain OPEN. Next attack must either exploit
multi-scale global consistency across overlapping Bohr hosts or prove
adequate quadratic phase selection directly without passing through K.

[Exact statements, proofs, ceiling audit and updated dependency graph](docs/audits/BILINEAR_PAIR_INCIDENCE_20261024.md).

## October 24 multi-scale Bohr overlap results

**MS24:** Pointwise hole support B(v) K_{1->2}(v, c) = 0 and spatial decoupling
<u_1, K_{1->2} f> = -a_1 <g_{1->2}, f> hold across arbitrary multi-scale hosts.
Density discrepancy shifts are annihilated on zero-mean phases:
<u_1, psi> = <u_2, psi> = <u_{12}, psi>.
Distinct quadratic phases are asymptotically orthogonal across overlapping Bohr hosts.

P12, W8 and DIRECT-Q-GAIN remain OPEN. The incidence route through K is closed
in both single-host and multi-host formulations. Next attack must prove adequate
quadratic phase selection directly on Bohr neighborhoods without passing through K,
or investigate the arithmetic low-mean branch m <= 2a^3 T / w using U^4 uniformity.

[Exact statements, proofs, multi-scale audit and updated dependency graph](docs/audits/MULTISCALE_BOHR_OVERLAPS_20261024.md).

## Previous record

The [superseded pre-correction version](history/proof_audit_20261021/before_updates/NEXT_AUTONOMOUS_ACTION.md) is preserved verbatim. Earlier dated sources remain in [docs/audits/](docs/audits/) and [history/](history/).
