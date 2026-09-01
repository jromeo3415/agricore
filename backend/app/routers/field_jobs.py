from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.schemas.field_job import FieldJobRead, FieldJobCreate, FieldJobDiscrepancy, ReliabilityMetrics
from app.models.field_job import FieldJob
from app.models.operator import Operator
from app.models.equipment import Equipment
from app.models.enums import JobStatus, UserRole
from app.models.user import User
from app.dependencies import require_role

router = APIRouter(prefix="/field_jobs", tags=["field jobs"])

@router.get("", response_model=list[FieldJobRead])
async def list_field_jobs(db: AsyncSession = Depends(get_db)) -> list[FieldJob]:
    statement = select(FieldJob)
    result = await db.execute(statement)
    return list(result.scalars().all())

@router.post("", response_model=FieldJobCreate, status_code=status.HTTP_201_CREATED)
async def create_field_jobs(payload: FieldJobCreate, db: AsyncSession = Depends(get_db), _: User = Depends(require_role(UserRole.OPERATIONS_ADMIN))) -> None:
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

@router.get("/reliability_metrics", response_model=list[ReliabilityMetrics])
async def list_reliability_metrics(db: AsyncSession = Depends(get_db)) -> list[ReliabilityMetrics]:
    statement = select(FieldJob.status, Equipment.model).join(Equipment, Equipment.id == FieldJob.equipment_id).where(FieldJob.status.in_([JobStatus.COMPLETED, JobStatus.FAILED]))
    result = await db.execute(statement)
    jobs = result.all()

    job_dict = {}

    for status, model in jobs:
        if model not in job_dict:
            job_dict[model] = {
                JobStatus.COMPLETED: 0,
                JobStatus.FAILED: 0
            }

        print(f"Status: {status} Model: {model}")
        job_dict[model][status.value] += 1

    return [ReliabilityMetrics(
        equipment_model=model,
        completed=data[JobStatus.COMPLETED],
        failed=data[JobStatus.FAILED],
        completed_to_failed= (
            0
            if data[JobStatus.FAILED] == 0
            else data[JobStatus.COMPLETED] / data[JobStatus.FAILED]
        )
    ) for model, data in job_dict.items()]