import unittest
from lib.scant_method import ScantMethod


class ScantMethodTest(unittest.TestCase):
    global scantObj
    scantObj = ScantMethod()

    def test_exponential_function1(self):
        self.assertEqual(scantObj.secant(lambda x: x ** 2 - 20, 4.5, 0.1, 20), 4.47213595499958)

    def test_exponential_function2(self):
        self.assertEqual(scantObj.secant(lambda x: x ** 2 - x - 1, 1, 2, 5), 1.6180257510729614)

    def test_exponential_function3(self):
        self.assertEqual(scantObj.secant(lambda x: (x ** 2) + 5, 1, 2, 5), None)


if __name__ == '__main__':
    unittest.main()
