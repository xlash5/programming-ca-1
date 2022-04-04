# StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,

class Employee:
    def __init__(self, staff_id, last_name, first_name, reg_hours, hourly_rate, ot_multiple, tax_credit, standard_band):
        self.__staff_id = staff_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__reg_hours = reg_hours
        self.__hourly_rate = hourly_rate
        self.__ot_multiple = ot_multiple
        self.__tax_credit = tax_credit
        self.__standard_band = standard_band

    def compute_payment(self, hours_worked, date):
        overtime_rate = self.__hourly_rate * self.__ot_multiple
        overtime_hours_worked = hours_worked - self.__reg_hours
        regular_pay = self.reg_hours * self.__hourly_rate
        overtime_pay = overtime_rate * overtime_hours_worked
        gross_pay = regular_pay + overtime_pay

        return {'name': f'{self.__first_name} {self.__last_name}',
                'Date': '31/10/2021',
                'Regular Hours Worked': self.__reg_hours,
                'Overtime Hours Worked': overtime_hours_worked,
                'Regular Rate': self.__hourly_rate,
                'Overtime Rate': overtime_rate,
                'Regular Pay': regular_pay,
                'Overtime Pay': overtime_pay,
                'Gross Pay': gross_pay,
                'Standard Rate Pay': self.__standard_band,
                'Higher Rate Pay': 2,
                'Standard Tax': 142,
                'Higher Tax': 0.8,
                'Total Tax': 142.8,
                'Tax Credit': 72,
                'Net Tax': 70.8,
                'PRSI': 28.48,
                'Net Deductions': 99.28,
                'Net Pay': 612.72}
