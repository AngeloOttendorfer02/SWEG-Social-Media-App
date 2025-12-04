from sqlalchemy.orm import Session
from models import Post
from schemas import PostCreate
from typing import Optional
from datetime import datetime

def create_post(db: Session, data: PostCreate, image_path: Optional[str]):
    post = Post(
        username=data.username,
        text=data.text,
        image_path=image_path,
        created_at=datetime.utcnow()
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all_posts(db: Session):
    return db.query(Post).order_by(Post.created_at.desc()).all()


def get_posts_by_user(db: Session, username: str):
    return (
        db.query(Post)
        .filter(Post.username == username)
        .order_by(Post.created_at.desc())
        .all()
    )


def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
