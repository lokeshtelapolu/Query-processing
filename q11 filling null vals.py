import pandas as pd
import numpy as np

# Create a dictionary with order data
data = {
    'order_number': [1001, 1002, 1003, 1004, 1005],
    'purchase_amount': [150.5, np.nan, 230.2, np.nan, 125.7],
    'order_date': ['2021-07-10', '2021-07-11', np.nan, '2021-07-13', '2021-07-14'],
    'customer_id': [101, 102, 103, 104, np.nan],
    'salesman_id': [1001, np.nan, 1003, 1004, 1005]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing values using different methods
# 1. Replace NaN with a specified value (e.g., 0 for numeric, 'Unknown' for strings)
df_replace_value = df.fillna({'purchase_amount': 0, 'order_date': 'Unknown', 'customer_id': 0, 'salesman_id': 0})
print("\nDataFrame after replacing NaNs with specified values:")
print(df_replace_value)

# 2. Replace NaN using forward fill method
df_ffill = df.fillna(method='ffill')
print("\nDataFrame after forward fill:")
print(df_ffill)

# 3. Replace NaN using backward fill method
df_bfill = df.fillna(method='bfill')
print("\nDataFrame after backward fill:")
print(df_bfill)

# 4. Replace NaN with the mean (only for numeric columns)
df_mean = df.copy()
df_mean['purchase_amount'] = df_mean['purchase_amount'].fillna(df_mean['purchase_amount'].mean())
print("\nDataFrame after replacing NaNs with mean (numeric columns):")
print(df_mean)
