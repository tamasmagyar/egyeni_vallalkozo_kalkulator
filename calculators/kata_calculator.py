from calculators.base_calculator import BaseCalculator


class KataCalculator(BaseCalculator):

    def __init__(self, revenue: int, cost_of_goods: int = 0, cost_of_kata: int = 50000, ipa: int = 25000):
        super().__init__(revenue, cost_of_goods)
        self.cost_of_kata = cost_of_kata
        self.ipa = ipa

    def calculate(self):
        pass
