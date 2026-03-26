from fastapi import APIRouter
from app.services.weather_service import get_weather_cached

router = APIRouter(prefix="/weather", tags=["Weather"])

@router.get("/")
def fetch_weather(lat: float = 18.5, lon: float = 73.8):
    return get_weather_cached(lat, lon)