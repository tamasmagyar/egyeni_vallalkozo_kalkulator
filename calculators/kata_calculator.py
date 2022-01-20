from calculators.base_calculator import BaseCalculator
from constants.amounts import TWELVE_MILLION_HUF, THREE_MILLION_HUF


class KataCalculator(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, cost_of_kata: int = 50000*12, ipa: int = 25000):
        super().__init__(revenue, cost_of_goods)
        self.cost_of_kata = cost_of_kata
        self.ipa = ipa
        self.penalty_ratio = 0.4

    def calculate(self, is_domestic: bool = False, is_connected: bool = False):
        net_income = self.revenue
        if is_domestic and not is_connected:
            if self.revenue > TWELVE_MILLION_HUF:
                net_income = (self.revenue - TWELVE_MILLION_HUF) * self.penalty_ratio
        elif not is_domestic and is_connected:
            net_income = self.revenue - (self.revenue * 0.7142 * self.penalty_ratio)
        elif not is_domestic:
            net_income = (self.revenue-(self.revenue - THREE_MILLION_HUF) * 0.7142 * self.penalty_ratio)
        return int(net_income - self.cost_of_kata - self.ipa)
