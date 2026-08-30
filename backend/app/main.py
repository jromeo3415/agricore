from fastapi import FastAPI

from app.routers import field_jobs, equipments

app = FastAPI(
    title="Agricore Farm Operations Command Center",
    description="Farm Management API for managing equipment inventories, field  job assignments, service reports, and equipment health",
    version="0.1.0"
)

app.include_router(field_jobs.router)
app.include_router(equipments.router)

# sample health endpoint to verify application is running correctly
@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}