#! /var/bin/env python3
import unittest
from metodo_biseccion import *
from newton_Rapson import *
from polinomio_taylor import *
from integral_Rieman import *
from metodo_trapecio import *

class test(unittest.TestCase):
	def test_biseccion_method(self):
		print("\n\n==========  METODO DE BISECCIÓN  ====================================")
		f1 = lambda x: math.exp(-x) - math.log(x)
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		f4 = lambda x: (x + 1)**0.5 - math.tan(x)
		self.assertEqual(bisection_method(f1,1,1.5,0.05,20),1.3125)
		self.assertEqual(bisection_method(f2,1,2,0.05,20),1.4375)
		self.assertEqual(bisection_method(f3,0,1,0.04,20),0.578125)
		self.assertEqual(bisection_method(f4,0.5,1,0.01,20),0.9453125)
	def test_newton_raphson_method(self):
		print("\n\n==========  METODO DE NEWTHON RAPHSON  ===============================")
		f1 = lambda x: math.exp(x) - 2*x**2
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(newton_raphson(f1,0.5,0.02,10),2.6212275327680024)
		self.assertEqual(newton_raphson(f2,1,0.05,20),1.4124215461418443)
		self.assertEqual(newton_raphson(f3,0.5,0.02,10),0.5885488916184832)
	def test_polinomio_taylor_method(self):
		print("\n\n==========  POLINOMIO DE TAYLOR  =====================================")
		f1 = lambda x: math.exp(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(view_result_polinomio(f1,1,0,5),2.730287258710013)
		self.assertEqual(view_result_polinomio(f3,1,0,3),0.49251258302209866)
	def test_Rieman_method(self):
		print("\n\n==========  METODO DE RIEMAN  ========================================")
		f1 = lambda x: x / (x**2 + 1)
		f2 = lambda x: x * (x**2 + 1)**0.5
		self.assertEqual(view_result_Rieman(f1,0,1,4),0.2788235294117647)
		self.assertEqual(view_result_Rieman(f2,1,2,4),2.4116477770123668)
	def test_trapezoid_method(self):
		print("\n\n==========  METODO DEL TRAPECIO  =====================================")
		f1 = lambda x: x*math.cos(x**2)
		f2 = lambda x: math.sin(x) - x**2
		self.assertEqual(view_result_trapeze(f1,0,1,4),0.23858922110272346)
		self.assertEqual(view_result_trapeze(f2,0,1,4),0.046867405336244575)


if __name__ == '__main__':
	unittest.main()