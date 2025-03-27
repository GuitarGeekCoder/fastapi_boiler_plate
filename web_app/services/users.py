from fastapi import HTTPException


class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, user, model_name):
        # Check if a user already exists with the same email
        existing_user = (
            self.db.query(model_name).filter(model_name.email == user.email).first()
        )

        if existing_user:
            # User already exists, return a message or handle as needed
            raise HTTPException(
                status_code=400, detail="User with this email already exists."
            )
        db_user = model_name(name=user.name, email=user.email)

        # Add user to the session and commit to save to the database
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, id, model_name):
        user = self.db.query(model_name).filter(model_name.id == id).first()
        if user is None:
            raise HTTPException(status_code=400, detail="user not found")
        return user

    def get_all_user(self, model_name):
        users = self.db.query(model_name).all()
        if users is None:
            raise HTTPException(status_code=400, detail="users not found")
        return users
