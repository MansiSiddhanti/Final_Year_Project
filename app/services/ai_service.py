def generate_ai_insights(weather, irrigation=None):

    insights = []

    # =============================
    # ✅ SAFE WEATHER CONVERSION
    # =============================
    if weather is None:
        return ["Weather data unavailable"]

    # Convert Pydantic model → dict
    if hasattr(weather, "dict"):
        weather = weather.dict()

    # Convert object → dict
    if not isinstance(weather, dict):
        try:
            weather = vars(weather)
        except Exception:
            return ["Weather data unavailable"]

    # =============================
    # TEMPERATURE INSIGHT
    # =============================
    forecast = weather.get("forecast", [])

    tomorrow_temp = None
    if isinstance(forecast, list) and len(forecast) > 1:
        tomorrow_temp = forecast[1].get("max_temp")

    if tomorrow_temp and tomorrow_temp > 35:
        insights.append(
            "High temperature expected tomorrow. Increase irrigation."
        )

    # =============================
    # RAIN INSIGHT
    # =============================
    rain = weather.get("rain_prediction", {})

    if isinstance(rain, dict):
        advice = rain.get("advice", "").lower()

        if "avoid" in advice:
            insights.append("Rain expected. Skip irrigation.")

    # =============================
    # SOIL MOISTURE INSIGHT
    # =============================
    if isinstance(irrigation, dict):
        soil = irrigation.get("soil_moisture")

        if soil is not None:
            if soil < 30:
                insights.append(
                    "Soil moisture low. Irrigation recommended."
                )
            elif soil > 70:
                insights.append(
                    "Soil already wet. Avoid overwatering."
                )

    # =============================
    # DEFAULT INSIGHT
    # =============================
    if not insights:
        insights.append("Farm conditions look stable today.")

    return insights