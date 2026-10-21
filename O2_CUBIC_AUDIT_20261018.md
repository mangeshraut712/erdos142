# Independent audit of the O2 quantifier and cubic note

18 October 2026. Offline audit. The local target and (P12) remain OPEN.
This audit does not modify the 17 October note or historical outputs.

## Quantifiers

The exact negation and the two-sequence characterization in
`O2_QUANTIFIERS_CUBIC_BOUND_20261017.md` are correct. In particular the
divergent multiplier must be selected before the counterexample. Failure
for a specified multiplier does not establish failure for all multipliers.

For the converse characterization, absence of a bounded-qrel sequence
with density tending to zero gives `m(s)->infinity`. Absence of a
positive-density sequence with prime tending to infinity and qrel tending
to zero gives the positive baseline on the complementary density range.
These two assertions apply uniformly over all eligible presentations of
the hosts. The function `min(a^(-1/4),m0(a)/b)` is a finite real-valued,
divergent function bounded below by one. At any actually eligible density,
`m0(a)` is finite because the defining infimum includes that triple; this
justifies the final comparison there even when the lower envelope can
take value infinity at other arguments.

## Cubic estimate and boundary

The Vandermonde absorption in (C1) has the correct coefficients and signs.
The change of variables between two distinct slots is bijective for
`p>3`, and the coefficients of the third slot in those two variables are
nonzero. The Fourier supremum bound and two Parseval factors therefore
give `q U` with no missing normalization.

For the actual proper host, an omitted indicator can change a cubic term
only when an occupied slot lies in the eroded boundary. The nonnegative
weight and degree estimate bound this error by
`(mu+p^(-1/2))b+1/p`. Multiplying each of the four terms by `a` gives (C2).
All these statements include the zero difference.

For the original `tau=a^2/log p`, the leading normalized boundary cost is
`2/(a log p)`; it need not tend to zero at logarithmic density. Replacing
tau by `a^3/log p` makes that cost `2/log p`. On the reachable class,
`r,S=o(sqrt(log p))` and `1/a=O_epsilon(log p)`, so the new baseline still
has `log(1/mu0)=o(log p)`. This verifies that the first and second residual
estimates survive the replacement. It remains a different weight, and
does not establish the original fixed-weight (P12).

The spectral deficit is correctly recorded: after normalizing, the
principal cubic bound contains
`4c(1-a)(w/mu)a^(-1/2)R(a)`. There is no argument in these estimates that
makes this small under failed selection.

## Quartic identity

The two branches of the chirp orthogonality equations are the AP branch
and the pairing branch, meeting in the common diagonal. Their normalized
contributions are respectively `Lambda4(u)`, `U^2`, and `E u^4/p`.
This proves (C4) with the stated sign and normalization. The unnormalized
frequency sum in (C5) really has the factor `p`; it cannot be discarded.

The weighted quartic identity in the 18 October continuation has also
been checked algebraically. In this audit subsection only, D_s denotes
the RAW product Q_u(c,t)conjugate(Q_u(c+s,t)); the main quartic note uses
D_s for the centered product. With
`s=(N-3C)/2`, `gamma=(N-5C)/2`, the product

    D_s(c,t) conjugate(D_s(3c+gamma,3t-beta))

has slot quadratic coefficients `(0,gamma,-gamma-s,s)` and linear
coefficients `(0,-beta,beta,0)`. The three quadratic sums are `0,C,N`,
as required. Its pairing branch equals `|m_s|^2`. Every frequency row of
`D_s` sums to `m_s`, so subtracting `m_s/p` from each entry cancels that
branch exactly. Independently,

    sum_(c,t) |D_s(c,t)|^2 = U^2+|m_s|^2-E u^4/p,
    sum_(c,t) |D_s(c,t)-m_s/p|^2 = U^2-E u^4/p.

These follow from the two branches of equal first and second moments;
only odd characteristic is needed for this latter norm identity.
Consequently the weighted centered covariance formula has the elementary
uniform consequence

    -U^2+2 E u^4/p <= R4^F <= U^2.

This is a valid bound for the original positive-tent weight, but its
scale `U^2` is insufficient for (P12).

## Verification

The original cubic/quantifier verifier reran successfully: **468 checks**,
maximum identity discrepancy `1.5265566588595902e-16`. Its finite tests do
not verify the quantifier theorem or the asymptotic target domain.

The new `verify_o2_cubic_audit_20261018.py` adds **48 checks**, maximum
identity discrepancy `2.7661073766277612e-18`. It uses primes 257, 521,
1031, actual wrapped linear/quadratic interval hosts, nonempty eroded
hosts, the original positive tent, and the actual cyclically AP-free set
`{0,1,2}`. The omitted-indicator correction is explicitly nonzero in each
case. The structured results are in `O2_CUBIC_AUDIT_20261018.json`.
These cases establish finite algebra and boundary sanity checks only;
their compliance with the logarithmic target domain is not asserted.

No defect requiring a correction to the 17 October note was found. No
new phase selection theorem or sufficient (P12) bound was obtained.
