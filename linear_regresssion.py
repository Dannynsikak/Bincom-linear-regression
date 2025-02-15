import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
file_path = 'car_price_dataset.csv' 
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())
print(df.head())

# Select relevant features
X = df[['Year', 'Mileage', 'Engine_Size']]  # Adjust based on dataset columns
y = df['Price']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# 🔹 Plot actual vs predicted values with enhancements
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color="royalblue", edgecolors="k", label="Predictions")

# 🔹 Add an identity line (perfect predictions)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], color="red", linestyle="--", linewidth=2, label="Ideal Fit (y=x)")

# 🔹 Improve visualization
plt.xlabel("Actual Prices", fontsize=12, fontweight="bold")
plt.ylabel("Predicted Prices", fontsize=12, fontweight="bold")
plt.title("Actual vs Predicted Car Prices", fontsize=14, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# Save and show the plot
plt.savefig("actual_vs_predicted_car_prices.png", dpi=300)  # High-resolution save

