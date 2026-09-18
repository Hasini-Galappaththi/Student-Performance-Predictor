import streamlit as st
import joblib
import pandas as pd


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

model = joblib.load("models/student_performance_model.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #64748b;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        color: #1e3a8a;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-top: 20px;
    }

    .info-box {
        padding: 18px;
        border-radius: 10px;
        background-color: #eff6ff;
        border-left: 5px solid #2563eb;
        margin-top: 20px;
    }

    .warning-box {
        padding: 18px;
        border-radius: 10px;
        background-color: #fff7ed;
        border-left: 5px solid #f97316;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A machine learning application that predicts student performance '
    'using academic and lifestyle-related factors.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# Prediction section
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📝 Student Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=6.0,
        step=0.5
    )

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=1.0
    )

    previous_marks = st.number_input(
        "📊 Previous Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )


with col2:

    assignment_score = st.number_input(
        "📝 Assignment Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0
    )

    sleep_hours = st.number_input(
        "😴 Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )


st.write("")


# --------------------------------------------------
# Prediction button
# --------------------------------------------------

predict_button = st.button(
    "🔮 Predict Student Performance",
    width="stretch"
)

if predict_button:

    # Prepare input data
    features = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignment_score": assignment_score,
        "sleep_hours": sleep_hours
    }])

    # Make prediction
    result = model.predict(features)[0]

    # Calculate probability
    probability = model.predict_proba(features)[0][1] * 100

    probability = round(probability, 2)

    st.divider()

    # --------------------------------------------------
    # Prediction result
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">📌 Prediction Result</div>',
        unsafe_allow_html=True
    )

    if result == 1:

        st.success("✅ Prediction: PASS")

    else:

        st.error("❌ Prediction: FAIL")


    # Probability
    st.metric(
        label="Probability of Passing",
        value=f"{probability:.2f}%"
    )

    st.progress(int(probability))


    # --------------------------------------------------
    # Student input summary
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">📋 Student Input Summary</div>',
        unsafe_allow_html=True
    )

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:

        st.write(f"**Study Hours:** {study_hours}")

        st.write(f"**Attendance:** {attendance}%")

    with summary_col2:

        st.write(f"**Previous Marks:** {previous_marks}")

        st.write(f"**Assignment Score:** {assignment_score}")

    with summary_col3:

        st.write(f"**Sleep Hours:** {sleep_hours}")


# --------------------------------------------------
# Model information
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🤖 Model Information</div>',
    unsafe_allow_html=True
)

info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:

    st.metric("Algorithm", "Logistic Regression")

    st.metric("Dataset Size", "500 Records")


with info_col2:

    st.metric("Test Set", "100 Records")

    st.metric("Accuracy", "98.00%")


with info_col3:

    st.metric("Precision", "100.00%")

    st.metric("Recall", "95.74%")


# --------------------------------------------------
# Important limitation
# --------------------------------------------------

st.markdown(
    """
    <div class="warning-box">

    <strong>⚠️ Important Note</strong><br><br>

    This project uses a synthetic dataset generated using a mathematical
    rule. Therefore, the reported model metrics demonstrate performance
    on this dataset and should not be interpreted as real-world
    student-performance prediction accuracy.

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Project information
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">📊 Project Overview</div>',
    unsafe_allow_html=True
)

st.write(
    """
    This project demonstrates a complete beginner-friendly machine
    learning workflow including data generation, data exploration,
    visualization, model training, evaluation, and deployment.
    """
)

st.write(
    """
    **Features used by the model:**
    Study Hours • Attendance • Previous Marks • Assignment Score • Sleep Hours
    """
)


# --------------------------------------------------
# Footer
# --------------------------------------------------



st.divider()

st.markdown(
    '<div class="section-title">📊 Data Visualizations</div>',
    unsafe_allow_html=True
)

st.write(
    "The following visualizations provide a simple overview of the "
    "dataset used for training the machine learning model."
)

viz_col1, viz_col2 = st.columns(2)

with viz_col1:
    st.image(
        "static/correlation_heatmap.png",
        caption="Feature Correlation Heatmap",
        width="stretch"
    )

with viz_col2:
    st.image(
        "static/pass_fail_distribution.png",
        caption="Pass vs Fail Distribution",
        width="stretch"
    )

st.image(
    "static/study_hours_vs_marks.png",
    caption="Study Hours vs Previous Marks",
    width="stretch"
)

st.caption(
    "Student Performance Predictor • Machine Learning Project • "
    "BSc (Hons) in Computer Science"
)