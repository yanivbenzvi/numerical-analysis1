from lib.scant_method import ScantMethod
from lib.bisection_method import bisection
from lib.polynomialAprox_method import polynomialAproxMethod


def round_4_digit(x):
    return float("%.4f" % x)


def filter_negative_number(arr):
    return list(filter(lambda x: x > 0, arr))


def round_list(arr):
    return list(map(lambda x: round_4_digit(x), arr))


def calc_c(f):
    ## calc f root by one method ScantMethod
    scant_method_result = [ScantMethod.secant(f, 0, 0.5, 1000),
                           ScantMethod.secant(f, 0.6, 1.2, 1000),
                           ScantMethod.secant(f, -1.5, 0, 1000)]
    scant_method_result = filter_negative_number(scant_method_result)
    scant_method_result = round_list(scant_method_result)

    ## calc f root by one method ScantMethod
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


def calc_k(x, y):
    k = polynomialAproxMethod.polynomialAproxMethod(x, y)
    print(k)



def main():
    x = [1, 3, 5]
    y = [10.5, 6.1, 3.5]
    h = 200
    f = lambda x: 16 * (x ** 3) - 16 * (x ** 2) + 1
    c = calc_c(f)
    k = calc_k(x, y)
    print("Equation c element : {0}".format(c))
    print("Equation k element : {0}".format(k))


if __name__ == "__main__":
    main()
