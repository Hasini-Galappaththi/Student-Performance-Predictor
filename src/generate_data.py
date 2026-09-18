import numpy as np
import pandas as pd


# Make the results reproducible
np.random.seed(42)


# Number of students
number_of_students = 500


# Generate student features
study_hours = np.random.uniform(1, 10, number_of_students)

attendance = np.random.uniform(50, 100, number_of_students)

previous_marks = np.random.uniform(40, 95, number_of_students)

assignment_score = np.random.uniform(40, 95, number_of_students)

sleep_hours = np.random.uniform(5, 9, number_of_students)


# Create a performance score
performance_score = (
    study_hours * 0.25
    + attendance * 0.25
    + previous_marks * 0.20
    + assignment_score * 0.20
    + sleep_hours * 0.10
)


# Convert the score into Pass/Fail
# Use the median performance score as the pass/fail boundary
threshold = np.median(performance_score)

pass_result = (performance_score >= threshold).astype(int)


# Create DataFrame
data = pd.DataFrame({
    "study_hours": study_hours.round(2),
    "attendance": attendance.round(2),
    "previous_marks": previous_marks.round(2),
    "assignment_score": assignment_score.round(2),
    "sleep_hours": sleep_hours.round(2),
    "pass": pass_result
})


# Save dataset
data.to_csv("data/students.csv", index=False)


print("================================")
print("DATASET GENERATED")
print("================================")

print(f"Number of students: {len(data)}")
print(f"Number of columns: {len(data.columns)}")

print("\nPass/Fail distribution:")
print(data["pass"].value_counts())

print("\nFirst 5 records:")
print(data.head())

print("\nDataset saved successfully!")