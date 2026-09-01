from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import TYPE_CHECKING

from app.models.base import Base
if TYPE_CHECKING:
    from app.models.operator import Operator

class Supervisor(Base):
    __tablename__ = "supervisors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    operators: Mapped[list["Operator"]] = relationship(back_populates="supervisors")