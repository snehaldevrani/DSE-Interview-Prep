import pandas as pd

# Sample sales data
data = {
    'product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'sales': [100, 150, 200, 120, 80, 90],
    'region': ['North', 'South', 'North', 'South', 'North', 'South']
}
df = pd.DataFrame(data)

print("=== Raw Sales ===")
print(df)

# Group by product
print("\n=== Sales by Product ===")
print(df.groupby('product')['sales'].sum())

# Group by region
print("\n=== Sales by Region ===")
print(df.groupby('region')['sales'].sum())

# Multiple groups + agg
print("\n=== Product + Region Summary ===")
print(df.groupby(['product', 'region'])['sales'].agg(['sum', 'mean', 'count']))
