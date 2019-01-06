import unittest
from bisection_method import bisection


class TestBisection_f1(unittest.TestCase):
    def test_bisection(self):
        def f1(x):
            return x ** 2 - 9
      #  def f1a(x):
       #     return x**6-4*(x**5)+3*(x**2)+6

        self.assertIsNotNone(bisection(f1, 2, 6))
        self.assertEqual(bisection(f1, 2, 6), 3)
        self.assertGreater(bisection(f1, 2, 6), 2.999)
        self.assertAlmostEquals(bisection(f1, -1, 6), 3)



class TestBisection_f2(unittest.TestCase):
    def test_bisection(self):
        def f2(x):
            return x ** 2

        self.assertIsNone(bisection(f2, 2, 6))


class TestBisection_f3(unittest.TestCase):
    def test_bisection(self):
        def f3(x):
            return x ** 3 - 27

        self.assertIsNotNone(bisection(f3, 0, 6))
        self.assertEqual(bisection(f3, 2, 6), 3)
        self.assertGreater(bisection(f3, 2, 6), 2.999)


if __name__ == '__main__':
    unittest.main()
