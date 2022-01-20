import os

from pywebio import start_server
from pywebio.input import input, FLOAT, select, NUMBER
from pywebio.output import put_text


def ev():
    expected_revenue = input("Mennyi a várható bevételed? (évente)：", type=NUMBER)
    expected_cost_of_goods = input("Mennyi a várható költséged? (évente)：", type=NUMBER)

    put_text(f"Ennyi marad: {expected_revenue - expected_cost_of_goods}")


port = int(os.environ.get("PORT", 5000))
start_server(ev, host='0.0.0.0', port=port, debug=True)

