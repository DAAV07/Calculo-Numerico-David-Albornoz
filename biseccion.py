#! /var/bin/env python3
import math

def biseccion(f, a, b, Es, NI):
    Ea = 100  # Error aproximado relativo.
    I = 1  # Contador del número de iteraciones.
    M_Actual = 0  # Punto medio actual.
    M_Previa = 0  # Punto medio previo.
    while (I < NI) & (Ea > Es):
        M_Previa = M_Actual
        M_Actual = (a + b) / 2
        if (f(M_Actual) * f(b) < 0):
            a = M_Actual
        else:
            b = M_Actual
        if I > 1:
            Ea = math.fabs(((M_Actual - M_Previa) / M_Actual))
            print("I(",I,")\nPunto medio: ",M_Actual,"\nError: ",Ea)
        I += 1
    return M_Actual

if __name__ == '__main__':
	f = lambda x: math.exp(x) - (3* pow(x,2))
	biseccion(f, 0, 1, 0.05, 20)
	
