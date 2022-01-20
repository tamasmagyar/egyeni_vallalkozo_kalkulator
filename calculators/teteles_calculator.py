from calculators.base_calculator import BaseCalculator
from constants.amounts import MINIMUM_WORKER_WAGE, DIVIDEND_RATIO, SZJA_RATIO, SZOCHO_RATIO, \
    TWENTY_FOUR_MONTH_MIN_WAGE


class TetelesCalculator(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, base_salary: int = MINIMUM_WORKER_WAGE):
        super().__init__(revenue, cost_of_goods)
        self.base_salary = base_salary
        self.yearly_salary = base_salary * 12
        self.ipa_to_pay = int(0.01 * self.revenue)
        self.szocho_to_pay_after_yearly_salary = self.yearly_salary * SZOCHO_RATIO * 1.125
        self.max_szocho_to_pay = int((TWENTY_FOUR_MONTH_MIN_WAGE - self.yearly_salary) * SZOCHO_RATIO)

    def calculate(self):
        tax_base = self.calculate_tax_base()
        dividend_base = tax_base - int(tax_base * DIVIDEND_RATIO)
        net_income = dividend_base - int(dividend_base * SZJA_RATIO)
        net_income -= int(self.calculate_szocho_to_pay(dividend_base))
        return int(net_income + (self.yearly_salary * 0.665))

    def calculate_szocho_to_pay(self, amount: int):
        szocho_to_pay = int(amount * SZOCHO_RATIO)

        if szocho_to_pay + self.szocho_to_pay_after_yearly_salary > self.max_szocho_to_pay:
            return self.max_szocho_to_pay
        return szocho_to_pay

    def calculate_tax_base(self):
        tax_base = (self.revenue - self.ipa_to_pay - self.yearly_salary
                    - self.szocho_to_pay_after_yearly_salary - self.cost_of_goods)
        return int(tax_base)
