from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler if available
model_path = "water_quality_model.pkl"
scaler_path = "scaler.pkl"

model = joblib.load(model_path) if os.path.exists(model_path) else None
scaler = joblib.load(scaler_path) if os.path.exists(scaler_path) else None

@app.route("/")
def home():
    if model is None or scaler is None:
        return "<h2 style='color:red;'>Model not trained yet. Please run train_model.py first.</h2>"
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or scaler is None:
        return "<h2 style='color:red;'>Model not available. Train it first.</h2>"
    try:
        features = [float(request.form[key]) for key in request.form]
        features = np.array(features).reshape(1, -1)
        features = scaler.transform(features)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][prediction]
        result = "Safe to Drink 💧" if prediction == 1 else "Not Safe to Drink ⚠️"
        return render_template("result.html", result=result, probability=round(probability * 100, 2))
    except Exception as e:
        return f"<h3 style='color:red;'>Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
