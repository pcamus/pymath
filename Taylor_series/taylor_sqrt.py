# File: taylor_sqrt.py
# Taylor serie for sqrt(1+x), accuracy vs number of terms.
# philippe.camus@hepl.be
# 30/11/2021

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

title="Calculation of sqrt(1+x) by Taylor's formula" # titre du graphique au format Latex

# calculation boundaries
lower_bound=0.0
upper_bound=4.0

nelem = 120 # numberof points to compute
                                # +1 to include upper boundary

# Vector of nelem elemnts creation
# linearly spaced values from lower_bound to upperer_bound
abscissa=np.linspace(lower_bound,upper_bound, nelem) # x

# Ordinates computation, element by element for the correct value
# then Taylor's approximation with 3, 4 & 5 terms
rc_ex=np.sqrt(1+abscissa) # y(x)
rc_3t=1+abscissa/2-abscissa**2/8+abscissa**3/16
rc_4t=1+abscissa/2-abscissa**2/8+abscissa**3/16-5*abscissa**4/128 
rc_5t=1+abscissa/2-abscissa**2/8+abscissa**3/16-5*abscissa**4/128+7*abscissa**5/256 

# Square root of 2
r2num=1 + 1/2 - 1/8 + 1/16 - 5/128 + 7/256 
r2py=np.sqrt(2)
print("Square root of 2 by Taylor's formula = ", r2num)
print("Square root of 2 with numpy = ", r2py)
print("Relative error", abs((r2py-r2num)/r2py))

# Creates plots in memory (4 plots)
plt.plot(abscissa, rc_ex, c="red",label="$\\sqrt{1+x}$")
plt.plot(abscissa, rc_3t, c='green', label="3 terms")
plt.plot(abscissa, rc_4t, c='blue', label="4 terms")
plt.plot(abscissa, rc_5t, c='gray', label="5 terms") 

# Graphical elements
plt.title(title) # $ is used to surround a Latex expression
plt.ylabel("y(x)")
plt.xlabel("x")

plt.grid(True) # displays grid if True
plt.legend()

# Displays plot on the screen.
plt.show()

