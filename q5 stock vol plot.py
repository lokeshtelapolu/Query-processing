import pandas as pd
import matplotlib.pyplot as plt

# Sample dictionary containing historical stock prices and trading volume
historical_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Volume': [1000000, 1100000, 100000, 1300000, 140000],
}

# Convert dictionary to DataFrame
df = pd.DataFrame(historical_data)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' column as the index
df.set_index('Date', inplace=True)

# Filter data between specific dates
start_date = '2024-01-01'
end_date = '2024-01-05'
filtered_df = df.loc[start_date:end_date]

# Plot the data
plt.figure(figsize=(10, 6))
filtered_df['Volume'].plot(kind='bar', color='orange')
plt.title('Trading Volume of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
