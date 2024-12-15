import torch
import torch.nn as nn

class ClaimModel(nn.Module):
def __init__(self, input_dim):
super(ClaimModel, self).__init__()
self.fc = nn.Sequential(
nn.Linear(input_dim, 64),
nn.ReLU(),
nn.Linear(64, 32),
nn.ReLU(),
nn.Linear(32, 1)  # Output is a single value (claim amount)
)

def forward(self, x):
return self.fc(x)
i
