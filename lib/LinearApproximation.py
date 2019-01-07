import numpy as np

def linear_approximation(x, y, x1):
    if (x == y).all():
        return None
    return np.poly1d(np.polyfit(x, y, 1))(x1)


'''https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html'''

if __name__ == '__main__':
    x = np.array([2, -1.5])
    y = np.array([3, -0.5])
    print(linear_approximation(x, y, 0.5))