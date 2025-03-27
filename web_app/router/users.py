# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from web_app.models.user import User
from web_app.schemas.user import UserCreate,UserResponse
from database import SessionLocal, engine, get_db
from fastapi import APIRouter
from web_app.services.users import UserService
from typing import List

# Create the tables in the database (if they don't exist)
User.metadata.create_all(bind=engine)

user_router = APIRouter(
    prefix="/users",
)


# API endpoint to create a new user
@user_router.post("/create/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    us = UserService(db=db)
    return us.create_user(user, User)


# API endpoint to get a user by ID
@user_router.get("/get/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    us = UserService(db=db)
    return us.get_user(user_id, User)


# API endpoint to get all users
@user_router.get("/get_all/", response_model=List[UserResponse])
def get_all_user(db: Session = Depends(get_db)):
    us = UserService(db=db)
    return us.get_all_user(User)
