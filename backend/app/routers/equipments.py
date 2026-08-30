from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from decimal import Decimal

from app.dependencies import get_db
from app.schemas.equipment import EquipmentRead
from app.models.equipment import Equipment

router = APIRouter(prefix="/equipments", tags=["equipments"])

@router.get("", response_model=list[EquipmentRead])
async def list_equipments(  fuel_threshold: Decimal | None = Query(
                                                                        default = None,
                                                                        ge=0,
                                                                        le=100,
                                                                        description="Only return equipments below this threshold, if a threshold is specified"
                                                                    ),
                            db: AsyncSession = Depends(get_db)) -> list[EquipmentRead]:
    statement = select(Equipment)

    if fuel_threshold is not None:
        statement = statement.where(Equipment.fuel_level < fuel_threshold)

    result = await db.execute(statement)
    return list(result.scalars().all())