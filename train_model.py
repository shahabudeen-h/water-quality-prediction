import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("water_potability.csv")

# Handle missing values by filling with mean
df["ph"] = df["ph"].fillna(df["ph"].mean())
df["Sulfate"] = df["Sulfate"].fillna(df["Sulfate"].mean())
df["Trihalomethanes"] = df["Trihalomethanes"].fillna(df["Trihalomethanes"].mean())

# Features and target
X = df.drop("Potability", axis=1)
y = df["Potability"]

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(n_estimators=100, learning_rate=0.4)
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "water_quality_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained and saved as water_quality_model.pkl & scaler.pkl")
