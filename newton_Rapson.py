#! /var/bin/env python3
import math
def derivada(f, h = 0.02):
    def _(x):
        return (f(x + h) - f(x))/h
    return _

def newton_raphson(f, x, ER, N):
    Ea=ER+1     #Error Relativo Actual
    i=1         #Numero de Iteracion
    xi=0        #Aproximacion actual
    while ( (Ea>ER) & (N>i) ):
        fd=derivada(f)
        xi = x - ( f(x) / fd(x) )
        Ea= abs( ( xi - x ) / xi)
        if(i>1):
            print(f"Iteración: {i} Aproximación: {xi : 4.4f} Error: {Ea : 4.4f}")
        else:
            print(f"Iteracion: {i} Aproximacion: {xi : 4.4f}")
        x=xi
        i+=1
    print("======================================================================")
    return xi
f1 = lambda x: math.exp(x) - ( 3 * pow(x,2))    
f2 = lambda x: math.sin(x) - math.exp(-x) 
f3 = lambda x: math.exp(-x) - math.log(x) 

if __name__ == "__main__":
    print ("El ultimo valor de Xi es: ",newton_raphson(f2, 0.5, 0.02, 10))