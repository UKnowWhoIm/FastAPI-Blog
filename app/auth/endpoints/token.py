from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models
from ..utils import verify_password, create_access_token
from ...db.database import get_db

token_router = APIRouter()


@token_router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username)
    if not user.first():
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(plain_password=form_data.password, hashed_password=user.first().password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user.first().email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


