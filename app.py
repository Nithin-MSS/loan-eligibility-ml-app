import streamlit as st
import pandas as pd

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Loan Eligibility & Risk Scoring",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Eligibility & Credit Risk Scoring System")
st.write(
    "An end-to-end system to assess loan eligibility and credit risk "
    "using financial and behavioral indicators."
)

# ------------------------------
# Load Dataset (for reference)
# ------------------------------
df = pd.read_csv("Data/loan_eligibility_data.csv")

# ------------------------------
# Risk Score Function
# ------------------------------
def calculate_risk_score(
    age,
    income,
    loan_amount,
    tenure_months,
    existing_emi,
    past_default,
    credit_score,
    employment_type
):
    score = 100

    # Credit score impact
    if credit_score < 600:
        score -= 25
    elif credit_score < 700:
        score -= 10

    # Past default penalty
    if past_default == 1:
        score -= 30

    # EMI burden check
    if existing_emi > 0.4 * income:
        score -= 20

    # Employment stability
    if employment_type == "Self-Employed":
        score -= 10

    # Loan to income ratio
    if loan_amount > income * 10:
        score -= 10

    return max(score, 0)

# ------------------------------
# User Inputs
# ------------------------------
st.subheader("📥 Applicant Details")

age = st.slider("Age", 21, 65, 30)

income = st.number_input(
    "Monthly Income (₹)",
    min_value=5000,
    step=1000
)

loan_amount = st.number_input(
    "Loan Amount (₹)",
    min_value=50000,
    step=10000
)

tenure_months = st.slider(
    "Loan Tenure (Months)",
    min_value=6,
    max_value=600,   # Up to 50 years
    value=120,
    step=6
)

existing_emi = st.number_input(
    "Existing Monthly EMI (₹)",
    min_value=0,
    step=1000
)

credit_score = st.slider(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700
)

employment_type = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-Employed"]
)

past_default = st.selectbox(
    "Past Default History",
    ["No", "Yes"]
)

past_default = 1 if past_default == "Yes" else 0

# ------------------------------
# Eligibility Check
# ------------------------------
if st.button("🔍 Check Loan Eligibility"):

    risk_score = calculate_risk_score(
        age,
        income,
        loan_amount,
        tenure_months,
        existing_emi,
        past_default,
        credit_score,
        employment_type
    )

    st.subheader("📊 Risk Assessment")

    st.progress(risk_score / 100)
    st.write(f"**Risk Score:** {risk_score} / 100")

    if risk_score >= 70:
        st.success("✅ Low Risk Applicant — Loan Likely to be Approved")
    elif risk_score >= 40:
        st.warning("⚠️ Medium Risk Applicant — Manual Review Required")
    else:
        st.error("❌ High Risk Applicant — Loan Rejected")

    # ------------------------------
    # Explainable Decision Logic
    # ------------------------------
    st.subheader("🧠 Decision Explanation")

    explanations = []

    if credit_score < 600:
        explanations.append("Low credit score significantly increased risk.")
    elif credit_score < 700:
        explanations.append("Moderate credit score reduced safety margin.")

    if past_default == 1:
        explanations.append("Past default history negatively impacted eligibility.")

    if existing_emi > 0.4 * income:
        explanations.append("High EMI burden compared to monthly income.")

    if employment_type == "Self-Employed":
        explanations.append("Income stability risk due to self-employment.")

    if loan_amount > income * 10:
        explanations.append("Requested loan amount is high relative to income.")

    if explanations:
        for item in explanations:
            st.write(f"- {item}")
    else:
        st.write("- All major financial risk indicators are within acceptable limits.")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("📌 This project is for educational and demonstration purposes only.")
