import pandas as pd
import joblib
import json

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("Placement_data_full_class.csv")

print("\nDataset Loaded Successfully\n")

# ===============================
# Data Cleaning
# ===============================

df.drop(columns=["sl_no", "salary"], inplace=True)

# ===============================
# Features & Target
# ===============================

X = df.drop("status", axis=1)
y = df["status"]

# Convert target to numeric
y = y.map({
    "Placed": 1,
    "Not Placed": 0
})

# ===============================
# Feature Types
# ===============================

categorical_features = [
    "gender",
    "ssc_b",
    "hsc_b",
    "hsc_s",
    "degree_t",
    "workex",
    "specialisation"
]

numeric_features = [
    "ssc_p",
    "hsc_p",
    "degree_p",
    "etest_p",
    "mba_p"
]

# ===============================
# Preprocessor
# ===============================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numeric_features
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ===============================
# Logistic Regression Pipeline
# ===============================

lr_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# ===============================
# Random Forest Pipeline
# ===============================

rf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ))
])

# ===============================
# Train Models
# ===============================

lr_pipeline.fit(X_train, y_train)
rf_pipeline.fit(X_train, y_train)

# ===============================
# Predictions
# ===============================

lr_pred = lr_pipeline.predict(X_test)
rf_pred = rf_pipeline.predict(X_test)

# ===============================
# Evaluation Function
# ===============================

def evaluate(name, y_true, y_pred):

    print("\n" + "="*60)
    print(name)
    print("="*60)

    print("Accuracy :", round(accuracy_score(y_true, y_pred)*100,2),"%")
    print("Precision:", round(precision_score(y_true, y_pred)*100,2),"%")
    print("Recall   :", round(recall_score(y_true, y_pred)*100,2),"%")
    print("F1 Score :", round(f1_score(y_true, y_pred)*100,2),"%")

    print("\nConfusion Matrix\n")
    print(confusion_matrix(y_true, y_pred))

    print("\nClassification Report\n")
    print(classification_report(y_true, y_pred))

evaluate("Logistic Regression", y_test, lr_pred)
evaluate("Random Forest", y_test, rf_pred)

# ===============================
# Choose Best Model
# ===============================

lr_acc = accuracy_score(y_test, lr_pred)
rf_acc = accuracy_score(y_test, rf_pred)

if rf_acc >= lr_acc:
    best_model = rf_pipeline
    best_name = "Random Forest"
    best_acc = rf_acc
else:
    best_model = lr_pipeline
    best_name = "Logistic Regression"
    best_acc = lr_acc

print("\nBest Model:", best_name)
print("Accuracy:", round(best_acc*100,2), "%")

# ===============================
# Save Best Model
# ===============================
metrics = {
    "best_model": best_name,
    "accuracy": round(best_acc * 100, 2),
    "precision": round(
        precision_score(
            y_test,
            lr_pred if best_name == "Logistic Regression" else rf_pred
        ) * 100,
        2
    ),
    "recall": round(
        recall_score(
            y_test,
            lr_pred if best_name == "Logistic Regression" else rf_pred
        ) * 100,
        2
    ),
    "f1_score": round(
        f1_score(
            y_test,
            lr_pred if best_name == "Logistic Regression" else rf_pred
        ) * 100,
        2
    ),
    "confusion_matrix": (
        confusion_matrix(
            y_test,
            lr_pred if best_name == "Logistic Regression" else rf_pred
        ).tolist()
    )
}
with open("model_metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

joblib.dump(best_model, "placement_model.pkl")

print("\nModel Saved Successfully!")