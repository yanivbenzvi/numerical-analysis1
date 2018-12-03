import unittest
from lib.Sor_method import sorMethod

class MyTestCase(unittest.TestCase):
    def test_sorMethod_function1(self):
        A = [10.0, -1.0, 2.0, 0.0]
        [-1.0, 11.0, -1.0, 3.0]
        [2.0, -1, 10.0, -1.0]
        [0.0, 3.0, -1.0, 8.0]

        b = [6.0, 25.0, -11.0, 15.0]
        self.assertEqual(sorMethod.sorMethod(A,B), False)


if __name__ == '__main__':
    unittest.main()
