import unittest
from biseccion import *

class test(unittest.TestCase):
	def test_biseccion_method(self):
		f1 = lambda x: math.exp(-x) - math.log(x)
		f2 = lambda x: pow((x-2),2) - math.log(x)
		f3 = lambda x: math.sin(x) - math.exp(-x)
		self.assertEqual(biseccion(f1,1,1.5,0.05,20),1.3125)
		self.assertEqual(biseccion(f2,1,2,0.05,20),1.4375)
		self.assertEqual(biseccion(f3,0,1,0.04,20),0.578125)
	
if __name__ == '__main__':
	unittest.main()