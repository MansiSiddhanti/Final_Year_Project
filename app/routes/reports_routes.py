from fastapi import APIRouter
from app.services.report_service import generate_report

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/")
def get_reports():
    return generate_report()