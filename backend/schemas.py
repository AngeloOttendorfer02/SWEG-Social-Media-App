from pydantic import BaseModel, constr, computed_field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    password: constr(min_length=4, max_length=72)


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    text: str


class PostResponse(BaseModel):
    id: int
    text: str
    image_path: Optional[str]
    resized_image_path: Optional[str]
    created_at: datetime
    user: UserResponse

    @computed_field
    @property
    def username(self) -> str:
        return self.user.username

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
