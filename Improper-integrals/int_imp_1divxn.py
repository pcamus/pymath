# File: int_imp_1divxn.py
# Computing a type 1 improper integral
# with scipy integrate function and with Riemann approach 
# Function: 1/x**n
# philippe.camus@hepl.be
# 9/3/2023

import scipy.integrate as sp
import numpy as np

def my_function(x,n):
    return (1/x**n)
#    return (np.exp(-x)) 

n=2.0
lower_bound=1.0
upper_bound=10000.0 # used to compute rectangles
# with scipy the upper boundary is infinite : np.inf

print(f"Integral from 1 to infinite of 1/x**{n}")
print()

# with scipy
int_imp=sp.quad(my_function, lower_bound,np.inf,args=(n,)) # return tuple (value, error)
print(f"Integral with scipy = {int_imp}")
print()

# with the sum of rectangles (Riemann)
nrect=100000 # steps number
deltax=(upper_bound-lower_bound)/nrect
x=lower_bound
int_imp=0

for i in range(nrect):
    x=x+deltax # rectangle to the left because delta is added first
    int_imp=int_imp + my_function(x,n)*deltax

print(f"Riemann integral from 1 to {upper_bound} = {int_imp}")
