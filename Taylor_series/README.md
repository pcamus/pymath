## Taylor series.

Taylor series give approximation of functions with a polynomial equation, around a value.

See [here](https://en.wikipedia.org/wiki/Taylor_series) for a description Taylor series.

We can use these polynomial to compute function with only the 4 elementary operations. But the accuracy with few terms is not very good.

See the following two examples: [taylor_sin.py](taylor_sin.py) and [taylor_sqrt.py](taylor_sqrt.py) 

Another, more powerful, algorithms exist, for instance the cordic algoritm.

*An interesting reference for high speed computation of the sine function:
https://www.embedded.com/whats-your-sine-finding-the-right-algorithm-for-digital-frequency-synthesis-on-a-dsp/*

The module sympy gives a method for symbolic expansion of Taylor series : [documentation is here](https://docs.sympy.org/latest/modules/series/series.html#more-intuitive-series-expansion).
Example : [sym_taylor.py](sym_taylor.py)
