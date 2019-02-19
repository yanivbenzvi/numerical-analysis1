from sympy import false
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

data = []


def calcError(a0, a1, yi, xi, m, flag=False):
    """
    :param a0: A0
    :param a1: A1
    :param yi: array Yi
    :param xi: array Xi
    :param m: num of point
    :return: Calculate the Error
    """
    sum = 0
    for i in range(m):
        sum = sum + ((yi[i] - (a1 * xi[i] + a0))) ** 2
        if flag == True:
            data[i].append(((yi[i] - (a1 * xi[i] + a0))) ** 2)
    return sum


def calcDi(di, flag=False):
    """
    :param di: is array Xi or Yi
    :return: sum Di
    """
    sum = 0
    for i in range(len(di)):
        sum = sum + di[i]
        if flag == True:
            data[i].append(di[i])
    return sum


def calcXiXi(xi, flag=False):
    """
    :param xi: is array Xi
    :return: sum Xi^2
    """
    sum = 0
    for i in range(len(xi)):
        sum = sum + xi[i] ** 2
        if flag == True:
            data[i].append(xi[i] ** 2)
    return sum


def calcXiYi(xi, yi, flag=False):
    """
    :param xi: array Xi
    :param yi: array Yi
    :return: sum array Xi*Yi
    """
    sum = 0
    for i in range(len(xi)):
        sum = sum + xi[i] * yi[i]
        if flag == True:
            data[i].append(xi[i] * yi[i])
    return sum


def calcA0(xi, yi, m):
    """
    :param xi: array Xi
    :param yi: array Yi
    :param m: num of point
    :return: A0
    """
    return ((calcXiXi(xi) * calcDi(yi)) - calcXiYi(xi, yi) * calcDi(xi)) / (m * calcXiXi(xi) - calcDi(xi) ** 2)


def calcA1(xi, yi, m):
    """
    :param xi: array Xi
    :param yi: array Yi
    :param m: num of point
    :return: A1
    """
    return (((m * calcXiYi(xi, yi)) - calcDi(xi) * calcDi(yi)) / ((m * calcXiXi(xi) - calcDi(xi) ** 2)))


def pxi(xi, f):
    for i in range(len(xi)):
        data[i].append(f(xi[i]))


def createDataTable(xi, yi):
    A0 = calcA0(xi, yi, m)
    A1 = calcA1(xi, yi, m)
    f = lambda x: A1 * x + A0
    Error = calcError(A0, A1, yi, xi, m)
    for i in range(len(xi)):
        data.append([])
    calcDi(xi, True)
    calcDi(yi, True)
    calcXiXi(xi, True)
    calcXiYi(xi, yi, True)
    pxi(xi, f)
    data.append(['-', '-', '-', '-', '-'])
    data.append([calcDi(xi), calcDi(yi), calcXiXi(xi), calcXiYi(xi, yi), 'Error= {0}'.format(Error)])
    return (A0, A1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


if __name__ == '__main__':
    yi = [1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13, 15.6]
    xi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = len(xi)
    b = createDataTable(xi, yi)
    print(tabulate(data
                   , headers=['Xi', 'Yi', 'Xi^2', 'XiYi', 'P(Xi) = {0}Xi - {1}'.format(b[1], b[0])], tablefmt='orgtbl'))
    plot_regression_line(np.array(xi), np.array(yi), b)
