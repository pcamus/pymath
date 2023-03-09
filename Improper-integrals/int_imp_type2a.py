# File: int_imp_type2a.py
# Computing improper integral of type 2
# with scipy integrate function and with Riemann
# function: 1/(x-1) between 0 and 3
# philippe.camus@hepl.be
# 9/3/2023

import scipy.integrate as sp
import numpy as np

def my_function(x):
    return (1/(x-1))


lower_bound=0.0
upper_bound=3.0 # used to compute rectangles


# with scipy
int_imp=sp.quad(my_function, lower_bound,upper_bound) # return tuple (value, error)
print(f"Integral with scipy = {int_imp}")
print()

# with the sum of rectangles (Riemann)
nrect=10000 # steps number
deltax=(upper_bound-lower_bound)/nrect
x=lower_bound
int_imp=0

for i in range(nrect):
    x=x+deltax # rectangle to the left because delta is added first
    int_imp=int_imp + my_function(x)*deltax

print(f"Riemann integral  = {int_imp}")
