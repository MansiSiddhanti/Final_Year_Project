import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../ml/train_crop_model.joblib")
saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
le_location = saved_data["le_location"]
le_soil = saved_data["le_soil"]
le_crop = saved_data["le_crop"]

def parse_temperature(temp_str):
    temp_str = temp_str.replace("°", "").replace("C", "").strip()
    if "-" in temp_str:
        start, end = temp_str.split("-")
        return (float(start) + float(end)) / 2
    return float(temp_str)

def predict_crop(location, temperature, soil_type):
    try:
        # Convert temperature string to numeric if needed
        temp_map = {
            "below 15": 10,
            "15-25": 20,
            "25-35": 30,
            "above 35": 40
        }
        temperature_numeric = temp_map.get(temperature, 20)

        # Encode location & soil type
        loc_encoded = le_location.transform([location.lower()])[0]
        soil_encoded = le_soil.transform([soil_type.lower()])[0]

        data = pd.DataFrame([{
            "location": loc_encoded,
            "temperature": temperature_numeric,
            "soil_type": soil_encoded
        }])

        crop_encoded = model.predict(data)[0]
        crop_name = le_crop.inverse_transform([crop_encoded])[0]

        return {"recommended_crop": crop_name}

    except Exception as e:
        return {"recommended_crop": f"Error: {str(e)}"}  # Always return key