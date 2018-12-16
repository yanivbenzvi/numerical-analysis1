#" URL :https://github.com/TheAlgorithms/Python/blob/master/arithmetic_analysis/bisection.py"
from numpy import *
def bisection(function, a, b):  # finds where the function becomes 0 in [a,b] using bolzano

    start = a
    end = b
    print (start)
    print(end)
    if function(a) == 0:  # one of the a or b is a root for the function
        print (a)
        return a
    elif function(b) == 0:
        print (b)
        return b
    elif function(a) * function(b) > 0:  # if none of these are root and they are both positive or negative,
        # then his algorithm can't find the root
        print(str(a*b) + ">0")
        print("couldn't find root in [a,b]")
        return
    else:
        mid = (start + end) / 2
        print("this is middle status:")
        print (mid)
        while abs(start - mid) > 10 ** -7:  # until we achieve precise equals to 10^-7
            if function(mid) == 0:
                print("this is middle status:")
                print (mid)
                return mid
            elif function(mid) * function(start) < 0: #find new middel number
                end = mid
                print("this is [a,mid=b] status:")
                print (end)
            else:
                start = mid
                print("this is [mid=a,b] status:")
                print (start)
            mid = (start + end) / 2 #finding new middel number
        return mid

