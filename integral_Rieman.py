#! /var/bin/env python3
import math

def integral_Rieman(f,a,b,n):
	area = 0
	h = (b-a)/n
	for i in range(n):
		area+= f(a+i*h)*h
	return area

f1=lambda x: x / (x**2 + 1)

def view_result_Rieman(f,a,b,n):
    Rieman = integral_Rieman(f,a,b,n)
    print("Valor Aproximado: ",Rieman)
    print("======================================================================")
    return Rieman

if __name__ == '__main__':
    view_result_Rieman(f1,0,1,4)