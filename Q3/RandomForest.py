import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('Q3dataset.csv')

# Splitting data into features (attributes) and target (class)
X = data.iloc[:, :-1].values  # All columns except the last one (target)
y = data.iloc[:, -1].values   # Last column (target)

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Implementing Random Forest
random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)

# Predicting the classes for the test set
y_pred = random_forest.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
