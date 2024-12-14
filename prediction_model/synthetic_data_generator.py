import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

# Parameters for synthetic data
n_samples = 10000  # Number of rows
n_features = 4    # Number of input features
n_informative = 3  # Number of informative features
n_classes = 3      # Low, Medium, High risk
class_labels = ['Low', 'Medium', 'High']

# Generate features and risk factor
X, y = make_classification(
n_samples=n_samples,
n_features=n_features,
n_informative=n_informative,
n_redundant=0,
n_classes=n_classes,
class_sep=1.5,  # Class separability
random_state=42
)

# Scale the features to make them realistic
age = (X[:, 0] * 10 + 30).astype(int)  # Age: ~30-70
income = (X[:, 1] * 20000 + 50000).astype(int)  # Income: ~30k-100k
driving_experience = np.clip((X[:, 2] * 5 + 10).astype(int), 0, 50)  # Experience: ~0-30 years
traffic_violations = np.clip((X[:, 3] * 2 + 2).astype(int), 0, 10)  # Violations: 0-10

# Generate other categorical features
np.random.seed(42)
gender = np.random.choice(['Male', 'Female'], size=n_samples)
vehicle_type = np.random.choice(['Sedan', 'SUV', 'Truck', 'Motorcycle'], size=n_samples)
married = np.random.choice(['Yes', 'No'], size=n_samples)
children = np.random.randint(0, 5, size=n_samples)  # Number of children: 0-4

# Add education levels
education_levels = ['High School', 'Bachelor\'s', 'Master\'s', 'PhD']
education = np.random.choice(education_levels, size=n_samples)

# Risk and claim likelihood
risk_factor = [class_labels[i] for i in y]
claim_likelihood = np.random.rand(n_samples)  # Claim likelihood between 0 and 1

# Create a DataFrame
data = pd.DataFrame({
'age': age,
'gender': gender,
'driving_experience': driving_experience,
'income': income,
'vehicle_type': vehicle_type,
