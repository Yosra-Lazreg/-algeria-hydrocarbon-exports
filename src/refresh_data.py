from pathlib import Path
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed" / "world_bank_fuel_exports.csv"
URL = "https://api.worldbank.org/v2/country/DZA/indicator/TX.VAL.FUEL.ZS.UN?format=json&per_page=100"

def main():
    payload = requests.get(URL, timeout=30).json()
    rows = payload[1]
    records = []
    for row in rows:
        if row.get("value") is not None:
            records.append({
                "year": int(row["date"]),
                "fuel_exports_pct_merchandise_exports": float(row["value"]),
                "source_note": "World Bank API refresh"
            })
    df = pd.DataFrame(records).sort_values("year")
    df.to_csv(OUT, index=False)
    print(f"Wrote {len(df)} rows to {OUT}")

if __name__ == "__main__":
    main()
