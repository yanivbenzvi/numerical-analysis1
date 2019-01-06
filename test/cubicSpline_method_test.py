import unittest
import CubicSpline_method


class Test(unittest.TestCase):

    def test_param(self):
        x = [-0.5, 0.0, 0.5, 1.0, 1.5]
        y = [3.2, 2.7, 6, 5, 6.5]
        sp = CubicSpline_method.Spline(x, y)
        self.assertEqual(sp.a[0], 3.2)
        self.assertEqual(sp.a[1], 2.7)
        self.assertEqual(sp.a[2], 6.0)
        self.assertEqual(sp.a[3], 5.0)

        self.assertAlmostEqual(sp.b[0], -3.7392857142857139)
        self.assertAlmostEqual(sp.b[1], 4.4785714285714278)
        self.assertAlmostEqual(sp.b[2], 2.6249999999999991)

        self.assertAlmostEqual(sp.c[0], 0.0)
        self.assertAlmostEqual(sp.c[1], 16.435714285714283)
        self.assertAlmostEqual(sp.c[2], -20.142857142857142)
        self.assertAlmostEqual(sp.c[3], 12.535714285714285)

    def test_example(self):
        x = [1., 2., 3., 4.]
        y = [1., 0.5, 1 / 3, 0.25]
        sp = CubicSpline_method.Spline(x, y)
        self.assertEqual(sp.a[0], 1)
        self.assertEqual(sp.a[1], 0.5)
        self.assertEqual(sp.a[2], 1 / 3)
        self.assertEqual(sp.a[3], 0.25)

        self.assertAlmostEqual(sp.b[0], -3.7392857142857139)
        self.assertAlmostEqual(sp.b[1], 4.4785714285714278)
        self.assertAlmostEqual(sp.b[2], 2.6249999999999991)


if __name__ == '__main__':
    unittest.main()
