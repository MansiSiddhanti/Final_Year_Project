# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# ✅ IMPORT ALL MODELS BEFORE create_all
from app.ml.irrigation_model import IrrigationReading

# ROUTES
from app.routes.crops_routes import router as crop_router
from app.routes.auth_routes import router as auth_router
from app.routes.weather_routes import router as weather_router
from app.routes.irrigation_routes import router as irrigation_router
from app.routes.reports_routes import router as reports_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.settings_routes import router as settings_router

app = FastAPI(title="FarmBuddy Backend")

# ✅ CREATE TABLES
Base.metadata.create_all(bind=engine)

# ✅ TEMP DEV CORS (ALLOW EVERYTHING)
# Allow your frontend origin(s)
# Example: origins = ["http://localhost:8080"]

# Allow only your frontend origin (React dev server)
origins = [
    "http://localhost:8080",  # your frontend
    "http://127.0.0.1:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(auth_router, prefix="/auth")
app.include_router(crop_router, prefix="/crops")  # final route: /crops/recommend
app.include_router(weather_router)                 # weather_router already has prefix inside
app.include_router(irrigation_router, prefix="/irrigation")
app.include_router(reports_router, prefix="/reports")
app.include_router(dashboard_router, prefix="/dashboard")
app.include_router(settings_router, prefix="/settings")

@app.get("/")
def root():
    """
    Health check endpoint
    """
    return {"status": "FarmBuddy backend running successfully"}