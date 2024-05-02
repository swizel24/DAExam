import pandas as pd
import numpy as np

df = pd.read_csv('sample_data.csv')

# Drop irrelevant columns (assuming 'ID' is irrelevant for analysis)
df.drop('ID', axis=1, inplace=True)

# Rename columns for clarity
df.rename(columns={'Age': 'Age (years)', 'Income': 'Income (USD)', 'Height': 'Height (cm)', 'Weight': 'Weight (kg)'}, inplace=True)

# Drop duplicate rows if any
df.drop_duplicates(inplace=True)

# Checking for null values after cleaning
print("Null Values after cleaning:")
print(df.isnull().sum())

# Replace null values with mean for numerical columns
df.fillna(df.mean(), inplace=True)

# Displaying the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)

df.to_csv('cleaned_data.csv', index=False)