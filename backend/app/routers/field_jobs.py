from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.schemas.field_job import FieldJobRead, FieldJobCreate, FieldJobDiscrepancy
from app.models.field_job import FieldJob
from app.models.operator import Operator
from app.models.equipment import Equipment

router = APIRouter(prefix="/field_jobs", tags=["field jobs"])

@router.get("", response_model=list[FieldJobRead])
async def list_field_jobs(db: AsyncSession = Depends(get_db)) -> list[FieldJob]:
    statement = select(FieldJob)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.post("", response_model=FieldJobCreate, status_code=status.HTTP_201_CREATED)
async def create_field_jobs(payload: FieldJobCreate, db: AsyncSession = Depends(get_db)) -> None:
    field_job = FieldJob(**payload.model_dump())

    db.add(field_job)
    await db.commit()
    await db.refresh(field_job)
    return field_job

@router.get("/discrepancies", response_model=list[FieldJobDiscrepancy])
async def list_colocation_discrepancies(db: AsyncSession = Depends(get_db)) -> list[FieldJobDiscrepancy]:
    statement = select(FieldJob.id, FieldJob.title, Equipment.facility_id.label('equipment_farm_id'), Operator.farm_id.label('operator_farm_id')).join(Equipment, Equipment.id == FieldJob.equipment_id).join(Operator, Operator.id == FieldJob.operator_id).where(Operator.farm_id != Equipment.facility_id)
    result = await db.execute(statement)
    print(f"RESULT: {result}")
    return list(result.mappings().all())
