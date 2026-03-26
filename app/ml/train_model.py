# train_model.py
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

# Sample data
data = [
    ['Pune', '25-35', 'loamy', 'Sugarcane'],
    ['Pune', '15-25', 'sandy', 'Wheat'],
    ['Pune', '25-35', 'clayey', 'Rice'],
    ['Mumbai', '25-35', 'sandy', 'Rice'],
]

df = pd.DataFrame(data, columns=['location', 'temperature', 'soil_type', 'crop'])

X = df[['location', 'temperature', 'soil_type']]
y = df['crop']

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

model = RandomForestClassifier()
model.fit(X_encoded, y_encoded)

joblib.dump(model, 'crop_model.pkl')
joblib.dump(encoder, 'encoder.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')