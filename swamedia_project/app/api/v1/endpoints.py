from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, service: UserService = Depends()):
    return await service.create_user(user)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, service: UserService = Depends()):
    return await service.get_user(user_id)
