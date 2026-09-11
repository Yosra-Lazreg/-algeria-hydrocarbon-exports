# Case Study 4 — Algeria Hydrocarbon Exports Dependency Dashboard

## Context

Algeria's public finances, foreign-exchange earnings, and energy-security decisions are closely connected to hydrocarbons. This project translates official Sonatrach reporting and a national export-composition indicator into an operational dashboard for Sonatrach, ministries, ONS, and policy analysts.

## Business question

How exposed is Algeria's export position to hydrocarbons, and how did the reported export volume, revenue, and product mix change over time?

## What I built

- A reproducible Streamlit dashboard
- A validated Sonatrach series for 2022–2024 export volumes and reported revenue
- Product-level export revenue breakdowns for 2022 and 2023
- A World Bank API refresh workflow for fuel exports as a share of merchandise exports, with the dashboard transparently showing that the available Algeria series currently ends in 2017
- Automated tests that reconcile product totals to Sonatrach's reported export totals

## Findings shown in the dashboard

- Sonatrach-reported hydrocarbon exports were 91.6 Mtoe in 2022, 95.0 Mtoe in 2023, and 91.4 Mtoe in 2024.
- Reported export revenue moved from DZD 8,422 billion in 2022 to DZD 6,759 billion in 2023 and DZD 6,019 billion in 2024.
- In 2023, natural gas, crude oil, LNG, refined products, LPG, and condensate made up the reported export product mix.
- The national fuel-export-share series is displayed as a complementary dependency lens, not as the same measure as Sonatrach's company reporting. The included World Bank data currently runs through 2017.

## Why it matters

The dashboard helps decision-makers monitor exposure, communicate changes transparently, and separate company-level commercial performance from national trade dependence. It is intentionally designed with source notes and caveats because official series use different scopes, units, and reporting boundaries.

## Technical implementation

Python, pandas, Plotly, Streamlit, requests, pytest, and public primary-source documents. The repository can run offline with the included processed data, or refresh the World Bank series through its public API.

## Repository

The accompanying GitHub repository contains the application, processed datasets, refresh script, tests, and documentation.
