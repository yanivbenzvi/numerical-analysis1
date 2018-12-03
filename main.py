from lib.scant_method import ScantMethod
from lib.bisection_method import bisection
from lib.polynomialAprox_method import polynomialAproxMethod
from numpy import e
import numpy as np


def round_digit(x):
    return float("%.4f" % x)


def filter_negative_number(arr):
    return list(filter(lambda x: x > 0, arr))


def round_list(arr):
    return list(map(lambda x: round_digit(x), arr))


def calc_c(f):
    ## calc f root by one method ScantMethod
    print("##################### scant method print ###################")
    scant_method_result = [ScantMethod.secant(f, 0, 0.5, 1000),
                           ScantMethod.secant(f, 0.6, 1.2, 1000),
                           ScantMethod.secant(f, -1.5, 0, 1000)]
    scant_method_result = filter_negative_number(scant_method_result)
    scant_method_result = round_list(scant_method_result)
    print("##################### end scant method print ###################")

    ## calc f root by one method bisection
    print("##################### bisection method print ###################")
    bisection_method_result = [bisection(f, 0, 0.5),
                               bisection(f, 0.6, 1.2),
                               bisection(f, -1.5, 0)]
    bisection_method_result = filter_negative_number(bisection_method_result)
    bisection_method_result = round_list(bisection_method_result)
    print("##################### end bisection method print ###################")
    print(scant_method_result)
    print(bisection_method_result)
    if scant_method_result == bisection_method_result:
        return sum(scant_method_result) / len(scant_method_result)
    else:
        print("the result are not equal")


def calc_k(x, y, k_const):
    k = polynomialAproxMethod.polynomialAproxMethod(x, y)
    print(k)
    return round_digit((lambda x: k[0] + k[1] * x + k[2] * (x ** 2))(k_const))


def calc_mu(f):
    ## calc f root by one method ScantMethod
    scant_method_result = [ScantMethod.secant(f, 0.2, 1, 1000),
                           ScantMethod.secant(f, 1, 3, 1000)]
    scant_method_result = filter_negative_number(scant_method_result)
    scant_method_result = round_list(scant_method_result)

    ## calc f root by one method bisection
    bisection_method_result = [bisection(f, 0.2, 1),
                               bisection(f, 1, 3)]
    bisection_method_result = filter_negative_number(bisection_method_result)
    bisection_method_result = round_list(bisection_method_result)
    print(scant_method_result)
    print(bisection_method_result)
    arr = np.array(scant_method_result)
    if scant_method_result == bisection_method_result:
        return round_digit(arr.min() / 100)
    else:
        print("the result are not equal")


def calc_r(i, j, h):
    if (i == j):
        return 200 ** 2
    elif (i == 1 and j == 4):
        return 2 * (100 * 2) + h * 2
    elif (i == 4 and j == 1):
        return 2 * (100 * 2) + h * 2
    elif (i == 2 and j == 3):
        return 2 * (100 * 2) + h * 2
    elif (i == 3 and j == 2):
        return 2 * (100 * 2) + h * 2
    else:
        return 100 * 2 + h * 2


def calc_d_pos(c, k, mu, i, j, h):
    r = calc_r(i, j, h)
    return round_digit(c * (1 + k * calc_r(i, j, h) * (e ** (mu * r))) / (r ** 2))


def calc_d_mat(c, k, mu):
    d_mat = np.zeros(shape=(4, 4))
    print(calc_d_pos(c, k, mu, 1, 1, 200))
    d_mat[0][0] = calc_d_pos(c, k, mu, 1, 1, 200)
    d_mat[0][1] = calc_d_pos(c, k, mu, 1, 2, 200)
    d_mat[0][2] = calc_d_pos(c, k, mu, 1, 3, 200)
    d_mat[0][3] = calc_d_pos(c, k, mu, 1, 4, 200)

    d_mat[1][0] = calc_d_pos(c, k, mu, 2, 1, 200)
    d_mat[1][1] = calc_d_pos(c, k, mu, 2, 2, 200)
    d_mat[1][2] = calc_d_pos(c, k, mu, 2, 3, 200)
    d_mat[1][3] = calc_d_pos(c, k, mu, 2, 4, 200)

    d_mat[2][0] = calc_d_pos(c, k, mu, 3, 1, 200)
    d_mat[2][1] = calc_d_pos(c, k, mu, 3, 2, 200)
    d_mat[2][2] = calc_d_pos(c, k, mu, 3, 3, 200)
    d_mat[2][3] = calc_d_pos(c, k, mu, 3, 4, 200)

    d_mat[3][0] = calc_d_pos(c, k, mu, 4, 1, 200)
    d_mat[3][1] = calc_d_pos(c, k, mu, 4, 2, 200)
    d_mat[3][2] = calc_d_pos(c, k, mu, 4, 3, 200)
    d_mat[3][3] = calc_d_pos(c, k, mu, 4, 4, 200)
    print(d_mat)
    return d_mat


def main():
    ## cont func varaible
    x = [1, 3, 5]
    y = [10.5, 6.1, 3.5]
    k_const = 4.74
    h = 200
    f1 = lambda x: 16 * (x ** 3) - 16 * (x ** 2) + 1
    f2 = lambda x: x * (e ** -x) - 0.25
    ## cont func varaible

    ## calcluation
    c = calc_c(f1)
    k = calc_k(x, y, k_const)
    mu = calc_mu(f2)
    print(mu)
    print("Equation c element : {0}".format(c))
    print("Equation k element : {0}".format(k))
    d = calc_d_mat(c, k, mu)
    print(d)


if __name__ == "__main__":
    main()
