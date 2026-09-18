import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("data/students.csv")

# Calculate correlations
correlation = data.corr()

# Create the heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Student Performance Variables")

# Save the chart
plt.savefig("static/correlation_heatmap.png", bbox_inches="tight")

# Close the figure
plt.close()

print("Correlation heatmap saved successfully!")
# Create Pass vs Fail bar chart
pass_fail_counts = data["pass"].value_counts().sort_index()

plt.figure(figsize=(7, 5))

plt.bar(
    ["Fail", "Pass"],
    [
        pass_fail_counts.get(0, 0),
        pass_fail_counts.get(1, 0)
    ]
)

plt.title("Pass vs Fail Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")

# Save the chart
plt.savefig(
    "static/pass_fail_distribution.png",
    bbox_inches="tight"
)

plt.close()

print("Pass vs Fail chart saved successfully!")
# Create Study Hours vs Previous Marks scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["study_hours"],
    data["previous_marks"],
    alpha=0.6
)

plt.title("Study Hours vs Previous Marks")
plt.xlabel("Study Hours")
plt.ylabel("Previous Marks")

# Save the chart
plt.savefig(
    "static/study_hours_vs_marks.png",
    bbox_inches="tight"
)

plt.close()

print("Study Hours vs Previous Marks chart saved successfully!")