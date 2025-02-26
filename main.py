import sys
import os

sys.path.append(os.path.abspath("src"))

from processing import load_data
from plotting import (
    plot_top_clientes_quantidade,
    plot_top_clientes_valor,
    plot_top_ref_quantidade,
    plot_top_ref_valor,
)

df = load_data()

if df is not None:
    plot_top_clientes_quantidade(df)
    plot_top_clientes_valor(df)
    plot_top_ref_quantidade(df)
    plot_top_ref_valor(df)
