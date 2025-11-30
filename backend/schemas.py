from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    username: str
    text: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    image_path: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True  # correct for Pydantic v2
