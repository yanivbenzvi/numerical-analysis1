from numpy import array, zeros, diag, diagflat, dot
import numpy as np


def matrix_toFixed(numObj, digits=0):
    for i in range(numObj.shape[0]):
        for j in range(numObj.shape[1]):
            numObj[i, j] = f"{numObj[i,j]:.{digits}f}"
    return numObj


def jsum(i, A, x):
    res = 0
    for j in range(A.shape[0]):
        if i == j:
            continue
        res += A[i, j] * x[j, 0]
    return res


def jsumm(A):
    res = []
    for i in range(A.shape[0]):
        a = 0
        for j in range(A.shape[0]):
            if i == j:
                continue
            a += abs(A[i, j])
        res.append(a)
    return res


def jacobi(A, b):
    x = np.matrix(np.ones([b.shape[0], b.shape[1]]))
    x0 = np.matrix(np.zeros([b.shape[0], b.shape[1]]))
    eps = 10 ** (-4)
    for i in range(A.shape[0]):
        if abs(A[i, i]) < jsumm(A)[i]:
            raise TypeError
    while ((abs(x0 - x)).max()) >= eps:
        for i in range(A.shape[0]):
            x[i, 0] = x0[i, 0]
            x0[i, 0] = (b[i, 0] - jsum(i, A, x0)) / A[i, i]
    return x0


'''https://gist.github.com/angellicacardozo/3a0891adfa38e2c4187612e57bf271d1'''
if __name__ == '__main__':
    A = []
    B = []
    a = np.matrix(A)
    b = np.matrix(B)
    res2 = jacobi(a, b)
    print("Method Jacobi:\nx={0}\n\n".format(matrix_toFixed(res2, 4)))
