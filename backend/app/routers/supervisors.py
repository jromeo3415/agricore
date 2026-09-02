'''
Reporting Lines: 
How many farmhands reporting to a specific Regional Agronomy Supervisor 
have active field jobs assigned to them?
'''

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.schemas.supervisor import SupervisorRead, SupervisorActiveOperators
from app.models.supervisor import Supervisor

router = APIRouter(prefix="/supervisors", tags=["supervisors"])

@router.get("", response_model=list[SupervisorRead])
async def list_supervisors(db: AsyncSession = Depends(get_db)) -> list[SupervisorRead]:
    result = await db.execute(select(Supervisor))
    return result.scalars().all()

@router.get("/{id}/active_operators", response_model=list[SupervisorActiveOperators])
async def count_active_operators_for_supervisor(db: AsyncSession = Depends(get_db)) -> list[SupervisorActiveOperators]:
    pass