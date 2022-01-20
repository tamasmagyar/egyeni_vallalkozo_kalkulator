from grappa import expect

from calculators.atalany_calculator import AtalanyCalculator
from calculators.teteles_calculator import TetelesCalculator
from constants.amounts import TWELVE_MILLION_HUF, ONE_MILLION_HUF, MINIMUM_WAGE


class TestTetelesCalculator:

    def test_calculate_tax_base(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF)
        tax_base = teteles_calculator.calculate_tax_base()
        expect(tax_base).to.be.equal.to(8303700)

    def test_calculate_tax_base_min_wage(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF, base_salary=MINIMUM_WAGE)
        tax_base = teteles_calculator.calculate_tax_base()
        expect(tax_base).to.be.equal.to(9129000)

    def test_calculate_twenty_four_millions(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF*2)
        net_income = teteles_calculator.calculate()
        expect(net_income).to.be.equal.to(17468492)

    def test_calculate_twenty_four_millions_with_two_million_costs_of_goods(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF*2, cost_of_goods=ONE_MILLION_HUF*2)
        net_income = teteles_calculator.calculate()
        expect(net_income).to.be.equal.to(15921492)

    def test_calculate_twelve_millions(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF)
        net_income = teteles_calculator.calculate()
        expect(net_income).to.be.equal.to(8279312)

    def test_calculate_twelve_millions_with_minimum_wage(self):
        teteles_calculator = TetelesCalculator(revenue=TWELVE_MILLION_HUF, base_salary=MINIMUM_WAGE)
        net_income = teteles_calculator.calculate()
        expect(net_income).to.be.equal.to(8345282)
