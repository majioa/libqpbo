QPBO
====

# QPBO with large graph support
This is a ready-to-use QPBO adaptation for OpenGM (original code courtesy of V. Kolmogorov) for very large graphs. Original source code availbable at http://pub.ist.ac.at/~vnk/software.html.

## Original description
Implements algorithms for minimizing functions of binary variables with unary and pairwise terms based on roof duality described in the following papers:

<ul><b>Roof duality, complementation and persistency in quadratic 0-1 optimization. </b><br>
P. L. Hammer, P. Hansen, and B. Simeone.<br>
<em>Mathematical Programming, 28:121-155, 1984.</em>
</ul>

<ul><b>Network flows and minimization of quadratic pseudo-Boolean functions. </b><br>
E. Boros, P. L. Hammer, and X. Sun.<br>
<em>Technical Report RRR 17-1991, RUTCOR Research Report, May 1991.</em>
</ul>


<ul><b>Preprocessing of Unconstrained Quadratic Binary Optimization. </b><br>
E. Boros, P. L. Hammer, and G. Tavares.<br>
<em>Technical Report RRR 10-2006, RUTCOR Research Report, April 2006.</em>
</ul>

<ul><b>Optimizing binary MRFs via extended roof duality. </b><br>
C. Rother, V. Kolmogorov, V. Lempitsky, and M. Szummer.<br>
<em>CVPR 2007.</em>
</ul>

Original implementation by Vladimir Kolmogorov.
The source is originated from several ones: [1](https://github.com/fgrsnau/libqpbo.git), [2](https://github.com/Skielex/QPBO.git), [3](https://github.com/NSchertler/QPBO-opengm.git), and [4](https://github.com/micmacIGN/micmac/tree/master/src/uti_phgrm/GraphCut/QPBO-v1.4).

## Modifications
Changed to allow for very large graphs with up to 2.1 billion nodes and "any number" of edges/terms.

Main changes include:
- Changed edge variables to `long long`.
- Changed a few other variables to `long long`.
- Reduced `sizeof(Node)` by changing some variable types in the `struct`.
