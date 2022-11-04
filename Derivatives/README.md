## Working with derivatives.

The derivative of a function f(x) at a point indicates how the function varies near that point.

Derivative of f(x) -> $(\frac{df(x)}{dx})_{x=a}$ $=lim_{h->0}\frac{f(a+h)-f(a)}{h}$

$(\frac{df(x)}{dx})_{x=a}$

$=lim_{h->0} \frac{f(a+h)-f(a)}{h}$

$h=\frac{R.T}{\mu.g}ln(\frac{p}{p_0})$
 
The derivative only exists if the limit exists.

With a physical function depending on time, the derivative is the speed of variation of the physiqcal quantity associated with the function near the evaluation point.

With a function depending on coordinates, it gives the slope near the evaluation point.

If we calculate the derivative of a function f at a point x, we obtain the derivative function of f, ie a symbolic expression of the derivative valid for all the points where the derivative exists.

- [Finite difference error](err_der_geo.py).
- [Symbolic approach](der_sympy.py).
