import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# -----------------------------
# 1) Load dataset
# -----------------------------
file_path = "Decision_Tree_Large_Practice_Dataset.xlsx"
df = pd.read_excel(file_path)

print("=== Dataset Preview ===")
print(df.head())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Duplicate Rows ===")
print("Duplicates:", df.duplicated().sum())

# -----------------------------
# 2) Prepare features and target
# -----------------------------
X = df.drop(columns=['Customer_ID', 'Made_Purchase'])
y = df['Made_Purchase'].map({'Yes': 1, 'No': 0})

# Convert categorical columns into dummy variables
X_encoded = pd.get_dummies(X, drop_first=True)

# -----------------------------
# 3) Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# 4) Build SVC classifier with scaling
# -----------------------------
model = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42))
])
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# -----------------------------
# 5) Evaluate model
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
print("\n--- Model Evaluation ---")
print(f"Accuracy Score: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No', 'Yes']))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# 6) Confusion matrix plot
# -----------------------------
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title('SVC Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()

# -----------------------------
# 7) Hyperparameter tuning using GridSearchCV
# -----------------------------
param_grid = {
    'svc__C': [0.1, 1, 10, 100],
    'svc__kernel': ['linear', 'rbf', 'poly'],
    'svc__gamma': ['scale', 'auto', 0.1, 1]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\n=== Best Parameters Found by GridSearchCV ===")
print(grid_search.best_params_)

best_model = grid_search.best_estimator_
y_pred_tuned = best_model.predict(X_test)
accuracy_tuned = accuracy_score(y_test, y_pred_tuned)
print(f"\nTuned Model Test Accuracy: {accuracy_tuned * 100:.2f}%")
