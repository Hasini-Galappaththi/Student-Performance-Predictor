import pandas as pd

# Load the dataset
data = pd.read_csv("data/students.csv")

# Display the dataset
print(data)

# Display the first 5 rows
print("\nFirst 5 rows:")
print(data.head())

# Display the number of rows and columns
print("\nDataset shape:")
print(data.shape)

# Display information about the dataset
print("\nDataset information:")
print(data.info())

# Display basic statistics
print("\nBasic statistics:")
print(data.describe())