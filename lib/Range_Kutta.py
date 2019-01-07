from numpy import *
from math import *

#
# Runge-Kutta (Order Four)

# To approximate the solution of the initial-value problem y'=f(t,y), a <= t <= b, y(a) = ⍺,

# at (N+1) equally spaced numbers in the interval [a,b]:

# INPUT: Endpoints a, b; integer N; initial condition ⍺.

# OUTPUT: Approximation w to y at the (N+1) values of t.

# test command :runge_kutta(f, 0, 2 , 3 ,0.01)

f = lambda t, y: y - t ** 2 + 1


def runge_kutta(f, a, b, N, y0):
    h = (b - a) / N

    t = a;
    w = y0

    print('Initial Value (t0,y0) = ', t, ',', w)

    for i in range(1, N + 1):
        K_1 = h * f(t, w)

        K_2 = h * f(t + h / 2, w + K_1 / 2)

        K_3 = h * f(t + h / 2, w + K_2 / 2)

        K_4 = h * f(t + h, w + K_3)

        t = a + i * h

        w = w + (K_1 + 2 * K_2 + 2 * K_3 + K_4) / 6

        print('[' + str(i) + ']', 't:', t, 'w:', w)

    return t, w


if __name__ == "__main__":
    f = lambda t, y: y - t ** 2 + 1

print(runge_kutta(f, 0, 2, 3, 0.01))
