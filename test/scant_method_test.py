import unittest
from lib.scant_method import ScantMethod


class ScantMethodTest(unittest.TestCase):
    global scantObj
    scantObj = ScantMethod()

    def test_regular(self):
        def f(x):
            return x ** 2 - 20

        self.assertEqual(scantObj.secant(f, 4.5, 0.1, 20), 4.47213595499958)


if __name__ == '__main__':
    unittest.main()
