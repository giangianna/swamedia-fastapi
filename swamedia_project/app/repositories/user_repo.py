from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.database import get_db
from fastapi import Depends

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def create_user(self, user: UserCreate):
        new_user = User(username=user.username, email=user.email, password_hash="hashed_password")
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
