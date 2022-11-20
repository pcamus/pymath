# File solve_complex.py
# Various operations with complex numbers in a symbolic way
# and equation roots finding.
# Note that imaginary vlue i (or j) is denoted by I in sympy
# philippe.camus@hepl.be
# 20/11/2022

import sympy as sp

sp.init_printing(use_unicode=False)

# Root of equation
x = sp.Symbol('x')
expr=x**2 + 1
result = sp.solve(expr, x)

print("Root of equation")
sp.pprint(expr)
sp.pprint(result)
print("---------------------------------------------------------------------")
print()

# Complex number manipulation
a = sp.Symbol('a', real=True)
b = sp.Symbol('b', real=True)
expr= a+sp.I*b

print("Real part, imaginary part, conjugate, modulus and argument of:")
sp.pprint(expr)
print()
sp.pprint(sp.re(expr))
sp.pprint(sp.im(expr))
sp.pprint(sp.conjugate(expr))
sp.pprint(sp.Abs(expr))
sp.pprint(sp.arg(expr))
print("---------------------------------------------------------------------")
print()

expr = 1+sp.I
print("Modulus and argument of:")
sp.pprint(expr)
sp.pprint(sp.Abs(expr))
sp.pprint(sp.arg(expr))
print("---------------------------------------------------------------------")
print()

#Find real and imaginary part of following expression. For which value is the imaginary part = 0 ?
a = sp.Symbol('a', real=True)
b = sp.Symbol('b', real=True)
expr = (1+a*sp.I)/(2*a-((a**2-1)*sp.I))

print(" Find real and imaginary part of following expression.")
sp.pprint(expr)
print()
print("Real part:")
sp.pprint(sp.simplify(sp.re(expr))) # real part
print()
print("Imaginary part:")
expr_sim=sp.simplify(sp.im(expr)) # imaginary part
sp.pprint(expr_sim)
print()
print("For which values of a is the expression real?")
print("Value of a:")
sp.pprint((sp.solve(expr_sim),a)) # value of a for a real value
print("---------------------------------------------------------------------")
print()

# Imaginary part ofthe following expression
expr = (2-sp.I)**8
print("Imaginary part of:") 
sp.pprint(expr)
print()
sp.pprint(sp.im(expr))
print("---------------------------------------------------------------------")
print()

# Trigonometric formulation ofthe following expression
expr = ((-3-4*sp.I)**3)/(sp.exp(sp.I*2*sp.pi/5))**7
print("Trigonometric expression of:") 
sp.pprint(expr)
print()
print("Modulus :")
sp.pprint(sp.Abs(expr))
print()
print("Argument :")
sp.pprint(sp.arg(expr))
print("---------------------------------------------------------------------")
print()

# Solve following equation in C
z=sp.Symbol('z')
x = sp.Symbol('x', real=True)
y = sp.Symbol('y', real=True)
z=x+sp.I*y
expr = z**3-(sp.I/sp.conjugate(z))
print("Solve in C space:")
sp.pprint(expr)
print()
sp.pprint(sp.solve(expr,(x,y)))
print("---------------------------------------------------------------------")
print()

# Root of equation in R and C space
x = sp.Symbol('x',real=True)
expr = x**6+64
print("Root in Real and Complex space of equation:")
sp.pprint(expr)
print()
print("In Real space:")
sp.pprint(sp.solve(expr,x))
print()
x = sp.Symbol('x')
expr = x**6+64
print("In Complex space:")
sp.pprint(sp.solve(expr,x))
print("---------------------------------------------------------------------")
print()


x = sp.Symbol('x',real=True)
expr = x**5-8*x**4+26*x**3-40*x**2+25*x
print("Root in Real and Complex space of equation:")
sp.pprint(expr)
print()
print("In Real space:")
sp.pprint(sp.solve(expr,x))

x = sp.Symbol('x')
expr = x**5-8*x**4+26*x**3-40*x**2+25*x
print("In Complex space:")
sp.pprint(sp.solve(expr,x)) # Note : we have two double roots
print("---------------------------------------------------------------------")
print()


x = sp.Symbol('x', real=True)
print("Root in Real and Complex space of equation:")
sp.pprint(expr)
print()
print("In Real space:")
expr = x**5+7*x**3-20*x**2+6*x-20
sp.pprint(sp.solve(expr,x))

x = sp.Symbol('x')
expr = x**5+7*x**3-20*x**2+6*x-20
print("In Complex space:")
sp.pprint(sp.solve(expr,x))

