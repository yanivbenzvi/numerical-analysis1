import unittest
from lib.vandermonde_method import *
import numpy


class MyTestCase(unittest.TestCase):
    def test_solve(self):
        n = 5
        x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)

        ref_sol = numpy.ones(n)
        V = matrix(x)
        b = numpy.dot(V, ref_sol)

        sol = solve(x, b)

        self.assertTrue(max(abs(sol - ref_sol)) < 1.0e-14)
        return

    def test_solve_transpose(self):
        n = 5
        x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)

        ref_sol = numpy.ones(n)
        V = matrix(x)
        b = numpy.dot(V.T, ref_sol)

        sol = solve_transpose(x, b)

        self.assertTrue(max(abs(sol - ref_sol)) < 1.0e-14)
        return

    def test_determinant(self):
        n = 5
        x = numpy.linspace(0.0, 1.0, n, dtype=numpy.float64)
        d = numpy.linalg.det(matrix(x))
        self.assertTrue(abs(d - det(x)) < 1.0e-14)
        return

    def test_example(self):
        n = 3
        x = numpy.array([1., 2., 4.])
        ref_sol = numpy.array([-6., 2., 12.])
        V = matrix(x)
        b = numpy.dot(numpy.linalg.inv(V), ref_sol)
        self.assertEqual(b.tolist(), numpy.array([-16., 11., -1.]).tolist())


if __name__ == '__main__':
    unittest.main()
