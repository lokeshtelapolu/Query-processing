import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Function to swap cases in a specified column
def swap_case_column(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: x.swapcase())
    return df

# Swap cases in the 'Name' column
df = swap_case_column(df, 'Name')

print(df)
