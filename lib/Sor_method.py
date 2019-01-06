import numpy as np


def iterative(matrix, b, c):
    result = []
    sum = 0
    count = 0
    k = 0
    flag = 0
    flag2 = 0

    for i in range(len(matrix)):
        result.append(0)

    while(flag2 == 0 and count <= 1000):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                sum = sum + (matrix.item(i, j)*result[j])
            sum = sum + c[i]
            if  b[i] > 0.001:
                sum = sum / b[i]
            if abs(sum - result[i]) > 0.0000001:
                flag = 1
            result[i] = sum
            sum = 0
        if flag == 0:
            flag2 = 1
        else:
            flag = 0
        count = count + 1

    return result


def is_close(line, b, result, eps):
    sum = 0
    for i in range(line.getA().size):
        sum = sum +(result[i] * line.item(0,i))
    if abs(sum - b) < eps:
        return True
    return False

def sum_m(mat1, mat2):
        result = []

        for i in range(len(mat1)):
            mylist = []
            for j in range(len(mat2)):
                mylist.append(0.0)
            result.append(mylist)

        mat = np.matrix(result)

        for i in range(len(mat1)):
            for j in range(len(mat2)):
                mat.itemset((i, j), (mat1.item(i, j) + mat2.item(i, j)))

        new_mat = np.matrix(mat)
        return new_mat

def multi_m(mat1, mat2):
    result = []

    for i in range(len(mat1)):
        mylist = []
        for j in range(len(mat1)):
            mylist.append(0.0)
        result.append(mylist)

    mat = np.matrix(result)

    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)):
                mat.itemset((i, j), (mat1.item(i, k) + mat2.item(k, j)))

    new_mat = np.matrix(mat)
    return new_mat

def multi_scalar(mat, num):
    result = []

    for i in range(len(mat)):
        mylist = []
        for j in range(len(mat)):
            mylist.append(mat.item(i, j) * num)
        result.append(mylist)

    new_mat = np.matrix(result)
    return new_mat

def create_D(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i == j:
                m.append(matrix.item(i, j))
            else:
                m.append(0.0)
        result.append(m)
    D = np.matrix(result)
    return D

def create_L(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i > j:
                m.append(matrix.item(i, j))
            else:
                m.append(0.0)
        result.append(m)
    L = np.matrix(result)
    return L

def create_U(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i < j:
                m.append(matrix.item(i, j))
            else:
                m.append(0.0)
        result.append(m)
    U = np.matrix(result)
    return U

def SOR(matrix, b):
    flag = 0
    w = 0.05
    while flag == 0 and w <= 2:
        D = create_D(matrix)
        L = create_L(matrix)
        U = create_U(matrix)

        W_L = multi_scalar(L, w)
        D_WL = sum_m(W_L, D)

        W_D = multi_scalar(D, 1 - w)

        W_U = multi_scalar(U, w)

        new_b = []
        for i in range(len(b)):
            new_b.append(b[i] * w)
        result = []

        for i in range(len(matrix)):
            m = []
            for j in range(0, i):
                m.append(-D_WL.item(i,j))
            m.append(W_D.item(i,i))
            for k in range(i + 1, len(matrix)):
                m.append(-W_U.item(i, k))
            result.append(m)
        mat = np.matrix(result)

        vector = []
        for i in range(len(matrix)):
            vector.append(D.item(i, i))

        r = iterative(mat, vector, new_b)
        close = True
        for i in range(len(matrix)):
            if is_close(matrix[i], b[i], r, 0.0001) == False:
                close = False

        if close == False:
            w = w + 0.05
        else:
            flag = 1

    return r

def gaus(matrix, b):
    D = create_D(matrix)
    L = create_L(matrix)
    U = create_U(matrix)

    L_D = sum_m(L, D)
    L_D_INVERSE = (L_D.I)
    L_D_U = np.matmul(L_D_INVERSE, U)
    L_D_b = np.matmul(L_D_INVERSE, b)
    L_D_U_1 = multi_scalar(L_D_U,-1)

    new_b = []
    for i in range(len(b)):
        new_b.append(1.0)

    L_D_b = L_D_b.getA()[0]
    r = iterative(L_D_U_1, new_b ,L_D_b)
    return r

def normMax(mat):
    '''
    :param matrixList: matrix
    :param size: Size of matrix
    :return: Max Norm
    '''
    sum = 0
    list = []

    for i in range(len(mat)):
        for j in range(len(mat.getA().item(0))):
            sum = sum + abs(mat.item(i)[j])
        list.append(sum)
        sum = 0
    return(max(list))

def calcDominant(mat):
    mat = np.matrix(mat)
    newOrder = list(range(len(mat)))
    found = False
    for n in range(len(mat)):
        for m in range(n, len(mat)):
            if (abs(mat[n, m]) > abs(np.sum(mat[n, :]) - mat[n, m])):
                newOrder.pop(m)
                newOrder.insert(n, m)
                found = True
        if not found:
            return None
        mat = mat[:, newOrder]
        newOrder = list(range(len(mat)))
        found = False
    return mat


if __name__ == '__main__':

    """norm_A = normMax(mat)
    print(norm_A)
    A_inv = mat.I
    norm_A_inv = normMax(A_inv)
    cond = norm_A * norm_A_inv
    print("cond: ", cond) """

    a = np.matrix([[5, 2, 4], [3, 10, -5], [5, 2, 9]])
    b = [-7, 3, -3.5]

    #new_mat = calcDominant(a)

    print(SOR(a, b))
    print(gaus(a, b))

