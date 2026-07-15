import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("Placement_data_full_class.csv")

# ----------------------------------------
# Title
# ----------------------------------------

st.title("📊 Dataset Explorer")

st.write("Explore the Campus Placement Dataset used to train the Machine Learning model.")

st.divider()

# ----------------------------------------
# Dataset Overview
# ----------------------------------------

st.header("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

# ----------------------------------------
# Dataset Preview
# ----------------------------------------

st.header("📋 Dataset Preview")

st.dataframe(df, use_container_width=True)

# ----------------------------------------
# Data Types
# ----------------------------------------

st.header("📑 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df, use_container_width=True)

# ----------------------------------------
# Missing Values
# ----------------------------------------

st.header("❌ Missing Values")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(missing_df, use_container_width=True)

# ----------------------------------------
# Statistics
# ----------------------------------------

st.header("📈 Statistical Summary")

st.dataframe(df.describe(), use_container_width=True)

# ----------------------------------------
# Placement Distribution
# ----------------------------------------

st.header("📊 Placement Distribution")

fig, ax = plt.subplots(figsize=(5,4))

df["status"].value_counts().plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Placement Status")
ax.set_ylabel("Count")
ax.set_title("Placement Distribution")

st.pyplot(fig)

# ----------------------------------------
# Histograms
# ----------------------------------------

st.header("📉 Feature Distributions")

numeric_columns = [
    "ssc_p",
    "hsc_p",
    "degree_p",
    "etest_p",
    "mba_p"
]

feature = st.selectbox(
    "Select Numerical Feature",
    numeric_columns
)

fig, ax = plt.subplots(figsize=(7,4))

ax.hist(df[feature], bins=15)

ax.set_xlabel(feature)
ax.set_ylabel("Frequency")
ax.set_title(feature)

st.pyplot(fig)

# ----------------------------------------
# Correlation Heatmap
# ----------------------------------------

st.header("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(8,6))

heat = ax.imshow(corr)

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90)

ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

plt.colorbar(heat)

st.pyplot(fig)

# ----------------------------------------
# Footer
# ----------------------------------------

st.divider()

st.caption("Campus Placement Dataset | Student Placement Prediction Project")