# Student Performance Analysis using Linear Regression

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings

# Step 1: Load the dataset
print("=== تحليل أداء الطلاب ===")
data = pd.read_csv('Student_Performance.csv')
print(data.info())

# Step 2: Data preprocessing
# Encode categorical features
le = LabelEncoder()
data["Extracurricular Activities"] = le.fit_transform(data["Extracurricular Activities"])

# Drop irrelevant features
new_data = data.drop(["Extracurricular Activities", "Sleep Hours", "Sample Question Papers Practiced"], axis=1)

# Display correlation matrix
print("\n=== Correlation Matrix ===")
print(new_data.corr())

# Step 3: Split data into training and testing sets
data_train = new_data.loc[:7000,:]
x_train = data_train.drop("Performance Index", axis=1)
y_train = data_train["Performance Index"]

data_test = new_data.loc[7001:,:]
x_test = data_test.drop("Performance Index", axis=1)
y_test = data_test["Performance Index"]

# Step 4: Train the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Step 5: Evaluate the model
model_score_test = model.score(x_test, y_test)
print(f"\n=== Model Evaluation ===")
print(f"score  {model_score_test:.4f}")

# Step 6: Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, model.predict(x_test), alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Performance', fontsize=12)
plt.ylabel('Predicted Performance', fontsize=12)
plt.title('Student Performance Prediction', fontsize=14)
plt.grid(True)

# Display feature importance
plt.figure(figsize=(12, 6))
feature_importance = pd.DataFrame({
    'Feature': x_train.columns,
    'Importance': model.coef_
})
feature_importance = feature_importance.sort_values('Importance', ascending=False)
plt.bar(feature_importance['Feature'], feature_importance['Importance'])
plt.xticks(rotation=45, ha='right')
plt.xlabel('Features', fontsize=12)
plt.ylabel('Importance', fontsize=12)
plt.title('Feature Importance', fontsize=14)
plt.tight_layout()

plt.show()

