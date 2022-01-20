from grappa import expect

from calculators.atalany_calculator import AtalanyCalculator
from constants.amounts import TWELVE_MILLION_HUF, ONE_MILLION_HUF


class TestAtalanyCalculator:

    def test_calculate_twelve_millions(self):
        atalany_calculator = AtalanyCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = atalany_calculator.calculate()
        expect(net_income).to.be.equal.to(9123600)

    def test_calculate_twelve_millions_with_a_million_cost_of_goods(self):
        atalany_calculator = AtalanyCalculator(revenue=TWELVE_MILLION_HUF, cost_of_goods=ONE_MILLION_HUF)
        net_income = atalany_calculator.calculate()
        expect(net_income).to.be.equal.to(8123600)

    def test_calculate_twenty_four_millions(self):
        atalany_calculator = AtalanyCalculator(revenue=TWELVE_MILLION_HUF*2)
        net_income = atalany_calculator.calculate()
        expect(net_income).to.be.equal.to(17689200)
