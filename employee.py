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
        overtime_rate = int(self.__hourly_rate * self.__ot_multiple)
        overtime_hours_worked = hours_worked - self.__reg_hours
        regular_pay = self.__reg_hours * self.__hourly_rate
        overtime_pay = int(overtime_rate * overtime_hours_worked)
        gross_pay = int(regular_pay + overtime_pay)
        higher_rate_pay = 0 if gross_pay < self.__standard_band else gross_pay - \
            self.__standard_band
        standart_tax = int("{:.0f}".format(gross_pay * 0.2))
        higher_tax = higher_rate_pay * 0.4
        total_tax = standart_tax + higher_tax
        prsi = gross_pay * 0.04
        net_tax = float("{:.1f}".format(total_tax - self.__tax_credit))
        net_deductions = prsi + net_tax

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
                'Higher Rate Pay': higher_rate_pay,
                'Standard Tax': standart_tax,
                'Higher Tax': higher_tax,
                'Total Tax': total_tax,
                'Tax Credit': self.__tax_credit,
                'Net Tax': net_tax,
                'PRSI': prsi,
                'Net Deductions': net_deductions,
                'Net Pay':  gross_pay - net_deductions}
