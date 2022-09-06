# Fichier num_sequence.py
# Computes and displays an indexed sequence of value  
# philippe.camus@hepl.be
# 6/9/2022

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# Here is the function for evaluating each element of the sequence
def my_function(n):
    return (n**2-25)/(2*n**2+1) 

# Some parameters we need *****************************************************
plot_title="a_n=\\frac{n^2-25}{2n^2+1}" # Latex formated graphic name

# maximum value of the index
max_index=22

# Vector allocation ***********************************************************
abscissa=np.zeros(max_index+1) # x values are stored here (= horizontal coordinate)
ordinate=np.zeros(max_index+1) # corresponding y(x) values are here (= vertical coordinate)

# Filling vectors *************************************************************
for i in range(max_index+1):
    abscissa[i]= i # compute ith abscissa from preceding one
                                      
for i in range(max_index+1):
    ordinate[i]=my_function(i) # function value at i position

# Note : add 1 to max_index to include max_index element (0,1,2...max_index)

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
