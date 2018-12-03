def NewtonRaphsonMethod(f, f_, x0, TOL=0.001, NMAX=100):#puting f anf f' tolrence,number of itration
    n=1
    while n<=NMAX:#while we didnt got to the end continue
        x1 = x0 - (f(x0)/f_(x0))#first x0 - the func(x0)/f'(x0) and put it in the next x1
        if x1 - x0 < TOL:#if it closet to the tolorence return the next result of the result
            return x1
        else: #else continue promote the x
            x0 = x1
    return False #if we couldn't find root return fail
