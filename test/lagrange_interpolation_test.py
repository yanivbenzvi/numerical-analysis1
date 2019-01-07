import unittest
from lib.Lagrange_interpolation import *
import numpy as np


class LagrangeInterpolationTestCase(unittest.TestCase):
    global x, y, u
    x = [1, 2.5, 4, 9.7, 7]
    y = [0.0, 0.97, 1.39, 1.70, 1.95]
    u = 6
    estim = lagrange_interpolation(x, y, u)
    exact = log(u)

    def test_jacob_function1(self):
        self.assertEqual(lagrange_interpolation(x, y, u), 1.770248714354829)


if __name__ == '__main__':
    unittest.main()
