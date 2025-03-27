
from database import SessionLocal, engine, get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from web_app.services.organization import OrganizationService
from web_app.models.organization import Organization
from web_app.schemas.organization import OrganizationCreate,OrganizationResponse

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
def create_org(org:OrganizationCreate, db: Session = Depends(get_db)):
    os = OrganizationService(db=db)
    return os.create_org(Organization, org)

