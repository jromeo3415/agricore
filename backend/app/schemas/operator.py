from pydantic import BaseModel, Field, ConfigDict

class OperatorBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    farm_id: int

class OperatorRead(OperatorBase):
    id: int
    model_config =ConfigDict(from_attributes=True)