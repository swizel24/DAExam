import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('Q3dataset.csv')

# Splitting data into features (attributes) and target (class)
X = data.iloc[:, 1:].values  # All columns except the first one (Attribute 1)
y = data.iloc[:, 0].values    # First column (Attribute 1) as the target

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Implementing Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Predicting Attribute 1 for the test set
y_pred = linear_reg.predict(X_test)

# Calculating Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
