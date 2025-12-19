from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from contextlib import asynccontextmanager
import numpy as np
import joblib
## Loading the model
ml_models={}

@asynccontextmanager
async def lifespan(app:FastAPI):
    try:
        ml_models["Lr"] =joblib.load("kidney_disease.joblib")
        print("Model is loaded!")
    except Exception as e:
        print(f"Model is not Loaded!:{e}")
    yield
    ml_models.clear()

app =FastAPI(lifespan=lifespan)

## Cheacking the health
@app.get("/health")
def health_check():
    return{"status":"online","model":"Loaded"}

## Validity of the Input
class PatientInput(BaseModel):
    Age: float
    Blood_pressure: float
    Specific_gravity: float
    albumin: float
    Sugar: float
    Red_blood_cells: int
    Pus_cell: int
    Pus_cell_clumps: int
    Bacteria: int
    Blood_glucose_random: float
    Blood_urea: float
    Serum_creatinine: float
    Sodium: float
    Potassium: float
    Haemoglobin: float
    Packed_cell_volume: float
    White_blood_cell_count: float
    Red_blood_cell_count: float
    Hypertension: int
    Diabetes_mellitus: int
    Coronary_artery_disease: int
    Appetite: int
    Peda_edema: int
    Aanemia: int


## Prediction
@app.post("/predict")
def predict_kidney_disease(data:PatientInput):
    model =ml_models.get("Lr")
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not Loaded!")
        
    input_values=[list(data.model_dump().values())]

    try:
        prediction = model.predict(input_values)
        probability= model.predict_proba(input_values).max()

        return {
            "prediction": int(prediction[0]),
            "result": "Patient have a Disease" if prediction[0] == 1 else "Patient do no have a Disease",
            "confidence": f"{round(probability * 100, 2)}%"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference error: {str(e)}")
    
    
