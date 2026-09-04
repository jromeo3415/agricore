from pydantic import BaseModel, Field, ConfigDict

class SupervisorBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)

class SupervisorRead(SupervisorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SupervisorActiveOperators(SupervisorRead):
    farmhands_active_jobs: int