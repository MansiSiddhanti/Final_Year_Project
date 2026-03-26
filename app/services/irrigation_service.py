from datetime import datetime
import random

# -----------------------------
# FAKE DATABASE (no IoT yet)
# -----------------------------
irrigation_history = []


# -----------------------------
# CURRENT SENSOR SIMULATION
# -----------------------------
def get_current_irrigation_status():

    soil_moisture = random.randint(30, 70)
    temperature = random.randint(25, 38)
    humidity = random.randint(40, 80)

    irrigation_on = soil_moisture < 40

    log = {
        "time": datetime.now().strftime("%H:%M"),
        "soil_moisture": soil_moisture,
        "temperature": temperature,
        "humidity": humidity,
        "irrigation_on": irrigation_on,
    }

    irrigation_history.append(log)

    return log


# -----------------------------
# AI IRRIGATION DECISION ENGINE
# -----------------------------
def get_irrigation_decision():

    data = get_current_irrigation_status()

    soil = data["soil_moisture"]
    temp = data["temperature"]
    humidity = data["humidity"]

    decision = "OFF"
    reason = "Soil moisture sufficient"

    if soil < 40:
        decision = "ON"
        reason = "Low soil moisture detected"

    if temp > 35 and soil < 50:
        decision = "ON"
        reason = "High temperature + drying soil"

    return {
        "decision": decision,
        "reason": reason,
        "soil_moisture": soil,
        "temperature": temp,
        "humidity": humidity,
    }


# -----------------------------
# HISTORY FOR DASHBOARD
# -----------------------------
def irrigation_logs():

    if not irrigation_history:
        get_current_irrigation_status()

    return irrigation_history