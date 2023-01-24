# File num_int_para.py
# Compute approximate of an integral with sum of rectangles
# Function used here is a parabola
# philippe.camus@hepl.be
# 24/01/2023

def my_function(x):
    return (x**2) 

# Integral boundaries
lower_bound=0.0
upper_bound=5.0  # correct value for the integral is 41.666666666...

n=1000000# number of rectangles
deltax=(upper_bound-lower_bound)/n

#x=lower_bound + deltax/2 # to use centered rectangle
x=lower_bound 

area=0

for i in range(n):  # rectangle to the left
    x=x+deltax 
    area=area + my_function(x)*deltax 

# for i in range(n): # rectangle to the right
#     area=area + my_function(x)*deltax
#     x=x+deltax
    

print(f"n ={n}  S ={area}")
