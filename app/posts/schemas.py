from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    uid: int
    time_stamp: datetime
    author_uid: int

    class Config:
        orm_mode = True


class PostUpdate(PostBase):
    pass
