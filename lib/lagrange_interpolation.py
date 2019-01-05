"""https://trinket.io/python/bccab55640"""
from math import *
def lagrange_interpolation(x, y, u):
    '''
    Parameters
    ----------
    x : list of floats
    y : list of floats
    u : float

    Returns
    -------
    float
        an estimate at the point u
    '''
    r = range(len(y))
    a = [y[i] / product(x[i] - x[j] for j in r if j != i) for i in r]
    return sum(a[i] * product([u - x[j] for j in r if j != i]) for i in r)


def product(a):
    p = 1
    for i in a: p *= i
    return p


if __name__ == '__main__':


    x = [1, 2.5, 4, 9.7, 7]
    y = [0.0, 0.97, 1.39, 1.70, 1.95]
    u = 6
    estim = lagrange_interpolation(x, y, u)
    exact = log(u)
    print(estim, exact)