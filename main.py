from lib import Neville
from lib.scant_method import ScantMethod
from Bisection_method import bisection
from lib.polynomialAprox_method import polynomialAproxMethod
from lib.Gauss_method import gauss
from numpy import e
import numpy as np
import math


def round_digit(x):
    return float("%.4f" % x)


def filter_negative_number(arr):
    return list(filter(lambda x: x > 0, arr))


def round_list(arr):
    return list(map(lambda x: round_digit(x), arr))


def calc_c(f):
    ## calc f root by one method ScantMethod
    print("##################### scant method print ###################")
    scant_method_result = [ScantMethod.secant(f, 0, 0.5, 100),
                           ScantMethod.secant(f, 0.6, 1.2, 100),
                           ScantMethod.secant(f, -1.5, 0, 100)]
    scant_method_result = filter_negative_number(scant_method_result)
    print("##################### end scant method print ###################")

    ## calc f root by one method bisection
    print("##################### bisection method print ###################")
    bisection_method_result = [bisection(f, 0, 0.5),
                               bisection(f, 0.6, 1.2),
                               bisection(f, -1.5, 0)]
    bisection_method_result = filter_negative_number(bisection_method_result)
    print("##################### end bisection method print ###################")
    print(scant_method_result)
    print(bisection_method_result)
    if round_list(scant_method_result) == round_list(bisection_method_result):
        print("C: the method solution result are equal.\n {0}".format(scant_method_result))
        return sum(scant_method_result) / len(scant_method_result)
    else:
        print("the result are not equal")
        exit()


def calc_k(x, y, k_const):
    k = polynomialAproxMethod.polynomialAproxMethod(x, y)
    print(k)
    return round_digit((lambda x: k[0] + k[1] * x + k[2] * (x ** 2))(k_const))


def calc_mu(f):
    ## calc f root by one method ScantMethod
    scant_method_result = [ScantMethod.secant(f, 0.2, 1, 100),
                           ScantMethod.secant(f, 1, 3, 100)]
    scant_method_result = filter_negative_number(scant_method_result)

    ## calc f root by one method bisection
    bisection_method_result = [bisection(f, 0.2, 1),
                               bisection(f, 1, 3)]
    bisection_method_result = filter_negative_number(bisection_method_result)
    print(scant_method_result)
    print(bisection_method_result)
    arr = np.array(scant_method_result)
    if round_list(scant_method_result) == round_list(bisection_method_result):
        print("MU: the method solution result are equal")
        return (arr.min() / 100)
    else:
        print("the result are not equal")
        exit()


def calc_r(i, j, h):
    if i == j:
        return h
    elif i != j:
        if (i, j) in ((1, 4), (4, 1), (2, 3), (3, 2)):
            return math.sqrt(
                h ** 2 +
                100 ** 2 + 100 ** 2
            )
        else:
            return math.sqrt(100 ** 2 + h ** 2)


def calc_d_pos(c, k, mu, i, j, h):
    r = calc_r(i, j, h)
    return c * (1 + k * h * (e ** (mu * r))) / (r ** 2)


def calc_d_mat(c, k, mu, h):
    d_mat = np.zeros(shape=(4, 4))
    for i in range(4):
        for j in range(4):
            d_mat[i][j] = calc_d_pos(c, k, mu, i + 1, j + 1, h)
            print("d_mat[{0}][{1}] = {2}".format(i, j, d_mat[i][j]))
    # d_mat[0][0] = calc_d_pos(c, k, mu, 1, 1, 200)
    return d_mat


def main():
    ## cont func varaible
    x = [1, 3, 5]
    y = [10.5, 6.1, 3.5]
    m = np.array([900, 950, 1000, 1100])
    k_const = 4.74
    h = 200
    f1 = lambda x: 16 * (x ** 3) - 16 * (x ** 2) + 1
    f2 = lambda x: x * (e ** -x) - 0.25
    ## cont func varaible

    ## calcluation
    c = calc_c(f1)
    k = calc_k(x, y, k_const)
    mu = calc_mu(f2)
    print("Equation mu element : {0}".format(mu))
    print("Equation c element : {0}".format(c))
    print("Equation k element : {0}".format(k))
    d = calc_d_mat(c, k, mu, h)

    d_inverse = np.linalg.inv(d)
    print("matrix d solution:")
    print(d)
    print("matrix d inverse solution:")
    print(d_inverse, end='\n\n\n')

    #################### c calculate 1 #######################
    print("final solution calc c = (D^-1) X M :")
    c = np.matmul(d_inverse, m)
    print(c)
    print("check result (D^-1) X D = I")
    print(np.matmul(d, d_inverse))

    #################### c calculate 2 #######################
    c = gauss(d, m, [1, 1, 1, 1], 1000)
    print("gauss method solution:")
    print(c)

    f9 = lambda x: x ** 3 - math.cos(x)
    print("----------------------Test-------------------------")

    datax = [8.1, 8.3, 8.6, 8.7]
    datay = [16.9446, 17.56492, 18.50515, 18.82091]

    print(Neville(datax, datay, 8.4))

    print("----------------------Test-------------------------")


if __name__ == "__main__":
    main()
