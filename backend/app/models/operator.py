from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from app.models.base import Base
if TYPE_CHECKING:
    from app.models.field_job import FieldJob
    from app.models.farm import Farm

class Operator(Base):
    __tablename__ = "operators"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    farm_id: Mapped[int] = mapped_column(Integer, ForeignKey("farms.id"))

    field_jobs: Mapped[list["FieldJob"]] = relationship(back_populates="operators")
    farms: Mapped["Farm"] = relationship(back_populates="operators")
