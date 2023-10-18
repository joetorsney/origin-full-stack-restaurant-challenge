from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from server.crud.users import get_user_from_username
from server.utils import get_db

auth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def fake_decode_token(token: str, db_session: Session = Depends(get_db)):
    # This doesn't provide any security at all
    return get_user_from_username(db_session, token)

def get_user(token: str = Depends(auth_scheme), db_session: Session = Depends(get_db)):
    user = fake_decode_token(token, db_session)
    return user