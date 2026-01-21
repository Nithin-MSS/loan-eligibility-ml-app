import numpy as np
import pandas as pd

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "Age": np.random.randint(21, 65, n),
    "Monthly_Income": np.random.randint(15000, 120000, n),
    "Employment_Type": np.random.choice(["Salaried", "Self-Employed"], n),
    "Loan_Amount": np.random.randint(50000, 800000, n),
    "Loan_Tenure": np.random.randint(6, 60, n),
    "Existing_EMI": np.random.randint(0, 30000, n),
    "Past_Default": np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "Credit_Score": np.random.randint(300, 850, n)
})

conditions = [
    (df["Credit_Score"] >= 700) &
    (df["Loan_Amount"] <= df["Monthly_Income"] * 20) &
    (df["Past_Default"] == 0),

    (df["Credit_Score"] >= 550) &
    (df["Loan_Amount"] <= df["Monthly_Income"] * 30)
]

df["Eligibility_Status"] = np.select(conditions, [2, 1], default=0)

df.to_csv("data/loan_eligibility_data.csv", index=False)

print("✅ Dataset generated successfully")
print(df.head())
