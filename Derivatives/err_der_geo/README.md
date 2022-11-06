## Error with the finite difference approximation.

The finite difference approximation consists in replacing the correct expression of the derivative using a $\displaystyle\lim_{h \to 0}$ by an expression with a small, finite value for h.

The code [err_der_geo.py](err_der_geo.py) shows how finite differences behaves with the size of h. We try several values of h ranging from 1 to $10^{-20}$ 

In the code the expression for $\displaystyle f(x)=x^2$ derivative finite difference approximation is: **`((x0+hval[i])**2-(x0)**2)/hval[i]`**

x0 is the point where we calculate the derivative, hval[i] the h value for the current step of the loop.

The explanation of the code is very similar to the one in the [graph_seq](https://github.com/pcamus/pymath/tree/main/graph_seq) section.
