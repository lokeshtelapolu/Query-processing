import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with random values
np.random.seed(0)  # For reproducibility
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Step 2: Define a function to format values based on positive or negative
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

# Step 3: Apply the style formatting
styled_df = df.style.applymap(color_negative_red)

# Step 4: Display the styled DataFrame
styled_df