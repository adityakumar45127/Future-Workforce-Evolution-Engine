import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


# ============================================================
# 1. Load Dataset
# ============================================================

df = pd.read_csv("data/processed/career_dataset.csv")

print("Dataset Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())


# ============================================================
# 2. Features and Target
# ============================================================

X = df.drop("Career", axis=1)
y = df["Career"]


# ============================================================
# 3. Encode Target
# ============================================================

encoder = LabelEncoder()
y = encoder.fit_transform(y)


# ============================================================
# 4. Train-Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining Shape:", X_train.shape)
print("Test Shape:", X_test.shape)


# ============================================================
# 5. Random Forest Hyperparameter Tuning
# ============================================================

rf = RandomForestClassifier(
    random_state=42
)


param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 5, 10, 15],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["sqrt", "log2"]
}


grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring="f1_weighted",
    n_jobs=-1,
    verbose=1
)


print("\nStarting Random Forest Hyperparameter Tuning...")

grid_search.fit(X_train, y_train)


# ============================================================
# 6. Best Model
# ============================================================

best_model = grid_search.best_estimator_

print("\n========================================")
print("       BEST MODEL PARAMETERS")
print("========================================")

print(grid_search.best_params_)
print("Best CV F1 Score:", round(grid_search.best_score_, 4))


# ============================================================
# 7. Final Test Prediction
# ============================================================

y_pred = best_model.predict(X_test)


# ============================================================
# 8. Final Evaluation
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)


print("\n========================================")
print("       FINAL RANDOM FOREST RESULTS")
print("========================================")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")


print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# 9. Dataset Information
# ============================================================

print("\n========================================")
print("          DATASET INFORMATION")
print("========================================")

print("Total Dataset :", X.shape)
print("Training Set  :", X_train.shape)
print("Test Set      :", X_test.shape)
print("Features      :", X.shape[1])
print("Classes       :", len(encoder.classes_))


# ============================================================
# 10. Save Best Model
# ============================================================

joblib.dump(
    best_model,
    "models/career_model.pkl"
)

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)

print("\nBest Random Forest model saved successfully.")