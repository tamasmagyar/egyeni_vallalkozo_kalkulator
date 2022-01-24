from calculators.base_calculator import BaseCalculator
from constants.amounts import MIN_SZOCHO_TO_PAY, MIN_TB_TO_PAY, SZJA_RATIO, TB_RATIO, SZOCHO_RATIO


class Atalany(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, cost_ratio: float = 0.4):
        super().__init__(revenue, cost_of_goods, "Átalányadózás")
        self.cost_ratio = cost_ratio
        self.tax_free_amount = 1200000
        self.ipa_ratio = 1.2 * 0.01

        self.revenue = revenue
        self.tax_free_revenue = int(self.revenue * self.cost_ratio)
        self.tax_base = self.revenue - self.tax_free_revenue - self.tax_free_amount

        self.tb_to_pay = self.calculate_tb_to_pay(self.tax_base)
        self.szocho_to_pay = self.calculate_szocho_to_pay(self.tax_base)
        self.szja_to_pay = self.tax_base * SZJA_RATIO
        self.ipa_to_pay = (self.revenue - self.tax_free_revenue) * self.ipa_ratio
        self.net_income = self.calculate_net_income()

    def calculate_net_income(self):
        revenue_left = self.tax_base
        for tax_to_pay in [self.tb_to_pay, self.szja_to_pay, self.szocho_to_pay, self.ipa_to_pay]:
            revenue_left -= tax_to_pay
        return int(revenue_left) + self.tax_free_revenue + self.tax_free_amount - self.cost_of_goods

    def calculate_tb_to_pay(self, tax_base: int):
        if tax_base * TB_RATIO < MIN_TB_TO_PAY:
            return MIN_TB_TO_PAY
        return tax_base * TB_RATIO

    def calculate_szocho_to_pay(self, tax_base: int):
        if tax_base * SZOCHO_RATIO < MIN_SZOCHO_TO_PAY:
            return MIN_SZOCHO_TO_PAY
        return tax_base * SZOCHO_RATIO
