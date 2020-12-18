from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from ..db.database import Base


class User(Base):
    __tablename__ = "users"
    uid = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    posts = relationship("app.posts.models.Post", back_populates="author")