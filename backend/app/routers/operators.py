from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.operator import OperatorRead
from app.dependencies import get_db
from app.models.operator import Operator

router = APIRouter(prefix="/operators", tags=["operators"])

@router.get("", response_model=list[OperatorRead])
async def list_operators(db: AsyncSession = Depends(get_db)) -> list[OperatorRead]:
    result = await db.execute(select(Operator))
    return result.scalars().all()