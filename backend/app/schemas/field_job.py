from pydantic import Field, BaseModel, ConfigDict

from app.models.enums import JobPriority, JobStatus

class FieldJobBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    priority: JobPriority
    status: JobStatus
    equipment_id: int
    operator_id: int

class FieldJobRead(FieldJobBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class FieldJobCreate(FieldJobBase):
    pass

class FieldJobDiscrepancy(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    equipment_farm_id: int
    operator_farm_id: int

class ReliabilityMetrics(BaseModel):
    equipment_model: str = Field(min_length=1, max_length=100)
    completed: int
    failed: int
    completed_to_failed: float