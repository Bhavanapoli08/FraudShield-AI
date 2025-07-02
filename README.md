# 💳 FraudShield AI – Credit Card Fraud Detection

![GitHub repo size](https://img.shields.io/github/repo-size/Bhavanapoli08/FraudShield-AI)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/github/license/Bhavanapoli08/FraudShield-AI)


FraudShield AI is a machine learning-powered web app that detects **fraudulent credit card transactions** using key features like transaction type, balances, and timing. It is built using **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🚀 Demo

📺 [Live Demo (Optional: Add your deployed URL)](https://your-live-demo-url.com)

---

## 🧠 Tech Stack

| Component    | Tech Used            |
|--------------|----------------------|
| Backend API  | FastAPI (Python)     |
| ML Model     | Scikit-learn         |
| Frontend     | Streamlit            |
| Dataset      | [PaySim on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1) |
| Deployment   | Localhost / Docker / (Coming Soon) |

---

## 📦 Features

- ✅ Real-time fraud prediction
- 📈 Trained on simulated transaction dataset (PaySim)
- 🔐 Fraud detection based on:
  - Amount
  - Transaction type
  - Balance changes
  - Hours elapsed
- 💻 Clean UI via Streamlit
- 🔗 API integration between frontend and ML backend


## 🛠️ Installation Guide

### 🔹 1. Clone the repository

```bash
git clone https://github.com/Bhavanapoli08/FraudShield-AI.git
cd FraudShield-AI

🔹 2. Create virtual environment and install dependencies

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

🔹 3. Run the FastAPI backend

cd backend
uvicorn app:app --reload
Check: http://127.0.0.1:8000/docs

🔹 4. Run the Streamlit frontend
Open new terminal tab:
cd frontend
streamlit run app.py
Visit: http://localhost:8501

📂 Folder Structure

FraudShield-AI/
├── backend/               # FastAPI backend
│   └── app.py
├── frontend/              # Streamlit frontend
│   └── app.py
├── credit_fraud.pkl       # Trained ML model
├── requirements.txt
├── Dockerfile (optional)
└── README.md

🧪 Example Prediction
{
  "step": 10,
  "types": 3,
  "amount": 200,
  "oldbalanceorig": 1000,
  "newbalanceorig": 800,
  "oldbalancedest": 500,
  "newbalancedest": 700,
  "isflaggedfraud": 0
}

✅ Output

"not fraudulent"

This represents a legitimate payment (types: 3 = "Payment") where:

The amount is small ($200)

Balances are consistent before and after the transaction

The system did not flag it as suspicious
