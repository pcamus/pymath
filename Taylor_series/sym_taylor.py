# File: sym_taylor.py
# Symbolic calculation of Taylor series.
# https://docs.sympy.org/latest/modules/series/series.html#more-intuitive-series-expansion
# philippe.camus@hepl.be
# 7/11/2023

import sympy as sp # https://numpy.org/

sp.init_printing(use_unicode=True)

x=sp.Symbol('x')

# Taylor serie for cos(x) up to the term of order 10
sp.pprint(sp.series(sp.cos(x),x, n=10))
print()

# Taylor serie for exp(x) up to the term of order 10
sp.pprint(sp.series(sp.exp(x),x, n=10))
print()

# Taylor serie for square root of (1+x) up to the term of order 10
sp.pprint(sp.series(sp.sqrt(1+x),x, n=10))
print()

# Compute square root of 2 (x=1) using Taylor serie for square root of (1+x)
# up to the term of order 100 and then substituting x with 1
result=sp.series(sp.sqrt(1+x),x, n=100)
result=result.removeO()
result=result.subs(x,1)

print(result.evalf())
