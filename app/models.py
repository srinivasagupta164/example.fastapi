from sqlalchemy import Column,Integer, String , Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable = False) 
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    owener_id = Column(Integer,ForeignKey("users.id", ondelete ="CASCADE"), nullable = False)
    owner = relationship("User")


class User(Base):
    __tablename__ ="users"
    
    id = Column(Integer, nullable =False, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),nullable = False, server_default = text('now()'))
    phone_no = Column(String)

class Vote(Base):
    __tablename__ ="votes"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),primary_key = True)


