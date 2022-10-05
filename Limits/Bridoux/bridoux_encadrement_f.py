# File bridoux_encadrement_f.py
# Draws frames around the limiting value of an indexed sequence of value  
# christel.ruwet@hepl.be
# 3/10/2022

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# Here is the function for evaluating each element of the sequence

def seq_f(n):
    return (-1)**n/(n**2+1)

# Vector allocation ***********************************************************
max_index=20
absc=np.zeros(max_index+1) # x values are stored here (= horizontal coordinate)
ord_f=np.zeros(max_index+1) # corresponding y(x) values are here (= vertical coordinate)

# Filling vectors *************************************************************
for i in range(max_index+1):
    absc[i]= i+1
    ord_f[i]=seq_f(i+1) # function value at i position

# graphic
plt.plot(absc, ord_f, ".")
plot_title="f_n=\\frac{(-1)^n}{2n^2+1}" # Latex formated graphic name
plt.title("Sequence : $%s$"%plot_title) # Put plot_title value as graph title
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$f_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true
plt.axhline(y=0, color='b', linestyle='-')  # Add a horizontal line at the limiting value L
plt.axhline(y=-0.1, color='r', linestyle='-') # Add 2 horizontal lines to frame the values between L-0.1 and L+0.1
plt.axhline(y=0.1, color='r', linestyle='-')
plt.axhline(y=-0.01, color='g', linestyle='-')  # Add 2 horizontal lines to frame the values between L-0.01 and L+0.01
plt.axhline(y=0.01, color='g', linestyle='-')

# Show the graphic on the screen.
plt.show()
