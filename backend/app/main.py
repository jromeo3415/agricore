from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from sqlalchemy.exc import IntegrityError


from app.routers import field_jobs, equipments, farms, operators, auth, supervisors

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
    allow_origins=["*"],

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
app.include_router(supervisors.router)

# sample health endpoint to verify application is running correctly
@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={"detail": "A database constraint was violated (e.g. a duplicate value)."},
    )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error has occured."}
    )