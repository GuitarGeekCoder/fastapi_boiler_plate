from pydantic import BaseModel
from typing import Optional
class OrganizationCreate(BaseModel):
    name : str
    user_id : int

class OrganizationResponse(OrganizationCreate):
    id : int

    class Config:
        orm_mode = True 

class OrganizationUpdate(BaseModel):
    name : Optional[str] = None
    user_id : Optional[int] = None