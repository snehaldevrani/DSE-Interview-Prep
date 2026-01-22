# day8_pandas_merge.py
# Day 8: Pandas LEFT JOIN practice (SQL equivalent)
# Purpose: Merge sales + customers (handle missing data)

import pandas as pd

# Dataset 1: Sales
sales = pd.DataFrame({
    'order_id': [1,2,3,4,5],
    'customer_id': ['A','B','A','C','D'],
    'amount': [100, 200, 150, 300, 50]
})

# Dataset 2: Customers  
customers = pd.DataFrame({
    'customer_id': ['A','B','C','E'],
    'region': ['North','South','East','West']
})

print("Sales:\n", sales)
print("\nCustomers:\n", customers)

# LEFT JOIN on customer_id
result = sales.merge(customers, on='customer_id', how='left')
print("\nMerged (LEFT JOIN):\n", result)

# Region totals (missing D becomes NaN, excluded)
totals = result.groupby('region', dropna=True)['amount'].sum()
print("\nRegion Totals:\n", totals)

# Notes:
# - how='left' keeps all sales records
# - Missing customers (D) → NaN region
# - DSE use case: sales data + customer demographics
