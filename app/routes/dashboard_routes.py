from app.ml.weather import get_weather_data
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.ml.irrigation_model import IrrigationReading
from app.services.ai_service import generate_ai_insights

router = APIRouter()


@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):

    # =========================
    # 1️⃣ Latest Soil Data
    # =========================
    latest_reading = (
        db.query(IrrigationReading)
        .order_by(IrrigationReading.recorded_at.desc())
        .first()
    )

    soil_moisture = latest_reading.soil_moisture if latest_reading else 0
    irrigation_on = latest_reading.irrigation_on if latest_reading else False

    # =========================
    # 2️⃣ Moisture History
    # =========================
    history = (
        db.query(IrrigationReading)
        .order_by(IrrigationReading.recorded_at.desc())
        .limit(12)
        .all()
    )

    moisture_history = [
        {
            "time": r.recorded_at.strftime("%H:%M"),
            "value": r.soil_moisture,
        }
        for r in reversed(history)
    ]

    # =========================
    # 3️⃣ Weather Data
    # =========================
    weather = get_weather_data()

    # =========================
    # 4️⃣ Recommended Crops
    # =========================
    if soil_moisture < 30:
        recommended_crops = ["Millet", "Groundnut"]
    elif soil_moisture < 60:
        recommended_crops = ["Maize", "Soybean"]
    else:
        recommended_crops = ["Rice", "Sugarcane"]

    # =========================
    # 5️⃣ AI Insights ✅ FIXED
    # =========================
    ai_insights = generate_ai_insights(
        weather,
        {"soil_moisture": soil_moisture}
    )

    # =========================
    # 6️⃣ Final Response
    # =========================
    return {
        "soil_moisture": soil_moisture,
        "irrigation_on": irrigation_on,
        "recommended_crops": recommended_crops,
        "weather": weather,
        "ai_insights": ai_insights,
        "moisture_history": moisture_history,
    }