from unittest import TestCase
from lib.Neville import neville


class TestNevilleIsNotNull(TestCase):
    def test_neville(self):
        '''testing the function on idle condition expected is not none'''

        self.assertIsNotNone(neville([16,64,100], [0.25,0.125,0.1], 81))




class TestNevilleIsEqual(TestCase):
    '''given a function x^2+x+3 and set of values we want to get 33 when using x=5 as the value used for interpolation  '''

    def test_neville(self):
        self.assertEqual(neville([1, 2, 3, 6], [5, 9, 15, 45], 5), 33);

class TestNevilleIsNone(TestCase):
    '''testing the function on x1,x2...Xn (n x's) and Y1,Y2...Ym  n!=m expected is none'''
    def test_neville(self):
        self.assertIsNone(neville([1, 2, 3, 6], [5, 9, 15], 5));