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
    "An end-to-end FinTech application for loan eligibility assessment, "
    "credit risk scoring, sanctioned loan estimation, and data analysis."
)

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("Data/loan_eligibility_data.csv")

# ==============================
# Helper: Safe column resolver
# ==============================
def find_column(possible_names):
    for col in df.columns:
        for name in possible_names:
            if name.lower() in col.lower():
                return col
    return None

COL_INCOME = find_column(["income"])
COL_LOAN = find_column(["loan"])
COL_CREDIT = find_column(["credit"])
COL_DEFAULT = find_column(["default"])
COL_EMPLOYMENT = find_column(["employment"])

# ==============================
# Risk Score Function
# ==============================
def calculate_risk_score(
    income,
    loan_amount,
    existing_emi,
    past_default,
    credit_score,
    employment_type
):
    score = 100

    if credit_score < 600:
        score -= 25
    elif credit_score < 700:
        score -= 10

    if past_default == 1:
        score -= 30

    if existing_emi > 0.4 * income:
        score -= 20

    if employment_type == "Self-Employed":
        score -= 10

    if loan_amount > income * 10:
        score -= 10

    return max(score, 0)

# ==============================
# Sanctioned Loan Calculation
# ==============================
def calculate_sanctioned_amount(
    income,
    risk_score,
    employment_type
):
    # Base eligibility multiplier (banks use 30–60x monthly income)
    if employment_type == "Salaried":
        base_multiplier = 60
    else:
        base_multiplier = 48

    base_amount = income * base_multiplier

    # Risk-based adjustment
    if risk_score >= 70:
        factor = 1.0
    elif risk_score >= 40:
        factor = 0.6
    else:
        factor = 0.0

    sanctioned_amount = base_amount * factor
    return round(sanctioned_amount, -3)

# ==============================
# Tabs
# ==============================
tab1, tab2 = st.tabs(
    ["🔍 Loan Eligibility & Risk Scoring", "📊 Data Analysis Dashboard"]
)

# ============================================================
# TAB 1 — LOAN ELIGIBILITY, RISK & SANCTION
# ============================================================
with tab1:
    st.subheader("📥 Applicant Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 21, 65, 30)
        income = st.number_input("Monthly Income (₹)", min_value=5000, step=1000)
        loan_amount = st.number_input("Requested Loan Amount (₹)", min_value=50000, step=10000)
        credit_score = st.slider("Credit Score", 300, 900, 700)

    with col2:
        tenure_months = st.slider(
            "Loan Tenure (Months)",
            min_value=6,
            max_value=600,
            value=120,
            step=6
        )
        existing_emi = st.number_input("Existing Monthly EMI (₹)", min_value=0, step=1000)
        employment_type = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])
        past_default = st.selectbox("Past Default History", ["No", "Yes"])

    past_default = 1 if past_default == "Yes" else 0

    if st.button("🔍 Check Loan Eligibility"):

        risk_score = calculate_risk_score(
            income,
            loan_amount,
            existing_emi,
            past_default,
            credit_score,
            employment_type
        )

        sanctioned_amount = calculate_sanctioned_amount(
            income,
            risk_score,
            employment_type
        )

        st.subheader("📊 Risk Assessment")
        st.progress(risk_score / 100)
        st.write(f"**Risk Score:** {risk_score} / 100")

        if risk_score >= 70:
            st.success("✅ Low Risk Applicant — Loan Approved")
        elif risk_score >= 40:
            st.warning("⚠️ Medium Risk Applicant — Manual Review Required")
        else:
            st.error("❌ High Risk Applicant — Loan Rejected")

        st.subheader("💰 Loan Sanction Decision")

        if sanctioned_amount > 0:
            st.success(f"**Maximum Loan Amount That Can Be Sanctioned:** ₹ {sanctioned_amount:,}")

            if loan_amount > sanctioned_amount:
                st.warning(
                    "Requested loan amount exceeds eligible sanctioned limit. "
                    "Partial sanction or revised amount recommended."
                )
        else:
            st.error("No loan amount can be sanctioned due to high risk.")

        # ------------------------------
        # Explanation
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
            explanations.append("High EMI burden compared to income.")

        if employment_type == "Self-Employed":
            explanations.append("Income stability risk due to self-employment.")

        if loan_amount > income * 10:
            explanations.append("Requested loan amount is high relative to income.")

        if explanations:
            for e in explanations:
                st.write(f"- {e}")
        else:
            st.write("- Applicant meets all major eligibility criteria.")

# ============================================================
# TAB 2 — DATA ANALYSIS DASHBOARD
# ============================================================
with tab2:
    st.subheader("📊 Loan Data Analysis Dashboard")

    st.markdown("### Dataset Preview")
    st.dataframe(df.head())

    st.markdown("### Summary Statistics")
    st.dataframe(df.describe(include="all"))

    col3, col4 = st.columns(2)

    with col3:
        if COL_CREDIT:
            st.markdown("### Credit Score Distribution")
            st.bar_chart(df[COL_CREDIT].value_counts())

        if COL_EMPLOYMENT:
            st.markdown("### Employment Type Distribution")
            st.bar_chart(df[COL_EMPLOYMENT].value_counts())

    with col4:
        if COL_DEFAULT:
            st.markdown("### Past Default History")
            st.bar_chart(df[COL_DEFAULT].value_counts())

        if COL_INCOME and COL_LOAN:
            st.markdown("### Income vs Loan Amount")
            st.scatter_chart(df, x=COL_INCOME, y=COL_LOAN)

    st.markdown("### 📌 Key Insights")
    st.write(
        "- Credit score strongly influences loan approval decisions.\n"
        "- Higher income enables larger sanctioned loan amounts.\n"
        "- Past defaults significantly reduce loan eligibility.\n"
        "- Employment stability affects maximum sanctionable loan."
    )

# ==============================
# Footer
# ==============================
st.markdown("---")
st.caption("📌 This project is for educational and demonstration purposes only.")
