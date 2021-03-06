# StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,
# I tried to keep decimal places same as example
# Moved constant values to different file. I thought it would be easier to read.
import datetime
from constants import *


class Employee:
    def __init__(self, staff_id, last_name, first_name, reg_hours, hourly_rate, ot_multiple, tax_credit, standard_band):
        if (reg_hours or hourly_rate or ot_multiple or tax_credit or standard_band) < 0:
            raise ValueError("Negative value not allowed")

        self.__staff_id = staff_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__reg_hours = reg_hours
        self.__hourly_rate = hourly_rate
        self.__ot_multiple = ot_multiple
        self.__tax_credit = tax_credit
        self.__standard_band = standard_band

    def compute_payment(self, hours_worked, date):
        # validate date format
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
        except Exception as e:
            raise ValueError('Invalid date format')

        if hours_worked < 0:
            raise ValueError('Hours work must be positive')

        # if hours worked exceeding reg_hours then returning max reg_hours
        reg_hours_worked = self.__reg_hours if self.__reg_hours <= hours_worked else hours_worked
        overtime_rate = int(self.__hourly_rate * self.__ot_multiple)
        overtime_hours_worked = hours_worked - reg_hours_worked
        regular_pay = reg_hours_worked * self.__hourly_rate
        overtime_pay = int(overtime_rate * overtime_hours_worked)
        gross_pay = int(regular_pay + overtime_pay)
        # if gross pay is less than standard_band then return 0 as higher_rate_pay
        higher_rate_pay = 0 if gross_pay < self.__standard_band else gross_pay - \
            self.__standard_band
        standart_tax = int(gross_pay * STANDARD_RATE)
        higher_tax = higher_rate_pay * HIGHER_RATE
        total_tax = standart_tax + higher_tax
        prsi = gross_pay * PRSI_RATE
        # if tax_credit is greater than total_tax then return 0 as net tax because it cannot be negative
        net_tax = 0 if self.__tax_credit > total_tax else float(
            "{:.1f}".format(total_tax - self.__tax_credit))
        net_deductions = prsi + net_tax

        return {'name': f'{self.__first_name} {self.__last_name}',
                'Date': date,
                'Regular Hours Worked': reg_hours_worked,
                'Overtime Hours Worked': overtime_hours_worked,
                'Regular Rate': self.__hourly_rate,
                'Overtime Rate': overtime_rate,
                'Regular Pay': regular_pay,
                'Overtime Pay': overtime_pay,
                'Gross Pay': gross_pay,
                'Standard Rate Pay': self.__standard_band,
                'Higher Rate Pay': higher_rate_pay,
                'Standard Tax': standart_tax,
                'Higher Tax': higher_tax,
                'Total Tax': total_tax,
                'Tax Credit': self.__tax_credit,
                'Net Tax': net_tax,
                'PRSI': prsi,
                'Net Deductions': net_deductions,
                'Net Pay': float("{:.2f}".format(gross_pay - net_deductions))}
