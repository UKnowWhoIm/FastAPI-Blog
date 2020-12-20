import json

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..commons import get_current_user
from ..schemas import UserUpdate
from ..utils import create_access_token
from ..crud import create_user, get_user_by_email, get_user_by_id, update_user
from fastapi import Depends
from app.commons import oauth2_scheme
from ...db.database import get_db
user_router = APIRouter()


@user_router.post("/", status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    await create_user(db, models.User(email=user.email, password=user.password))
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/{user_id}/", response_model=schemas.User)
async def retrieve_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_user_by_id(db, user_id)


@user_router.patch("/{user_id}/")
async def partial_update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = await get_current_user(token=token, db=db)
    if current_user.uid != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    allowed_fields = ("email", "password")
    data = {key: val for key, val in user_data.__dict__.items() if key in allowed_fields and val is not None}
    await update_user(db, data, user_id)
    access_token = create_access_token(
        data={"sub": data.get("email", get_user_by_id(db, user_id).email)}
    )
    return {"access_token": access_token, "token_type": "bearer"}
