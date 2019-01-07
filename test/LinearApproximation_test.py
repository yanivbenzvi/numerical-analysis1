import unittest
import numpy as np
from lib.LinearApproximation import *


class LinearApproximationTestCase(unittest.TestCase):
    global delta
    delta = 0.5

    def test_LinearApproximation_function1(self):
        x = np.array([2, -1.5])
        y = np.array([3, -0.5])
        self.assertTrue(abs(linear_approximation(x, y, 0.5) - 1.5) < 0.0005)
        self.assertTrue(abs(linear_approximation(x, y, -0.5) - 0.5) < 0.0005)
        self.assertTrue(abs(linear_approximation(x, y, 0) - 1.0) < 0.0005)

    def test_LinearApproximation_function2(self):
        x = np.array([0, -1.5])
        y = np.array([0, -1.5])
        self.assertIsNone(linear_approximation(x, y, 0.5))


if __name__ == '__main__':
    unittest.main()
