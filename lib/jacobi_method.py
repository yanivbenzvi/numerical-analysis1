from numpy import array, zeros, diag, diagflat, dot


class jacobi_method:
    @staticmethod
    def jacobi(a, b, n=25, x=None):
        """Solves the equation Ax=b via the Jacobi iterative method."""
        # Create an initial guess if needed
        if x is None:
            x = zeros(len(a[0]))

        # Create a vector of the diagonal elements of A
        # and subtract them from A
        d = diag(a)
        r = a - diagflat(d)

        # Iterate for N times
        for i in range(n):
            x = (b - dot(r, x)) / d
        return x

