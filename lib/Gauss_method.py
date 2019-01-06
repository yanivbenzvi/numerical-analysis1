import numpy as np
from scipy.linalg import solve
"""
   The method is fairly straight forward, given a standard system of linear equations, Ax = b. Where, A is a matrix (often representing a series of equations),
   x is a vector of x variables (Gauss-Seidel method is used to solve this vector) and b is the solution vector. In Gauss-Seidel method,
   we then split the A matrix into Upper (U) and Lower (L) matrices (the lower matrix in this case also contains the diagonal), then iterate using the following method:

inputs: A - the main matrix , b - the sulotion vector, x - the unit vector, n - the number of the itaration for finding the x vector.
output: x - this is the vector we looking for in the Cross product of Ax=b with a knoun A and b.


"""

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
