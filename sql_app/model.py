from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.types import Text

class User(Base):
    __tablename__ = "user_info"

    user_name  = Column(String)
    student_num = Column(Integer, primary_key=True)
    user_email = Column(String)
    phone_num = Column(Integer)
    user_password = Column(String)
    user_role = Column(String)

    comments = relationship("Comment", back_populates="owner")

class Comment(Base):
    __tablename__ = "comment_info"

    hashtags = Column(Integer)
    message = Column(Text)
    comment_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("user_info.student_num"))

    owner = relationship("User", back_populates="comments")