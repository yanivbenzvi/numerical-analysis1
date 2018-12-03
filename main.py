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
    scant_method_result = [ScantMethod.secant(f, 0, 0.5, 1000),
                           ScantMethod.secant(f, 0.6, 1.2, 1000),
                           ScantMethod.secant(f, -1.5, 0, 1000)]
    scant_method_result = filter_negative_number(scant_method_result)
    scant_method_result = round_list(scant_method_result)

    ## calc f root by one method bisection
    f_ = lambda x: 48 * (x ** 2) - 32 * x
    bisection_method_result = [bisection(f, 0, 0.5),
                               bisection(f, 0.6, 1.2),
                               bisection(f, -1.5, 0)]
    bisection_method_result = filter_negative_number(bisection_method_result)
    bisection_method_result = round_list(bisection_method_result)
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
    f_ = lambda x: 48 * (x ** 2) - 32 * x
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
    def calc_x1(i):
        return i * 50

    def calc_x2(j):
        return j * 50

    def calc_y1(i):
        return i * 50

    def calc_y2(j):
        return i * 50

    return (calc_x1(i) - calc_x2(j))**2 + (calc_y1(i) - calc_y2(j))**2 + h ** 2


def calc_d_pos(c, k, mu, i, j, h):
    r = calc_r(i, j, h)
    return c * (1 + k * calc_r(i, j, h) * (e ** (mu * r))) / (r ** 2)


def calc_d_mat(c, k, mu):
    d_mat = []
    d_mat[0] = [calc_d_pos(c, k, mu, 1, 1), calc_d_pos(c, k, mu, 1, 2)]
    d_mat[1] = [calc_d_pos(c, k, mu, 2, 1), calc_d_pos(c, k, mu, 2, 2)]
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
    d = calc_d_mat(c, k, mu)
    print(mu)
    print("Equation c element : {0}".format(c))
    print("Equation k element : {0}".format(k))


if __name__ == "__main__":
    main()
