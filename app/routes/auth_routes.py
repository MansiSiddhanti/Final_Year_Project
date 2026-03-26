from fastapi import APIRouter
from app.services.auth_service import authenticate_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(payload: dict):
    return authenticate_user(payload)
