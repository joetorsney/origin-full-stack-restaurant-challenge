import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .routers.orders import router as orders_router
from .routers.plates import router as plates_router
from .routers.login import router as login_router
from .routers.register import router as register_router
from .routers.users import router as user_router
from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(root_path='/api/', version="0.3.0")

app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(plates_router, prefix="/plates", tags=["plates"])
app.include_router(login_router, prefix='/login')
app.include_router(register_router, prefix='/register')
app.include_router(user_router, prefix='/user')

@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
