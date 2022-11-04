# File: err_der_geo.py
# This program computes derivative of f(x)=x**2 with finite differences
# Value of step h vs accuracy is checked, printed and plotted
# f'(x)~[f(x+h)-f(x)]/h
# philippe.camus@hepl.be 
# 30/11/2021

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# step boundaries
upper_bound=1
lower_bound=1.0E-20
nelem = 20 # number of iterations
x0 = 1 # value where the derivative is computed
exact_val= 2 # exact value ofd derivative in x0 

# Empty vector for storing the approximate derivatives
der_num=np.zeros(nelem) 

# Geometrically spaced h value from upper_bound to lower_bound
hval=np.geomspace(upper_bound, lower_bound, nelem) # 

# Compute derivatives 
for i in range(nelem):
    der_num[i]=((x0+hval[i])**2-(x0)**2)/hval[i] 

error=abs((der_num-exact_val)/exact_val) # relative error vs exact value

for i in range(nelem):
    print("h= %.2E   Relative error= %.2E"%(hval[i],error[i]))

plt.scatter(hval, error) # Creates graph in memory
# Title and axis names
plt.title("Relative error on the derivative of $y=x^2$ in x="+str(x0)) # $ entoure une expression mathématique
plt.ylabel("Relative error")
plt.xlabel("h")

# Uses scientific notation for numbers
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.ticklabel_format(axis='x',style='sci',scilimits=(0,0))
plt.grid(True) # Uses a grid

# Plots the graph on the screen
plt.show()

# Note: Use magnifying glass on the graph to watch points
