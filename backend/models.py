from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    text = Column(String)
    image_path = Column(String, nullable=True)
    resized_image_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
