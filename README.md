# Agglomerative-Clustering

Loading and Preparing Data:

It starts by loading the Iris dataset using a function called load_iris().
It also separately loads the features (X) and target labels (y) using the same dataset.
Then, it creates a variable className which seems to be an error, as it should be target_names.
Data Scaling:

It applies Standard Scaling to the feature data (X) using the StandardScaler() from the scikit-learn library. The scaled data is stored in sc_iris_df.
Agglomerative Clustering:

It initializes an Agglomerative Clustering model with 3 clusters (n_clusters=3).
The linkage method is set to 'complete' and the affinity (distance metric) is set to 'euclidean'.
Then, it applies the clustering to the scaled Iris data (sc_iris_df) and assigns cluster labels to each data point.
Plotting the Clusters:

This section is for visualizing the clustered data.
It creates a scatter plot where the x-axis represents Feature 1 and the y-axis represents Feature 2.
The points are colored according to the assigned cluster labels (c=cluster_labels), using the 'cool' colormap.

Result:
![image](https://github.com/evanjephi/Agglomerative-Clustering/assets/73504127/15fd27a5-f911-4071-b18c-a9e25bdfc17f)
