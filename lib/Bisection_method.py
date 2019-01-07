# " URL :https://github.com/TheAlgorithms/Python/blob/master/arithmetic_analysis/bisection.py"




from numpy import *
import numpy as np
import matplotlib.pyplot as plt

""" 

The method is applicable for numerically solving the equation f(x) = 0 for the real variable x, 
where f is a continuous function defined on an interval [a, b] and where f(a) and f(b) have opposite signs.
 In this case a and b are said to bracket a root since, by the intermediate value theorem, the continuous function f must have at least one root in the interval (a, b).
At each step the method divides the interval in two by computing the midpoint c = (a+b) / 2 of the interval and the value of the function f(c) at that point.
 Unless c is itself a root (which is very unlikely, but possible) there are now only two possibilities: either f(a) and f(c) have opposite signs and bracket a root, 
 or f(c) and f(b) have opposite signs and bracket a root.[5] The method selects the subinterval that is guaranteed to be a bracket as the new interval to be used in the next step. 
  In this way an interval that contains a zero of f is reduced in width by 50% at each step. The process is continued until the interval is sufficiently small.
Explicitly, if f(a) and f(c) have opposite signs, then the method sets c as the new value for b,
and if f(b) and f(c) have opposite signs then the method sets c as the new a.
 (If f(c)=0 then c may be taken as the solution and the process stops.) In both cases, the new f(a) and f(b) have opposite signs, so the method is applicable to this smaller interval.[6]


inputs: function - the function to work with for the Algorithm, a - the left side, b - the right side.
output: mid - is the root of the function.

"""
def bisection(function, a, b):  # finds where the function becomes 0 in [a,b] using bolzano
    start = a
    end = b
    print(start)
    print(end)
    if function(a) == 0:  # one of the a or b is a root for the function
        print(a)
        return a
    elif function(b) == 0:
        print(b)
        return b
    elif function(a) * function(b) > 0:  # if none of these are root and they are both positive or negative,
        # then his algorithm can't find the root
        print(str(a * b) + ">0")
        print("couldn't find root in [a,b]")
        return
    else:
        mid = (start + end) / 2
        print("this is middle status:")
        print(mid)
        while abs(start - mid) > 10 ** -7:  # until we achieve precise equals to 10^-7
            if function(mid) == 0:
                print("this is middle status:")
                print(mid)
                return mid
            elif function(mid) * function(start) < 0:  # find new middel number
                end = mid
                print("this is [a,mid=b] status:")
                print(end)
            else:
                start = mid
                print("this is [mid=a,b] status:")
                print(start)
            mid = (start + end) / 2  # finding new middel number
        return mid



if __name__ == '__main__':
    f = lambda x: (x ** 3) - 27
    bisection(f, 2, 6)

    t1 = np.arange(-30, 30, 0.5)
    t2 = []
    t3 = []
    for i in range(len(t1)):
        t2.append(f(i))
    plt.subplots()
    plt.plot(t1, t2, '-r', label='Original f(x)=x^3 - 27')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
