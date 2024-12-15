import torch
from sklearn.metrics import classification_report, mean_squared_error
from data_preprocessing import preprocess_data
from risk_model import RiskModel
from claim_model import ClaimModel

def evaluate(file_path, input_dim, risk_output_dim):
# Preprocess data
_, X_test, y_risk_test, _, _, y_claim_test = preprocess_data(file_path)

# Load models
risk_model = RiskModel(input_dim, risk_output_dim)
risk_model.load_state_dict(torch.load("risk_model.pth"))
risk_model.eval()

claim_model = ClaimModel(input_dim)
claim_model.load_state_dict(torch.load("claim_model.pth"))
claim_model.eval()

# Convert data to tensors
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_risk_test_tensor = torch.tensor(y_risk_test.values, dtype=torch.long)
y_claim_test_tensor = torch.tensor(y_claim_test.values, dtype=torch.float32)

# Evaluate risk model
risk_outputs = risk_model(X_test_tensor)
risk_preds = torch.argmax(risk_outputs, dim=1).numpy()
print("Risk Model Evaluation:")
print(classification_report(y_risk_test, risk_preds))

# Evaluate claim model
claim_preds = claim_model(X_test_tensor).squeeze().detach().numpy()
mse = mean_squared_error(y_claim_test, claim_preds)
print(f"Claim Model Evaluation: MSE = {mse:.4f}")

