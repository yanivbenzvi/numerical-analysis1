import unittest
import numpy as np
from NewtonRephson import NewtonRaphsonMethod1


class NewtonTest(unittest.TestCase):
    def test_Newton_Test(self):
        self.assertEqual(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,0,-5), -0.22649903505000893)

    def test_Newton_Test2(self):
        self.assertEqual(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,5,1), 0.9275641025641026)

if __name__ == '__main__':
    unittest.main()
