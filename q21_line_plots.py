import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:/Users/Harsha/OneDrive/Documents/1 query processing lab\q21_line_plots_financial_data.csv")

#The error you're encountering is due to the use of backslashes in the file path string, 
# which can be interpreted as escape sequences in Python strings. 
# To fix this, you can either use raw strings by prefixing the string with r, 
# or you can replace the backslashes with forward slashes, which are also supported on Windows.
#data = pd.read_csv(r"C:\Users\Harsha\OneDrive\Documents\1 query processing lab\q21_line_plots_financial_data.csv")
#data = pd.read_csv("C:/Users/Harsha/OneDrive/Documents/1 query processing lab/q21_line_plots_financial_data.csv")

plt.figure(figsize=(10, 5))
    
    # Plot Open prices
plt.plot(data['Date'], data['Open'], marker='o', label='Open')
    
    # Plot High prices
plt.plot(data['Date'], data['High'], marker='o', label='High')
    
    # Plot Low prices
plt.plot(data['Date'], data['Low'], marker='o', label='Low')
    
    # Plot Close prices
plt.plot(data['Date'], data['Close'], marker='o', label='Close')
    
    # Customize the plot
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
    
    # Show the plot
plt.show()
