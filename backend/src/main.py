from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.model.model_utils import load_model, preprocess_domains
from datetime import datetime

app = FastAPI()


# model
model = load_model()

# request schema
class DomainRequest(BaseModel):
    clean_domain: List[str]
    not_before: List[datetime]
    not_after: List[datetime]


# health check
@app.get("/health_check")
def health_check():
    return {"status": "ok"}


# hello endpoint
@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


# predict endpoint
@app.post("/predict")
def predict(request: DomainRequest):
    try:
        df = preprocess_domains(
            clean_domain_list=request.clean_domain,
            not_before_list=request.not_before,
            not_after_list=request.not_after
        )

        predictions = model.predict(df)
        return {"predictions": predictions.tolist()}

    except Exception as e:
        return {"error": str(e)}
        
