import os

from pywebio import start_server
from pywebio.input import input, NUMBER, input_group, radio
from pywebio.output import put_link, put_table, popup, put_buttons, close_popup, put_text
from pywebio.session import run_js, hold

from calculators.atalany_calculator import Atalany
from calculators.kata_calculator import Kata
from calculators.teteles_calculator import Teteles
from constants.texts import ATALANY_80_DESC, ATALANY_40_DESC, ATALANY_90_DESC
from results.result_printer import ResultPrinter


def ev():
    # Intro message
    # nem minden eset van lekezelve pl szja kedvezmeny, mixed belfoldi/kulfoldi partnerek, 1 partnerre funkcional
    # AFAt sem tartalmazza
    # felellossegvallas
    popup('Olvass el', [
        put_text('Az oldalon található információk nem minősülnek adótanácsadásnak, felelősséget nem vállalunk értük.'
                 'Szabadon elérhető online forrásokra alapszik, '
                 'célja az információmegosztás, vállalkozók tájékoztatása.'),
        # todo email kontakt
        put_buttons(['Rendben'], onclick=lambda _: close_popup())
    ])
    put_table([
        ["Útmutató a kitöltéshez:"],
        ["1.) Kapcsolt vállalkozás = Közeli családtagé ahova számlázol, vagy nagy tulajdonrészed van a vállalkozásban",
         put_link("Bővebben arról, hogy mitől kapcsolt egy vállalkozás",
                  "https://mkvkok.hu/a-kapcsolt-vallalkozasokrol")],
    ])

    base_inputs = input_group("Egyéni Vállalkozó Kalkulátor", [
        radio("Hova számláznál?", ["belföld", "külföld"], name="to_where", value="belföld"),
        radio("Kapcsolt vállalkozás? (Kitöltési útmutató 1. pont)", ["igen", "nem"], name="connected", value="nem"),
        radio("Melyik illik a tevékenységi körödre?",
              [ATALANY_40_DESC, ATALANY_80_DESC, ATALANY_90_DESC], name="cost_ratio", value=ATALANY_40_DESC),
        input("Mennyi a várható bevételed? (évente)：", type=NUMBER, name="revenue", required=True),
        input("Mennyi a várható költséged? (évente)：", type=NUMBER, name="cost_of_goods", value="0")])

    revenue = int(base_inputs["revenue"])
    is_connected = True if base_inputs["connected"] == "igen" else False
    cost_of_goods = int(base_inputs["cost_of_goods"])
    cost_ratio = int(base_inputs["cost_ratio"].split(" ")[0])
    is_domestic = True if base_inputs["to_where"] == "belföld" else False

    atalany = Atalany(revenue=revenue, cost_of_goods=cost_of_goods, cost_ratio=cost_ratio / 100)
    kata = Kata(revenue=revenue, cost_of_goods=cost_of_goods, is_domestic=is_domestic, is_connected=is_connected)
    teteles = Teteles(revenue=revenue, cost_of_goods=cost_of_goods)

    res = ResultPrinter(kata, atalany, teteles)
    res.print_table()
    # todo back button
    # NFA discl
    # todo email kontakt
    # put_buttons(["Új számolás indítása"], onclick=run_js("window.location.reload()"))
    # hold()
    # todo ez ujra toltes


port = int(os.environ.get("PORT", 5000))
start_server(ev, host='0.0.0.0', port=port, debug=True)
