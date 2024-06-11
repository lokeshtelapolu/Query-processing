import pandas as pd

# Create the DataFrame from the provided data
data = {
    'year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['pacific', 'americas', 'africa', 'americas', 'americas'],
    'country': ['viet nam', 'uruguay', "cte d' ivoire", 'colombia', 'saint kitts and nevis'],
    'beverage type': ['wine', 'other', 'wine', 'beer', 'beer'],
    'value': [0.00, 1.50, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

# Display the dimensions or shape of the DataFrame
print("Dimensions of the DataFrame:", df.shape)

# Extract and display the column names
print("\nColumn names of the DataFrame:")
print(df.columns.tolist())
