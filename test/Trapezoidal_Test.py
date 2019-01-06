import unittest
import numpy as np
from Trapezoidal_method import trapezoid_integral


class trapezoid_integralTest(unittest.TestCase):
    def test_Sitrapezoid_Test(self):
        f = lambda x: 10 * x ** 2 + 3 * x + 2
        self.assertEqual(trapezoid_integral(f, 0, 1, 4), 6.9375)

    def test_trapezoid_Test2(self):
        f = lambda x: 3 * x ** 2 + 5 * x + 3
        self.assertEqual(trapezoid_integral(f, 0, 3, 2), 61.875)

    def test_trapezoid_Test3(self):
        f = lambda x: 3 * x ** 2 + 5 * x + 3
        self.assertEqual(trapezoid_integral(f, 0, 3, 5),
                         'n should be even positive integer')


if __name__ == '_main_':
    unittest.main()
