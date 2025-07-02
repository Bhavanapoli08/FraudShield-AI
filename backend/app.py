from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="An API that detects credit card fraud using ML model.",
    version="1.0.0"
)

# Load model once
model = joblib.load('credit_fraud.pkl')

@app.get("/", response_class=PlainTextResponse)
async def root():
    return """
🚀 Credit Card Fraud Detection API is running!

📌 Visit /docs for Swagger UI or /redoc for ReDoc.
"""

@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.png")

# Define request schema
class fraudDetection(BaseModel):
    step: int
    types: int
    amount: float
    oldbalanceorig: float
    newbalanceorig: float
    oldbalancedest: float
    newbalancedest: float
    isflaggedfraud: float

# Prediction Endpoint
@app.post('/predict')
def predict(data: fraudDetection):
    features = np.array([[data.step, data.types, data.amount,
                          data.oldbalanceorig, data.newbalanceorig,
                          data.oldbalancedest, data.newbalancedest,
                          data.isflaggedfraud]])
    
    try:
        prediction = model.predict(features)[0]
        result = "fraudulent" if prediction == 1 else "not fraudulent"
        return {"result": result}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
