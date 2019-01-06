import numpy as np


def iterative(matrix, b, c, printList):
    result = []
    sum = 0
    count = 0
    k = 0
    flag = 0
    flag2 = 0

    for i in range(len(matrix)):
        result.append(0)
    while (flag2 == 0 and count <= 100):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                sum = sum + (matrix.item(i, j) * result[j])
            sum = sum + c[i]
            if b[i] > 0.001:
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
        printList.append(count)
        for j in result:
            printList.append(j)

    return result


def is_close(line, b, result, eps):
    sum = 0
    for i in range(line.getA().size):
        sum = sum + (result[i] * line.item(0, i))
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
                m.append(float(matrix.item(i, j)))
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
                m.append(float(matrix.item(i, j)))
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
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    U = np.matrix(result)
    return U


def PrintList(printList, size):
    for i in range(0, len(printList) - 1, size):
        print("number iteration:", printList[i])
        for j in range(1, size):
            print("x", j, ": ", printList[i + j])


def SOR(matrix, b):
    emptyL = [0 for i in b]
    flag = 0
    w = 0.05
    D = create_D(matrix)
    L = create_L(matrix)
    U = create_U(matrix)
    while flag == 0 and w <= 2:
        printList = []

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
                m.append(-D_WL.item(i, j))
            m.append(W_D.item(i, i))
            for k in range(i + 1, len(matrix)):
                m.append(-W_U.item(i, k))
            result.append(m)
        mat = np.matrix(result)

        vector = []
        for i in range(len(matrix)):
            vector.append(D.item(i, i))

        r = iterative(mat, vector, new_b, printList)
        close = True
        for i in range(len(matrix)):
            if is_close(matrix[i], b[i], r, 0.0001) == False:
                close = False

        if close == False:
            w = w + 0.05
        else:
            flag = 1
            print("SOR Method")
            print("Convergence is carried out for w = ", w)
            print("The calculate of the Vector results is running by the formula - (D+wL)Xr+1=[(1-w)D-wU]Xr+wb")
            print("The initial guess is - ", emptyL)
            print("Matrix D\n", D)
            print("Matrix L\n", L)
            print("Matrix U\n", U)
            print("Matrix D+wL\n", D_WL)
            print("Matrix (1-w)D\n", W_D)
            print("Matrix wU\n", W_U)
            print("Vector wb\n", new_b)
            print("The final Matrix\n", mat)
            PrintList(printList, len(r) + 1)
            print("The Vector results is - ")
    return r


def StrongcalcDominant(mat):
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


def calcDominant(mat, b):
    mat = np.matrix(mat)
    newOrder = list(range(len(mat)))
    found = False
    for m in range(len(mat)):
        c = []
        for n in range(m, len(mat)):
            if (abs(mat[n, m]) >= abs(np.sum(mat[n:, m]) - mat[n, m])):
                newOrder.pop(n)
                newOrder.insert(m, n)
                found = True
                break
        if not found:
            return None
        mat = mat[newOrder, :]
        for i in range(len(b)):
            c.append(b[newOrder[i]])
        b = c
        newOrder = list(range(len(mat)))
        found = False
    return mat, b


def dominant(mat, b):
    new_mat = StrongcalcDominant(mat)
    if type(new_mat) == type(None):
        new_mat = calcDominant(mat, b)
        if new_mat != None:
            return new_mat
    else:
        return new_mat, b
    return mat, b


if __name__ == "__main__":
    mat = np.matrix([[1, 3, 5], [1, 4, 2], [5, 2, 9]])
    b = [1, 2, 3]

<<<<<<< HEAD
    print(SOR(a, b))
    print(gaus(a, b))

=======
    r = dominant(mat, b)
    mat = r[0]
    b = r[1]
    print(SOR(mat, b))
>>>>>>> bf0991e5bf281cfdf75fbd8a825c7f7d04a92ce6
