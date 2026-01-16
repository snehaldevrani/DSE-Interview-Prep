import pandas as pd

# Create sample CSV data (no file needed)
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, None, 30, None],
    'city': ['Hyd', 'Blr', None, 'Pune']
}

df = pd.DataFrame(data)

print("=== Raw Data ===")
print(df)

print("\n=== Shape ===")
print(df.shape)  # (4, 3)

print("\n=== Missing Values ===")
print(df.isna().sum())  # age: 2, city: 1

# Fix missing values (DSE must-know)
df_clean = df.fillna({'age': 0, 'city': 'Unknown'})

print("\n=== Cleaned Data ===")
print(df_clean)

# Basic stats (interview favorite)
print("\n=== Average Age ===")
print(df_clean['age'].mean())  # 13.75 (after fillna)

print("\n=== City Count ===")
print(df_clean['city'].value_counts())
