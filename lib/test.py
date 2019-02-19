import numpy as np
import matplotlib.pyplot as plt


def calcError(yi, xi, b):
    def f(x):
        sum = 0
        for e in range(len(b)):
            sum += b[e] * x ** e
        return sum

    segma = 0
    for m in range(len(xi)):
        segma += (yi[m] - f(xi[m])) ** 2
    return segma


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    def f(x):
        sum = 0
        for e in range(len(b)):
            sum += b[e] * x ** e
        return sum

    # function to show plot
    t1 = np.arange(0, 1.1, 0.05)
    t2 = []
    for i in range(len(t1)):
        t2.append(f(t1[i]))

    plt.plot(t1, t2, '-r')
    plt.legend(loc='upper left')
    plt.show()


def polnomialLeastSquert(x, y, n):
    mat = []
    segma = 0

    if n>len(x):
        print("polynom degree can't be above number of point m")
        exit(0)
    for i in range(0, n):
        mat.append([])
    for i in range(len(mat)):
        for r in range(n):
            segma = 0
            for m in range(len(x)):
                segma += pow(x[m], i + r)
            mat[i].append(segma)
    b = []
    for i in range(0, n):
        segma = 0
        for m in range(len(x)):
            segma += y[m] * (x[m] ** i)
        b.append(segma)
    print(np.matrix(mat))
    b = np.linalg.inv(np.matrix(mat)).dot(b)
    return b.tolist()[0]


def main():
    # observations
    x = np.array([0, 0.25, 0.50, 0.75, 1.00])
    y = np.array([1.0, 1.2840, 1.6487, 2.1170, 2.7183])
    n = 3
    # estimating coefficients
    b = polnomialLeastSquert(x, y, n)
    print('sol: {0}'.format(b))
    # plotting regression polynomial line
    plot_regression_line(x, y, b)
    print("least square polynomial Error: {0}".format(calcError(y, x, b)))


if __name__ == "__main__":
    main()
