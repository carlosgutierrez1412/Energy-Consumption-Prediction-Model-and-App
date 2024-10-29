from flask import Flask, jsonify, render_template, request
import numpy as np
import joblib

# Load model (no scaler needed for now)
model = joblib.load("model/energy_forecast_model.pkl")

# Initialize Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get form data from the request
    data = request.json

    # Extract values (with defaults in case fields are empty)
    household_size = int(data.get("household_size", 1))
    home_type = data.get("home_type", "house")
    appliance_usage = data.get("appliance_usage", "medium")

    # Calculate a representative value based on user input
    representative_value = 10000  # Base value
    representative_value += household_size * 2000  # Increase by household size

    if home_type == "apartment":
        representative_value += 5000
    elif home_type == "house":
        representative_value += 10000

    if appliance_usage == "high":
        representative_value += 5000
    elif appliance_usage == "low":
        representative_value -= 2000

    # Create input for the model
    input_data = np.array(
        [[representative_value, representative_value, representative_value]]
    )

    # Predict energy consumption
    predicted_value = model.predict(input_data)[0]

    return jsonify({"predicted_value": predicted_value})


if __name__ == "__main__":
    app.run(debug=True)
