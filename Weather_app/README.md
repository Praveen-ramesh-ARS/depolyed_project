# 🌤️ Weather-Based Prediction Using Django & Machine Learning

## 📌 Project Overview

This project is a **Django web application** that predicts weather-related outcomes (such as *Rain Likely*, *Sunny*, *Poor Air Quality*, etc.) using a **pre-trained machine learning model**. Users can enter a city name, the system fetches current weather data using the **OpenWeatherMap API**, and makes a prediction using the ML model.

---

## 🔧 Features

- ✅ Input a city and fetch real-time weather data
- ✅ Predict outcomes based on temperature, humidity, wind speed, and pressure
- ✅ Store predictions in the database
- ✅ Admin panel with filter options
- ✅ User-friendly frontend UI
- ✅ Proper exception handling and validation
- ✅ Colored output and formatted prediction results

---

## 🧠 Technologies Used

- Python 3.x
- Django
- HTML/CSS (Bootstrap)
- scikit-learn
- joblib
- OpenWeatherMap API

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone (https://github.com/Praveen-ramesh-ARS/depolyed_project/tree/main/Weather_app)
cd weather-predictor

2. Create and activate virtual environment

python -m venv .venv
# For Windows:
.venv\Scripts\activate

# For macOS/Linux:
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up your environment variables (API Key)
You can either:

Add your OpenWeatherMap API key in settings.py, or

Create a .env file and read it from code

Example:

OPENWEATHER_API_KEY = "your_api_key_here"

5. Run migrations
python manage.py migrate

6. Start the development server

python manage.py runserver
Then open your browser and visit:
http://127.0.0.1:8000/

🧩 ML Model Integration
The ML model is stored as a .pkl file (model.pkl)

Loaded using joblib.load inside predictor.py

Input features: temperature, humidity, wind speed, pressure

The model returns a numerical class (0, 1, 2) which is mapped to readable labels like:

0 = Sunny

1 = Rain Likely

2 = Poor Air Quality

Example mapping in predictor.py:

label_map = {
    0: "Sunny",
    1: "Rain Likely",
    2: "Poor Air Quality"
}
🌐 Weather API Details
API: OpenWeatherMap

API returns: temperature, humidity, wind speed, and pressure

Required to register and get an API key

🔐 Admin Panel Access
To use the Django admin panel:

Create superuser:

python manage.py createsuperuser
Login at:
http://127.0.0.1:8000/admin/





