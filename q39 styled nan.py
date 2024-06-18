import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with random values
np.random.seed(0)  # For reproducibility
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Step 2: Introduce NaN values randomly
nan_indices = [(np.random.randint(10), np.random.randint(4)) for _ in range(5)]
for i, j in nan_indices:
    df.iat[i, j] = np.nan

# Step 3: Define a function to highlight NaN values
def highlight_nan(val):
    color = 'background-color: yellow' if pd.isna(val) else ''
    return color

# Step 4: Apply the style formatting
styled_df = df.style.applymap(highlight_nan)

# Display the styled DataFrame
styled_df