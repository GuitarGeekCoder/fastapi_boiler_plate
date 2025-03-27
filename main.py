# main.py
from fastapi import FastAPI
from web_app.router.users import user_router
from web_app.router.organization import org_router
from fastapi_boiler_plate.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(org_router)
