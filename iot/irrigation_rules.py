# irrigation_rules.py

def irrigation_decision(soil_moisture, rainfall_expected=False):
    """
    Decide whether irrigation is needed
    """

    if rainfall_expected:
        return "OFF", "Rain expected, irrigation not required"

    if soil_moisture < 40:
        return "ON", "Soil is dry, irrigation required"

    if 40 <= soil_moisture <= 60:
        return "OFF", "Soil moisture is adequate"

    return "OFF", "Soil is wet, irrigation not required"
