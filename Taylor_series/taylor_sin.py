# File: taylor_sin.py
# Taylor serie for sin(x), accuracy vs number of terms.
# philippe.camus@hepl.be
# 30/11/2021

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

title="Calculation of sin(x) by Taylor's formula" # titre du graphique au format Latex

# calculation boundaries
lower_bound=0.0
upper_bound=3*np.pi/2

nelem = 120 # numberof points to compute
                                # +1 to include upper boundary

# Vector of nelem elemnts creation
# linearly spaced values from lower_bound to upperer_bound
abscissa=np.linspace(lower_bound,upper_bound, nelem) # x

# Ordinates computation, element by element for the correct value
# then Taylor's approximation with 3, 4 & 5 terms
sin_ex=np.sin(abscissa) # y(x)
sin_3t=abscissa-abscissa**3/np.math.factorial(3)+abscissa**5/np.math.factorial(5)
sin_4t=abscissa-abscissa**3/np.math.factorial(3)+abscissa**5/np.math.factorial(5) \
       -abscissa**7/np.math.factorial(7) 
sin_5t=abscissa-abscissa**3/np.math.factorial(3)+abscissa**5/np.math.factorial(5) \
       -abscissa**7/np.math.factorial(7)+abscissa**9/np.math.factorial(9) 

# Creates plots in memory (4 plots)
plt.plot(abscissa, sin_ex, c="red",label="sin exact value")
plt.plot(abscissa, sin_3t, c='green', label="3 terms")
plt.plot(abscissa, sin_4t, c='blue', label="4 terms")
plt.plot(abscissa, sin_5t, c='gray', label="5 terms") 

# Graphical elements
plt.title(title) # $ is used to surround a Latex expression
plt.ylabel("y(x)")
plt.xlabel("x")

plt.grid(True) # displays grid if True
plt.legend()

# Displays plot on the screen.
plt.show()
