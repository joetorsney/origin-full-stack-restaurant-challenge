from fastapi import APIRouter
from server.schemas import UserAuth

router = APIRouter()

@router.post("/")
def login(data: UserAuth):
    """Validate user data and supply JWT if appropriate

    """
    message = "fail"
    if data.username == "joetorsney" and data.password == "password":
        message = "success"

    return {"message": message}