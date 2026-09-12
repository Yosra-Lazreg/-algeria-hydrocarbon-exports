from src.data_checks import load_data, validate_core_figures

def test_core_figures():
    exports, _, _ = load_data()
    validate_core_figures(exports)

def test_product_totals_match_reported_totals():
    _, products, _ = load_data()
    totals = products.groupby("year")["export_revenue_billion_dzd"].sum().to_dict()
    assert totals[2022] == 8422
    assert totals[2023] == 6759
