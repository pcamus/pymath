# Fichier num_funcR.py
# Computes and displays a real-valued function in a defined range  
# philippe.camus@hepl.be
# 6/9/2022

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# Here is the function
# Note that t is the variable, a and f are parameters of the function
def my_function(x):
    return np.tan(x) 

# Some parameters we need *****************************************************
plot_title="y(x)=tan(x)" # Latex formated graphic name

# boundaries used to compute values of the function
low_bnd=0
high_bnd=5

delta=0.05 # calculation step

disp_range = high_bnd-low_bnd #the range we will display 
niter = int(disp_range/delta)+1 # number of points to compute
                                # +1 to include high boundary


# Vector allocation, index from 0 to niter ***********************************
abscissa=np.zeros(niter) # x values are stored here (= horizontal coordinate)
ordinate=np.zeros(niter) # corresponding y(x) values are here (= vertical coordinate)

# Filling vectors *************************************************************
# To begin, initialise the first element.
abscissa[0]=low_bnd

# Then compute all elements
for i in range(1,niter):
    abscissa[i]=abscissa[i-1] + delta # compute ith abscissa from preceding one
                                      
for i in range(niter):
    ordinate[i]=my_function(abscissa[i]) # function value at abscissa i


# Prepare and display the function as a set of line segments ******************

# The plot is first created in memory 
plt.plot(abscissa, ordinate) # points are connected by line segments 

# Plot elements and formatting parameters are added below
plt.title("Function : $%s$"%plot_title) # Put plot_title value as graph title

plt.xlabel("x") # give a label to horizontal axis
plt.ylabel("y(x)") # give a label to vertical axis
# Note : use $ char on each side of an expression to tell it's latex coding  

# Uncomment if you want to use scientific notation for numbers
#plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
#plt.ticklabel_format(axis='x',style='sci',scilimits=(0,0))

plt.grid(True) # Display a x,y grid if true

# Show the graphic on the screen.
plt.show()
