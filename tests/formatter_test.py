from grappa import expect

from utils.formatter import to_huf


class TestFormatter:
    def test_one_hundred(self):
        in_huf = to_huf(100)
        expect(in_huf).to.be.equal.to("100 ft")

    def test_one_thousand(self):
        in_huf = to_huf(1000)
        expect(in_huf).to.be.equal.to("1.000 ft")

    def test_one_ten_k(self):
        in_huf = to_huf(10000)
        expect(in_huf).to.be.equal.to("10.000 ft")

    def test_one_hundred_k(self):
        in_huf = to_huf(100000)
        expect(in_huf).to.be.equal.to("100.000 ft")

    def test_one_million(self):
        in_huf = to_huf(1000000)
        expect(in_huf).to.be.equal.to("1.000.000 ft")

    def test_ten_million(self):
        in_huf = to_huf(10000000)
        expect(in_huf).to.be.equal.to("10.000.000 ft")
