import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load data
df = pd.read_csv('/home/mokshith/burnout_project/student_data.csv')

# Prepare features and target
X = df.drop(['student_id', 'burnout_risk'], axis=1)
y = df['burnout_risk']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Model Performance:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model
with open('/home/mokshith/burnout_project/burnout_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save feature names
with open('/home/mokshith/burnout_project/feature_names.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)

print("\nModel saved successfully!")
print(f"\nFeature Importance:")
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")
