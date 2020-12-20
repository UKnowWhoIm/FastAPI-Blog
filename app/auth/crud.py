from sqlalchemy.orm import Session
from . import models
from app.auth.utils import hash_password


async def create_user(db: Session, user: models.User):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def list_user(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, uid: int):
    return db.query(models.User).filter(models.User.uid == uid).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


async def update_user(db: Session, data: dict, uid: int, hashed=False):
    if not hashed and data.get("password"):
        data["password"] = hash_password(data["password"])
    db.query(models.User).filter(models.User.uid == uid).update(data)
    db.commit()
