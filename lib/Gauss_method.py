import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        # print( str(i).zfill(3)),
        # print(x)
    return x

'''___MAIN___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]

A2 = np.array([[5.0, -1.0, 2.0], [3.0, 8.0, -2.0], [1.0, 1.0, 4.0]])
b2 = [12.0, -25.0, 6.0]
x = [1, 1, 1]

n = 20
print(gauss(A, b, x, n))
print(solve(A, b))

print(gauss(A2, b2, x, n))
print(solve(A2, b2))