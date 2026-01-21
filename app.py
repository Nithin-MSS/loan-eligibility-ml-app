import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/loan_eligibility_data.csv")

# Encode categorical column
df = pd.get_dummies(df, columns=["Employment_Type"], drop_first=True)

# Split features and target
X = df.drop("Eligibility_Status", axis=1)
y = df["Eligibility_Status"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ---------------- STREAMLIT UI ----------------
st.title("🏦 Loan Eligibility & Credit Scoring System")

st.write("Enter applicant details to check loan eligibility")

age = st.slider("Age", 21, 65, 30)
income = st.number_input("Monthly Income", 15000, 150000, step=5000)
loan_amount = st.number_input("Loan Amount", 50000, 1000000, step=10000)
loan_tenure = st.slider("Loan Tenure (months)", 6, 60, 24)
existing_emi = st.number_input("Existing EMI", 0, 50000, step=1000)
past_default = st.selectbox("Past Default", [0, 1])
credit_score = st.slider("Credit Score", 300, 850, 650)
employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])

# Prepare input data
input_data = pd.DataFrame({
    "Age": [age],
    "Monthly_Income": [income],
    "Loan_Amount": [loan_amount],
    "Loan_Tenure": [loan_tenure],
    "Existing_EMI": [existing_emi],
    "Past_Default": [past_default],
    "Credit_Score": [credit_score],
    "Employment_Type_Self-Employed": [1 if employment == "Self-Employed" else 0]
})

# Scale input
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Check Eligibility"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 2:
        st.success("✅ Loan Approved (Low Risk)")
    elif prediction == 1:
        st.warning("⚠️ Manual Review Required (Medium Risk)")
    else:
        st.error("❌ Loan Rejected (High Risk)")
