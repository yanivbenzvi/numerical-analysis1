import numpy as np
import matplotlib.pyplot as plt
from math import fabs


def romberIntegration(f, a, b, n=400000):
    '''Approximate the integral of f(x) from a to b using Rombergs method
        Using the Trapezoid rule and returns T(h,h/2,h/4)=T(h/2,h/4)+1/15*(T(h/2,h/4)-T(h,h/2))
        Where T(h) is the integral using the Trapezoid rule and
        T(h,h/2) is T(f,a,b,n)+1/3*(T(f,a,b,n)-T(f,a,b,2*n))
        T(h/2,h/4)=T(h/4)=1/3*(T(h/4)-T(h/2))
        h=(b-a)/N
        Higher N value will give better result

        Parameters
        ----------
        f : function
            Vectorized function of a single variable
        a , b : numbers[
            Interval of integration [a,b]
        N : integer
            Number of subintervals of [a,b]
            default is N=400,000

        Returns
        -------
        float
            Approximation of the integral of f(x) from a to b using the
            Rombergs method
    '''
    val1 = trapz(f, a, b, n * 4) + 1 / 3 * (trapz(f, a, b, n * 4) - trapz(f, a, b, n * 2))
    val2 = 1 / 15 * (val1 - trapz(f, a, b) + 1 / 3 * (trapz(f, a, b, 2 * n) - trapz(f, a, b)))
    return val2 + val1


def trapz(f, a, b, N=400000):
    x = np.linspace(a, b, N + 1)  # Intervals through [a,b]
    y = f(x)
    sum = y[0] + y[len(y) - 1]  # f(x[0])+f(x[N])
    for i in range(1, len(y) - 1):
        sum += 2 * y[i]  # [k=1,N-1]Σf(x[k])
    dx = (b - a) / N  # Δx
    return (dx / 2) * np.sum(sum)  # Δx/2*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])


if __name__ == '__main__':
    def f(x):
        return 13 * pow(x, 12) - 1.25 * pow(x, 3)


    realVal = 1.069932037782943 * pow(10, 14)
    rombergVal = romberIntegration(f, 3, 12)
    print("Definite integral of f using the Rombergs method for [3,12]: {}".format(rombergVal))
    print("Real value of the integral: {}".format(realVal))
    print("Error: {}".format(fabs(realVal - rombergVal)))

    x = np.linspace(3, 12, 20)
    y = f(x)
    plt.plot(x, y)
    for i in range(20 - 1):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
    plt.title('Romberg method, N = {} (N=400,000)'.format(20))
    plt.show()


    def g(x):
        return np.exp(x) * (1 + np.sin(x))


    print(romberIntegration(g, 0, 1))
