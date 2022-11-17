# File: ballistic.py
# Symbolic computation for the frictionless ballistic problem
# Uses sympy module (sympy.org)
# philippe.camus@hepl.be
# 16/11/2022

import sympy as sp  # sympy.org
import matplotlib.pyplot as plt

# Uncomment to run the desired option

# Ballistic

# Origin and range
x = sp.Symbol('x')
alpha = sp.Symbol('alpha')
g = sp.Symbol('g')
v0 = sp.Symbol('v0')
question="Origin and range:"
#
expr=sp.tan(alpha)*x-(1/2)*g*(x**2)/(v0**2*sp.cos(alpha)**2) # trajectory
#
result=sp.solve(expr,x)

# # Apogee
# x = sp.Symbol('x')
# alpha = sp.Symbol('alpha')
# g = sp.Symbol('g')
# v0 = sp.Symbol('v0')
# question="Apogee value (along x):"
# 
# expr=sp.tan(alpha)*x-(1/2)*g*(x**2)/(v0**2*sp.cos(alpha)**2) # trajectory
# 
# interm1=sp.diff(expr,x) # derivative of trajectory relative to x
# interm2=sp.solve(interm1,x) # x value to get a zero for the derivative, result is a list
# result=expr.subs(x,interm2[0]) # substitute x with the above value in the trajectory equation

 
# # Angle for maximum range
# x = sp.Symbol('x')
# alpha = sp.Symbol('alpha')
# g = sp.Symbol('g')
# v0 = sp.Symbol('v0')
# question="Angle for maximum range:"
# expr=sp.tan(alpha)*x-(1/2)*g*(x**2)/(v0**2*sp.cos(alpha)**2)
# interm1=sp.solve(expr,x) # range = x value where y=0
#                          # interm1[0]=origin, interm1[1]=range
# interm2=sp.diff(interm1[1],alpha) # range function derivative relative to alpha
# result=sp.solve(interm2, alpha) # alpha value to get a zero for the derivative
# 
# print(result)

# Uses matplot graph to render latex formula without graph ;-)
plt.figure("Resulting equation",figsize=(6,4)) # 8" x 1 " window
plt.text(0.5,0.95,question, fontsize=14,ha="center")
plt.text(0.5,0.80,"Trajectory equation:",fontsize=12,ha="center")
plt.text(0.5,0.65,"$%s$"%sp.latex(expr), fontsize=16,ha="center")
plt.text(0.5,0.4,"Solution :", fontsize=12,ha='center',c="blue")
plt.text(0.5,0.25,"$%s$"%sp.latex(result), fontsize=16,ha="center",c="blue")
plt.axis("off") # no axis
plt.show()

