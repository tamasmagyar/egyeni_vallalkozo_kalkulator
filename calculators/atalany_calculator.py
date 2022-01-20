from calculators.base_calculator import BaseCalculator
from constants.amounts import MIN_SZOCHO_TO_PAY, MIN_TB_TO_PAY, SZJA_RATIO, TB_RATIO, SZOCHO_RATIO


class AtalanyCalculator(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, cost_ratio: float = 0.4):
        super().__init__(revenue, cost_of_goods)
        self.tax_free_amount = 1200000
        self.ipa_to_pay = 1.2 * 0.01

        self.cost_ratio = cost_ratio

    def calculate(self):
        tax_free_revenue = int(self.revenue * self.cost_ratio)
        tax_base = self.revenue - tax_free_revenue - self.tax_free_amount
        revenue_left = tax_base
        revenue_left -= self.calculate_tb_to_pay(tax_base)
        revenue_left -= self.calculate_szocho_to_pay(tax_base)
        revenue_left -= tax_base * SZJA_RATIO
        revenue_left -= (self.revenue- tax_free_revenue) * self.ipa_to_pay
        return int(revenue_left) + tax_free_revenue + self.tax_free_amount - self.cost_of_goods

    def calculate_tb_to_pay(self, tax_base: int):
        if tax_base * TB_RATIO < MIN_TB_TO_PAY:
            return MIN_TB_TO_PAY
        return tax_base * TB_RATIO

    def calculate_szocho_to_pay(self, tax_base: int):
        if tax_base * SZOCHO_RATIO < MIN_SZOCHO_TO_PAY:
            return MIN_SZOCHO_TO_PAY
        return tax_base * SZOCHO_RATIO
