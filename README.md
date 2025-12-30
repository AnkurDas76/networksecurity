# 🔐 Network Security – Phishing Website Detection (End-to-End ML Project)

An end-to-end machine learning project to detect phishing websites using URL and website-based features. The system classifies websites as **Phishing** or **Legitimate** and serves predictions through a clean, production-ready **FastAPI** application.

Built with best ML engineering practices: modular code, custom logging & exception handling, data validation, experiment tracking with MLflow, and a deployable API.

## 🚨 Problem Statement

Phishing websites mimic trusted sites to steal sensitive information. As phishing tactics evolve, rule-based detection falls short.

**Goal**: Develop a machine learning model that automatically and accurately identifies phishing websites, integrated into a scalable REST API.

## 📊 Dataset

- **File**: `phishingdata.csv` (in `Network_Data/`)
- **Source**: Standard Phishing Websites Dataset (commonly used from UCI / PhishTank collections)
- **Rows**: 11,055
- **Columns**: 31 (30 features + 1 target)
- **Target Column**: `result`
  - `0` → Phishing
  - `1` → Legitimate
- **Features**: 30 engineered features from URLs and page content (URL length, IP presence, "@" symbols, SSL status, iframes, etc.)

## 🛠 Project Structure
networksecurity/
├── app.py                     # FastAPI application
├── final_model/               # Trained model & preprocessor
├── networksecurity/
│   ├── components/            # Data ingestion, preprocessing, training
│   ├── pipeline/              # Training & prediction pipelines
│   ├── utils/                 # Helper functions
│   ├── exception/             # Custom exception handling
│   └── logging/               # Centralized logging
├── data_schema/               # Data validation schema
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

## ⚙️ Machine Learning Pipeline

### Training Pipeline (`main.py`)
1. Data ingestion & validation
2. Preprocessing (scaling, encoding)
3. Model training & evaluation
4. Experiment tracking with **MLflow**
5. Saves final preprocessor and model to `final_model/`

### Prediction
- Loads saved artifacts
- Accepts batch CSV upload
- Returns styled HTML table with human-readable predictions

## 🚀 FastAPI Application (`app.py`)

### Endpoints

| Method | Endpoint   | Description                                      |
|--------|------------|--------------------------------------------------|
| GET    | `/`        | Redirects to interactive docs                    |
| GET    | `/docs`    | Swagger UI for testing                           |
| GET    | `/train`   | Triggers full training pipeline                  |
| POST   | `/predict` | Upload CSV → Beautiful results table with predictions |

##### Run Locally

uvicorn app:app --reload
Train: Visit "http://127.0.0.1:8000/train"
Predict: Use /docs → upload a CSV with the same 30 features → see results instantly

```bash
🛠 Tech Stack

Python 3.x
FastAPI + Uvicorn
Scikit-learn, Pandas, NumPy
MLflow,dagshub (experiment tracking)
Jinja2 + Bootstrap (for clean prediction display)
MongoDB (optional data ingestion)

🔮 Future Ideas (Not Implemented Yet)

Real-time URL → feature extraction → prediction
Cloud deployment (AWS, GCP, Render, etc.)
Frontend dashboard
API authentication

📚 What This Project Demonstrates

Complete end-to-end ML workflow
Clean, modular, maintainable code
Custom logging & exception handling
Batch inference via REST API
Production-ready API design with FastAPI

👨‍💻 Author
Ankur Das – Machine Learning Enthusiast

