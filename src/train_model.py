import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv("data/students.csv")

# Features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_score",
        "sleep_hours"
    ]
]

# Target
y = data["pass"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("================================")
print("MODEL EVALUATION")
print("================================")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save trained model
joblib.dump(model, "student_performance_model.pkl")

print("\nModel saved successfully!")