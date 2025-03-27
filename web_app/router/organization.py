from database import SessionLocal, engine, get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from web_app.services.organization import OrganizationService
from web_app.models.organization import Organization
from web_app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
)

# Create the tables in the database (if they don't exist)
Organization.metadata.create_all(bind=engine)

org_router = APIRouter(
    prefix="/org",
)


@org_router.get("/get_org/{org_id}")
def get_org(org_id: int, db: Session = Depends(get_db)):
    os = OrganizationService(db=db)
    return os.get_org_by_id(Organization, org_id)


@org_router.post("/create/", response_model=OrganizationResponse)
def create_org(org: OrganizationCreate, db: Session = Depends(get_db)):
    os = OrganizationService(db=db)
    return os.create_org(Organization, org)


@org_router.delete("/delete/{org_id}")
def delete_org(org_id: int, db: Session = Depends(get_db)):
    os = OrganizationService(db=db)
    return os.delete_org(Organization, org_id)


@org_router.patch("/update/{org_id}")
def update_org(
    org_id: int, org_data: OrganizationUpdate, db: Session = Depends(get_db)
):
    os = OrganizationService(db=db)
    return os.update_org(Organization, org_id=org_id, org_data=org_data)
