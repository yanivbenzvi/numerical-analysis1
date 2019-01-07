import unittest
from lib.jacobi_method import jacobi, dominant
import numpy as np


class JacobiTestCase(unittest.TestCase):
    global a, b

    a = np.matrix([[1, 3, 5], [1, 4, 2], [5, 2, 9]])
    b = [1, 2, 3]
    r = dominant(a, b)
    a = r[0]
    b = r[1]

    def test_jacob_function1(self):
        guess = np.array([1.0, 1.0])
        self.assertEqual(jacobi(a, b), [0.7999999711018695, 0.39999999887340987, -0.19999999354441983])

    def test_jacob_function2(self):
        self.assertEqual(jacobi(a, b), [0.7999999711018695, 0.39999999887340987, -0.19999999354441983])


if __name__ == '__main__':
    unittest.main()
