
class AtalanyResult:

    def __init__(self, revenue, cost_of_goods, cost_ratio, ipa, tax_free_revenue, tax_base, tb_to_pay,
                 szocho_to_pay, szja_to_pay, ipa_to_pay, net_income):
        self.revenue = revenue
        self.ipa = ipa
        self.cost_ratio = cost_ratio
        self.net_income = net_income
        self.cost_of_goods = cost_of_goods
        self.tax_free_revenue = tax_free_revenue
        self.szocho_to_pay = szocho_to_pay
        self.szja_to_pay = szja_to_pay
        self.ipa_to_pay = ipa_to_pay
        self.tb_to_pay = tb_to_pay
        self.tax_base = tax_base
