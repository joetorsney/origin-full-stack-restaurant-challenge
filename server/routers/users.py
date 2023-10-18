from fastapi import Depends, APIRouter

from server.auth import get_user
from server.schemas import User

router = APIRouter()

@router.get("/me")
async def read_user(current_user: User = Depends(get_user)):
    return current_user