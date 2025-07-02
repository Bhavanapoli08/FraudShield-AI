import streamlit as st
import pandas as pd
import numpy as np
import json
import requests  # ✅ Use full 'requests', not 're'

# -------------------- UI HEADER --------------------
st.title("FraudShield AI – Credit Card Fraud Detection")

st.image("https://github.com/Nneji123/Credit-Card-Fraud-Detection/raw/main/image.png")

st.markdown("""
### 🔐 Problem Statement
Credit card fraud is the unauthorized use of someone else's credit card to make purchases or withdraw funds.

This app uses a machine learning model served via FastAPI to predict whether a transaction is **fraudulent or legitimate** based on the transaction details.

**Dataset:** [PaySim Dataset on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)  
**Made by:** Bhavana Poli (Project Lead & Developer)
""")

# -------------------- SIDEBAR INPUTS --------------------
st.sidebar.header('🧾 Transaction Details')

sender_name = st.text_input("Sender ID")
receiver_name = st.text_input("Receiver ID")
step = st.sidebar.slider('⏱️ Hours it took for the transaction:', min_value=0, max_value=100)

types = st.sidebar.selectbox(
    "💳 Type of Transfer:",
    (0, 1, 2, 3, 4),
    format_func=lambda x: ['Cash In', 'Cash Out', 'Debit', 'Payment', 'Transfer'][x]
)

amount = st.sidebar.number_input("💵 Amount ($)", min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before ($)", min_value=0, max_value=110000)
newbalanceorg = st.sidebar.number_input("Sender Balance After ($)", min_value=0, max_value=110000)
oldbalancedest = st.sidebar.number_input("Receiver Balance Before ($)", min_value=0, max_value=110000)
newbalancedest = st.sidebar.number_input("Receiver Balance After ($)", min_value=0, max_value=110000)

isflaggedfraud = st.sidebar.selectbox('🚩 Flagged as Fraud by System?', (0, 1))

# -------------------- ON SUBMIT --------------------
if st.button("🔍 Detect Fraud"):

    if sender_name.strip() == "" or receiver_name.strip() == "":
        st.error("❌ Please enter both Sender and Receiver IDs.")
    else:
        # ✅ Match keys with FastAPI backend
        values = {
            'step': step,
            'types': types,
            'amount': amount,
            'oldbalanceorig': oldbalanceorg,
            'newbalanceorig': newbalanceorg,
            'oldbalancedest': oldbalancedest,
            'newbalancedest': newbalancedest,
            'isflaggedfraud': isflaggedfraud
        }

        try:
            # ⚠️ Change to local if running locally
            res = requests.post("http://127.0.0.1:8000/predict", json=values)

            if res.status_code == 200:
                response = res.json()
                if 'result' in response:
                    st.success(f"✅ The transaction between **{sender_name}** and **{receiver_name}** is **{response['result'].upper()}**.")
                else:
                    st.warning(f"⚠️ Unexpected response format: {response}")
            else:
                st.error("⚠️ API responded with an error. Please check the request or try again later.")

        except Exception as e:
            st.error(f"❌ Failed to connect to prediction API.\n\nError: {e}")








