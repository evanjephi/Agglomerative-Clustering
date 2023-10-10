# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import numpy as np

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

import matplotlib.pyplot as plt
import numpy as np

# Use only petal length and petal width for visualization
X = iris.data[:, 2:4]
y = iris.target

# Initialize and train the Support Vector Machine Classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X, y)

# Define a mesh grid to plot decision boundaries
h = .02  # Step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict the decision boundary
Z = svm_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundaries
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)

# Set labels and title
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('SVM Classifier Decision Boundaries')

# Show plot
plt.show()
