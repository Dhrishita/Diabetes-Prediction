# Diabetes Prediction

Welcome to the Diabetes prediction! This repository contains the source code and documentation for a diabetes prediction developed as part of a university project.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Installation](#installation)
- [Contact](#contact)

## Introduction

This project aims to predict the likelihood of a person having diabetes based on various health parameters using machine learning techniques. The model is trained on the Pima Indians Diabetes Dataset, which includes attributes such as glucose levels, BMI, age, high BP, high cholestrol and more. The goal is to provide a tool that can assist healthcare professionals in early detection and management of diabetes.

## Features

- Data preprocessing including handling missing values and scaling features.
- Implementation of various machine learning algorithmns (e.g., Naive Bayes, Decision Tree, Support vector machine, K-Nearest Neighbour and Logistic Regression).
- The performance of each algorithm is evaluated using metrics such as Recall, Accuracy and Precision derived from the Confusion matrix.
- Experimental results show that the Naive Bayes algorithm achieves the highest accuracy in predicting diabetes.
- Easy to use and extend for other datasets or additional features.

## Dataset
The dataset used in this project contains samples from 768 patients, each with 22 features that are used for prediction. The dataset was obtained from Kaggle. The key feature to be predicted is the "Outcome" where 0 indicates no diabetes and 1 indicates diabetes.

You can access the dataset here: [Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/your-dataset-link)

## Methodology
1. Data Preprocessing:
   
- **Missing Values Removal:** Instances with zero values are eliminated.
- **Data Splitting:** The data is split into training and testing sets.

2. Machine Learning Models:

- **Support Vector Machine (SVM):** Finds the optimal hyperplane that separates data points into different classes.
- **K-Nearest Neighbors (KNN):** Makes predictions based on the majority class among its k nearest neighbors.
- **Naive Bayes:** A probabilistic classifier based on Bayes' theorem with an assumption of feature independence.
- **Decision Tree:** Recursively splits data based on features to create a tree-like structure of decision rules.
- **Logistic Regression:** Models the probability of a binary outcome using the logistic function.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/Dhrishita/diabetes-prediction.git
   cd diabetes-prediction
   
2. Create a virtual environment and activate it:
   
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   
4. Run the prediction script:

   ```bash
   python predict_diabetes.py
   
## Contact
If you have any questions or suggestions, feel free to open an issue or contact:
Dhrishita Parve: dhrishitap18@gmail.com


