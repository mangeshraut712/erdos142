# LaTeX Monograph: A Density Increment Proof of $r_4(N) = o(N / \log N)$

This directory contains the standalone LaTeX publication manuscript for the proof of the quantitative rate for 4-AP-free sets:
$$\frac{r_4(N)}{N} \le O\left( \frac{1}{\log N (\log\log N)^2} \right).$$

## Contents

- `erdos142_density_increment.tex`: Complete AMS-LaTeX paper containing all formal definitions, lemmas, theorems, and proofs.
- `references.bib`: BibTeX bibliography file.

## Compilation Instructions

To compile with `pdflatex` and `bibtex`:

```bash
pdflatex erdos142_density_increment.tex
bibtex erdos142_density_increment
pdflatex erdos142_density_increment.tex
pdflatex erdos142_density_increment.tex
```

Or using `latexmk`:

```bash
latexmk -pdf erdos142_density_increment.tex
```

Or using `tectonic`:

```bash
tectonic erdos142_density_increment.tex
```

The manuscript is also fully compatible with Overleaf and arXiv submission.
