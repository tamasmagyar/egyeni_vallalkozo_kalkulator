from grappa import expect

from calculators.kata_calculator import KataCalculator
from constants.amounts import TEN_MILLION_HUF, TWELVE_MILLION_HUF


class TestKataCalculator:

    def test_calculate_domestic_and_not_connected(self):
        kata_calculator = KataCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = kata_calculator.calculate(is_domestic=True)
        expect(net_income).to.be.equal.to(11375000)

    def test_calculate_domestic_and_connected(self):
        kata_calculator = KataCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = kata_calculator.calculate(is_domestic=True, is_connected=True)
        expect(net_income).to.be.equal.to(11375000)

    def test_calculate_foreign_and_not_connected(self):
        kata_calculator = KataCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = kata_calculator.calculate(is_foreign=True)
        expect(net_income).to.be.equal.to(8803880)

    def test_calculate_foreign_and_connected(self):
        kata_calculator = KataCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = kata_calculator.calculate(is_foreign=True, is_connected=True)
        expect(net_income).to.be.equal.to(7946840)

