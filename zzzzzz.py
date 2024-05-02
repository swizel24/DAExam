import pandas as pd

# Create a DataFrame with 20 rows and 5 columns
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70,
            32, 28, 37, 42, 48, 58, 63, 68, 26, 31],
    'Income': [50000, 60000, 70000, 80000, 90000,
               55000, 65000, 75000, 85000, 95000,
               52000, 62000, 72000, 82000, 92000,
               58000, 68000, 78000, 88000, 98000],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master',
                  'PhD', 'Bachelor', 'Master', 'PhD', 'Bachelor',
                  'Master', 'PhD', 'Bachelor', 'Master', 'PhD',
                  'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female'],
    'Marital_Status': ['Married', 'Single', 'Married', 'Single', 'Married',
                       'Single', 'Married', 'Single', 'Married', 'Single',
                       'Married', 'Single', 'Married', 'Single', 'Married',
                       'Single', 'Married', 'Single', 'Married', 'Single']
})

# Save the dataset to a CSV file
data.to_csv('sensible_dataset.csv', index=False)