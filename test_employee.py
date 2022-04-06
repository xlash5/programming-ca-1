import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # Net pay cannot exceed gross pay
    def testNetLessEqualGross(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(1, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    # Overtime pay cannot be negative.
    def testOvertimePayNegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(30, '31/10/2021')
        self.assertGreaterEqual(pi['Overtime Pay'], 0)

    # Overtime hours cannot be negative.
    def testOvertimeHoursNegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(30, '31/10/2021')
        self.assertGreaterEqual(pi['Overtime Hours Worked'], 0)

    # Regular Hours Worked cannot exceed hours worked
    def testRegularHoursWorked(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(50, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'],
                             pi['Regular Hours Worked'] + pi['Overtime Hours Worked'])

    # Higher Tax cannot be negative.
    def testHigherTax(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(20, '31/10/2021')
        self.assertGreaterEqual(pi['Higher Tax'], 0)

    # Net Pay cannot be negative.
    def testNetPay(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.compute_payment(10, '31/10/2021')
        self.assertGreaterEqual(pi['Net Pay'], 0)

    # Date format should be DD-MM-YYYY
    def testDateFormat(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        with self.assertRaises(ValueError):
            pi = e.compute_payment(10, '60/18/2721')


unittest.main(argv=['ignored'], exit=False)
