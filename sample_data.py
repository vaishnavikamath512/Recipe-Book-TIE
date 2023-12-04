# sample_data.py

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Generate sample data
np.random.seed(42)
ages = np.random.randint(18, 70, size=100).reshape(-1, 1)
recipes = np.random.choice([0, 1, 2, 3], size=100)  # 4 sample recipes

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(ages, recipes, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'sample_model.joblib')
