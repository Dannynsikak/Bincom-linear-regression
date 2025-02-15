# Car Price Prediction Using Linear Regression

This project performs Linear Regression Analysis on a dataset of car prices. It aims to predict the price of a car based on its year of manufacture, mileage, and engine size.

📂 Project Structure

    📁 Bincom-linear-regression
    │── 📄 car_price_dataset.csv # Dataset containing car details
    │── 📄 linear_regression.py # Python script for Linear Regression analysis
    │── 📄 README.md # Documentation for the project
    📊 Dataset Overview
    The dataset car_price_dataset.csv contains the following columns:

    Brand: The manufacturer of the car
    Model: The specific model name
    Year: The year of manufacture
    Engine_Size: The size of the engine in liters
    Fuel_Type: Type of fuel used (Petrol, Diesel, Electric, etc.)
    Transmission: Type of transmission (Automatic, Manual)
    Mileage: Distance covered by the car in kilometers
    Doors: Number of doors in the car
    Owner_Count: Number of previous owners
    Price: Selling price of the car (Target variable)
    🚀 Features Used for Prediction
    The model considers the following features to predict the price of a car:
    ✅ Year – Newer cars generally have higher prices.
    ✅ Mileage – Higher mileage usually reduces the price.
    ✅ Engine_Size – Bigger engines may increase the price.

🔧 Installation & Setup
1️⃣ Clone the repository

    git clone https://github.com/your-username/Bincom-linear-regression.git

cd Bincom-linear-regression
2️⃣ Create a virtual environment (optional but recommended)

    python3 -m venv .venv
    source .venv/bin/activate # On MacOS/Linux

# OR

    .venv\Scripts\activate # On Windows

3️⃣ Install dependencies

pip install -r requirements.txt

    (Create a requirements.txt file with the following content if needed:)

        nginx

        pandas
        numpy
        matplotlib
        scikit-learn

▶️ Running the Model
Run the script with:

python3 linear_regression.py
📌 Expected Output (Example)
mathematica

Mean Absolute Error (MAE): 888.98
Mean Squared Error (MSE): 1137718.10
Root Mean Squared Error (RMSE): 1066.64
R² Score: 0.8762
This means the model predicts prices with 87.62% accuracy based on the available features.

📈 Visualization
The script plots actual vs. predicted car prices, showing how well the model fits the data.

✅ Blue dots represent predictions.
✅ Red dashed line shows the perfect fit (y = x).

The plot is saved as:

actual_vs_predicted_car_prices.png
Example Plot:

🛠️ Model Evaluation Metrics
Mean Absolute Error (MAE) – Measures the average absolute difference between actual and predicted values.
Mean Squared Error (MSE) – Penalizes large errors more than small ones.
Root Mean Squared Error (RMSE) – Similar to MSE but in the same units as the target variable.
R² Score – Measures how well the independent variables explain the variance in price (closer to 1 is better).
📌 Future Improvements
🔹 Add more features (e.g., fuel type, transmission, brand).
🔹 Use polynomial regression for better predictions.
🔹 Train on a larger dataset for better generalization.
🔹 Integrate with a web interface for user input.

💡 Conclusion
This project demonstrates how machine learning can predict car prices using Linear Regression. By optimizing features and improving the dataset, we can build a more robust pricing model.

📢 Contributions & Suggestions are Welcome! 🎯
