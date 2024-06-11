import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, np.nan, 3, np.nan, 5],
    'D': [1, 2, 3, 4, np.nan]
}

df = pd.DataFrame(data)

# Detect missing values
missing_values = df.isnull()

# Display the DataFrame with missing values as True or False
print(missing_values)
