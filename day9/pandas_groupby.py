
import pandas as pd

df = pd.DataFrame({
    'dept': ['HR','IT','HR','IT','Sales'],
    'salary': [50000,80000,60000,90000,70000],
    'years': [2,5,3,6,4]
})

# Multi-agg by dept
result = df.groupby('dept').agg({
    'salary': ['mean','max','count'],
    'years': 'mean'
})
print(result)
