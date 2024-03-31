import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5, 5, 6,7,7,7,7,7]}
df = pd.DataFrame(data)

# Find the maximum value in the column
max_value = df['A'].max()

# Count occurrences of the maximum value
count_max_value = df['A'].eq(max_value).sum()

# Check if the maximum value is unique
is_unique_max = count_max_value == 1

print("Maximum value repeats:", count_max_value)
