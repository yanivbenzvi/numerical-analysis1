from numpy import array, zeros, diag, diagflat, dot

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

def jacobi(matrix, b):
    D = create_D(matrix)
    L = create_L(matrix)
    U = create_U(matrix)

    D_1 = D.I
    D_minus_1 = multi_scalar(D_1, -1)
    L_U = sum_m(L, U)
    L_U_D_1 = np.matmul(D_minus_1, L_U)
    L_D_b = np.matmul(D_1, b)

    new_b = []
    for i in range(len(b)):
        new_b.append(1.0)

    L_D_b = L_D_b.getA()[0]

    printList = []
    print("Jaccobi Method")
    print("The calculate of the Vector results is running by the formula - Xr+1=-D^-1(L+U)Xr+D^-1*b")
    r = iterative(L_U_D_1, new_b ,L_D_b, printList)
    print("Matrix D\n", D)
    print("Matrix L\n", L)
    print("Matrix U\n", U)
    print("Matrix -D^-1\n", D_minus_1)
    print("Matrix L+U\n", L_U)
    print("Matrix -D^-1*(L+U)\n", L_U_D_1)
    print("Vector D^-1*b\n", L_D_b)
    PrintList(printList, len(r) + 1)
    print("The Vector results is - ")
    return r


'''https://gist.github.com/angellicacardozo/3a0891adfa38e2c4187612e57bf271d1'''
if __name__ == '__main__':
    a = array([[2.0, 1.0], [5.0, 7.0]])
    b = array([11.0, 13.0])
    guess = array([1.0, 1.0])
    print(jacobi_method.jacobi(a, b, n=25, x=guess))