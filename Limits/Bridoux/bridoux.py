# File bridoux.py
# Computes, displays and finds limiting value of an indexed sequence of value  
# christel.ruwet@hepl.be
# 3/10/2022

import numpy as np # https://numpy.org/
import matplotlib.pyplot as plt  # https://matplotlib.org/

# Here is the functions for evaluating each element of the sequences
def seq_a(n):
    return (n**2-25)/(2*n**2+1)

def seq_b(n):
    return ((-1)**n)/20

def seq_c(n):
    return np.cos(n)/n

def seq_d(n):
    return np.cos(n)

def seq_e(n):
    if n<4 : 
        return n
    elif n==4 :
        return -1
    else :
        return 2
    
def seq_f(n):
    return (-1)**n/(n**2+1)

def seq_g(n):
    return np.cos(n*np.pi/6)

def seq_h(n):
    return np.sin(1/np.sqrt(n))

def seq_i(n):
    return n**2+1


# Vector allocation ***********************************************************
max_index=15
absc=np.zeros(max_index+1) # x values are stored here (= horizontal coordinate)
ord_a=np.zeros(max_index+1) # corresponding y(x) values are here (= vertical coordinate)
ord_b=np.zeros(max_index+1)
ord_c=np.zeros(max_index+1)
ord_d=np.zeros(max_index+1)
ord_e=np.zeros(max_index+1)
ord_f=np.zeros(max_index+1)
ord_g=np.zeros(max_index+1)
ord_h=np.zeros(max_index+1)
ord_i=np.zeros(max_index+1)

# Filling vectors *************************************************************
for i in range(max_index+1):
    absc[i]= i+1
    ord_a[i]=seq_a(i+1) # function value at i position
    ord_b[i]=seq_b(i+1)
    ord_c[i]=seq_c(i+1)
    ord_d[i]=seq_d(i+1)
    ord_e[i]=seq_e(i+1)
    ord_f[i]=seq_f(i+1)
    ord_g[i]=seq_g(i+1)
    ord_h[i]=seq_h(i+1)
    ord_i[i]=seq_i(i+1)
    

# graphics
plt.subplot(3, 3, 1)  # used to obtain a 3x3 array of 9 graphs and put the following at place 1
plt.plot(absc, ord_a, ".")
#plot_title="a_n=\\frac{n^2-25}{2n^2+1}" # Latex formated graphic name
#plt.title("Sequence : $%s$"%plot_title) # Put plot_title value as graph title
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$a_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 2)  # used to obtain a 3x3 array of 9 graphs and put the following at place 2
plt.plot(absc, ord_b, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$b_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 3)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_c, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$c_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 4)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_d, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$d_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 5)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_e, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$e_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 6)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_f, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$f_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 7)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_g, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$g_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 8)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_h, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$h_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

plt.subplot(3, 3, 9)  # used to obtain a 3x3 array of 9 graphs and put the following at place 3
plt.plot(absc, ord_i, ".")
plt.xlabel("n") # give a label to horizontal axis
plt.ylabel("$i_n$") # give a label to vertical axis
plt.grid(True) # Display a x,y grid if true

# Show the graphic on the screen.
plt.show()
