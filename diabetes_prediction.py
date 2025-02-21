# -*- coding: utf-8 -*-
"""Diabetes Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ofz-j_I52IFyqrBK-76rvv6K3snjmE6-
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Load the diabetes dataset
data = pd.read_csv("/content/drive/MyDrive/SEM 6/Colab Notebooks/ML/Diabetes.csv")

# Separate features (X) and target variable (y)
# ============================================
# X = data.drop('Diabetes_binary', axis=1)
# y = data['Diabetes_binary']
# ============================================
X= data.iloc[:,1:8]
y= data.iloc[:,8]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Standardize the features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Define and train machine learning models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(kernel='rbf', random_state=32),
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression": LogisticRegression(random_state=42)
}

# Create a dictionary to store model metrics
model_metrics = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    model_metrics[model_name] = {"Accuracy": accuracy, "Confusion Matrix": confusion, "Classification Report": classification_rep}

# Plotting accuracy for each model
plt.bar(model_metrics.keys(), [m["Accuracy"] for m in model_metrics.values()], color='skyblue')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison of Different Models')
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting confusion matrix for the first model (Decision Tree)
model_name = "Naive Bayes"
model_nam1 = "Decision Tree"
model_name2 = "Support Vector Machine"
model_name3 = "K-Nearest Neighbour"
model_name4 = "Logistic Regression"

# ================================================
# plt.imshow(model_metrics[model_name]["Confusion Matrix"], cmap='Blues', interpolation='nearest')
# plt.title(f'Confusion Matrix for {model_name}')
# plt.colorbar()
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.xticks([0, 1], ['No Diabetes', 'Diabetes'])
# plt.yticks([0, 1], ['No Diabetes', 'Diabetes'])
# plt.tight_layout()
# plt.show()
# ==============================================
# Plotting confusion matrix for the first model (Decision Tree)
# This line should be changed to the desired model name

plt.imshow(model_metrics[model_name]["Confusion Matrix"], cmap='Blues', interpolation='nearest')
plt.title(f'Confusion Matrix for {model_name}')
plt.colorbar()
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.xticks([0, 1], ['No Diabetes', 'Diabetes'])
plt.yticks([0, 1], ['No Diabetes', 'Diabetes'])
plt.tight_layout()
plt.show()


# Evaluate and print model performance
for model_name, metrics in model_metrics.items():
    print(f"----- {model_name} -----")
    print(f"Accuracy: {metrics['Accuracy']:.2f}")
    print("Confusion Matrix:\n", metrics["Confusion Matrix"])
    print("Classification Report:\n", metrics["Classification Report"])
    print("Accuracy:", accuracy_score(y_test, models[model_name].predict(X_test)))



    prediction = models[model_name].predict(X_test)
    result = "Yes" if 1 in prediction else "No"
    print("Predicted Result (Diabetes):", result)

    print()