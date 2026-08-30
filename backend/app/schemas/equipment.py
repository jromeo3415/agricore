from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

from app.models.enums import EquipmentStatus

class EquipmentBase(BaseModel):
    serial_number: str = Field(min_length=1, max_length=150)
    model: str = Field(min_length=1, max_length=100)
    status: EquipmentStatus
    fuel_level: Decimal
    facility_id: int

class EquipmentRead(EquipmentBase):
    id: int
    model_config=ConfigDict(from_attributes=True)