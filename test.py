import unittest
from biseccion import *
from newton_Rapson import *
from polinomio_taylor import *

class test(unittest.TestCase):
	def test_biseccion_method(self):
		f1 = lambda x: math.exp(-x) - math.log(x)
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(biseccion(f1,1,1.5,0.05,20),1.3125)
		self.assertEqual(biseccion(f2,1,2,0.05,20),1.4375)
		self.assertEqual(biseccion(f3,0,1,0.04,20),0.578125)
	def test_newton_raphson_method(self):
		f1 = lambda x: math.exp(x) - 2*x**2
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(newton_raphson(f1,0.5,0.02,10),2.6212275327680024)
		self.assertEqual(newton_raphson(f2,1,0.05,20),1.4124215461418443)
		self.assertEqual(newton_raphson(f3,0.5,0.02,10),0.5885488916184832)
	def test_polinomio_taylor_method(self):
		f1 = lambda x: math.exp(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(test_polinomio(f1,1,0,5),2.730287258710013)
		self.assertEqual(test_polinomio(f3,1,0,3),-0.12807521949042044)
if __name__ == '__main__':
	unittest.main()