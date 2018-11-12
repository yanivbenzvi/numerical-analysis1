class ScantMethod:
    def secant(self, f, a, b, n):
        '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

        Parameters
        ----------
        f : function
            The function for which we are trying to approximate a solution f(x)=0.
        a,b : numbers
            The interval in which to search for a solution. The function returns
            None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        N : (positive) integer
            The number of iterations to implement.

        Returns
        -------
        m_N : number
            The x intercept of the secant line on the the Nth interval
                m_n = a_n - f(a_n)(b_n - a_n)/(f(b_n) - f(a_n))
            The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
            for some intercept m_n then the function returns this solution.
            If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
            iterations, the secant method fails and return None.

        Examples
        --------
        #>>> f = lambda x: x**2 - x - 1
        #>>> secant(f,1,2,5)
        1.6180257510729614
        '''
        if f(a) * f(b) >= 0:
            print("Secant method fails.")
            return None
        a_n = a
        b_n = b
        for n in range(1, n + 1):
            m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
            f_m_n = f(m_n)
            if f(a_n) * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif f(b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Secant method fails.")
                return None

        return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
