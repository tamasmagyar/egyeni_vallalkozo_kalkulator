import logging
from abc import abstractmethod


class BaseCalculator:

    def __init__(self, revenue: int, cost_of_goods: int, name: str):
        self.cost_of_goods = cost_of_goods
        self.revenue = revenue
        self.name = name
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def calculate_net_income(self, **kwargs):
        pass
