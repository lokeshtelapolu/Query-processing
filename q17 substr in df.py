import pandas as pd

# Create a sample DataFrame
data = {
    'school': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['v', 'v', 'vi', 'vi', 'v', 'vi'],
    'name': ['ajay', 'raj', 'joy', 'john', 'ram', 'nandy'],
    'dob': ['15-05-2002', '17-05-2002', '16-02-1999', '25-09-1998', '11-05-2002', '15-09-1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['st1', 'st2', 'st3', 'st1', 'st2', 'st4']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Define the substring to search for
substring = 's002'

# Find the indices of rows where the substring is present in the 'school' column
matching_indices = df[df['school'].str.contains(substring, na=False)].index

print(f"\nIndices of rows where the substring '{substring}' is present in the 'school' column:")
print(matching_indices.tolist())
