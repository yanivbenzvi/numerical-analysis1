import unittest
from lib.Sor_method import SOR
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_sorMethod_function1(self):
        a = np.matrix([[5, 2, 4], [3, 10, -5], [5, 2, 9]])
        b = [-7, 3, -3.5]
        self.assertEqual(SOR(a, b), [-2.522720098768155, 1.4068126714022822, 0.6999962475642652])


if __name__ == '__main__':
    unittest.main()
