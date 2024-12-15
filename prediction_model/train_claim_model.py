import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from claim_model import ClaimModel
from data_preprocessing import preprocess_data

def train_claim_model(file_path, input_dim, epochs=10, batch_size=64, lr=0.001):
# Preprocess data
X_train, X_test, _, _, y_train, y_test = preprocess_data(file_path)

# Convert data to tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)

# Create DataLoader
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Initialize model, loss function, and optimizer
model = ClaimModel(input_dim)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# Training loop
for epoch in range(epochs):
model.train()
for X_batch, y_batch in train_loader:
optimizer.zero_grad()
outputs = model(X_batch).squeeze()
loss = criterion(outputs, y_batch)
loss.backward()
optimizer.step()
print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item():.4f}")

# Save model
torch.save(model.state_dict(), "claim_model.pth")
print("Claim model training complete and saved to claim_model.pth!")

