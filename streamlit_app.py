import streamlit as st
import json
import requests
import requests as re

st.title("Credit Card Fraud Detection Web App")

st.image("image.png")

st.write("""# FRAUDSHIELD-AI: Credit Card Fraud Detection
![image.png](https://github.com/Nneji123/Credit-Card-Fraud-Detection/raw/main/image.png)

# Problem Statement
Credit card fraud is a form of identity theft that involves the unauthorized use of someone else's credit card information to make purchases or withdraw funds.

This project builds a machine learning model capable of detecting fraudulent transactions using key features such as transaction amount, type, and account balances before and after the transaction.

🔍 Dataset
The dataset used in this project is available on Kaggle:
👉 PaySim Dataset on Kaggle :[https://www.kaggle.com/datasets/ealaxi/paysim1]

👨‍💻 Developed by
FraudShield AI Team

Bhavana Poli (Project Lead & Developer)""")



st.sidebar.header("Input Features of the Transaction")

sender_name = st.sidebar.text_input("Sender ID")
receiver_name = st.sidebar.text_input("Receiver ID")
step = st.sidebar.slider("Hours it took the Transaction to complete:", 0, 744, 0)

st.sidebar.subheader("Transaction Type:")
st.sidebar.markdown("""
- 0: Cash In  
- 1: Cash Out  
- 2: Debit  
- 3: Payment  
- 4: Transfer
""")
types = st.sidebar.selectbox("Select Type", (0, 1, 2, 3, 4))
type_map = ['Cash In', 'Cash Out', 'Debit', 'Payment', 'Transfer']
x = type_map[types]

amount = st.sidebar.number_input("Amount ($)", 0, 1000000)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before Transaction", 0, 1000000)
newbalanceorg = st.sidebar.number_input("Sender Balance After Transaction", 0, 1000000)
oldbalancedest = st.sidebar.number_input("Recipient Balance Before Transaction", 0, 1000000)
newbalancedest = st.sidebar.number_input("Recipient Balance After Transaction", 0, 1000000)

# Automatic flag based on amount
isflaggedfraud = 1 if amount >= 200000 else 0

# ------------------- Prediction Logic -------------------
if st.button("Detection Result"):
    if sender_name.strip() == '' or receiver_name.strip() == '':
        st.error("⚠️ Please enter both Sender and Receiver IDs.")
    else:
        data = {
            "step": step,
            "types": types,
            "amount": amount,
            "oldbalanceorig": oldbalanceorg,
            "newbalanceorig": newbalanceorg,
            "oldbalancedest": oldbalancedest,
            "newbalancedest": newbalancedest,
            "isflaggedfraud": isflaggedfraud
        }

        st.write("### Transaction Details:")
        st.json({
            "Sender ID": sender_name,
            "Receiver ID": receiver_name,
            "Type": x,
            "Amount": amount,
            "Sender Balance Before": oldbalanceorg,
            "Sender Balance After": newbalanceorg,
            "Recipient Balance Before": oldbalancedest,
            "Recipient Balance After": newbalancedest,
            "Flagged (auto)": isflaggedfraud
        })

        try:
            response = requests.post("https://credit-fraud-ml-api.herokuapp.com/predict", json=data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"✅ The transaction between **{sender_name}** and **{receiver_name}** is **{result['result'].upper()}**.")
            else:
                st.error("❌ API returned an error. Please check your backend or try again later.")
        except Exception as e:
            st.error(f"❌ Could not connect to API: {e}")