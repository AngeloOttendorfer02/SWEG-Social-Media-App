import os
from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import PostResponse, PostBase
from typing import Optional, List
import crud
from uuid import uuid4
from fastapi.staticfiles import StaticFiles


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")
# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Ensure images folder exists
if not os.path.exists("images"):
    os.makedirs("images")


@app.post("/create-post", response_model=PostResponse)
async def create_post(
    username: str = Form(...),
    text: str = Form(...),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):

    image_path = None

    if image:
        file_ext = image.filename.split(".")[-1]
        filename = f"{uuid4()}.{file_ext}"
        file_location = f"images/{filename}"

        with open(file_location, "wb") as f:
            f.write(await image.read())

        image_path = file_location

    post_data = PostBase(username=username, text=text)
    post = crud.create_post(db, post_data, image_path)

    return post


@app.get("/get-all-posts", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return crud.get_all_posts(db)


@app.get("/get-all-posts-by-user/{username}", response_model=List[PostResponse])
def get_posts_by_user(username: str, db: Session = Depends(get_db)):
    return crud.get_posts_by_user(db, username)


@app.delete("/delete-post/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
