import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Load the dataset
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


# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)


# Get student information
study_hours = float(input("Study hours: "))
attendance = float(input("Attendance (%): "))
previous_marks = float(input("Previous marks: "))
assignment_score = float(input("Assignment score: "))
sleep_hours = float(input("Sleep hours: "))


# Create input for the model
new_student = pd.DataFrame(
    [[
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        sleep_hours
    ]],
    columns=[
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_score",
        "sleep_hours"
    ]
)


# Make prediction
prediction = model.predict(new_student)[0]

# Get probability
probability = model.predict_proba(new_student)[0][1]


# Display result
print("\n-----------------------------")
print("Student Performance Prediction")
print("-----------------------------")

if prediction == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

print(f"Probability of passing: {probability:.2%}")