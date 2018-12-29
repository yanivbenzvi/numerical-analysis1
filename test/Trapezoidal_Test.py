import unittest
import numpy as np
from Trapezoidal import trapezoid_integral


class trapezoid_integralTest(unittest.TestCase):
    def test_Sitrapezoid_Test(self):
        self.assertEqual(trapezoid_integral(lambda x: 10*x**2+3*x+2,0,1,4),6.9375)

    def test_trapezoid_Test2(self):
        self.assertEqual(trapezoid_integral(lambda x: 3*x**2+5*x+3,0,3,2),61.875)

    def test_trapezoid_Test3(self):
        self.assertEqual(trapezoid_integral(lambda x: 3*x**2+5*x+3,0,3,5),'n should be even positive integer')


if __name__== '_main_':
    unittest.main()