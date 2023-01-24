# File: antder_sympy.py
# Antiderivative symbolic computation
# x**3.cos(x**4+2)
# Sympy module(sympy.org)
# philippe.camus@hepl.be
# 24/1/2023

import sympy as sp  # sympy.org

sp.init_printing(use_unicode=True)

# Function to use
x = sp.Symbol('x')
expr=x**3*sp.cos(x**4+2)
print("Function:")
print()
sp.pprint(expr)
print()

# Antiderivative
antder=sp.integrate(expr,x)
print("Antiderivative:")
print()
sp.pprint(antder)
print()
# Note using the integrate method with only the symbol leads to antiderivative
# Using a tuple with symbol and boundaries as in sp.integrate(expr,(x,0,1))
# leads to compute the integral

# Derivative to control if we get the initial function.
der=sp.simplify(sp.diff(antder))
print("Control:")
print()
sp.pprint(der)
