import numpy as np
from numpy.linalg import inv


class polynomialAproxMethod:
    @staticmethod
    def polynomialAproxMethod(X, Y):
        matX = np.vander(X, len(X), True)
        invMatX = inv(matX)
        res = np.dot(invMatX, Y)
        print("Polynom: ", end='')
        for i in range(len(res) - 1):
            print("{}x^{} + ".format(res[i], i), end='')
        print("{}x^{}".format(res[len(res) - 1], len(res) - 1), end='')
        return res
