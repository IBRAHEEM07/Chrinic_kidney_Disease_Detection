
# 🩺 Chronic Kidney Disease Prediction API

## 📌 Overview
This project is an **end-to-end Machine Learning application** for predicting **Chronic Kidney Disease (CKD)** using patient medical data.

The trained ML model is deployed using **FastAPI** and exposed as a REST API that accepts patient data and returns a prediction with confidence score.

This project demonstrates **real-world Data Science + Development skills**, not just model training.

---

## 🎯 Problem Statement
Chronic Kidney Disease is often diagnosed late due to lack of early detection.  
This project predicts the likelihood of CKD using clinical attributes such as blood pressure,Albumin, Hypertension, and other medical indicators.

---

## 🗂 Dataset
- Dataset: Chronic Kidney Disease from Kaggle
- Format: CSV
- Target: Presence of kidney disease (Binary Classification)

### Key Features
- Age
- Blood Pressure
- Specific Gravity
- Albumin
- Sugar
- Serum Creatinine
- Hemoglobin
- Diabetes Mellitus
- Hypertension

---

## 🧠 Machine Learning
- Algorithm: Logistic Regression-Supervised Classification (Scikit-learn)
- Data preprocessing & feature engineering
- Model trained in Jupyter Notebook
- Model saved using `joblib`

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib

---

## 📁 Project Structure
```

chronic-kidney-disease-prediction-api/
│
├── app/
│   └── main.py              # FastAPI application
│
├── model/
│   └── kidney_model.joblib  # Trained ML model
│
├── data/
│   └── kidney_disease.csv   # Dataset
│
├── notebooks/
│   └── kidney_disease_training.ipynb
│
├── requirements.txt
└── README.md

````

---

## 🚀 API Usage

### Endpoint
**POST** `/predict`

### Sample Request
```json
{
  "Age": 45,
  "Blood_pressure": 120,
  "Specific_gravity": 1.02,
  "albumin": 1,
  "Sugar": 0,
  "Red_blood_cells": 1,
  "Pus_cell": 0,
  "Pus_cell_clumps": 0,
  "Bacteria": 0,
  "Blood_glucose_random": 110,
  "Blood_urea": 25,
  "Serum_creatinine": 1.1,
  "Sodium": 140,
  "Potassium": 4.0,
  "Haemoglobin": 14,
  "Packed_cell_volume": 42,
  "White_blood_cell_count": 8000,
  "Red_blood_cell_count": 4.5,
  "Hypertension": 1,
  "Diabetes_mellitus": 0,
  "Coronary_artery_disease": 0,
  "Appetite": 1,
  "Peda_edema": 0,
  "Aanemia": 0
}
````

### Sample Response

```json
{
  "prediction": 1,
  "result": "Patient have a Disease",
  "confidence": "99.05%"
}
```

---

## ▶ Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start API server

```bash
uvicorn app.main:app --reload
```

### Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Model Testing

* Tested using:

  * Swagger UI
  * Python `requests` library
* API successfully returns predictions with confidence score

---

## 🚀 Future Improvements

* Dockerize the application
* Deploy to cloud (AWS / Render / Railway)
* Add authentication
* Model monitoring

---

## 👤 Author

**Muhammad Ibraheem**
Aspiring Data Scientist | Machine Learning Engineer




