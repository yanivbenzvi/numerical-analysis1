from math import *

from sympy.parsing.sympy_parser import parse_expr


def NewtonRaphsonMethod1(f , f_d ,up,down, OL=0.01, NMAX=10):

    a = float(down)
    b = float(up)

    xn = a #semi-arbitrary starting point
    y = f(xn)
    derivY = f_d(xn)
    print ("xn = "),
    print (xn)
    print ("y = "),
    print (y)
    print ("derivative of y = "),
    print (derivY)

    steps = 0

    print ("\n********starting ********\n")

    while (abs(y) > 0.0000001):
        xnn = xn - (y / derivY)
        xn = xnn
        print ("new x is now at ",)
        print (xn)
        y = f(xn)
        print ("y value is now ",)
        print (y)
        derivY = f_d(xn)
        steps = steps+1
        print ("\n <><><><><><><><><><><><><><> \n")

    print ("\n********ended ********\n")

    print ("Newton's Method approximates that there is an x intercept at x = {0} ".format(xn))
    print ("{0} steps were taken.\n".format(steps))
    print ("RUN MULTIPLE TIMES WITH TARGETED RANGES TO FIND ALL INTERCEPTS.\n")
    return xn
print(NewtonRaphsonMethod1(lambda x : 16*x**3-16*x**2+1,lambda x: 48*x**2-32*x,5,1))
