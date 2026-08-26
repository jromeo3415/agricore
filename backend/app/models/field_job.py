from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Enum as SqlEnum
from typing import TYPE_CHECKING

from app.models.base import Base
from app.models.enums import JobPriority, JobStatus
if TYPE_CHECKING:
    from app.models.equipment import Equipment
    from app.models.operator import Operator

class FieldJob(Base):
    __tablename__ = "field_jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    priority: Mapped[JobPriority] = mapped_column(SqlEnum(
                                                            JobPriority,
                                                            name="job_priority",
                                                            values_callable = lambda enum_cls: [member.value for member in enum_cls]
                                                        ))
    status: Mapped[JobStatus] = mapped_column(SqlEnum(
                                                        JobStatus,
                                                        name="job_status",
                                                        values_callable = lambda enum_cls: [member.value for member in enum_cls]
    ))
    equipment_id: Mapped[int] = mapped_column(Integer, ForeignKey("equipments.id"))
    operator_id: Mapped[int] = mapped_column(Integer, ForeignKey("operators.id"))

    equipment: Mapped["Equipment"] = relationship(back_populates="field_jobs")
    operator: Mapped["Operator"] = relationship(back_populates="field_jobs")