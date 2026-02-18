CREATE TABLE sales (
  date TEXT,
  region TEXT,
  product TEXT,
  actual_demand INTEGER,
  unit_price INTEGER
);

CREATE TABLE forecast (
  date TEXT,
  region TEXT,
  product TEXT,
  forecast_demand INTEGER
);

CREATE TABLE inventory (
  date TEXT,
  region TEXT,
  product TEXT,
  inventory_level INTEGER,
  holding_cost INTEGER
);

CREATE TABLE supply (
  date TEXT,
  region TEXT,
  product TEXT,
  supply_qty INTEGER
);