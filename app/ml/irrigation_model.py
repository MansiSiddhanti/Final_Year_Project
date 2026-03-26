from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime

from app.database import Base


class IrrigationReading(Base):
    __tablename__ = "irrigation_readings"

    id = Column(Integer, primary_key=True, index=True)
    soil_moisture = Column(Float, nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    recorded_at = Column(DateTime, default=datetime.utcnow)