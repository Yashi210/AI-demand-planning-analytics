SELECT
  s.date,
  s.region,
  s.product,

  -- Overstock Cost
  CASE
    WHEN i.inventory_level > s.actual_demand
    THEN (i.inventory_level - s.actual_demand) * i.holding_cost
    ELSE 0
  END AS overstock_cost,

  -- Stockout Loss
  CASE
    WHEN sp.supply_qty < s.actual_demand
    THEN (s.actual_demand - sp.supply_qty) * s.unit_price
    ELSE 0
  END AS stockout_loss,

  -- Forecast Error Cost
  ABS(s.actual_demand - f.forecast_demand) * s.unit_price AS forecast_error_cost

FROM sales s
JOIN inventory i USING(date, region, product)
JOIN supply sp USING(date, region, product)
JOIN forecast f USING(date, region, product);