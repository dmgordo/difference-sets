---
layout: single
title: "The La Jolla Difference Set Repository"
mathjax: true
---

A $(v,k,\lambda)$-difference set in a group $G$ is a subset $D = $ {$d_1, d_2, ..., d_k$} of $G$ such that each nonzero element of $G$ can each be represented as a difference $(d_i - d_j)$ in exactly $\lambda$ different ways.

This database gives information about possible parameters for
difference sets in abelian groups $G$. All parameters with
$v&lt;100000$ passing basic tests (counting, Schutzenberger,
Bruck-Ryser-Chowla) are
listed here, and an attempt has been made to include all known
difference sets. Most known for large $v$ are Paley, which are easily
constructed, so those are omitted for $v&gt;1000$.


See [the La Jolla Combinatorics Repository](https://dmgordo.github.io) for more
information about this and other combinatorial datasets I've made.
This is an experiment in making a FAIR (Findable, Accessible,
Interoperable, Reusable) mathematical database (see [The FAIR Guiding
Principles for scientific data management and
stewardship](https://doi.org/10.1038/sdata.2016.18) for details.

This repository contains a json file with all the data from the paper, and
python code to read it and display the results.  It can be run interactively
with [binder](https://mybinder.org), or downloaded and run locally.  Anyone
wishing to further develop the code to do research on difference sets is
welcome to under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0)
license (giving attribution to the original work).

To run the notebook with binder, click here:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmgordo/difference-sets/master?filepath=difference_sets.ipynb)

## Contact 
If you encounter any problems with this repository, please report them
to <dmgordo@gmail.com>.
