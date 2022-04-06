# https://github.com/xlash5/programming-ca-1
# check the link above to see repository online
from employee import Employee
import datetime

jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)

print(jg.compute_payment(2, '31/10/2021'))
