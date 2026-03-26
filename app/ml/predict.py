import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model and encoder
model = joblib.load(os.path.join(BASE_DIR, "crop_model.pkl"))
soil_encoder = joblib.load(os.path.join(BASE_DIR, "soil_encoder.pkl"))

# UI → Numeric mapping
TEMP_MAP = {
    "Cool": 10,
    "Moderate": 20,
    "Warm": 30,
    "Hot": 40
}

def predict_crop(temperature_label, soil_label, humidity=70, rainfall=100):
    """
    Predict crop based on user input
    """

    temperature = TEMP_MAP.get(temperature_label, 25)
    soil_encoded = soil_encoder.transform([soil_label])[0]

    input_data = [[temperature, soil_encoded, humidity, rainfall]]

    prediction = model.predict(input_data)

    return prediction[0]
