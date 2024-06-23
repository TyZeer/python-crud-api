from fastapi import APIRouter

from users.schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["USERS"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(created_user=user)
