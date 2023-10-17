from fastapi import APIRouter, Depends
from server.schemas import UserAuth
from server.crud.users import add_user
from server.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def post_new_user(
    auth: UserAuth,
    db_session: Session = Depends(get_db),
):
    """Find user by ID and register them if the ID doesn't exist

    """
    return add_user(db_session, auth)