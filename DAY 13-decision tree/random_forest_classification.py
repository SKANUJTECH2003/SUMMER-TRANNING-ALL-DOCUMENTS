import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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
# 4) Build Random Forest classifier
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    criterion='entropy',
    max_depth=4,
    random_state=42
)
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
# 6) Feature importance plot
# -----------------------------
importances = pd.Series(model.feature_importances_, index=X_encoded.columns).sort_values(ascending=False)

plt.figure(figsize=(14, 7))
sns.barplot(x=importances.values, y=importances.index, orient='h')
plt.title('Random Forest Feature Importance')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()

# -----------------------------
# 7) Hyperparameter tuning using GridSearchCV
# -----------------------------
param_grid = {
    'n_estimators': [100, 200, 300],
    'criterion': ['gini', 'entropy', 'log_loss'],
    'max_depth': [2, 3, 4, 5, 6, None],
    'min_samples_split': [2, 3, 5, 10],
    'min_samples_leaf': [1, 2, 4, 6],
    'max_features': ['sqrt', 'log2', None]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
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
