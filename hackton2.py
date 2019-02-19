import numpy as np
from lib.Scant_method import *
from lib.Bisection_method import *
from lib.Romberg_method import *
from lib.Sor_method import *
from lib.Lagrange_interpolation import *
from lib.Neville_method import *
from lib.Trapezoidal_method import *
from lib.Simpson_method import *

import matplotlib.pyplot as plt


def question1():
    print("question1 :")
    f = lambda x: np.log(x) - ((x + 1) / (x - 1))
    print("Method 1 solution: ")
    scant_method_result = [ScantMethod.secant(f, 0.2, 0.6, 10), ScantMethod.secant(f, 4, 4.8, 10)]
    print("Scant Method final result :", scant_method_result)
    print("Method 2 solution: ")
    bisection_method_result = [bisection(f, 0.2, 0.8), bisection(f, 2, 5)]
    print("bisection Method final result :", bisection_method_result)


def question2():
    f = lambda t: (2000 * np.log((140000) / (140000 - (2100 * t))) - (9.8 * t))
    print("question2 :")
    print("The final sum of areas [{},{}] is :  {}".format(8, 30, trapezoid_integral(f, 8, 30, 20000)))
    print("simpsons method :")
    n = 2000
    print("The total sum of the function : ", simps(f, 8, 30, n))


def question3():
    f = lambda x: 5 / ((x - 2) * (x + 2) * (x - 4))

    print("question3 :")
    rombergVal = romberIntegration(f, 1, 1.99999999) + romberIntegration(f, 2.00000001, 3)
    print("Romberg integral final value result :", rombergVal)


def question4():
    print("question4 :")
    m = [[5, 1, 10, 1.5],
         [10, 8, 1, -7],
         [4, 10, -5, 2]]
    print(sor(m, 1.15))


def question5():
    print("question5 :")
    x = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    y = [13.7241, 13.9776, 14.0625, 13.9776, 13.7241, 13.3056, 12.7281]
    u = 0.65
    print("Neville_method: ", neville(x, y, u))


def question6():
    print("question2 :")
    x = [65, 67, 70, 80]
    y = [2.14451, 2.35585, 2.74748, 5.67127]
    u = 69
    print("Neville_method: ", neville(x, y, u))
    estim = lagrange_interpolation(x, y, u)
    print("lagrange_interpolation: ", estim)


if __name__ == '__main__':
    # question1()
    # question2()
    # question3()
    question4()
# question5()
# question6()
