import sympy
from math import factorial




def chebyshev_method(f_symb,x0,n):
	x = sympy.Symbol('x')
	An = x
	expr = x0
	y0 = f_symb.subs(x,x0)

	for i in range(n-1):
		An = An.diff()/f_symb.diff()
		expr = expr + (An.subs(x,x0)*(-y0)**(i+1))/factorial(i+1)

	return expr
y = sympy.Symbol('y')
x = sympy.Symbol('x')
f= x**3 - 2.1*x**2 + 1.56*x - 0.36

inv = chebyshev_method(f,0,12)
print(f.subs(x,inv))

'''
def chebyshev_mthd(f_symb,interval,accuracy = 10**-6):
	x0 = (interval[0] + intervalp[1])/2

	finv = find_inv(f,x0,n)
'''