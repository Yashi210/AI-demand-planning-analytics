import sqlite3
import pandas as pd

conn = sqlite3.connect('demand_planning.db')

files = {
    'sales': 'data/sales_data.csv',
    'forecast': 'data/forecast_data.csv',
    'inventory': 'data/inventory_data.csv',
    'supply': 'data/supply_data.csv'
}

for table, file in files.items():
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists='replace', index=False)

conn.close()
print("Data loaded successfully")
