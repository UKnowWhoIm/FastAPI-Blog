from fastapi import APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..commons import get_current_user
from ..utils import hash_password, create_access_token
from fastapi import Depends
from app.commons import oauth2_scheme
from ...db.database import get_db
user_router = APIRouter()


@user_router.post("/", status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/{user_id}/", response_model=schemas.User)
async def retrieve_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db.query(models.User).filter(models.User.uid == user_id).first()


@user_router.patch("/{user_id}/", response_model=schemas.User)
async def partial_update_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    pass
