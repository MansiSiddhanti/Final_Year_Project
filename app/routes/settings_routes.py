from fastapi import APIRouter
from app.services.settings_service import get_settings, update_settings

router = APIRouter(
    prefix="/api/settings",
    tags=["Settings"]
)

@router.get("/")
def fetch_settings():
    return get_settings()

@router.post("/")
def save_settings(payload: dict):
    return update_settings(payload)
