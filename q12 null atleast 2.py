import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
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

# Keep rows with at least 2 NaN values
df_filtered = df[df.isnull().sum(axis=1) >= 2] #axis =1 represents along rows

print("\nDataFrame with rows containing at least 2 NaN values:")
print(df_filtered)
