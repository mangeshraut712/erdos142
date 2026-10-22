# Lean formalization draft: explicit remaining assumptions

This directory is incomplete formalization groundwork for auxiliary identities.
It is **not a formal proof** of the local target or DIRECT-Q-GAIN. See the
[October 21 correction](../../docs/audits/OCT21_CLOSURE_CORRECTION_20261021.md).

- `Erdos142/HoleSupport.lean` contains an admitted lemma (`sorry`).
- `Erdos142/TightFrame.lean` declares four project-specific axioms:
  `e_p_sub_conj`, `e_p_add`, `e_p_zero`, and `sum_linear_character`.
  Its frame argument is conditional on those declarations.
- Neither file proves phase concentration, a completion-mean lower bound,
  an unconditional density increment, or an asymptotic rate.

No successful Lean build was established by the Python verification suite.
The code and existing toolchain configuration are retained for repair and
independent checking. The mathematical hole-support and tight-frame identities
have elementary arguments; their truth does not certify this draft's Lean code.

To attempt a build with Lean/elan installed:

```bash
cd formalization/lean
lake update
lake build
```

Before claiming a completed formalization, remove the admitted lemma, prove
the four auxiliary character facts, record a successful build, and inspect
the axioms of each advertised theorem. Even that would establish auxiliary
identities only; the analytic selection step remains open.
