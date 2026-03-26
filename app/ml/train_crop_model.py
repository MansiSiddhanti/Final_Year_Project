# ml/train_crop_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Dummy example dataset
data = pd.DataFrame({
    "location": ["delhi", "mumbai", "pune"],
    "temperature": [25, 30, 28],
    "soil_type": ["loamy", "sandy", "clay"],
    "crop": ["wheat", "rice", "maize"]
})

# Encode categorical variables
le_location = LabelEncoder()
le_soil = LabelEncoder()
le_crop = LabelEncoder()

data["location"] = le_location.fit_transform(data["location"])
data["soil_type"] = le_soil.fit_transform(data["soil_type"])
data["crop"] = le_crop.fit_transform(data["crop"])

X = data[["location", "temperature", "soil_type"]]
y = data["crop"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model + encoders
MODEL_PATH = os.path.join(os.path.dirname(__file__), "train_crop_model.joblib")
joblib.dump({
    "model": model,
    "le_location": le_location,
    "le_soil": le_soil,
    "le_crop": le_crop
}, MODEL_PATH)

print(f"Model saved at {MODEL_PATH}")