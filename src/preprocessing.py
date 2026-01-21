import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("data/loan_eligibility_data.csv")

# Encode categorical variable
df = pd.get_dummies(df, columns=["Employment_Type"], drop_first=True)

# Separate features and target
X = df.drop("Eligibility_Status", axis=1)
y = df["Eligibility_Status"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale numerical features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Data preprocessing completed")
print("Train shape:", X_train_scaled.shape)
print("Test shape:", X_test_scaled.shape)
