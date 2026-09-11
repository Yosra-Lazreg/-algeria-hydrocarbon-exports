from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"

def load_data():
    exports = pd.read_csv(DATA_DIR / "sonatrach_exports.csv")
    products = pd.read_csv(DATA_DIR / "sonatrach_product_revenue.csv")
    wb = pd.read_csv(DATA_DIR / "world_bank_fuel_exports.csv")
    return exports, products, wb

def validate_core_figures(exports: pd.DataFrame):
    row_2024 = exports.loc[exports["year"].eq(2024)].iloc[0]
    assert row_2024["export_volume_mtoe"] == 91.4
    assert row_2024["export_revenue_billion_dzd"] == 6019
    assert row_2024["export_revenue_billion_usd"] == 45.0
    assert exports["year"].is_monotonic_increasing
