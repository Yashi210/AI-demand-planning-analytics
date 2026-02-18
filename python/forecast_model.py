import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/sales_data.csv')

df['month'] = pd.to_datetime(df['date']).dt.month

X = df[['month']]
y = df['actual_demand']

model = LinearRegression()
model.fit(X, y)

df['predicted_demand'] = model.predict(X)

print(df[['date', 'actual_demand', 'predicted_demand']])