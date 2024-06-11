import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Alphabet Inc. stock. You would typically load this from a CSV or a data source.
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Close': [100, 101, 102, 103, 104],
    'Volume': [1000, 1100, 100, 1300, 1400]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Define the date range
start_date = '2023-01-02'
end_date = '2023-01-04'

# Filter the DataFrame for the date range
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Volume'], filtered_df['Close'], color='blue')

# Adding labels and title
plt.xlabel('Trading Volume')
plt.ylabel('Stock Price')
plt.title('Alphabet Inc. Stock Prices vs. Trading Volume')

# Show the plot
plt.grid(True)
plt.show()
