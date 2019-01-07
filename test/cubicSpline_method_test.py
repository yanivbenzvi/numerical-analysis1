import unittest
from lib.CubicSpline_method import CubicSpline


class Test(unittest.TestCase):

    def test_example(self):
        x = [3, 6, 12, 15, 16, 16.2]
        y = [945, 15336, 247104, 604125, 782336, 822245.52]
        cs = CubicSpline(x, y)
        self.assertEqual(cs, cs)


if __name__ == '__main__':
    unittest.main()
