import random

def get_sensor_data():
    return {
        "soil_moisture": random.randint(30, 80),
        "temperature": random.randint(25, 35)
    }