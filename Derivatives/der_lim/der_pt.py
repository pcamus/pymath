# File der_pt.py
# Calculation of sin(x**4+2)/4 derivative at a:
# - Using small h approximation and symbolic calculation
# - Using the limit method
# - Using the diff method
# philippe.camus@hepl.be
# 13/12/2021

import numpy as np  # numpy.org
import sympy as sp  # sympy.org

sp.init_printing(use_unicode=True)

# Function used for numerical approximation of the limit
def my_function(a,h):
    return (np.sin((a+h)**4+2)-np.sin(a**4+2))/(4*h)

pta=5 # point where the derivative is evaluated
h=1E-6
result_num=my_function(pta,h)

# *************************************************************
# Numerical value of the approximation of the limit
print("Numerical method.")
print("Result for=",h, "is: ",result_num)
print()
print()


# *************************************************************
# *************************************************************
# Symbolic calculation of the derivative with the limit
h = sp.Symbol('h',real=True, positive=True)
a = sp.Symbol('a',real=True)
expr_lim=(sp.sin((a+h)**4+2)-sp.sin(a**4+2))/(4*h)
result_symlim=sp.limit(expr_lim,h,0)

# *************************************************************
# General expression of derivative at a with the limit
print("Symbolic calculation with the limit method.")
print("Limit for h->0")
sp.pprint(expr_lim)
print()
print("at a is: ")
sp.pprint(result_symlim)
print()
print()

# *************************************************************
# Derivative for a=pta
print("at a = %d is: "%pta)
sp.pprint(result_symlim.evalf(subs={a:pta}))
print()
print()


# *************************************************************
# *************************************************************
# Symbolic calculation of the derivative with the diff method
x = sp.Symbol('x',real=True)
expr_der=sp.sin(x**4 + 2)/4
result_der=sp.diff(expr_der,x)

# *************************************************************
# General expression of derivative at x with the diff method
print("Symbolic calculation with the diff method.")
print("Derivative of: ")
print()
sp.pprint(expr_der)
print()
print("in x is: ")
sp.pprint(result_der)
print()
print()

# *************************************************************
# Evaluate the derivate at a given point x=pta
print("in x = %d is: "%pta)
sp.pprint(result_der.evalf(subs={x:pta}))
print()
print()
