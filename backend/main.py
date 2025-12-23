import os
import json
from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import Optional, List
from uuid import uuid4
import pika

from database import get_db, create_tables
import crud
import models
from schemas import PostResponse, PostBase, UserCreate, UserResponse, Token
from rabbitmq_client import get_channel
from auth import create_access_token, get_current_user

create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = crud.create_user(db, user.username, user.password)
    
    token = create_access_token({"sub": new_user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    authenticated = crud.authenticate_user(db, user.username, user.password)
    if not authenticated:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token without expires_delta
    token = create_access_token({"sub": authenticated.username})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/create-post", response_model=PostResponse)
async def create_post(
    text: str = Form(...),
    image: Optional[UploadFile] = File(None),
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    image_path = None
    filename = None

    if image:
        file_ext = image.filename.split(".")[-1]
        filename = f"{uuid4()}.{file_ext}"
        file_location = f"images/full/{filename}"
        with open(file_location, "wb") as f:
            f.write(await image.read())
        image_path = file_location

    post_data = PostBase(username=current_user.username, text=text)
    post = crud.create_post(db, current_user, text, image_path)

    if image:
        connection, channel = get_channel()
        channel.basic_publish(
            exchange="",
            routing_key="image_resize",
            body=json.dumps({"post_id": post.id, "filename": filename}),
            properties=pika.BasicProperties(delivery_mode=2),
        )
        connection.close()

    return post


@app.get("/get-all-posts", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return crud.get_all_posts(db)


@app.delete("/delete-post/{post_id}")
def delete_post(
    post_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")

    db.delete(post)
    db.commit()

    return {"detail": "Post deleted successfully"}
