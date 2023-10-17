from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from server.schemas import UserAuth
from server.crud.users import get_user_from_username
from server.utils import get_db

router = APIRouter()

@router.post("/")
def login(data: UserAuth, db_session: Session = Depends(get_db),):
    """Validate user data and supply token

    """
    user = get_user_from_username(db_session, data)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if user.password != data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # For now, the token is just the username, obviously this is bad for security.
    return {"access_token": user.username, "token_type": "bearer"}
