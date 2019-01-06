import numpy as np
from scipy.linalg import solve
from unittest import TestCase

from lib.Gauss_method import gauss

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]


class TestNontNull(TestCase):
    def TestNontNull(self):
        self.assertIsNotNone(gauss(A, b, x, 20))


class TestIsEqual(TestCase):
    def TestIsEqual(self):
        self.assertAlmostEqual(gauss(A, b, x, 20).any(), solve(A, b).any())
