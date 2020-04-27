from sympy import Symbol
from sympy.plotting import plot

def simm_f(x_arr,y_arr,a,b):
	if a == b:
		print(y_arr[a])
		return (y_arr[a])
	if b - a  == 1:	
		res = (y_arr[b] - y_arr[a])/(x_arr[b] - x_arr[a])
		return res
	else:
		res = (simm_f(x_arr,y_arr,a + 1,b) - simm_f(x_arr,y_arr,a,b - 1))/(x_arr[b] - x_arr[a])
		return res

def add_new_point_newton(inter_f,x_arr,y_arr,newpoint):
	x = Symbol('x') 
	
	x_arr.append(newpoint[0])
	y_arr.append(newpoint[1])
	
	monom = 1
	for i in range(len(x_arr)-1):
		monom *= (x - x_arr[i])

	return inter_f + simm_f(x_arr,y_arr,0,len(x_arr) - 1) * monom

def interpolation_newton(x_arr,y_arr):
	
	if len(x_arr) != len(y_arr):
		f = open('errors.txt','w')
		f.write("xlen != ylen in interpolation_newton")
		f.close()
		return 0

	polinom = 0
	x = []
	y = []
	
	for i in range(len(x_arr)):
		newpoint = (x_arr[i],y_arr[i])
		polinom = add_new_point_newton(polinom,x,y,newpoint)
		
	return polinom

