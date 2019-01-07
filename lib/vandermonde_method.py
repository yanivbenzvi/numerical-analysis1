# -*- coding: utf-8 -*-
#
import numpy as np
import matplotlib.pyplot as plt


def matrix(x):
    """
            Creates a vector from the X range that he has received
            ----------
            x : array_like
                `x` Range of vector
            -------
            """
    return np.vander(x, increasing=True)


def solve_by_inverse(V):
    """
            create reverse matrix
            ----------
            v : array_like
                `v`
            -------
            """
    return np.dot(np.linalg.inv(V), ref_sol)


if __name__ == '__main__':
    f1 = lambda x: 12 * x ** 4 - x ** 3
    # x = np.array([1., 2., 4.])
    numberOfPoint = 6
    numberOfPoint *= 2
    x = np.array(list(range(1, numberOfPoint + 1, 2)))
    print("x: {}".format(x))
    # ref_sol = np.array([f1(x[0]), f1(x[1]), f1(x[2])])
    ref_sol = map(lambda x: f1(x), x)
    ref_sol = np.fromiter(ref_sol, dtype=np.float)
    print("y: {}".format(ref_sol))

    V = matrix(x)
    print("vandermonde solution of V dot x = b:", end="\n\n")
    print("[V] vandermonde Matrix :")
    print(V)
    print("[b] solution vector:")
    print(ref_sol)
    b = solve_by_inverse(V)
    print("solution x: {}".format(b.tolist()))

    text = ''
    for i in range(len(b.tolist())):
        text += "{}X^{}".format(b[i], i)
        if i != len(b.tolist()) - 1:
            text += ' + '
    print("Equation of order {}: {}".format(len(b.tolist()), text))


    def f2(b, x):
        result = 0
        for i in range(len(b.tolist())):
            result += b[i] * (x ** (i))
        return result


    t1 = np.arange(3, 8, 0.3)
    t2 = []
    t3 = []
    for i in range(len(t1)):
        t2.append(f1(i))
    for i in range(len(t1)):
        t3.append(f2(b, i))
    print("t2: {}".format(t2))

    print("t3: {}".format(t3))
    plt.plot(t1, t2, '-r', label='Original f(x)=12x^4-x^3')
    plt.plot(t1, t3, '--g', label='vandermonde cs(x)')
    plt.legend(loc='upper left')
    plt.show()
