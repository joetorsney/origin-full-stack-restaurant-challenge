from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.schemas import OrderBase, Order, User
from server.crud.orders import get_orders, add_order
from server.auth import get_user
from server.utils import get_db

router = APIRouter()

@router.get("", response_model=List[Order])
async def search_orders(db_session: Session = Depends(get_db), current_user: User = Depends(get_user)):
    """Find order by ID.

    """
    return get_orders(db_session, current_user)


@router.post("", response_model=Order)
async def add_new_order(
    item: OrderBase,
    db_session: Session = Depends(get_db),
    current_user: User = Depends(get_user)
):
    """Find order by ID.

    """
    return add_order(db_session, item, current_user)