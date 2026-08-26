from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from decimal import Decimal

from app.models.enums import EquipmentStatus
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.farm import Farm

class Equipment(Base):
    __tablename__ = "equipments"

    id: Mapped[int] = mapped_column(primary_key=True)
    serial_number: Mapped[str] = mapped_column(String(150), unique=True)
    model: Mapped[str] = mapped_column(String(100))
    status: Mapped[EquipmentStatus] = mapped_column(
        SqlEnum(
            EquipmentStatus,
            name="equipment_status",
            values_callable = lambda enum_cls: [member.value for member in enum_cls]
        )
    )
    fuel_level: Mapped[Decimal] = mapped_column[Numeric(5, 2)]
    facility_id: Mapped[int] = mapped_column[Integer, ForeignKey("farms.id")]

    farm: Mapped[Farm] = relationship(back_populates="equipments")