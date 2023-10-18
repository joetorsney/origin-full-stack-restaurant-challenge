from server.utils import get_db
from server.schemas import User
import server.models as md
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from server.crud.users import get_user_from_username


router = APIRouter()

auth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def fake_decode_token(token: str, db_session: Session = Depends(get_db)):
    # This doesn't provide any security at all
    return get_user_from_username(db_session, token)

def get_user(token: str = Depends(auth_scheme), db_session: Session = Depends(get_db)):
    user = fake_decode_token(token, db_session)
    return user

@router.get("/me")
async def read_user(current_user: User = Depends(get_user)):
    return current_user