from sympy import Symbol
from math import factorial

def chebyshev_method(f_symb,x0,n = 3,accuracy = 10**-12):
	x = Symbol('x')
	iterations = 0

	while abs(f_symb.subs(x,x0)) > accuracy:
		iterations+=1
		An = x
		y0 = f_symb.subs(x,x0)
		expr = x0
		for i in range(n-1):
			An   = An.diff()/f_symb.diff()
			expr = expr + (An.subs(x,x0)*(-y0)**(i+1))/factorial(i+1)
		x0 = expr
	print(iterations)
	return x0
