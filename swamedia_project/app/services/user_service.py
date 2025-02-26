from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate
from fastapi import Depends

class UserService:
    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    async def create_user(self, user: UserCreate):
        return await self.repo.create_user(user)

    async def get_user(self, user_id: int):
        return await self.repo.get_user(user_id)
