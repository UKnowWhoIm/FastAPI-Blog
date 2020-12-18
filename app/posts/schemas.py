from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    uid: int
    timestamp: datetime

    class Config:
        orm_mode = True
