from fastapi import APIRouter, Query
from app.services.crop_service import predict_crop

router = APIRouter()

@router.get("/recommend")
def recommend_crop(
    location: str = Query(...),
    temperature: str = Query(...),
    soil_type: str = Query(...)
):
    result = predict_crop(location, temperature, soil_type)
    return result  # Must be a dict like {"recommended_crop": "Wheat"}