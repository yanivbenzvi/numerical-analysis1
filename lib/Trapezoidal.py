import numpy as np
import matplotlib.pyplot as plt


def trapezoid_integral(f, a, b, n=40000):
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
    n : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.
    '''
    if n <= 0:
        return "Number of trapez must be positive integer"
    elif n % 2 == 0:
        x = a
        h = (b - a) / n
        T = f(a) + f(b)
        print('<><><><><><><><><><><><><><><>')
        for i in range(1, n):
            x += h
            T += 2 * f(x)
            if (n > 20 and i % (int(n / 10)) == 0):
                print('The current sum of areas of trapezoids [0,{}] is: {}'.format(x, T))
                print('<><><><><><><><><><><><><><><>')
        return T * (h / 2)
    else:
        return 'n should be even positive integer'


if __name__ == '__main__':
    f = lambda x: 13 * x ** 12 - 1.25 * x ** 3
    print("The final sum of areas [{},{}] is :  {}".format(3, 12, trapezoid_integral(f, 3, 12)))

    x = np.linspace(3, 12, 30)
    y = f(x)
    plt.plot(x, y)
    for i in range(30 - 1):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
    plt.title('Trapezoid Rule, N = {}'.format(30))
    plt.show()
