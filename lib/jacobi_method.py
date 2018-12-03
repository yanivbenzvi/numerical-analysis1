from numpy import array, zeros, diag, diagflat, dot


class jacobi_method:
    @staticmethod
    def jacobi(a, b, n=25, x=None):#gessing a and b
        """Solves the equation Ax=b via the Jacobi iterative method."""
        # Create an initial guess if needed
        if x is None:
            x = zeros(len(a[0]))
            print (x)
        # Create a vector of the diagonal elements of A
        # and subtract them from A
        d = diag(a)
        print(d)
        r = a - diagflat(d)
        print(r)

        # Iterate for N times
        for i in range(n):
            x = (b - dot(r, x)) / d
        return x


'''https://gist.github.com/angellicacardozo/3a0891adfa38e2c4187612e57bf271d1'''
