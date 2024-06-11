import pandas as pd

# Sample sales data dictionary
sales_data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Item': ['Item_A', 'Item_B', 'Item_A', 'Item_B', 'Item_A', 'Item_C'],
    'Category': ['Category_1', 'Category_1', 'Category_1', 'Category_1', 'Category_1', 'Category_2'],
    'Sales': [150, 200, 300, 250, 100, 500],
    'Quantity': [10, 20, 15, 25, 8, 50]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(sales_data)

# Create a Pivot table
pivot_table = df.pivot_table(values='Sales', index='Item', aggfunc=['max', 'min'])

# Rename columns for better readability
pivot_table.columns = ['Max_Sales', 'Min_Sales']

# Reset the index to make 'Item' a column
pivot_table.reset_index(inplace=True)

# Display the Pivot table
print(pivot_table)
