"""
A Python program for the Neville's algorithm.
Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"


def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)
    m = len(datay)
    if m != n:
        return None

    p = n * [0]
    for k in range(n):
        for i in range(n - k):
            if k == 0:
                p[i] = datay[i]
            else:
<<<<<<< HEAD
                p[i] = ((x-datax[i+k])*p[i] +  \
                        (datax[i]-x)*p[i+1]) / \
                        (datax[i]-datax[i+k])
            print(p)
    return p[0]


if __name__ == "__main__":
    datax = [8.1, 8.3, 8.6, 8.7]
    datay = [16.9446, 17.56492, 18.50515, 18.82091]

    print(neville(datax, datay, 8.4))

=======
                p[i] = ((x - datax[i + k]) * p[i] + (datax[i] - x) * p[i + 1]) / (datax[i] - datax[i + k])
            print(f"P{k},{i}: {p[i]}")
    return p[0]


if __name__ == '__main__':
    print(neville([1, 2, 3, 6], [5, 9, 15, 45], 5))
>>>>>>> bf0991e5bf281cfdf75fbd8a825c7f7d04a92ce6
