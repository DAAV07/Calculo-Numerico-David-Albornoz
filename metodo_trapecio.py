#! /var/bin/env python3
import math

def trapezoid_method(f,a,b,n):
	area = 0
	h = (b-a)/n
	x0 = a
	for i in range(n):
		xi = x0 + (i + 1) * h
		area+= (h/2)*(f(x0) + f(xi))
	return area

f1=lambda x: x* math.cos(x**2)

def view_result_trapeze(f,a,b,n):
    trapeze = trapezoid_method(f,a,b,n)
    print("Valor Aproximado: ",trapeze)
    print("======================================================================")
    return trapeze

if __name__ == '__main__':
    view_result_trapeze(f1,0,1,4)