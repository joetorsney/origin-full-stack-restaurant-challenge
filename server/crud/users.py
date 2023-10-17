from sqlalchemy.orm import Session
from fastapi import HTTPException

import server.models as md

def get_users(db_session: Session):
    return db_session.query(md.User).all()

def get_user_from_username(db_session: Session, item: md.User):
    result = db_session.query(md.User).filter(md.User.username == item.username)
    return result.first()

def add_user(db_session: Session, item: md.User):
    to_fetch = db_session.query(md.User).filter(md.User.username == item.username)

    if to_fetch.first():
        raise HTTPException(status_code=409, detail="Resource already exists.")

    item = md.User(username=item.username, password=item.password)

    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    return item
