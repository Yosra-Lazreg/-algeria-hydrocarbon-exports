# Algeria Hydrocarbon Exports — Dependency Dashboard

A reproducible, decision-oriented dashboard for monitoring Algeria's dependence on hydrocarbon exports. The project is relevant to Sonatrach, ministries, ONS, and public-sector analysts.

## What this repository delivers

- Official Sonatrach export volumes and export revenue for 2022–2024
- Product-level export revenue for 2022–2023 from Sonatrach annual reports
- A World Bank API refresh path for Algeria's fuel-export share of merchandise exports. The current API response available to this project ends in 2017, so the dashboard does not invent post-2017 values.
- Streamlit dashboard with KPI cards, trend charts, product mix, and data caveats
- Validation tests for the core published figures and dashboard inputs

## Key validated facts

- Sonatrach reports hydrocarbon exports of 91.4 million tonnes of oil equivalent in 2024, compared with 95.0 in 2023 and 91.6 in 2022.
- Sonatrach reports 2024 export revenue of DZD 6,019 billion, equivalent to USD 45 billion.
- The 2024 annual report reports hydrocarbon exports of DZD 6,019 billion in 2024 and DZD 6,759 billion in 2023. The 2023 annual report product table reconciles to DZD 8,422 billion in 2022 and DZD 6,759 billion in 2023.

These are company-reported figures and are not a complete national balance-of-payments series. The dashboard labels them accordingly.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The dashboard runs offline using the included processed data. To refresh the World Bank series from the public API:

```bash
python -m src.refresh_data
```

## Repository structure

```text
app.py                         Streamlit dashboard
src/refresh_data.py            Public API refresh script
src/data_checks.py             Validation and data loading helpers
data/processed/*.csv          Dashboard-ready data
tests/test_data_checks.py      Automated checks
```

## Sources

- Sonatrach Annual Report 2024 — https://sonatrach.com/wp-content/uploads/2025/12/ANNUAL-REPORT-2024.pdf
- Sonatrach Annual Report 2023 — https://sonatrach.com/wp-content/uploads/2025/01/Rapport_Annuel_2023-30M.pdf
- Sonatrach reports page — https://sonatrach.com/en/pdf-category/rapports-en/
- World Bank indicator TX.VAL.FUEL.ZS.UN — https://data.worldbank.org/indicator/TX.VAL.FUEL.ZS.UN
- World Bank API — https://api.worldbank.org/v2/country/DZA/indicator/TX.VAL.FUEL.ZS.UN?format=json&per_page=100
- EIA Algeria country analysis — https://www.eia.gov/international/content/analysis/countries_long/Algeria/

## Important interpretation note

The Sonatrach series is a company-reported commercial export series in tonnes of oil equivalent and DZD/USD revenue. The World Bank series is a national merchandise-export composition indicator sourced from UN Comtrade and currently available in the API through 2017 for Algeria. They should not be added together or treated as identical measures. The dashboard presents them as complementary lenses.
