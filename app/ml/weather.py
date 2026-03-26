import requests
import time
from datetime import datetime

API_KEY = "b172c2c9a1ac6c07cbaeb3266a8ff81f"

# ✅ Pune Location
PUNE_LAT = 18.5204
PUNE_LON = 73.8567

cache = {
    "data": None,
    "timestamp": 0
}

# ------------------ CURRENT WEATHER ------------------
def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"

    res = requests.get(url, params={
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    })

    res.raise_for_status()
    data = res.json()

    return {
        "temperature": round(data["main"]["temp"]),
        "humidity": data["main"]["humidity"],
        "cloud_cover": data["clouds"]["all"],
        "rainfall_24h": data.get("rain", {}).get("1h", 0)
    }

# ------------------ FORECAST ------------------
def get_forecast(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    res = requests.get(url, params={
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    })

    res.raise_for_status()
    data = res.json()

    days = {}

    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]

        if date not in days:
            days[date] = {"temps": [], "rain": 0}

        days[date]["temps"].append(item["main"]["temp"])
        days[date]["rain"] += item.get("rain", {}).get("3h", 0)

    forecast = []

    for d in list(days.keys())[:5]:
        forecast.append({
            "day": d,
            "min_temp": round(min(days[d]["temps"])),
            "max_temp": round(max(days[d]["temps"])),
            "rain": round(days[d]["rain"])
        })

    return forecast

# ------------------ RAIN PREDICTION ------------------
def get_rain_prediction(weather):
    if weather["rainfall_24h"] > 5:
        return {
            "message": "Heavy rainfall expected",
            "advice": "Avoid irrigation"
        }

    return {
        "message": "No rainfall expected",
        "advice": "Safe to irrigate today"
    }

# ------------------ CACHE ------------------
def get_weather_cached(lat, lon):

    # Use cache for 60 seconds
    if cache["data"] and time.time() - cache["timestamp"] < 60:
        return cache["data"]

    current = get_weather(lat, lon)
    forecast = get_forecast(lat, lon)
    rain_prediction = get_rain_prediction(current)

    result = {
        **current,
        "rain_prediction": rain_prediction,
        "forecast": forecast,
        "last_updated": datetime.now().strftime("%H:%M:%S")
    }

    cache["data"] = result
    cache["timestamp"] = time.time()

    return result


# ✅ MAIN FUNCTION FOR DASHBOARD
def get_weather_data():
    return get_weather_cached(PUNE_LAT, PUNE_LON)