import unittest
from biseccion import *

class test(unittest.TestCase):
	def test_biseccion_method(self):
		self.assertEqual(biseccion("math.exp(-x) - math.log(x)",1,1.5,0.05,20),1.3125)
		#self.assertEqual(biseccion("math.sin(x) + x - 1",0.57,1,0.001,20),0.5107177734374999)
if __name__ == '__main__':
	unittest.main()