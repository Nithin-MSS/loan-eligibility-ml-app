import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/loan_eligibility_data.csv")

print("Shape:", df.shape)
print("\nInfo:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nEligibility Status Distribution:")
print(df["Eligibility_Status"].value_counts())

# Plot 1: Eligibility distribution
sns.countplot(x="Eligibility_Status", data=df)
plt.title("Loan Eligibility Distribution")
plt.show()

# Plot 2: Income vs Loan Amount
sns.scatterplot(
    x="Monthly_Income",
    y="Loan_Amount",
    hue="Eligibility_Status",
    data=df
)
plt.title("Income vs Loan Amount")
plt.show()

# Plot 3: Credit Score vs Eligibility
sns.boxplot(
    x="Eligibility_Status",
    y="Credit_Score",
    data=df
)
plt.title("Credit Score vs Eligibility Status")
plt.show()
