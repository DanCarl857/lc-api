from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

# Post Table
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1000))
    user_id = Column(Integer, ForeignKey("users.id"))
