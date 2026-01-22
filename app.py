import streamlit as st
import pandas as pd

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Loan Eligibility & Risk Scoring System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Loan Eligibility & Credit Risk Scoring System")
st.write(
    "An end-to-end Machine Learning application for loan eligibility assessment, "
    "risk scoring, and financial data analysis."
)

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("Data/loan_eligibility_data.csv")

# ==============================
# Risk Score Function
# ==============================
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

    # Past defaults
    if past_default == 1:
        score -= 30

    # EMI burden
    if existing_emi > 0.4 * income:
        score -= 20

    # Employment risk
    if employment_type == "Self-Employed":
        score -= 10

    # Loan to income ratio
    if loan_amount > income * 10:
        score -= 10

    return max(score, 0)

# ==============================
# Tabs
# ==============================
tab1, tab2 = st.tabs(
    ["🔍 Loan Eligibility & Risk Scoring", "📊 Data Analysis Dashboard"]
)

# ============================================================
# TAB 1 — LOAN ELIGIBILITY & RISK SCORING
# ============================================================
with tab1:
    st.subheader("📥 Applicant Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 21, 65, 30)
        income = st.number_input("Monthly Income (₹)", min_value=5000, step=1000)
        loan_amount = st.number_input("Loan Amount (₹)", min_value=50000, step=10000)
        credit_score = st.slider("Credit Score", 300, 900, 700)

    with col2:
        tenure_months = st.slider(
            "Loan Tenure (Months)",
            min_value=6,
            max_value=600,   # Up to 50 years
            value=120,
            step=6
        )
        existing_emi = st.number_input("Existing Monthly EMI (₹)", min_value=0, step=1000)
        employment_type = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])
        past_default = st.selectbox("Past Default History", ["No", "Yes"])

    past_default = 1 if past_default == "Yes" else 0

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

        reasons = []

        if credit_score < 600:
            reasons.append("Low credit score significantly increased risk.")
        elif credit_score < 700:
            reasons.append("Moderate credit score reduced safety margin.")

        if past_default == 1:
            reasons.append("Past default history negatively impacted eligibility.")

        if existing_emi > 0.4 * income:
            reasons.append("High EMI burden compared to monthly income.")

        if employment_type == "Self-Employed":
            reasons.append("Income stability risk due to self-employment.")

        if loan_amount > income * 10:
            reasons.append("Requested loan amount is high relative to income.")

        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("- All major risk indicators are within acceptable limits.")

# ============================================================
# TAB 2 — DATA ANALYSIS DASHBOARD
# ============================================================
with tab2:
    st.subheader("📊 Loan Data Analysis Dashboard")
    st.write("Insights and patterns derived from loan applicant data.")

    st.markdown("### 📄 Dataset Preview")
    st.dataframe(df.head())

    st.markdown("### 📈 Summary Statistics")
    st.dataframe(df.describe())

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Credit Score Distribution")
        st.bar_chart(df["Credit_Score"].value_counts())

        st.markdown("### Employment Type Distribution")
        st.bar_chart(df["Employment_Type"].value_counts())

    with col4:
        st.markdown("### Past Default History")
        st.bar_chart(df["Past_Default"].value_counts())

        st.markdown("### Income vs Loan Amount")
        st.scatter_chart(df, x="Income", y="Loan_Amount")

    st.markdown("### 📌 Key Insights")
    st.write(
        "- Higher credit scores are associated with lower default risk.\n"
        "- Applicants with high EMI-to-income ratios show increased rejection rates.\n"
        "- Employment stability plays a significant role in loan decisions.\n"
        "- Past default history is a strong negative indicator."
    )

# ==============================
# Footer
# ==============================
st.markdown("---")
st.caption("📌 This project is for educational and demonstration purposes only.")
