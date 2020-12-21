from sqlalchemy.orm import Session
from .models import User
from app.auth.utils import hash_password


async def create_user(db: Session, user: User):
    hashed_password = hash_password(user.password)
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def list_user(db: Session):
    return db.query(User).filter(User.is_active)


def get_user_by_id(db: Session, uid: int):
    return db.query(User).filter(User.is_active and User.uid == uid)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email and User.is_active).first()


async def update_user(db: Session, data: dict, uid: int, hashed=False):
    if not hashed and data.get("password"):
        data["password"] = hash_password(data["password"])
    db.query(User).filter(User.uid == uid).update(data)
    db.commit()
