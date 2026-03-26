from fastapi import APIRouter
from app.services.irrigation_service import get_irrigation_decision

router = APIRouter(prefix="/irrigation", tags=["Irrigation"])


@router.get("/decision")
def irrigation_decision():
    return get_irrigation_decision()
