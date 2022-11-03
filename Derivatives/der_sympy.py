# Fichier : der_sympy.py
# Symbolic calculus
# Module sympy (sympy.org)
# This program can be used as a template
# to compute symbolically derivatives.
# philippe.camus@hepl.be
# 3/11/2022

import sympy as sp  # sympy.org
import matplotlib.pyplot as plt

# Compute derivative symbolically
x = sp.Symbol('x')
question="Derivative of :"
expr=sp.sin(x**4 + 2)/4
result=sp.diff(expr,x)

# The next section with print statements to satisfy our curiosity
# about the way things are coded :-)

# Regular expression
print("Result without formating:")
print(result)
print()

# Latex formated expression
print("Result converted in Latex format:")
print(sp.latex(result))


# Use a pyplot graphical windows (without a graphic!) to display formulas in math format
plt.figure("Resulting equation",figsize=(8,2)) # 8" x 1 " window
plt.text(0.5,0.92,question, fontsize=12,ha='center')
plt.text(0.5,0.7,'$%s$'%sp.latex(expr), fontsize=16,ha='center')
plt.text(0.5,0.35,"Solution :", fontsize=12,ha='center',c="blue")
plt.text(0.5,0.1,'$%s$'%sp.latex(result), fontsize=16,ha='center',c="blue")
plt.axis("off") # no axis
plt.show()
