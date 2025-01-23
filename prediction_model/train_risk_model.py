import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from risk_model import RiskModel
from data_preprocessing import preprocess_data

def train_risk_model(file_path, input_dim, output_dim, epochs=10, batch_size=64, lr=0.001):
    # Preprocess data
    X_train, X_test, y_risk_train, y_risk_test, _, _, _ = preprocess_data(file_path)

    # Convert data to tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_risk_train, dtype=torch.long)  # Fixed to handle int targets

    # Create DataLoader
    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # Initialize model, loss function, and optimizer
    model = RiskModel(input_dim, output_dim)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Training loop
    for epoch in range(epochs):
        model.train()
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item():.4f}")

    # Save model
    torch.save(model.state_dict(), "risk_model.pth")
    print("Risk model training complete and saved to risk_model.pth!")

if __name__ == "__main__":
    file_path = "synthetic_insurance_data.csv"  # Update this path
    input_dim = 14  # Update with actual number of features
    output_dim = 3  # Number of risk classes (low, medium, high)

    train_risk_model(file_path, input_dim, output_dim, epochs=10, batch_size=64, lr=0.001)

