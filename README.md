# water-quality-prediction
End-to-end ML project: water quality analysis, model training &amp; Flask web app for safe water prediction.
# 💧 Water Quality Prediction using XGBoost & Flask

This project is an **end-to-end Machine Learning application** that predicts the **potability of water** (whether water is safe for drinking) based on chemical properties.  
The model is trained using **XGBoost Classifier** (highest accuracy among tested models) and deployed using **Flask** with a simple web interface.

---

## 🚀 Features
- Data preprocessing & cleaning (handling missing values)
- Exploratory Data Analysis (EDA) with visualizations
- Model training using multiple ML algorithms
- Final deployment with **XGBoost (highest accuracy)**
- Flask-based web app for real-time predictions
- Styled frontend with background image & form

---

## 📊 Dataset
The dataset used is **Water Potability Dataset** (available on Kaggle).  
It contains water quality metrics such as:
- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity
- Potability (Target variable)

---

## ⚙️ Tech Stack
- **Python 3**
- **Flask** (Backend Framework)
- **Scikit-learn, XGBoost** (Machine Learning)
- **Pandas, Numpy** (Data Processing)
- **Matplotlib, Seaborn, Plotly** (Visualization)
- **HTML, CSS** (Frontend UI)

---

## 📂 Project Structure
water-quality-prediction/
│
├─ app.py # Flask app (loads scaler + XGBoost, serves UI)
├─ train_model.py # Script to train XGBoost & save model + scaler
├─ water_potability.csv # Dataset (place here; not committed if large)
├─ water_quality_model.pkl # Saved model (created after training) - optional to commit
├─ scaler.pkl # Saved StandardScaler (created after training)
├─ requirements.txt # Python dependencies
├─ README.md
│
├─ templates/
│ ├─ index.html # Input form (all features)
│ └─ result.html # Prediction result page
│
└─ static/
├─ style.css # Styles (includes background)
├─ testing-water-quality-lab.jpeg # Background image
├─ screenshot_home.png # Optional screenshot for README
└─ screenshot_result.png


---

## 🔧 Setup & Installation

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/water-quality-prediction.git
cd water-quality-prediction


(Recommended) Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Train the model (creates water_quality_model.pkl and scaler.pkl):

python train_model.py


If you already have the trained .pkl files, place them in the project root.

Run the web app:

python app.py


Open in browser:

http://127.0.0.1:5000

🧠 How it works (summary)

train_model.py: loads water_potability.csv, imputes missing values, standardizes features, trains XGBoost, and saves water_quality_model.pkl + scaler.pkl.

app.py: loads the saved model and scaler, renders index.html for inputs, scales incoming data, predicts potability, and renders result.html with result + confidence.

🛠 Troubleshooting

Blank page / TemplateNotFound → ensure templates/ folder is next to app.py and files are named correctly.

Model not found → run python train_model.py or place water_quality_model.pkl & scaler.pkl in project root.

Windows path error (unicodeescape) → use forward slashes (C:/path/...) or raw strings for paths.

Port in use → modify app.run(..., port=5001).

♻️ Notes on committing models & data

Large datasets and model binaries can bloat the repo. Consider:

Adding water_quality_model.pkl and water_potability.csv to .gitignore and including instructions to generate them with train_model.py.

Or upload large files as [GitHub Releases] or use Git LFS.

🧾 Requirements

See requirements.txt for exact packages. To generate from your environment:

pip freeze > requirements.txt


Minimal required packages:

flask
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
plotly

🖼 Screenshots

Add screenshots to static/ and reference them here:

![Home](static/screenshot_home.png)
![Result](static/screenshot_result.png)

👤 Author

Your Shahabudeen H — MCA Graduate | Python & Backend Developer
GitHub: https://github.com/shahabudeen-h

LinkedIn: https://www.linkedin.com/in/shahabudeen-h-389597326
