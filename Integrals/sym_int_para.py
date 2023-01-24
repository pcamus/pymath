# File : sym_int_para.py
# Symbolic method for integrals
# Parabola example
# Uses sympy module (sympy.org)
# philippe.camus@hepl.be
# 24/01/2023

import sympy as sp  # sympy.org

sp.init_printing(use_unicode=True)


# Deferred method (builds integral expression then solves it)
x = sp.Symbol('x')
expr=x**2
primit=sp.Integral(expr,(x,0,5)) 
sp.pprint(primit)
sp.pprint(primit.doit())
print()

# Direct method
x = sp.Symbol('x')
expr=x**2
primit=sp.integrate(expr,(x,0,5))
sp.pprint(primit)