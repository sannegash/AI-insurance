import torch
import pandas as pd
from sklearn.preprocessing import StandardScaler
from risk_model import RiskModel
from claim_model import ClaimModel

def preprocess_input(new_data, scaler, categorical_features):
"""
Preprocess new data for prediction:
- Apply one-hot encoding to categorical features.
- Scale numeric features using the provided scaler.
"""
data = pd.DataFrame([new_data])
data = pd.get_dummies(data, columns=categorical_features, drop_first=True)

# Align columns with training data (fill missing one-hot columns)
all_features = scaler.feature_names_in_
data = data.reindex(columns=all_features, fill_value=0)

# Scale numeric features
scaled_data = scaler.transform(data)
return torch.tensor(scaled_data, dtype=torch.float32)

def predict_risk_and_claim(new_data, scaler, input_dim, risk_model_path, claim_model_path):
# Load models
risk_model = RiskModel(input_dim, output_dim=3)  # 3 classes: Low, Medium, High Risk
risk_model.load_state_dict(torch.load(risk_model_path))
risk_model.eval()

claim_model = ClaimModel(input_dim)
claim_model.load_state_dict(torch.load(claim_model_path))
claim_model.eval()

# Preprocess new data
categorical_features = ['vehicle', 'education']
processed_data = preprocess_input(new_data, scaler, categorical_features)

# Risk prediction
risk_output = risk_model(processed_data)
risk_prediction = torch.argmax(risk_output, dim=1).item()
risk_label = ["Low", "Medium", "High"][risk_prediction]

# Claim prediction
claim_output = claim_model(processed_data)
claim_prediction = claim_output.item()

return risk_label, claim_prediction

if __name__ == "__main__":
# Replace with your new customer's input data
new_customer_data = {
'age': 35,
'bmi': 27.5,
'education': 'Bachelor\'s',
'income': 55000,
'vehicle': 'Sedan',
'married': 1,
'children': 2,
'traffic_violations': 0,
'number_of_accidents': 1
}

# Load scaler (trained during preprocessing)
scaler = StandardScaler()
scaler.feature_names_in_ = ['age', 'bmi', 'income', 'married', 'children', 'traffic_violations', 'number_of_accidents', 'vehicle_SUV', 'education_Master\'s']  # Example features

# Paths to models
risk_model_path = "risk_model.pth"
claim_model_path = "claim_model.pth"

# Input dimension (depends on training features)
input_dim = len(scaler.feature_names_in_)

# Predict
risk, claim = predict_risk_and_claim(new_customer_data, scaler, input_dim, risk_model_path, claim_model_path)
print(f"Predicted Risk: {risk}")
print(f"Predicted Claim Amount: ${claim:,.2f}")

