from fastapi import APIRouter
from ..services.sensor_service import process_sensor_data

router = APIRouter(prefix="/api/sensor", tags=["Sensors"])

@router.post("/")
def receive_sensor_data(payload: dict):
    return process_sensor_data(payload)
