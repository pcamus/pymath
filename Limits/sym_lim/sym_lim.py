# Fichier sym_lim.py
# Symbolic computation of a limit for a sequence and for a function.
# There is no difference for the symbolic computation.
# For information about limits : https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html#limits
# For information about assumption see : https://docs.sympy.org/latest/guides/assumptions.html
# philippe.camus@hepl.be
# 8/9/2022

import sympy as sp  # sympy.org

sp.init_printing(use_unicode=True)

# First example.
# Creates the symbolic expression with possible assumptions *******************
n = sp.Symbol('n', real=True) # n is a symbol, not a variable
                              # n is real number
expr1=(n**2-25)/(2*n**2+1) # expr1 is something looking more like text 
                          # than a traditional computer expression

print("Symbolic expression of the sequence  :")
sp.pprint(expr1) # pretty print prints expression to look like math expression

# Do symbolic computation of the limit for n at infinity **********************
print("")
print("Symbolic computation of the limit of the sequence :")
sp.pprint(sp.limit(expr1,n,sp.oo)) # oo (two lowercase o) is the symbol for infinity
print("")


# Second example.
# Creates the symbolic expression with possible assumptions *******************
t= sp.Symbol('t', real=True) # t is a real number
a = sp.Symbol('a', real=True, positive=True) # a is a real and positive number
f = sp.Symbol('f', real=True) # f is a real number
                                         
expr2=sp.exp(-a*t)*sp.cos(2*sp.pi*f*t)
print("")
print("Symbolic expression of the function  :")
sp.pprint(expr2)

# Do symbolic computation of the limit for t at infinity **********************
print("")
print("Symbolic computation of the limit of the function :")
sp.pprint(sp.limit(expr2,t,sp.oo)) # oo (two lowercase o) is the symbol for infinity

