import streamlit as st
import joblib
import numpy as np

# Load the trained machine learning model
model = joblib.load("models/student_performance_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Predict whether a student is likely to pass or fail "
    "based on academic and lifestyle-related factors."
)

st.divider()

# Student inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

assignment_score = st.number_input(
    "Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)

# Prediction button
if st.button("🔮 Predict Performance"):

    # Prepare the input data
    features = np.array([[
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        sleep_hours
    ]])

    # Make prediction
    result = model.predict(features)[0]

    # Calculate probability of passing
    probability = model.predict_proba(features)[0][1] * 100

    st.divider()

    # Display result
    if result == 1:
        st.success("✅ Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")

    st.metric(
        "Probability of Passing",
        f"{probability:.2f}%"
    )

    st.progress(int(probability))