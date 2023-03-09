# File: gauss.py
# Displays Normal distribution
# of samples ranging between 0 et 20 avec une moyenne de 12.5
# et un écart type de 2
# philippe.camus@hepl.be
# 3/3/20222

import numpy as np # https://numpy.org/
import scipy.integrate as sp
import matplotlib.pyplot as plt  # https://matplotlib.org/
titre="Normal distribution" # titel of the plot

def my_function(x):
    return (np.exp(-0.5*((x-12.5)/2)**2)/(2*np.sqrt(2*np.pi)))

# boundaries
lower_bound=0
upper_bound=20

delta=0.01 # plot step

range = upper_bound-lower_bound #range of the computation
nelem = int(range/delta)+1 # number of computation points
                                # +1 to include upper bound

# nelem points linearly spaced
abscissa=np.linspace(lower_bound,upper_bound, nelem) # x

# Computationof ordinates
ordinates_1=my_function(abscissa) 

# Area under the curve
bi_int=-np.inf
bs_int=np.inf
int_imp=sp.quad(my_function,bi_int,bs_int) # return tuple (value, error)
print(f"scipy value of integral from {bi_int} to {bs_int} = {int_imp}")

# Plot stored in internal memory
plt.plot(abscissa, ordinates_1, c="blue")

# Plot ornaments
plt.title(titre) 
plt.ylabel("Densité de probabilité")
plt.xlabel("x")
plt.grid(True) # plot grid
# Display plot onthe screen.
plt.show()
