from fastapi import APIRouter
from sqlalchemy.orm import Session
from . import models, schemas
from .utils import hash_password
from fastapi import Depends
from ..commons import get_db
router = APIRouter()


@router.post("/users/", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}/", response_model=schemas.User)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.uid == user_id).first()
