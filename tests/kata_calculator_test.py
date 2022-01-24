from grappa import expect

from calculators.kata_calculator import Kata
from constants.amounts import TWELVE_MILLION_HUF


class TestKataCalculator:

    def test_calculate_domestic_and_not_connected(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF, is_domestic=True)
        expect(kata.net_income).to.be.equal.to(11375000)

    def test_calculate_domestic_and_not_connected_twenty_four_million(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF * 2, is_domestic=True)
        expect(kata.net_income).to.be.equal.to(18575000)

    def test_calculate_domestic_and_connected(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF, is_domestic=True, is_connected=True)
        expect(kata.net_income).to.be.equal.to(11375000)

    def test_calculate_foreign_and_not_connected(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF, is_domestic=False)
        expect(kata.net_income).to.be.equal.to(8803880)

    def test_calculate_foreign_and_connected(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF, is_domestic=False, is_connected=True)
        expect(kata.net_income).to.be.equal.to(7946840)

    def test_calculate_cost_of_kata(self):
        kata = Kata(revenue=TWELVE_MILLION_HUF, cost_of_kata=75000 * 12)
        expect(kata.net_income).to.be.equal.to(8503880)

