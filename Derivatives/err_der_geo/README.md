## Error with the finite difference approximation.


The finite difference approximation consists in replacing the correct expression of the derivative using a $\displaystyle\lim_{h \to 0}$ with a finite, small value for h.

In the code this expression is: **`((x0+hval[i])**2-(x0)**2)/hval[i]`**

x0 is the point where we calculate the dérivative, hval[i] the h value for the current step of the loop.

