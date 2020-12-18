from ..db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"
    uid = Column(Integer, primary_key=True)
    title = Column(String)
    time_stamp = Column(DateTime)
    content = Column(String)
