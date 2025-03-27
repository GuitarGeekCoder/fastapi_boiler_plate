from pydantic import BaseModel
class OrganizationCreate(BaseModel):
    name : str
    user_id : int

class OrganizationResponse(OrganizationCreate):
    id : int

    class Config:
        orm_mode = True 