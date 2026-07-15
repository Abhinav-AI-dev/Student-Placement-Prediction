import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------------------------
# Title
# --------------------------------------------------------

st.title("ℹ️ About This Project")

st.markdown("""
Welcome to the **Student Placement Prediction System**.

This project uses **Machine Learning** to predict whether a student is likely to be placed based on their academic performance and educational background.
""")

st.divider()

# --------------------------------------------------------
# Objective
# --------------------------------------------------------

st.header("🎯 Project Objective")

st.write("""
The objective of this project is to build a supervised machine learning model
that predicts whether a student is likely to be placed during campus placements.

The prediction is based on several academic and personal attributes such as:

- 10th Percentage
- 12th Percentage
- Degree Percentage
- Employability Test Score
- MBA Percentage
- Work Experience
- Educational Background
""")

st.divider()

# --------------------------------------------------------
# Dataset
# --------------------------------------------------------

st.header("📂 Dataset Information")

col1, col2 = st.columns(2)

with col1:

    st.info("""
Dataset Name

Campus Placement Dataset
""")

    st.info("""
Rows

215 Students
""")

with col2:

    st.info("""
Features

12 Input Features
""")

    st.info("""
Target

Placement Status
""")

st.divider()

# --------------------------------------------------------
# Machine Learning
# --------------------------------------------------------

st.header("🤖 Machine Learning")

st.write("""
### Algorithms Used

- Logistic Regression
- Random Forest Classifier

After comparing both algorithms, **Logistic Regression**
was selected because it achieved the highest accuracy.
""")

st.divider()

# --------------------------------------------------------
# Technologies
# --------------------------------------------------------

st.header("🛠 Technologies Used")

tech1, tech2 = st.columns(2)

with tech1:

    st.success("🐍 Python")

    st.success("📊 Pandas")

    st.success("📈 NumPy")

    st.success("🤖 Scikit-Learn")

with tech2:

    st.success("🌐 Streamlit")

    st.success("📉 Matplotlib")

    st.success("💾 Joblib")

    st.success("📂 JSON")

st.divider()

# --------------------------------------------------------
# Project Workflow
# --------------------------------------------------------

st.header("⚙️ Project Workflow")

st.markdown("""
1. Load Dataset

2. Data Cleaning

3. Exploratory Data Analysis (EDA)

4. Data Preprocessing

5. Feature Scaling

6. Train-Test Split

7. Model Training

8. Model Evaluation

9. Save Model

10. Streamlit Deployment
""")

st.divider()

# --------------------------------------------------------
# Future Improvements
# --------------------------------------------------------

st.header("🚀 Future Improvements")

st.write("""
Possible future enhancements include:

- More Machine Learning Algorithms
- Hyperparameter Tuning
- Deep Learning Models
- Student Report Generation (PDF)
- Cloud Deployment
- Better Visualizations
- Authentication System
""")

st.divider()

# --------------------------------------------------------
# Developer
# --------------------------------------------------------

st.header("👨‍💻 Developer")

st.write("""
**Developed by**

**Abhinav**

B.Tech CSE (Cloud Computing & AI)

United University, Prayagraj
""")

st.divider()

# --------------------------------------------------------
# Thank You
# --------------------------------------------------------

st.success("""
Thank you for using the Student Placement Prediction System.
""")