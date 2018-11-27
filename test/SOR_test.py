
from __future__ import division
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
from math import sqrt
import numpy as np
import pprint
import scipy
import scipy.linalg


# Define function
def solveBySOR(A, b, omegaVal, totlVal):
    #    Actual_1 = [1.0,-1.0,3.0]
    #    Actual_2 = [1.0, 2.0, -1.0, 1.0]
    #    Actual_3 = [[3.0,4.0,-5.0]]

    Asize = np.shape(A)
    rwsize = Asize[0]
    colsize = Asize[1]

    if rwsize != colsize:
        print("A is not a square matrix")
        exit(1)

    if rwsize != b.size:
        print("Dimensions of A and b do not match")
        exit(1)

    x = np.zeros((rwsize, 1))
    x0 = np.zeros((rwsize, 1))
    nk = 0
    err = totlVal + 1.0
    maxIter = 200.0

    while err > totlVal and nk < maxIter:
        nk += 1
        for i in range(0, rwsize):
            x0[i] = x[i]
            mysum = b[i]
            oldX = x[i][0]

            for j in range(0, rwsize):
                if i != j:
                    mysum = mysum - A[i][j] * x[j][0]

            x0[i] = x[i]
            mysum = b[i]
            oldX = x[i][0]

            for j in range(0, rwsize):
                if i != j:
                    mysum = mysum - A[i][j] * x[j][0]

            mysum = mysum / A[i][i]
            x[i][0] = mysum
            x[i][0] = mysum * omegaVal + (1.0 - omegaVal) * oldX

        diff = np.subtract(x, x0)
        err = np.linalg.norm(diff) / np.linalg.norm(x)
        print(np.linalg.norm(err))

    if (nk == maxIter):
        print("Maximum number of Iterations exceeded")
    else:
        print("The solution is:")
        print(x)
        print("The number of iterations used: %d" % (nk))
        print("Relative error: %.7f" % (err))