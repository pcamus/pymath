### Symbolic approach.

This method uses the **`sympy`** module to do a symbolic computation of the limit. The documentation can be faound [here](https://docs.sympy.org/latest/index.html).

The [sym_lim.py](sym_lim.py) program uses the previous examples in one program : sequence $\frac{n^2-25}{2n^2+1}$ and function $e^{-a.t}.cos(2.\\pi.f.t)$.

After importing the sympy module and initializing the pretty printer, each example is made of 3 parts.

- Symbol creation. Each symbol is optionally followed by [assumptions](https://docs.sympy.org/latest/guides/assumptions.html). Assumption means a restriction on the allowed value of the symbol (real, positive...) 
  **`n = sp.Symbol('n', real=True)`**
  
- Expression contruction followed by a check by printing ind with **`pprint()`**
  **`expr1=(n**2-25)/(2*n**2+1)`**  
