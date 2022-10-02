# File num_limit.py
# Try to find limits with a gradual approach 
# philippe.camus@hepl.be
# 8/9/2022

import numpy as np # https://numpy.org/

# Here is the function for evaluating each element of the sequence
def my_function(n):
    return (n**2-25)/(2*n**2+1) 

from_value = 100
to_value = 10000
step_value = 500

print("Limit approximation from %d to %d, step = %d"%(from_value, to_value, step_value))

for i in range (from_value,to_value,step_value):
    print ("Limit = %.10f" %my_function(i))

# display the approximate limit value and the difference between to succesive values
#for i in range (from_value + step_value,to_value,step_value):
#    print ("Limit = %.10f, delta= %G"%(my_function(i),my_function(i)-my_function(i-step_value)) )


""" Formating types.

See https://pyformat.info/ for a complete description.

%s = string
%d = default integer value
%f = default float value in fixed point notation
%n.mf = float value with n chararcters (count includes the dot) and m decimal
if n is omitted, the needed number of characters is reserved
%G = default float value in scientific notation

"""
