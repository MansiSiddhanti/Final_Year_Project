from pydantic import BaseModel

class CropRequest(BaseModel):
    location: str
    temperature: float
    soil_type: str