import streamlit as st

# --------------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------------

st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------------

st.markdown("""
<style>

/* Background */
.stApp{
    background-color:#0F172A;
}

/* Headings */
h1,h2,h3{
    color:white;
}

/* Paragraphs */
p{
    color:#CBD5E1;
}

/* Cards */

.card{
    background-color:#1E293B;
    padding:25px;
    border-radius:15px;
    border:1px solid #334155;
    text-align:center;
}

.card:hover{
    border:1px solid #3B82F6;
}

/* Feature Cards */

.feature{
    background:#1E293B;
    padding:20px;
    border-radius:12px;
    border:1px solid #334155;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#111827;
}

/* Metric */

[data-testid="stMetric"]{
    background:#1E293B;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# TITLE
# --------------------------------------------------------

st.title("🎓 Student Placement Prediction System")

st.markdown("""
Predict whether a student is likely to be **Placed**
using **Machine Learning**.
""")

st.divider()

# --------------------------------------------------------
# METRICS
# --------------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Students",215)

with col2:
    st.metric("Features",12)

with col3:
    st.metric("Best Model","Logistic Regression")

with col4:
    st.metric("Accuracy","86.05 %")

st.write("")

# --------------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------------

st.header("📌 Project Overview")

st.write("""

This project predicts whether a student is likely to get
placed based on:

- Academic Performance
- Educational Background
- Employability Test
- Work Experience
- MBA Performance

The prediction is performed using a trained Machine
Learning model built with Scikit-Learn.

""")

st.write("")

# --------------------------------------------------------
# FEATURES
# --------------------------------------------------------

st.header("✨ Project Features")

c1,c2 = st.columns(2)

with c1:

    st.success("✔ Student Placement Prediction")

    st.success("✔ Interactive Dashboard")

    st.success("✔ Machine Learning Model")

    st.success("✔ Confidence Score")

with c2:

    st.success("✔ Dataset Explorer")

    st.success("✔ Model Performance")

    st.success("✔ Data Visualization")

    st.success("✔ Easy Navigation")

st.write("")

# --------------------------------------------------------
# TECHNOLOGIES
# --------------------------------------------------------

st.header("🛠 Technologies Used")

t1,t2,t3 = st.columns(3)

with t1:

    st.info("""
🐍 Python

📊 Pandas

📈 NumPy
""")

with t2:

    st.info("""
🤖 Scikit-Learn

🌐 Streamlit

📉 Matplotlib
""")

with t3:

    st.info("""
📊 Plotly

💾 Joblib

🎯 Machine Learning
""")

st.write("")

# --------------------------------------------------------
# HOW TO USE
# --------------------------------------------------------

st.header("🚀 How to Use")

st.write("""

1. Open **Prediction** page from sidebar.

2. Enter Student Details.

3. Click **Predict Placement**.

4. View Prediction Result.

5. Explore Dataset and Model Performance from sidebar.

""")

st.write("")

# --------------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------------

st.header("📂 Dataset")

st.write("""

**Dataset Name**

Campus Placement Dataset

**Rows**

215

**Features**

12

**Target Variable**

Status

""")

st.write("")

# --------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------

st.sidebar.title("Navigation")

st.sidebar.success("Select a page above.")

st.sidebar.markdown("---")

st.sidebar.info("""
🏠 Home

🎯 Prediction

📊 Dataset

📈 Model Performance

ℹ About
""")

# --------------------------------------------------------
# FOOTER
# --------------------------------------------------------

st.markdown("---")

st.markdown("""
<div class='footer'>

Made with ❤️ using Streamlit

</div>
""", unsafe_allow_html=True)