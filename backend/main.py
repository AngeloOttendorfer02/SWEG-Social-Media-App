import os
from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, create_tables, Base, engine
from schemas import PostResponse, PostBase
from typing import Optional, List
import crud
from uuid import uuid4
from fastapi.staticfiles import StaticFiles
import json
from rabbitmq_client import get_channel, send_test_message
from fastapi.responses import FileResponse
import pika

create_tables()

app = FastAPI()

FULL_DIR = "/backend/images/full"
RESIZED_DIR = "/backend/images/resized"

os.makedirs(FULL_DIR, exist_ok=True)
os.makedirs(RESIZED_DIR, exist_ok=True)

app.mount("/images", StaticFiles(directory="images"), name="images")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload-image/")
async def upload_image(file: UploadFile):
    filename = f"{uuid4()}.jpg"
    full_path = os.path.join(FULL_DIR, filename)

    with open(full_path, "wb") as f:
        f.write(await file.read())

    connection, channel = get_channel()
    message = {"filename": filename}
    channel.basic_publish(
        exchange="",
        routing_key="image_resize",
        body=json.dumps(message).encode("utf-8"),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()

    return {"filename": filename, "status": "queued"}


@app.get("/images/{size}/{filename}")
async def get_image(size: str, filename: str):
    if size not in ["full", "resized"]:
        return {"error": "Invalid size"}
    path = os.path.join(f"/backend/images/{size}", filename)
    return FileResponse(path)


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
        file_location = f"images/full/{filename}"

        with open(file_location, "wb") as f:
            f.write(await image.read())

        image_path = file_location

    post_data = PostBase(username=username, text=text)
    post = crud.create_post(db, post_data, image_path)

    if image:
        connection, channel = get_channel()
        message = {"post_id": post.id, "filename": filename}
        channel.basic_publish(
            exchange="",
            routing_key="image_resize",
            body=json.dumps(message).encode("utf-8"),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()

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


@app.get("/test-queue")
def test_queue():
    send_test_message()
    return {"status": "message sent"}
