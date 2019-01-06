import numpy as np
import matplotlib.pyplot as plt


def trapz(f, a, b, N=400000):
    '''Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral [a,b]∫f(x)dx by the sum:
    (dx/2)*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])
    where dx = (b - a)/N.

    Higher N value will give better result

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.
    '''
    x = np.linspace(a, b, N + 1)  # Intervals through [a,b]
    y = f(x)
    sum = y[0] + y[len(y) - 1]  # f(x[0])+f(x[N])
    for i in range(1, len(y) - 1):
        sum += 2 * y[i]  # [k=1,N-1]Σf(x[k])
        if (i % (int(N / 10)) == 0):
            print("The current sum of areas of trapezoids 0 to {} is: {}".format(i, sum))
    dx = (b - a) / N  # Δx
    return (dx / 2) * np.sum(sum)  # Δx/2*(f(x[0])+[k=1,N-1]Σf(x[k])+f(x[N])


'''Example'''
if __name__ == '__main__':
    def f(x):
        return 13 * pow(x, 12) - 1.25 * pow(x, 3)


    print("Definite integral of f using the Trapezoid rule for [3,12]: ", trapz(f, 3, 12))

    x = np.linspace(3, 12, 20)
    y = f(x)
    plt.plot(x, y)
    for i in range(20 - 1):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
    plt.title('Trapezoid Rule, N = {}'.format(20))
    plt.show()
