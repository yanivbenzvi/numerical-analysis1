import numpy as np


class LinearApproximation:
    @staticmethod
    def linear_approximation(x, y, x1):
        if (x == y).all():
            return None
        return np.poly1d(np.polyfit(x, y, 1))(x1)
