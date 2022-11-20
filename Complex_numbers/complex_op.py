# File complex_op.py
# Various operations with complex numbers  
# philippe.camus@hepl.be
# 2/10/2022

import numpy as np # https://numpy.org/
# List of functions : https://numpy.org/doc/stable/reference/generated/numpy.conj.html

a=1+2j
b=1-2j

print("a =", str(a), "  b =", str(b))

r1=a+b
r2=a-b
r3=a*b
r4=a/b

print()
print("a+b =", str(r1))
print("a-b =", str(r2))
print("a*b =", str(r3))
print("a/b =", str(r4))

op1=np.conj(a) # conjugate
op2=np.real(a) # real part
op3=np.imag(a) # imaginary part
op4=np.absolute(a) # absolute return absolute value for a real number, modulus for a complex number 
op5=np.angle(a, deg=True) # if deg = False return angle in radians

print()
print("conj(a) =", str(op1))
print("real(a) =", str(op2))
print("imag(a) =", str(op3))
print("absolute(a) =", str(op4))
print("angle(a) =", str(op5))


