## Symbolic calculation of derivatives.

The [der_sympy.py](der_sympy.py) will show you how to use symbolic calculation for derivatives with the sympy module.

This program can be use as a template for your symbolic derivative calculations.

Part of the code is dedicated to abetter presentaton of the formulas and are not mandatory.

The core of the code is:

**`x = sp.Symbol('x')`** resrve a symbol named 'x' with no constraints

expr=sp.sin(x**4 + 2)/4
result=sp.diff(expr,x)
