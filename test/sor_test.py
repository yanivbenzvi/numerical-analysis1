import unittest
from lib.Sor_method import sor

class TestSorMethods(unittest.TestCase):

    def test_sor(self):
        m = [[4, 3.2, 0.5, 9.2], [2.2, 3, -0.3, 0.9], [-3.1, -0.2, 4, 7]]
        self.assertEqual(sor(m), [2.9999968684468152, -1.4999993766953261, 3.9999986336198514])


if __name__ == '__main__':
    unittest.main()
