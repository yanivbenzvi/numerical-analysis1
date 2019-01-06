import unittest
import numpy as np
from NewtonRephson import NewtonRaphsonMethod1


class NewtonTest(unittest.TestCase):
    def test_Newton_Test(self):
        self.assertEqual(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,0,-5), -0.22580298148287167)

    def test_Newton_Test2(self):
        self.assertEqual(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,5,1), 0.9273188398592842)
    def test_Newton_Test3(self):
        self.assertEqual(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,5,1), 0.92731883985928)

if __name__ == '__main__':
    unittest.main()