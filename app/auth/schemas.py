from typing import List
from pydantic import BaseModel
from app.posts.schemas import Post

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    uid: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
