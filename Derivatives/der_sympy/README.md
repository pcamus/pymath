## Symbolic calculation of derivatives.

The [der_sympy.py](der_sympy.py) will show you how to use symbolic calculation for derivatives with the sympy module.

This program can be use as a template for your symbolic derivative calculations.

Part of the code is dedicated to abetter presentaton of the formulas and are not mandatory.

The core of the code is:

**`x = sp.Symbol('x')`** reserve a symbol named 'x' with no constraints.

**`expr=sp.sin(x**4 + 2)/4`** construct the expression to derivate, ie the function $\displaystyle\frac{sin(x^4+2)}{4}$ in our example.

**`result=sp.diff(expr,x)`** compute the symbolic derivative.
