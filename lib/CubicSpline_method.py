from scipy import interpolate
import matplotlib.pyplot as plt
from sympy import polys, Symbol, poly
from numpy import poly1d
import numpy as np

r"""
        Return a Cubic Spline.
        Given two 1-D arrays `x` and `y` of the same length, returns the Cubic spline
        polynomials through the points ``(x, y)``.
        Warning: For every i!=j, x[i]!=x[j] and y[i]!=y[j].
        ----------
        x : array_like
            `x` represents the x-coordinates of a set of datapoints.
        y : array_like
            `y` represents the y-coordinates of a set of datapoints, i.e. f(`x`).
        Returns
        -------
        f : function 
            'f' represents the function for calculating f(x) for every x in range (x[0],x[n]).
        s : list of poly1d objects (polynomials)
            's' contains the splines(S[i](x)) for i in range(0,n)     
        """


def CubicSpline(x, y):
    def generateSplines(x, y):
        sx = interpolate.CubicSpline(x, y)
        # generating the coefficients of the bspline
        s = []
        for i in range(0, len(x) - 1):
            s.append(createPoly(x[i], [sx.c[3, i], sx.c[2, i], sx.c[1, i], sx.c[0, i]]))
            # Create polynomials for each [x[i],x[i+1]] using the bspline coefficients
        return s

    def f(x):
        return interpolate.splev(x, cs)
        # splev() to actually evaluate the spline at the desired point.

    def createPoly(w, y):
        # Create polynomials bspline coefficients
        x = Symbol('x')  # using x to represent 'x' in the expression
        pol = polys.polytools.poly_from_expr(y[0] + y[1] * (x - w) + y[2] * (x - w) ** 2 + y[3] * (x - w) ** 3)
        # Creating a Poly object using expression
        pol = poly1d(pol[0].all_coeffs())
        # Creating poly1 object from the Poly object with its coefficients
        return pol

    s = generateSplines(x, y)
    # generating splines in String form
    cs = interpolate.splrep(x, y, k=3)
    # the coefficients describing the spline (of 3rd degree) curve are computed,using splrep().
    # splrep returns an array of tuples containing the coefficients.
    return f, s  # returning the f(x) function that was calculated


if __name__ == '__main__':
    # f=12x^4-x^3
    x = [3, 6, 12, 15, 16, 16.2]
    y = [945, 15336, 247104, 604125, 782336, 822245.52]
    cs, s = CubicSpline(x, y)
    for i in range(len(s)):
        print("{0} <= x <= {1} , S{2}(x): \n{3}".format(x[i], x[i + 1], i, s[i]))


    def f(x):
        return 12 * x ** 4 - x ** 3


    t1 = np.arange(3, 16.2, 0.1)
    t2 = []
    t3 = []
    for i in range(len(t1)):
        t2.append(f(t1[i]))
        t3.append(cs(t1[i]))
    plt.plot(t1, t2, '-r', label='Original f(x)=12x^4-x^3')
    plt.plot(t1, t3, '--g', label='Cubic spline cs(x)')
    plt.legend(loc='upper left')
    plt.show()

    t1 = np.arange(3, 8, 0.3)
    t2 = []
    t3 = []
    for i in range(len(t1)):
        t2.append(f(t1[i]))
        t3.append(cs(t1[i]))
    plt.plot(t1, t2, '-r', label='Original f(x)=12x^4-x^3')
    plt.plot(t1, t3, '--g', label='Cubic spline cs(x)')
    plt.legend(loc='upper left')
    plt.show()
