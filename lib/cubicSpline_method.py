#https://stackoverflow.com/questions/31543775/how-to-perform-cubic-spline-interpolation-in-python
import numpy as np
import scipy
from scipy import interpolate


def f(x):
    x_points = [ 0, 1, 2, 3, 4, 5]
    y_points = [12,14,22,39,58,77]

    tck = scipy.interpolate.splrep(x_points, y_points)
    return scipy.interpolate.splev(x, tck)


print(f(1.25))

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 11)
    y = np.sin(x)
    plt.scatter(x, y)

    x_new = np.linspace(0, 10, 201)
    plt.plot(x_new, f(x_new))

    plt.show()