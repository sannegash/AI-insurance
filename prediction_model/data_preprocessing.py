import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    # Load CSV file
    data = pd.read_csv(file_path)

    # Separate features and targets
    X = data[['age', 'gender', 'driving_experience', 'education','income', 'vehicle_type', 'married', 'children','traffic_violations', 'number_of_accidents']]
    y_risk = data['risk_factor']  # Target for risk classification
    y_claim = data['claim_likelihood']  # Target for claim regression

    # Encode categorical data (e.g., vehicle, education)
    X = pd.get_dummies(X, columns=['vehicle_type', 'education'], drop_first=True)

    # Split into train and test sets
    X_train, X_test, y_risk_train, y_risk_test = train_test_split(X, y_risk, test_size=0.2, random_state=42)
    _, _, y_claim_train, y_claim_test = train_test_split(X, y_claim, test_size=0.2, random_state=42)

    # Scale numeric features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_risk_train, y_risk_test, y_claim_train, y_claim_test

if __name__ == "__main__":
    file_path = "synthetic_insurance_data.csv"  # Update with your CSV path
    data = preprocess_data(file_path)
    print("Data preprocessing complete!")

