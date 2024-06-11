import pandas as pd

# Sample data
data = {
    'DEPARTMENT_ID': [10, 10, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270],
    'DEPARTMENT_NAME': ['Accounting', 'Accounting', 'Accounting', 'Accounting', 'Shipping', 'IT', 'Public Relations', 'Sales', 'Executive', 'Finance', 'Accounting', 'Treasury', 'Corporate Tax', 'Accounting', 'Shareholder Services', 'Benefits', 'Manufacturing', 'Construction', 'Contracting', 'Operations', 'IT Support', 'NOC', 'Accounting', 'Government Sales', 'Accounting', 'Recruiting', 'Accounting'],
    'MANAGER_ID': [200, 200, 200, 203, 121, 103, 204, 145, 100, 108, 205, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'LOCATION_ID': [1700, 1700, 1700, 2400, 1500, 1400, 2700, 2500, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700]
}

# Create DataFrame
df = pd.DataFrame(data)


print(df)
print()

df.drop_duplicates(inplace=True)
print(df)

distinct_department_ids = df['DEPARTMENT_ID'].unique()
print("unique department IDs")
print(distinct_department_ids)

# Convert to DataFrame for better presentation
distinct_department_ids_df = pd.DataFrame(distinct_department_ids, columns=['DISTINCT_DEPARTMENT_ID'])

# Print the result
print("coount ",distinct_department_ids_df["DISTINCT_DEPARTMENT_ID"].count())
print(distinct_department_ids_df)
