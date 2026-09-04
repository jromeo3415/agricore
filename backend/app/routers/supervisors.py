'''
Reporting Lines: 
How many farmhands reporting to a specific Regional Agronomy Supervisor 
have active field jobs assigned to them?
'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.dependencies import get_db
from app.schemas.supervisor import SupervisorRead, SupervisorActiveOperators
from app.models.supervisor import Supervisor
from app.models.enums import JobStatus
from app.models.field_job import FieldJob
from app.models.operator import Operator

router = APIRouter(prefix="/supervisors", tags=["supervisors"])

@router.get("", response_model=list[SupervisorRead])
async def list_supervisors(db: AsyncSession = Depends(get_db)) -> list[SupervisorRead]:
    result = await db.execute(select(Supervisor))
    return result.scalars().all()

'''
Reporting Lines: How many farmhands reporting to a specific Regional Agronomy Supervisor
have active (enum = In-Progress) field jobs assigned to them?

'''
@router.get("/{id}/active_operators", response_model=SupervisorActiveOperators)
async def count_active_operators_for_supervisor(id: int, db: AsyncSession = Depends(get_db)) -> SupervisorActiveOperators:
    statement = (
        select(
            Supervisor.id,
            Supervisor.name,
            func.count(FieldJob.id).label("operator_count"),
        )
        .join(Operator, Operator.supervisor_id == Supervisor.id)
        .join(FieldJob, FieldJob.operator_id == Operator.id)
        .where(Operator.supervisor_id == id)
        .where(FieldJob.status == JobStatus.IN_PROGRESS)
        .group_by(Supervisor.id, Supervisor.name)
    )
    result = await db.execute(statement)
    supervisor_data = result.mappings().one_or_none()

    if supervisor_data is None:
        raise HTTPException(
            status_code=404,
            detail="Supervisor not found or has no active jobs",
        )

    return SupervisorActiveOperators(
        id=supervisor_data["id"],
        name=supervisor_data["name"],
        farmhands_active_jobs=supervisor_data["operator_count"],
    )