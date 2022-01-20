from abc import abstractmethod


class BaseCalculator:

    def __init__(self, revenue: int, cost_of_goods: int):
        self.cost_of_goods = cost_of_goods
        self.revenue = revenue

    @abstractmethod
    def calculate(self, **kwargs):
        pass
