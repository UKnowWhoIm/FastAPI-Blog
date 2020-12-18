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
    author_uid: int

    class Config:
        orm_mode = True
