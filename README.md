# Loan Eligibility, Credit Risk & Loan Sanction System 🏦📊

An end-to-end **FinTech Machine Learning & Analytics application** that evaluates
loan eligibility, computes credit risk scores, estimates maximum sanctionable loan
amount, and provides an interactive data analysis dashboard.

🔗 **Live Application**  
https://loan-eligibility-ml-app-9bgujvzhetkqxzyblfu5zs.streamlit.app

---

## 🔍 Problem Statement
Financial institutions must assess loan applications efficiently while minimizing
default risk and ensuring responsible lending. Traditional manual screening is
time-consuming, inconsistent, and difficult to scale.

This project automates and enhances the loan approval process by combining:
- Risk-based decision logic  
- Income-based loan sanctioning  
- Explainable outcomes  
- Interactive data analytics  

---

## 🚀 Key Features
- **Loan Eligibility Decision** (Approve / Review / Reject)
- **Credit Risk Score (0–100)** using banking-style risk factors
- **Maximum Sanctionable Loan Amount** estimation
- Partial approval recommendations if requested amount exceeds eligibility
- Explainable decision logic (transparent & interpretable)
- Interactive **Data Analysis Dashboard**
- Deployed as a live web application on **Streamlit Cloud**

---

## 🧠 Risk Scoring Logic
The system evaluates applicants using key financial and behavioral indicators:
- Credit score
- Existing EMI burden
- Monthly income
- Loan-to-income ratio
- Employment type
- Past default history

Each factor contributes to a **risk score (0–100)**:
- **70–100** → Low Risk (Likely Approval)
- **40–69** → Medium Risk (Manual Review)
- **< 40** → High Risk (Rejected)

---

## 💰 Loan Sanctioning Logic
The app estimates the **maximum loan amount that can be sanctioned** using:
- Income-based multipliers (bank-style)
- Employment stability
- Risk score adjustment factors

This enables:
- Responsible lending
- Partial approvals
- Realistic credit assessment similar to banking systems

---

## 📊 Data Analysis Dashboard
An integrated analytics dashboard provides:
- Dataset preview & summary statistics
- Credit score distribution analysis
- Income vs loan amount visualization
- Employment type distribution
- Past default analysis
- Key insights for stakeholders

This demonstrates strong **Data Analysis + Visualization** capabilities.

---

## 🛠 Tech Stack
- **Python**
- **Pandas**
- **Streamlit**
- **Rule-based Credit Risk Modeling**
- **Data Visualization**
- **Git & GitHub**
- **Streamlit Cloud Deployment**

---

## 📂 Project Structure

```text
loan-eligibility-ml-app/
│
├── app.py                    # Streamlit application (Eligibility, Risk & Sanction)
├── requirements.txt          # Project dependencies
├── Data/
│   └── loan_eligibility_data.csv
├── src/
│   ├── preprocessing.py      # Data cleaning & transformations
│   ├── model_training.py     # Risk logic / model experiments
│   ├── eda.py                # Exploratory Data Analysis
│   └── data_generation.py    # Synthetic banking data generation
└── README.md


---

## 🎓 Skills Demonstrated
- Financial risk analysis
- Credit decision modeling
- Explainable AI concepts
- Data analysis & visualization
- Production-ready Streamlit deployment
- Version control with Git

---

## 👤 Author
**M. S. S. Nithin**  
B.Tech – Computer Science Engineering (AI & ML)

---

## 📌 Disclaimer
This application is built for educational and demonstration purposes only.
It does not represent real bank approval systems.
