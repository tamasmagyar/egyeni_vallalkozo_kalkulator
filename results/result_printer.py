from pywebio.output import put_table, put_text

from calculators.atalany_calculator import Atalany
from calculators.kata_calculator import Kata
from calculators.teteles_calculator import Teteles
from constants.amounts import SZOCHO_RATIO, TB_RATIO, SZJA_RATIO, TWENTY_FOUR_MONTH_MIN_WAGE, TWELVE_MILLION_HUF
from utils.formatter import to_huf


class ResultPrinter:

    def __init__(self, kata: Kata, atalany: Atalany, teteles: Teteles):
        self.kata = kata
        self.atalany = atalany
        self.teteles = teteles
        self.colors = self.set_colors()

    def insert_formatted_value(self, value, _type = None):
        return put_text(to_huf(value)).style(f"color: {self.colors[_type]if _type else 'black'}")

    def print_table(self):
        # First row with column names
        result = [["", "KATA 2022", "Átalányadózás", "Tételes költségelszámolás"]]

        for i, row_text, kata_text, atalany_text, teteles_text in zip(range(1, 13),
          ["Bevétel", "IPA", "KATA díja", "Vállalkozói kivét", "Adóalap", "Nyereségadó", f"SZJA {SZJA_RATIO * 100}%",
           f"TBJ {TB_RATIO * 100}%", f"SZOCHO {SZOCHO_RATIO * 100}%", f"Költséghányad {self.atalany.cost_ratio * 100}%",
           "Plusz fizetendő KATA", "Költségek"],
          ["revenue", "ipa", "cost_of_kata", "", "", "", "", "", "", "", "kata_penalty", "cost_of_goods"],
          ["revenue", "ipa_to_pay", "", "", "", "", "szja_to_pay", "tb_to_pay", "szocho_to_pay", "tax_free_revenue",
           "", "cost_of_goods"],
          ["revenue", "ipa_to_pay", "", "yearly_salary", "dividend_base", "dividend_tax", "szja_to_pay", "",
           "szocho_to_pay", "", "", "cost_of_goods"]
                                                                      ):
            kata_cell = self.kata.__getattribute__(kata_text) if kata_text else "-"
            atalany_cell = self.atalany.__getattribute__(atalany_text) if atalany_text else "-"
            teteles_cell = self.teteles.__getattribute__(teteles_text) if teteles_text else "-"

            result.append([put_text(row_text),
                           self.insert_formatted_value(kata_cell),
                           self.insert_formatted_value(atalany_cell),
                           self.insert_formatted_value(teteles_cell)])

        # Insert last row of the table, net income. Color formatted
        result.append(["Nettó",
                       self.insert_formatted_value(self.kata.net_income, "k"),
                       self.insert_formatted_value(self.atalany.net_income, "a"),
                       self.insert_formatted_value(self.teteles.net_income, "t"),
                       ])
        put_table(result)

    def set_colors(self):
        """
        Default color is black
            Grey for atalany if higher than 24 million huf
            else green for the highest net_income

        'k' stand for kata
        'a' stand for atalany
        't' stand for teteles
        """
        kata_column_color = "black"
        atalany_column_color = "black"
        teteles_column_color = "black"

        if self.atalany.net_income > 2 * TWELVE_MILLION_HUF:
            atalany_column_color = "grey"
            if self.kata.net_income > self.teteles.net_income:
                kata_column_color = "green"
            else:
                teteles_column_color = "green"
        else:
            if self.kata.net_income > self.teteles.net_income and self.kata.net_income > self.atalany.net_income:
                kata_column_color = "green"
            elif self.teteles.net_income > self.kata.net_income and self.teteles.net_income > self.atalany.net_income:
                teteles_column_color = "green"
            else:
                atalany_column_color = "green"

        return {
            "k": kata_column_color,
            "a": atalany_column_color,
            "t": teteles_column_color
        }
