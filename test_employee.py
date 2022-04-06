import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def testNetLessEqualGross(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(1, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])


unittest.main(argv=['ignored'], exit=False)
