from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("")
async def login():
    """Validate user credentials and supply JWT if appropriate

    """
    return {"message": "hi"}