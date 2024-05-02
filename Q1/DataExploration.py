import pandas as pd
import numpy as np

# Generating sample data
np.random.seed(0)
data = {
    'ID': range(1, 21),
    'Age': np.random.randint(18, 65, size=20),
    'Income': np.random.randint(20000, 100000, size=20),
    'Height': np.random.randint(150, 200, size=20),
    'Weight': np.random.randint(50, 100, size=20)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving DataFrame to CSV
df.to_csv('sample_data.csv', index=False)




#########################################################################################
# Reading the CSV file
df = pd.read_csv('sample_data.csv')

# Displaying the first few rows
print("Head:")
print(df.head())

# Displaying the last few rows
print("\nTail:")
print(df.tail())

# Getting basic information about the DataFrame
print("\nInfo:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean())

# Median
print("\nMedian:")
print(df.median())

# Mode
print("\nMode:")
print(df.mode())

# Standard deviation
print("\nStandard Deviation:")
print(df.std())

# Count
print("\nCount:")
print(df.count())

# Shape
print("\nShape:")
print(df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Checking for missing values
print("\nNull Values:")
print(df.isnull().sum())

# Inserting a new row
new_row = {'ID': 21, 'Age': 30, 'Income': 60000, 'Height': 170, 'Weight': 75}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\nAfter inserting a new row:")
print(df.tail())

# Deleting a row (let's delete the last row)
df.drop(df.index[-1], inplace=True)
print("\nAfter deleting the last row:")
print(df.tail())

# Inserting a new column
new_column = pd.Series(['Male'] * len(df), name='Gender')
df = pd.concat([df, new_column], axis=1)
print("\nAfter inserting a new column 'Gender':")
print(df.head())

# Deleting a column
df.drop('Gender', axis=1, inplace=True)
print("\nAfter deleting 'Gender' column:")
print(df.head())