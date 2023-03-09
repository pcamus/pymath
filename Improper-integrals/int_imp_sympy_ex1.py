# File: int_imp_sympy_ex1.py
# Symbolic calculation of the total power radiated by a body
# at température T using its spectrum and various formulas
# Module sympy (sympy.org)
# philippe.camus@hepl.be
# 9/3/2023

import sympy as sp  # sympy.org

sp.init_printing(use_unicode=True)

# Used symbols, integration is made from f
f = sp.Symbol('f', real=True)
h = sp.Symbol('h', real=True, positive=True)
c = sp.Symbol('c', real=True, positive=True)
kb = sp.Symbol('kb', real=True, positive=True)
T = sp.Symbol('T', real=True, positive=True)

a=2*h/c**2
b=h/(kb*T)

# Rayleigh-Jeans
expr_rj=2*f**2*kb*T/c**2
power_rj=sp.integrate(expr_rj,(f,0,sp.oo))
sp.pprint(power_rj)

# Wien
expr_w=a*f**3*sp.exp(-b*f)
power_w=sp.integrate(expr_w,(f,0,sp.oo))
sp.pprint(power_w)

# Planck
expr_p=a*f**3/(sp.exp(b*f)-1)
power_p=sp.integrate(expr_p,(f,0,sp.oo))
sp.pprint(power_p)

