from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.schemas.field_job import FieldJobRead, FieldJobCreate
from app.models.field_job import FieldJob

router = APIRouter(prefix="/field_jobs", tags=["field jobs"])

@router.get("", response_model=FieldJobRead)
async def list_field_jobs(db: AsyncSession = Depends(get_db)) -> list[FieldJob]:
    statement = select(FieldJob)
    result = await db.execute(statement)

    return result.scalars().all()

@router.post("", response_model=FieldJobCreate, status_code=status.HTTP_201_CREATED)
async def create_field_jobs(payload: FieldJobCreate, db: AsyncSession = Depends(get_db)) -> None:
    field_job = FieldJob(**payload.model_dump())

    db.add(field_job)
    await db.commit()
    await db.refresh(field_job)