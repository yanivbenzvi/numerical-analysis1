import numpy as np
import matplotlib.pyplot as plt


def simps(f, a, b, N=50):
    '''Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.
    '''
    if N % 2 == 1:  # Verify that N is even, mandatory for simpson!
        raise ValueError("N must be an even integer.")
    dx = (b - a) / N
    print(f"Value of dx is {dx}")
    # Create an array x that has N+1 values which the difference between them is equal, starts at 'a' ends at 'b'
    x = np.linspace(a, b, N + 1)
    print(f"Intervals of integration: {x}")
    y = f(x)
    print("Calculating the approximation of the integral with the values above")
    S = dx / 3 * np.sum(
        y[0:-1:2] + 4 * y[1::2] + y[2::2])  # Calculate the intervals according to the formula of Simpson
    return S


if __name__ == '__main__':
    f = lambda x: 3 * x ** 2
    n = 10
    print("The total sum of the function : ", simps(f, 0, 1, n))

    x = np.linspace(0, 1, n)
    y = f(x)
    plt.plot(x, y)
    for i in range(n - 1):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
    plt.title('Simson method, N = {} (N=400,000)'.format(n))
    plt.show()
