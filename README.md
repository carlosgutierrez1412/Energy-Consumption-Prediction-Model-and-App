# Energy Consumption Prediction App

A predictive web application that uses a Random Forest Regression model to forecast hourly energy consumption. This app demonstrates how AI can assist the Department of Energy (DOE) by providing accurate, real-time energy demand predictions based on user inputs and historical data, in the repo is also included a presentation of the project as well as the jupyer notebook where the predictive data analysis was performed.

## Features

- **AI Model**: Random Forest Regression model for hourly energy prediction.
- **User Inputs**: Customizable input fields for household size, home type, and appliance usage.
- **Real-Time Prediction**: Provides instant, hour-by-hour energy predictions to optimize resource planning.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the app at `http://127.0.0.1:5000` in your web browser.

## Usage

1. Open the app in a browser.
2. Input household details, select home type and appliance usage level.
3. Click **Get Prediction** to view the forecasted energy consumption for the next hour.

## Project Structure

- `app.py`: Main Flask application file.
- `dataset/`: Contains the energy dataset file.
  - `PJME_hourly.csv`: CSV file with historical energy consumption data.
- `model/`: Stores the machine learning model and scaler used in predictions.
  - `energy_forecast_model.pkl`: Pre-trained Random Forest Regression model.
  - `scaler.pkl`: Scaler for preprocessing input data.
- `notebook/`: Jupyter notebook(s) used for data analysis and model training.
  - `PJM_Hourly_Energy_Consumption.ipynb`: Notebook for data processing and model development.
- `presentation/`: Contains presentation files for project overview.
  - `AI-Driven Predictive Energy Analytics.pptx`: Presentation on AI applications for the DOE.
- `templates/`: HTML templates for the web interface.
  - `index.html`: Main HTML template for user input and prediction display.
- `venv/`: Python virtual environment for dependencies.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies for the project.

## Technologies Used

- **Python (Flask)**: Backend application framework.
- **HTML/CSS/JavaScript**: Front-end interface.
- **Pandas, Numpy, Matplotlib, Seaborn**: For the data analysis and data visualization.
- **Scikit-Learn**: For the Random Forest Regression Machine Learning model.
- **Joblib**: Model serialization and deserialization.
- **PDF**: Presentation of the project.

## Future Enhancements

- **Live Data Integration**: Pull real-time data from DOE sources for even more accurate forecasting.
- **Enhanced Visualization**: Add graphs to show historical vs. predicted energy usage patterns.
