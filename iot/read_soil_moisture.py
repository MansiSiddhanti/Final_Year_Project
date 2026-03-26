# read_soil_moisture.py

import random

def get_soil_moisture():
    """
    Reads soil moisture value from sensor
    Returns percentage (0–100)
    """

    # 🔹 Replace this with real sensor code later (ESP32 / Arduino)
    soil_moisture = random.randint(30, 80)

    return soil_moisture
