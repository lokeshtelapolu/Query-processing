import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with random values
np.random.seed(0)  # For reproducibility
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Step 2: Define the style properties
styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})

# Display the styled DataFrame
styled_df