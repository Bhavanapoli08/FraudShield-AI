from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""An API that uses a trained Machine Learning model to detect if a credit card transaction is fraudulent based on features like time, amount, and balances.""",
    version="1.0.0"
)

# Load model once during startup
model = joblib.load('credit_fraud.pkl')

# Health check endpoint
@app.get("/", response_class=PlainTextResponse)
async def running():
    return """
🚀 Credit Card Fraud Detection API is Running!

📌 Visit /docs for Swagger UI or /redoc for ReDoc.
"""

# Optional favicon route
@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.png')

# Request data model
class FraudDetection(BaseModel):
    step: int
    types: int
    amount: float
    oldbalanceorig: float
    newbalanceorig: float
    oldbalancedest: float
    newbalancedest: float
    isflaggedfraud: float

# Prediction endpoint
@app.post('/predict')
def predict(data: FraudDetection):
    try:
        features = np.array([[
            data.step,
            data.types,
            data.amount,
            data.oldbalanceorig,
            data.newbalanceorig,
            data.oldbalancedest,
            data.newbalancedest,
            data.isflaggedfraud
        ]])

        prediction = model.predict(features)[0]

        result = "fraudulent" if prediction == 1 else "not fraudulent"
        return {"result": result}
    
    except Exception as e:
        return {"error": f"Prediction failed. Reason: {str(e)}"}
