from calculators.base_calculator import BaseCalculator
from constants.amounts import TWELVE_MILLION_HUF, THREE_MILLION_HUF


class Kata(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, cost_of_kata: int = 50000 * 12, ipa: int = 25000,
                 is_domestic: bool = False, is_connected: bool = False):
        super().__init__(revenue, cost_of_goods, "KATA 2022")
        self.cost_of_kata = cost_of_kata
        self.ipa = ipa
        self.penalty_ratio = 0.4
        self.kata_penalty = 0
        self.net_income = self.calculate_net_income(is_domestic, is_connected)

    def calculate_net_income(self, is_domestic: bool, is_connected: bool):
        if is_domestic and not is_connected:
            if self.revenue > TWELVE_MILLION_HUF:
                self.kata_penalty = (self.revenue - TWELVE_MILLION_HUF) * self.penalty_ratio
        elif not is_domestic and is_connected:
            self.kata_penalty = self.revenue * 0.7142 * self.penalty_ratio
        elif not is_domestic:
            self.kata_penalty = (self.revenue - THREE_MILLION_HUF) * 0.7142 * self.penalty_ratio
        income = self.revenue - self.kata_penalty
        return int(income - self.cost_of_kata - self.ipa)
