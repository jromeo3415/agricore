from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routers import field_jobs, equipments, farms, operators, auth

load_dotenv()

app = FastAPI(
    title="Agricore Farm Operations Command Center",
    description="Farm Management API for managing equipment inventories, field  job assignments, service reports, and equipment health",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware, 

    # Endpoint for our frontend
    allow_origins=[os.getenv("FRONTEND_ORIGIN")],

    # this allows us to pass an authorization header using JWT
    allow_credentials=True,

    # this allows all methods and headers through
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(field_jobs.router)
app.include_router(equipments.router)
app.include_router(farms.router)
app.include_router(operators.router)

# sample health endpoint to verify application is running correctly
@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}