# -*- coding: utf-8 -*-
#
import numpy


def matrix(x):
    return numpy.vander(x, increasing=True)


def det(x):
    return numpy.prod([
        x[j] - x[i] for i in range(len(x)) for j in range(i+1, len(x))
        ])


def solve(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(1, n):
        x[k:n] -= x[k-1:n-1]
        x[k:n] /= alpha[k:n] - alpha[0:n-k]

    for k in range(n-1, 0, -1):
        x[k-1:n-1] -= alpha[k-1] * x[k:n]

    return x


def solve_transpose(alpha, b):
    assert len(alpha) == len(b)
    n = len(b)

    x = b.copy()

    for k in range(n):
        x[k+1:n] -= alpha[k] * x[k:n-1]

    for k in range(n-1, 0, -1):
        x[k:n] /= alpha[k:n] - alpha[:n-k]
        x[k-1:n-1] -= x[k:n]

    return x
