# -*- coding: utf-8 -*-
#
import numpy as np
import matplotlib.pyplot as plt


def matrix(x):
    return np.vander(x, increasing=True)


def det(x):
    return np.prod([
        x[j] - x[i] for i in range(len(x)) for j in range(i + 1, len(x))
    ])


def solve(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(1, n):
        x[k:n] -= x[k - 1:n - 1]
        x[k:n] /= alpha[k:n] - alpha[0:n - k]

    for k in range(n - 1, 0, -1):
        x[k - 1:n - 1] -= alpha[k - 1] * x[k:n]

    return x


def solve_transpose(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(n):
        x[k + 1:n] -= alpha[k] * x[k:n - 1]

    for k in range(n - 1, 0, -1):
        x[k:n] /= alpha[k:n] - alpha[:n - k]
        x[k - 1:n - 1] -= x[k:n]

    return x


if __name__ == '__main__':
    f1 = lambda x: 12 * x ** 4 - x ** 3
    n = 10
    # x = np.array([1., 2., 4.])
    numberOfPoint = 6
    numberOfPoint *= 2
    x = np.array(list(range(1, numberOfPoint + 1, 2)))
    print("x: {}".format(x))
    # ref_sol = np.array([f1(x[0]), f1(x[1]), f1(x[2])])
    ref_sol = map(lambda x: f1(x), x)
    ref_sol = np.fromiter(ref_sol, dtype=np.float)

    V = matrix(x)
    print("vandermonde solution of V dot x = b:")
    print("[V] vandermonde Matrix :")
    print(V)
    print("[b] solution vector:")
    print(ref_sol)
    b = np.dot(np.linalg.inv(V), ref_sol)
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
