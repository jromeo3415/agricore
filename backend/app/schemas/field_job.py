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