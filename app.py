from flask import Flask, render_template, request
import joblib
import pandas as pd


# Create Flask application
app = Flask(__name__)


# Load the trained machine learning model
model = joblib.load("models/student_performance_model.pkl")


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None

    if request.method == "POST":

        # Get values from the HTML form
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])
        assignment_score = float(request.form["assignment_score"])
        sleep_hours = float(request.form["sleep_hours"])

        # Create a DataFrame with the same feature names
        # used when training the model
        input_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignment_score": assignment_score,
            "sleep_hours": sleep_hours
        }])

        # Make prediction
        result = model.predict(input_data)[0]

        # Get probability of passing
        probability = model.predict_proba(input_data)[0][1] * 100

        # Convert prediction into readable text
        if result == 1:
            prediction = "PASS"
        else:
            prediction = "FAIL"

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )


# Start Flask application
if __name__ == "__main__":
    app.run(debug=True)