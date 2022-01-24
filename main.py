import os

from pywebio import start_server
from pywebio.input import input, FLOAT, select, NUMBER, input_group, slider, radio, checkbox
from pywebio.output import put_text, put_link, toast, put_buttons, put_file, put_table, put_markdown, put_html

from calculators.atalany_calculator import Atalany
from calculators.kata_calculator import Kata
from calculators.teteles_calculator import Teteles
from results.result_printer import ResultPrinter


def ev():

    # Intro message
    # nem minden eset van lekezelve pl szja kedvezmeny, mixed belfoldi/kulfoldi partnerek, 1 partnerre funkcional
    # AFAt sem tartalmazza
    # felellossegvallas

    # todo
    put_table([
        ["Útmutató a kitöltéshez:"],
        ["1.) Közeli családtagé ahova számlázol, vagy nagy tulajdonrészed van a vállalkozásban"],
        ["2.) Nézd meg, hogy egyéni vállalkozó tevékenységének melyik típusa illik rád a NAVos linken. A bevételből levonható költséghányad oszlopban lévő százalék számra lesz szükseg a kalkulációhoz",
         put_link(
            "NAV oldala",
            url="https://nav.gov.hu/szja/tajekoztatok/kedvezo-valtozasok-2022-tol-az-egyeni-vallalkozok-atalanyadozasaban")]
    ])

    base_inputs = input_group("Egyéni Vállalkozó Kalkulátor", [
        radio("Hova számláznál?", ["belföld", "külföld"], name="to_where", value="belföld"),
        radio("Kapcsolt vállalkozás? (Kitöltési útmutató 1. pont)", ["igen", "nem"], name="connected", value="nem"),
        radio("Vállakozás típusa, költséghányad? (Kitöltési útmutató 2. pont)", ["40", "80", "90"], name="cost_ratio", value="40"),
        input("Mennyi a várható bevételed? (évente)：", type=NUMBER, name="revenue", required=True),
        input("Mennyi a várható költséged? (évente)：", type=NUMBER, name="cost_of_goods", value="0")])

    revenue = int(base_inputs["revenue"])
    is_connected = True if base_inputs["connected"] == "igen" else False
    cost_of_goods = int(base_inputs["cost_of_goods"])
    cost_ratio = int(base_inputs["cost_ratio"])
    is_domestic = True if base_inputs["to_where"] == "belföld" else False

    atalany = Atalany(revenue=revenue, cost_of_goods=cost_of_goods, cost_ratio=cost_ratio/100)
    kata = Kata(revenue=revenue, cost_of_goods=cost_of_goods, is_domestic=is_domestic, is_connected=is_connected)
    teteles = Teteles(revenue=revenue, cost_of_goods=cost_of_goods)

    res = ResultPrinter(kata, atalany, teteles)
    res.print_table()
    # todo back button
    # NFA discl

port = int(os.environ.get("PORT", 5000))
start_server(ev, host='0.0.0.0', port=port, debug=True)
