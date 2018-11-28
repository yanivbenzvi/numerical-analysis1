def NewtonRaphsonMethod(f, f_, x0, TOL=0.001, NMAX=100):
    n=1
    while n<=NMAX:
        x1 = x0 - (f(x0)/f_(x0))
        if x1 - x0 < TOL:
            return x1
        else:
            x0 = x1
    return False
