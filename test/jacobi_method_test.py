import unittest
from lib.jacobi_method import jacobi_method
from numpy import array


class JacobiTestCase(unittest.TestCase):
    global a, b
    a = array([[2.0, 1.0], [5.0, 7.0]])
    b = array([11.0, 13.0])

    def test_jacob_function1(self):
        guess = array([1.0, 1.0])
        self.assertEqual(jacobi_method.jacobi(a, b, n=25, x=guess).tolist(), [7.111102020047106, -3.22220342490943])

    def test_jacob_function2(self):
        self.assertEqual(jacobi_method.jacobi(a, b, n=25, x=None).tolist(), [7.111104173193844, -3.2222003489855178])


if __name__ == '__main__':
    unittest.main()
