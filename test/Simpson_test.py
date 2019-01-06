import unittest
import numpy as np
from lib.Simpson import simps


class SimpsonTest(unittest.TestCase):
    def test_Simpson_Test(self):
        self.assertEqual(simps(lambda x : 3*x**2,0,1,10), 1.0)

    def test_Simpson_Test2(self):
        self.assertEqual(simps(np.sin,0,np.pi/2,100), 1.0000000003382361)

    def test_Simpson_Test3(self):
        self.assertRaises(ZeroDivisionError, simps, lambda x : x,0,0,0)

    def test_Simpson_Test4(self):
        self.assertRaises(ValueError, simps, lambda x: 3*x**2,0,1,1)


if __name__ == '__main__':
    unittest.main()
