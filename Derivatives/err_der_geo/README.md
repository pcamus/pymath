## Error with the finite difference approximation.

The finite difference approximation consists in replacing the correct expression of the derivative using a $\displaystyle\lim_{h \to 0}$ by an expression with a small, finite value for h.

The code [err_der_geo.py](err_der_geo.py) shows how finite differences behave with the size of h. We try several values of h ranging from 1 to $10^{-20}$ and we compare the results with the correct value of the derivative in 1 the realtive error formula: **`error=abs((der_num-exact_val)/exact_val)`**.

In the code the expression for $\displaystyle f(x)=x^2$ derivative finite difference approximation is: **`((x0+hval[i])**2-(x0)**2)/hval[i]`**

**`x0`** is the point where we calculate the derivative (1 in this example), **`hval[i]`** the h value for the current step of the loop.

The explanation of the code is very similar to the one in the [graph_seq](https://github.com/pcamus/pymath/tree/main/graph_seq) section.

We use the expression **`hval=np.geomspace(upper_bound, lower_bound, nelem)`** to generate a vector of nelem with values in a [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression). In this way, the h values will change faster than in a linear sequence so we can inspect a broader range of values in a few steps.

We also use the **`plt.scatter(  )`** instruction instead of the **`plt.plot(  )`** instruction.

Notice what happen when h is very small. It is due to the fact that real numbers are approximated in Python with the float type ([IEEE-754 double precision format](https://docs.python.org/3/tutorial/floatingpoint.html)).

