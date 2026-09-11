import pandas as pd
import plotly.express as px
import streamlit as st
from src.data_checks import load_data

st.set_page_config(page_title="Algeria Hydrocarbon Exports", page_icon="🇩🇿", layout="wide")
exports, products, wb = load_data()

st.title("🇩🇿 Algeria Hydrocarbon Exports")
st.caption("Dependency dashboard for Sonatrach, ministries, ONS, and public-sector analysts")

latest = exports.sort_values("year").iloc[-1]
previous = exports.sort_values("year").iloc[-2]
volume_delta = latest.export_volume_mtoe - previous.export_volume_mtoe
revenue_delta = latest.export_revenue_billion_dzd - previous.export_revenue_billion_dzd

c1, c2, c3, c4 = st.columns(4)
c1.metric("2024 export volume", f"{latest.export_volume_mtoe:.1f} Mtoe", f"{volume_delta:+.1f} vs 2023")
c2.metric("2024 export revenue", f"DZD {latest.export_revenue_billion_dzd:,.0f} bn", f"{revenue_delta:+,.0f} bn vs 2023")
c3.metric("2024 reported USD revenue", "$45.0 bn")
wb_latest = wb.sort_values("year").iloc[-1]
c4.metric(f"{int(wb_latest.year)} fuel share of merchandise exports", f"{wb_latest.fuel_exports_pct_merchandise_exports:.1f}%")

st.subheader("Export volume and reported revenue")
fig = px.line(exports, x="year", y=["export_volume_mtoe", "export_revenue_billion_dzd"], markers=True, title="Sonatrach-reported export series")
fig.update_yaxes(title="Value", rangemode="tozero")
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Product mix by export revenue")
    selected_year = st.selectbox("Select year", sorted(products.year.unique(), reverse=True))
    mix = products[products.year.eq(selected_year)]
    fig_mix = px.bar(mix.sort_values("export_revenue_billion_dzd"), x="export_revenue_billion_dzd", y="product", orientation="h", text_auto=True, title=f"{selected_year} export revenue by product")
    fig_mix.update_xaxes(title="DZD billion")
    st.plotly_chart(fig_mix, use_container_width=True)
with right:
    st.subheader("National dependency lens")
    fig_wb = px.line(wb, x="year", y="fuel_exports_pct_merchandise_exports", markers=True, title="Fuel exports as % of merchandise exports")
    fig_wb.update_yaxes(title="Percent", range=[0, 105])
    st.plotly_chart(fig_wb, use_container_width=True)

st.info("Interpretation: Sonatrach commercial exports and the World Bank national merchandise-export share are different measures. Compare trends, not levels.")

with st.expander("Data dictionary and caveats"):
    st.markdown("""
    - **Mtoe** means million tonnes of oil equivalent.
    - Sonatrach revenue is reported in billion DZD; the 2024 annual report also provides a USD equivalent.
    - Product-level revenue is available for 2022–2023 in the Sonatrach 2023 annual report.
    - The World Bank indicator is a national macroeconomic ratio and is refreshed through the public API.
    - No causal claim is made between export dependence and any single fiscal or macroeconomic outcome.
    """)

st.download_button("Download Sonatrach export data", exports.to_csv(index=False), "sonatrach_exports.csv", "text/csv")
