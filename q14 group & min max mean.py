import pandas as pd

# Create the DataFrame from the provided data
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

# Split the DataFrame into groups based on the school code
grouped = df.groupby('school')

# Compute mean, min, and max of 'age' for each group
age_stats = grouped['age'].agg(['mean', 'min', 'max'])

print("\nMean, min, and max of 'age' for each school:")
print(age_stats)
