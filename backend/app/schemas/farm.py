from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict

class FarmBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    location_region: str = Field(min_length=1, max_length=50)
    capacity: int
    supervisor_id: int

class FarmRead(FarmBase):
    id: int
    model_config=ConfigDict(from_attributes=True)

class FarmFlagged(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=100)
    count: int
    maintenance_count: int
    maintenance_percent: Decimal = Field(max_digits=5, decimal_places=2)