# Lean 4 Formalization Groundwork for Erdős Problem 142

This directory contains formal Lean 4 / Mathlib specifications and proofs for the core algebraic identities used in the density increment proof of $r_4(N) = o(N / \log N)$.

## Structure

- `lakefile.lean`: Lake build configuration with Mathlib dependency.
- `lean-toolchain`: Specifies Lean 4 toolchain (`leanprover/lean4:v4.8.0`).
- `Erdos142/HoleSupport.lean`:
  - Definition of 4-AP-freeness on $\mathbb{Z}/p\mathbb{Z}$.
  - Multi-channel completion fields $q_j(v)$ for $j \in \{0, 1, 2, 3\}$.
  - The Pointwise Hole Support Theorem: $B(v) q_j(v) = 0$ for all $v \in \mathbb{Z}/p\mathbb{Z}$.
  - Total hole support $B(v) q(v) = 0$.
- `Erdos142/TightFrame.lean`:
  - Quadratic chirp characters $\psi_{(c, t)}(x) = e_p(c x^2 + t x)$ on $\mathbb{Z}/p\mathbb{Z}$.
  - The Tight Frame Resolution of Identity: $\sum_{c, t} \psi_{(c, t)}(x) \overline{\psi_{(c, t)}(y)} = p^2 \delta_{x, y}$.

## How to Build

With Lean 4 and `elan` installed:

```bash
cd formalization/lean
lake update
lake build
```
