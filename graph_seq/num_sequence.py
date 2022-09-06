# Fichier num_sequence.py
# Computes and displays an indexed sequence of value  
# philippe.camus@hepl.be
# 6/9/2022

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# Here is the function to compute each element of the sequence
def my_function(n):
    return (n**2-25)/(2*n**2+1) 

# Some parameters we need *****************************************************
plot_title="a_n=(n^2-25)/(2n^2+1)]" # Latex formated graphic name

# boundaries used to compute values of the sequence
low_bnd=4
high_bnd=100

delta=1 # calculation step

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
    ordinate[i]=my_function(abscissa[i]) # function value at i position


# Prepare and display the sequence values *************************************

# The plot is first created in memory 
#plt.plot(abscissa, ordinate) # points are connected by line segments 
plt.plot(abscissa, ordinate, ".") # points not connected, "." char used
                                  # to display points 

# Plot elements and formatting parameters are added below
plt.title("Sequence : $%s$"%plot_title) # Put plot_title value as graph title

plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$a_n$") # give a label to vertical axis
# Note : use $ char on each side of an expression to tell it's latex coding  

# Uncomment if you want to use scientific notation for numbers
#plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
#plt.ticklabel_format(axis='x',style='sci',scilimits=(0,0))

plt.grid(True) # Display a x,y grid if true

# Show the graphic on the screen.
plt.show()
