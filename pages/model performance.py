import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------------
# Load Metrics
# -------------------------------------------------------

try:
    with open("model_metrics.json", "r") as file:
        metrics = json.load(file)
except FileNotFoundError:
    st.error("❌ model_metrics.json not found. Please run train_model.py first.")
    st.stop()

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("📈 Model Performance Dashboard")
st.markdown("View the performance of the trained Machine Learning model.")

st.divider()

# -------------------------------------------------------
# Best Model
# -------------------------------------------------------

st.success(f"🏆 Best Model : **{metrics['best_model']}**")

# -------------------------------------------------------
# Performance Metrics
# -------------------------------------------------------

st.subheader("📊 Evaluation Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        f"{metrics['accuracy']}%"
    )

with col2:
    st.metric(
        "Precision",
        f"{metrics.get('precision','--')}%"
    )

with col3:
    st.metric(
        "Recall",
        f"{metrics.get('recall','--')}%"
    )

with col4:
    st.metric(
        "F1 Score",
        f"{metrics.get('f1_score','--')}%"
    )

st.divider()

# -------------------------------------------------------
# Accuracy Progress
# -------------------------------------------------------

st.subheader("🎯 Model Accuracy")

accuracy = metrics["accuracy"]

st.progress(int(accuracy))

st.write(f"Current Accuracy : **{accuracy}%**")

st.divider()

# -------------------------------------------------------
# Confusion Matrix
# -------------------------------------------------------

if "confusion_matrix" in metrics:

    st.subheader("📉 Confusion Matrix")

    cm = np.array(metrics["confusion_matrix"])

    fig, ax = plt.subplots(figsize=(5,5))

    image = ax.imshow(cm)

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j,
                i,
                cm[i,j],
                ha="center",
                va="center",
                fontsize=15,
                color="white"
            )

    ax.set_xticks([0,1])
    ax.set_yticks([0,1])

    ax.set_xticklabels(["Not Placed","Placed"])
    ax.set_yticklabels(["Not Placed","Placed"])

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    plt.colorbar(image)

    st.pyplot(fig)

st.divider()

# -------------------------------------------------------
# Performance Summary
# -------------------------------------------------------

st.subheader("📌 Model Summary")

st.info(f"""

✅ Best Model : {metrics['best_model']}

✅ Accuracy : {metrics['accuracy']}%

✅ Precision : {metrics.get('precision','--')}%

✅ Recall : {metrics.get('recall','--')}%

✅ F1 Score : {metrics.get('f1_score','--')}%

""")

st.divider()

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.caption("Student Placement Prediction System | Machine Learning Dashboard")