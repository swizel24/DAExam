import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Q3dataset.csv')

# Extracting features (attributes)
X = data.iloc[:, :-1].values  # All columns except the last one (target)

# Implementing K-means with k=3 clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('Attribute 1')
plt.ylabel('Attribute 2')
plt.title('K-means Clustering')
plt.show()