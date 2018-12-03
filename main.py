from lib.scant_method import ScantMethod
from lib.NewtonRaphson import NewtonRaphsonMethod

def round_4_digit(x):
    return "%.4f" % x


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
    newtonRpson_method_reult = [Ne]
    print(scant_method_result)


def main():
    h = 200
    f = lambda x: 16 * (x ** 3) - 16 * (x ** 2) + 1
    calc_c(f)


if __name__ == "__main__":
    main()
