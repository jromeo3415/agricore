from decimal import Decimal

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.enums import EquipmentStatus
from app.schemas.farm import FarmRead, FarmFlagged
from app.dependencies import get_db
from app.models.farm import Farm
from app.models.equipment import Equipment

router = APIRouter(prefix="/farms", tags=["farms"])

@router.get("", response_model=list[FarmRead])
async def list_farms(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Farm))
    return list(result.scalars().all())

@router.get("/maintenance_flags" , response_model=list[FarmFlagged])
async def list_flagged_farms(db: AsyncSession = Depends(get_db)):
    statement = select(Equipment.facility_id, Equipment.status, Farm.name).join(Farm, Equipment.facility_id == Farm.id)
    result = await db.execute(statement)
    equipments = result.mappings().all()

    farm_data = {}
    for equipment in equipments:
        facility_id = equipment["facility_id"]

        farm = farm_data.setdefault(
            facility_id, 
            {
                "status": equipment["status"],
                "name": equipment["name"],
                "count": 0,
                "maintenance-count": 0
            }
        )

        farm_data[facility_id]["count"] += 1

        if farm_data[facility_id]["status"] == EquipmentStatus.MAINTENANCE:
            farm_data[facility_id]["maintenance-count"] += 1

    flagged_farms = list()
    for farm_id, farm_data in farm_data.items():
        if farm_data["count"] == 0:
            continue

        maintenance_ratio = Decimal(farm_data["maintenance-count"]) / Decimal(farm_data["count"])

        if maintenance_ratio > 0.3:
            flagged = FarmFlagged(
                id = farm_id,
                name = farm_data["name"],
                count = farm_data["count"],
                maintenance_count = farm_data["maintenance-count"],
                maintenance_percent = maintenance_ratio,
            )
            flagged_farms.append(flagged)

    return flagged_farms