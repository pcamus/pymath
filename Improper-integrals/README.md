## Improper integrals.

Welcome to the topic of improper integrals and how to use SymPy to solve them. Integrals are an essential tool in calculus, used to find areas under curves, volumes of solids, and many other applications. However, not all integrals can be solved using the standard techniques of calculus. Improper integrals arise when the function being integrated has some property that makes the integral diverge or undefined.

An improper integral is an integral that either has one or both limits of integration infinite or contains a singularity within the limits of integration. Improper integrals require a more nuanced approach to solve, and this is where SymPy comes in.

SymPy is a Python library for symbolic mathematics that provides tools for algebraic manipulations, calculus, and much more. One of its powerful features is its ability to solve integrals symbolically, including improper integrals.

In this tutorial, we will explore what an improper integral is and how to use SymPy to solve it. We will start by defining what constitutes an improper integral, including types such as Type 1 and Type 2. Then, we will dive into how to use SymPy to solve different types of improper integrals, including integrals with infinite limits and integrals with discontinuities.

Moreover, we will explore how to use various SymPy integration functions to handle different types of improper integrals, including the integrate and Integral functions. We will also look at how to use these functions to compute definite integrals and how to use the limit function to evaluate limits that may arise from solving improper integrals.

By the end of this tutorial, you will have a good understanding of what constitutes an improper integral and how to use SymPy to solve them symbolically. You will also be able to apply these techniques to solve a wide range of mathematical problems involving improper integrals.

*This introduction was made by ChatGPT* :-)

Examples:

- Computing total power radiated by a body: [int_imp_sympy_ex1.py](int_imp_sympy_ex1.py)
- Computing 1/x**n with a sum of rectangles and with the scipy module: [int_imp_1divxn.py](int_imp_1divxn.py)
- Normal distribution example (plot and area under the curve): [gauss.py](gauss.py)
- Two examples of type 2 integrals: 
  - [int_imp_type2a.py](int_imp_type2a.py) (not converging)
  - [int_imp_type2b.py](int_imp_type2b.py) (converging)

Note: scipy is a usefull module dedicated to scientific computing in Python (see: [scipy.org](https://scipy.org/))
