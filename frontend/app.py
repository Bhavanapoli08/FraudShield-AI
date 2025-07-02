import streamlit as st
import json
import requests

# -------------------- HEADER --------------------
st.title("💳 Credit Card Fraud Detection Web App")
st.image("image.png")

st.markdown("""
## 🧾# FRAUDSHIELD-AI: Credit Card Fraud Detection
![image.png](https://github.com/Nneji123/Credit-Card-Fraud-Detection/raw/main/image.png)

# Problem Statement
Credit card fraud is a form of identity theft that involves the unauthorized use of someone else's credit card information to make purchases or withdraw funds.

This project builds a machine learning model capable of detecting fraudulent transactions using key features such as transaction amount, type, and account balances before and after the transaction.

🔍 Dataset
The dataset used in this project is available on Kaggle:
👉 PaySim Dataset on Kaggle :[https://www.kaggle.com/datasets/ealaxi/paysim1]

👨‍💻 Developed by
FraudShield AI Team

Bhavana Poli (Project Lead & Developer)
""")

# -------------------- SIDEBAR --------------------
st.sidebar.header('📥 Input Transaction Features')

sender_name = st.sidebar.text_input("👤 Sender ID")
receiver_name = st.sidebar.text_input("👤 Receiver ID")
step = st.sidebar.slider("⏱️ Hours taken to complete transaction", 0, 100)

st.sidebar.markdown("#### 💳 Type of Transaction")
st.sidebar.markdown("""
- 0: Cash In  
- 1: Cash Out  
- 2: Debit  
- 3: Payment  
- 4: Transfer
""")

types = st.sidebar.selectbox("Select Type", (0, 1, 2, 3, 4))
type_mapping = ['Cash In', 'Cash Out', 'Debit', 'Payment', 'Transfer']
type_text = type_mapping[types]

amount = st.sidebar.number_input("💵 Amount ($)", 0, 110000)
oldbalanceorg = st.sidebar.number_input("🏦 Sender Balance Before", 0, 110000)
newbalanceorg = st.sidebar.number_input("🏦 Sender Balance After", 0, 110000)
oldbalancedest = st.sidebar.number_input("🏦 Recipient Balance Before", 0, 110000)
newbalancedest = st.sidebar.number_input("🏦 Recipient Balance After", 0, 110000)
isflaggedfraud = st.sidebar.selectbox("🚩 System Flagged as Fraud?", (0, 1))

# -------------------- PREDICTION --------------------
if st.button("🔍 Detection Result"):

    if not sender_name.strip() or not receiver_name.strip():
        st.error("❗ Please enter both Sender and Receiver IDs.")
    else:
        values = {
            "step": step,
            "types": types,
            "amount": amount,
            "oldbalanceorig": oldbalanceorg,
            "newbalanceorig": newbalanceorg,
            "oldbalancedest": oldbalancedest,
            "newbalancedest": newbalancedest,
            "isflaggedfraud": isflaggedfraud
        }

        # 🧾 Display input details
        st.subheader("📄 Transaction Summary")
        st.markdown(f"""
- **Sender ID:** {sender_name}  
- **Receiver ID:** {receiver_name}  
- **Transaction Type:** {type_text}  
- **Hours Taken:** {step}  
- **Amount:** ${amount}  
- **Sender Before:** ${oldbalanceorg}  
- **Sender After:** ${newbalanceorg}  
- **Receiver Before:** ${oldbalancedest}  
- **Receiver After:** ${newbalancedest}  
- **System Flagged Fraud?:** {isflaggedfraud}
""")

        try:
            # 🔗 API Endpoint
            api_url = "http://127.0.0.1:8000/predict"  # Or use Docker hostname if needed

            res = requests.post(api_url, json=values)

            if res.status_code == 200:
                result = res.json()
                result_text = result["result"]
                st.success(f"✅ The transaction is **{result_text.upper()}**")
            else:
                st.error("⚠️ Received an invalid response from the prediction API.")

        except Exception as e:
            st.error(f"❌ Failed to connect to the API.\n\nError: {e}")





