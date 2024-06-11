import pandas as pd
import matplotlib.pyplot as plt

# Sample dictionary containing historical stock prices
historical_stock_prices = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Close_Price': [1500, 1510, 1520, 1530, 1540],
}

# Convert dictionary to DataFrame
df = pd.DataFrame(historical_stock_prices)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' column as the index
#df.set_index('Date', ...): This sets the Date column as the index of the DataFrame df.
# The index is a unique identifier for each row in the DataFrame,
#  and using the Date as the index allows for easier filtering and plotting by date.
#inplace=True: This modifies the DataFrame in place, 
# meaning that the original DataFrame is updated and
#  no new DataFrame is created.
df.set_index('Date', inplace=True)

# Filter data between specific dates
#This filters the DataFrame df to include only the rows 
# where the index (Date) is between start_date and end_date, inclusive.
start_date = '2024-01-01'
end_date = '2024-01-03'
filtered_df = df.loc[start_date:end_date]
print(df)
print(filtered_df)
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(filtered_df.index, filtered_df['Close_Price'], marker='o', linestyle='-')
plt.title('Historical Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
