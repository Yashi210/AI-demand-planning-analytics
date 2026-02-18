# AI-Driven Demand Planning & Value Leakage Analytics

##  Project Overview

This project simulates an enterprise-level demand planning and analytics
solution to identify value leakage caused by demand--supply mismatches,
inventory inefficiencies, and forecast errors.

Using SQL, Python, ETL pipelines, and a localhost dashboard, the project
delivers actionable insights to support S&OP (Sales & Operations
Planning) and executive decision-making.

##  Business Problem

Organizations often face: - Overstocking leading to high holding costs -
Stockouts causing lost sales - Inaccurate demand forecasting impacting
planning decisions

This project quantifies where and why value leakage occurs and provides
data-driven visibility across regions and products.

## Tech Stack

-   Python (Pandas, Scikit-learn, Streamlit)
-   SQL 
-   ETL Pipelines
-   Localhost Dashboard (Streamlit)
-   Power BI (optional)

##  Project Structure

AI_Demand_Planning_Project/ data/ sql/ python/ powerbi/
demand_planning.db README.md

##  ETL Process

-   CSV ingestion using Python
-   Data stored in SQLite
-   SQL-based analytics and joins

## AI Demand Forecasting

Linear Regression model to forecast demand and calculate forecast error
impact.

## Value Leakage Metrics

-   Overstock Cost
-   Stockout Loss
-   Forecast Error Cost

## Dashboard

Runs on http://localhost:8501 using Streamlit.

##  How to Run

pip install streamlit pandas matplotlib scikit-learn\
python python/load_data.py\
python python/forecast_model.py\
streamlit run python/dashboard.py


