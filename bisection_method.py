def sgn(x):
	if x > 0
		return 1
	else:
		return -1 


def bisection(func,interval,accuracy = 10**-6)
	left  = interval[0]
	right = interval[1]
	midle = 1/2 * (left + right)
	
	if sgn(func(left)) * sgn(func(right)) > 0:
		with f in open("errors.txt","w"):
			f.write("in bisection: non similar signs error")
		return None
	
	flag = 1
	if sgn(func(left)) > 0:
		flag = -1
	

	while abs(func(midle)) > accur:
		if func(midle)*flag > 0:
			right = midle 
			midle = 1/2 * (left + right) 
		else:
			left = midle
			midle = 1/2 * (left + right)

	return midle


