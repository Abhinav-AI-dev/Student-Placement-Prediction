import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------
# Load Model
# ---------------------------------------

model = joblib.load("placement_model.pkl")

# ---------------------------------------
# Title
# ---------------------------------------

st.title("🎯 Student Placement Prediction")

st.write("Fill in the student's details and click **Predict Placement**.")

st.divider()

# ---------------------------------------
# Input Form
# ---------------------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["M", "F"]
    )

    ssc_p = st.number_input(
        "10th Percentage",
        0.0,
        100.0,
        70.0
    )

    ssc_b = st.selectbox(
        "10th Board",
        ["Central", "Others"]
    )

    hsc_p = st.number_input(
        "12th Percentage",
        0.0,
        100.0,
        70.0
    )

    hsc_b = st.selectbox(
        "12th Board",
        ["Central", "Others"]
    )

    hsc_s = st.selectbox(
        "12th Stream",
        ["Science", "Commerce", "Arts"]
    )

with col2:

    degree_p = st.number_input(
        "Degree Percentage",
        0.0,
        100.0,
        70.0
    )

    degree_t = st.selectbox(
        "Degree Type",
        ["Sci&Tech", "Comm&Mgmt", "Others"]
    )

    workex = st.selectbox(
        "Work Experience",
        ["Yes", "No"]
    )

    etest_p = st.number_input(
        "Employability Test %",
        0.0,
        100.0,
        70.0
    )

    specialisation = st.selectbox(
        "MBA Specialisation",
        ["Mkt&HR", "Mkt&Fin"]
    )

    mba_p = st.number_input(
        "MBA Percentage",
        0.0,
        100.0,
        65.0
    )

st.write("")

predict = st.button(
    "Predict Placement",
    use_container_width=True
)

# ---------------------------------------
# Prediction
# ---------------------------------------

if predict:

    input_data = pd.DataFrame({

        "gender":[gender],

        "ssc_p":[ssc_p],

        "ssc_b":[ssc_b],

        "hsc_p":[hsc_p],

        "hsc_b":[hsc_b],

        "hsc_s":[hsc_s],

        "degree_p":[degree_p],

        "degree_t":[degree_t],

        "workex":[workex],

        "etest_p":[etest_p],

        "specialisation":[specialisation],

        "mba_p":[mba_p]

    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = max(probability)

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success("✅ Student is likely to be PLACED")

    else:

        st.error("❌ Student is likely to NOT be placed")

    st.write("### Confidence")

    st.progress(int(confidence*100))

    st.metric(
        "Prediction Confidence",
        f"{confidence*100:.2f}%"
    )

    st.write("")

    st.info("""
The prediction is generated using the trained Logistic Regression
model based on the student's academic profile.
""")