import numpy as np
from scipy.linalg import solve


def gauss(A, b, x, n):
    L = np.tril(A)
    U = A - L
    count = 0
    prev = None
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        if count > 3:
            break
        if prev is None:
            prev = x
        elif np.array_equal(prev, x):
            count += 1
        prev = x
        print("count :", count)
        print(x)
    print(x)
    return x


'''___MAIN___'''
if __name__ == '__main__':
    A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
    b = [1.0, 2.0, 3.0]
    x = [1, 1, 1]

    n = 200
    print(gauss(A, b, x, n))
    print("Solution in regular: ", solve(A, b))
