import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(file_path):
    # Load CSV file
    data = pd.read_csv(file_path)
    
    # Check for missing values and handle them
    if data.isnull().sum().any():
        data = data.fillna(0)
    
    # Separate features and targets
    X = data[['age', 'gender', 'driving_experience', 'education', 'income', 
              'vehicle_type', 'married', 'children', 'traffic_violations', 'number_of_accidents']].copy()
    y_risk = data['risk_factor']  # Target for risk classification
    y_claim = data['claim_likelihood']  # Target for claim regression
    
    # Encode categorical data
    X['gender'] = X['gender'].map({'Male': 0, 'Female': 1})
    X['married'] = X['married'].map({'Yes': 1, 'No': 0})
    
    # One-hot encode multi-class categorical features
    X = pd.get_dummies(X, columns=['vehicle_type', 'education'], drop_first=True)
    
    # Encode y_risk as integers (if categorical)
    label_encoder = LabelEncoder()
    y_risk = label_encoder.fit_transform(y_risk)
    
    # Split into train and test sets
    X_train, X_test, y_risk_train, y_risk_test, y_claim_train, y_claim_test = train_test_split(
        X, y_risk, y_claim, test_size=0.2, random_state=42
    )
    
    # Scale numeric features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_risk_train, y_risk_test, y_claim_train, y_claim_test, label_encoder.classes_

if __name__ == "__main__":
    file_path = "synthetic_insurance_data.csv"  # Update with your CSV path
    try: 
        data = preprocess_data(file_path)
        print("Data preprocessing complete!")
    except Exception as e:
        print(f"An error occurred: {e}")


