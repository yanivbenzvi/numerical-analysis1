from cmath import sin


def trapezoid_integral(f, a, b, n):
    if n<= 0 or n :
        return "Number of trapez must be positive integer"
    elif n % 2 == 0:
        x = a
        h = (b - a) / n
        T = f(a) + f(b)
        for i in range(1, n):
            x += h
            T += 2 * f(x)
        return T * (h / 2)
    else:
        return 'n should be even positive integer'


def composite_midpoint_integral(f, a, b, n):
    return 1


print((trapezoid_integral(lambda x: 10*x**2+3*x+2,0,1,4)))
print((trapezoid_integral(lambda x: 3*x**2+5*x+3,0,3,2)))
print((trapezoid_integral(lambda x: 3*x**2+5*x+3,0,3,-2)))