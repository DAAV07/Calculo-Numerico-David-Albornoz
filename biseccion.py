import math
def biseccion(f, a, b, Es, NI):
    Ea = 100  # Error aproximado relativo.
    I = 1  # Contador del número de iteraciones.
    M_Actual = 0  # Punto medio actual.
    M_Previa = 0  # Punto medio previo.
    while (I < NI) & (Ea > Es):

        M_Previa = M_Actual
        M_Actual = (a + b) / 2

        if (eval(f, {"x": M_Actual,"math":math})) * (eval(f, {"x": b,"math":math})) < 0:
            a = M_Actual
        else:
            b = M_Actual
        if I > 1:
            Ea = abs(((M_Actual - M_Previa) / M_Actual) * 100)

        I += 1
    print(M_Actual)
    print(Ea)
    print(I)
    c = input()
def transformExprection(f):
	f = f.replace('^','**')
	f = f.replace('sin','math.sin')
	f = f.replace('cos','math.cos')
	f = f.replace('log','math.log')
	f = f.replace('ln','math.ln')
	return f

f = input("ingrese la funcion f(x):")
f = transformExprection(f)
a = float(input("ingrese el valor del punto a:"))
b = float(input("ingrese el valor del punto b:"))
Es = float(input("ingrese el vlaor de Error:"))
NI = int(input("ingrese el numero limite de iteraciones:"))
biseccion(f, a, b, Es, NI)
