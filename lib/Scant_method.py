import numpy as np
import matplotlib.pyplot as plt


class ScantMethod:
    @staticmethod
    def secant(func, a, b, iterations):
        '''
        Approximate solution of f(x)=0 on interval [a,b] by the secant method.

        Parameters
        ----------
        func : function
            The function for which we are trying to approximate a solution f(x)=0.
        a,b : numbers
            The interval in which to search for a solution. The function returns
            None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        iterations : (positive) integer
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
        if func(a) * func(b) >= 0:
            print("Secant method fails.")
            return None
        x0 = a
        x1 = b
        print("the first guess : {}", format(x0))
        print("the second guess : {}", format(x1))
        for n in range(1, iterations + 1):
            m_n = x0 - func(x0) * (x1 - x0) / (func(x1) - func(x0))
            print("the value we got is: {}".format(m_n))
            f_m_n = func(m_n)
            print("current a: {0} b: {1}".format(m_n, f_m_n), end='\n\n')
            if func(x0) * f_m_n < 0:
                x0 = x0
                x1 = m_n
                print("change the valus for x1 the next itaration if the result<0")
                print(str(x1) + "new value")
            elif func(x1) * f_m_n < 0:
                x0 = m_n
                x1 = x1
                print("change the valus for x0 the next itaration if the result<0")
                print("new value: ", str(x0))
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Secant method fails.")
                return None

        return x0 - func(x0) * (x1 - x0) / (func(x1) - func(x0))


if __name__ == '__main__':
    f = lambda x: x ** 2 - 20


    def f(x):
        return x ** 2 - 20


    collection1 = [1, 2, 3, 4, 5]

    filter(lambda x: x % 2 == 0, collection1)

    ScantMethod.secant(f, 4.5, 0.1, 20)

    t1 = np.arange(-100, 100, 0.3)
    t2 = []
    for i in range(len(t1)):
        t2.append(f(i))

    plt.plot(t1, t2, '-r', label='f(x)=x^2 - 20')
    plt.legend(loc='upper left')
    plt.show()

