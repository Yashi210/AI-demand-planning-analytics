import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="AI Demand Planning Dashboard", layout="wide")

st.title("📊 AI-Driven Demand Planning & Value Leakage Analytics")

# Database connection
conn = sqlite3.connect("demand_planning.db")

# Load leakage data
query = """
SELECT
  s.date,
  s.region,
  s.product,

  CASE
    WHEN i.inventory_level > s.actual_demand
    THEN (i.inventory_level - s.actual_demand) * i.holding_cost
    ELSE 0
  END AS overstock_cost,

  CASE
    WHEN sp.supply_qty < s.actual_demand
    THEN (s.actual_demand - sp.supply_qty) * s.unit_price
    ELSE 0
  END AS stockout_loss,

  ABS(s.actual_demand - f.forecast_demand) * s.unit_price AS forecast_error_cost

FROM sales s
JOIN inventory i USING(date, region, product)
JOIN supply sp USING(date, region, product)
JOIN forecast f USING(date, region, product)
"""

df = pd.read_sql(query, conn)

# Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.multiselect(
    "Select Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

product = st.sidebar.multiselect(
    "Select Product",
    options=df["product"].unique(),
    default=df["product"].unique()
)

filtered_df = df[
    (df["region"].isin(region)) &
    (df["product"].isin(product))
]

# KPIs
total_overstock = filtered_df["overstock_cost"].sum()
total_stockout = filtered_df["stockout_loss"].sum()
total_forecast_error = filtered_df["forecast_error_cost"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("📦 Overstock Cost", f"₹ {total_overstock:,.0f}")
col2.metric("❌ Stockout Loss", f"₹ {total_stockout:,.0f}")
col3.metric("📉 Forecast Error Cost", f"₹ {total_forecast_error:,.0f}")

st.divider()

# Leakage by Product
st.subheader("Value Leakage by Product")

leakage_product = filtered_df.groupby("product")[
    ["overstock_cost", "stockout_loss", "forecast_error_cost"]
].sum()

st.bar_chart(leakage_product)

# Leakage by Region
st.subheader("Value Leakage by Region")

leakage_region = filtered_df.groupby("region")[
    ["overstock_cost", "stockout_loss"]
].sum()

st.bar_chart(leakage_region)

# Detailed Table
st.subheader("Detailed Leakage Table")
st.dataframe(filtered_df)

conn.close()
