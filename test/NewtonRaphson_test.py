import unittest
from lib.NewtonRaphson import NewtonRaphsonMethod
import math


class NewtonRaphsonTest_Equation_RootOfEquation(unittest.TestCase):
    def test_NewtonRaphson_Test(self):
        self.assertEqual(NewtonRaphsonMethod(lambda x: math.pow(x,3) - x -2,lambda x: 3*math.pow(x,2)-1,1), 1.6363636363636362)

    def test_NewtonRaphson_Test2(self):
        self.assertEqual(NewtonRaphsonMethod(lambda x: math.pow(x,3) -3 * x +2,lambda x: 3*math.pow(x,2)-3,-2.4), -2.0000000000491913)


if __name__ == '__main__':
    unittest.main()
