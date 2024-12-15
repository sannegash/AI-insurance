import torch
import torch.nn as nn

class RiskModel(nn.Module):
def __init__(self, input_dim, output_dim):
super(RiskModel, self).__init__()
self.fc = nn.Sequential(
nn.Linear(input_dim, 64),
nn.ReLU(),
nn.Linear(64, 32),
nn.ReLU(),
nn.Linear(32, output_dim)  # Output for classification (low, medium, high risk)
)

def forward(self, x):
return self.fc(x)

