from ..db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"
    uid = Column(Integer, primary_key=True)
    title = Column(String)
    time_stamp = Column(DateTime)
    content = Column(String)
    author_uid = Column(Integer, ForeignKey("users.uid"))
    author = relationship("app.auth.models.User", back_populates="posts")
