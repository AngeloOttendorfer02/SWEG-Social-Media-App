import os
import time
import json
from models import Post
from PIL import Image
import pika


FULL_DIR = "/backend/images/full"
RESIZED_DIR = "/backend/images/resized"

os.makedirs(FULL_DIR, exist_ok=True)
os.makedirs(RESIZED_DIR, exist_ok=True)
print("📁 Image directories ensured", flush=True)


RABBITMQ_URL = os.getenv(
    "RABBITMQ_URL",
    "amqp://user:password@rabbitmq:5672/"
)

while True:
    try:
        parameters = pika.URLParameters(RABBITMQ_URL)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="image_resize", durable=True)
        print("✅ Connected to RabbitMQ", flush=True)
        break
    except pika.exceptions.AMQPConnectionError:
        print("⏳ RabbitMQ not ready, retrying in 3 seconds...", flush=True)
        time.sleep(3)


def get_db_session():
    from database import SessionLocal
    return SessionLocal()


def resize_image(filename: str) -> str:
    full_path = os.path.join(FULL_DIR, filename)
    resized_path = os.path.join(RESIZED_DIR, filename)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Full image not found: {full_path}")

    with Image.open(full_path) as img:
        img.thumbnail((200, 200))
        img.save(resized_path)

    print(f"✅ Resized image saved: {resized_path}", flush=True)
    return resized_path


def callback(ch, method, properties, body):
    if not body:
        print("Empty body, nacking")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        return
    try:
        message = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}, body: {body}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        return
    db = get_db_session()
    try:
        post_id = message["post_id"]
        filename = message["filename"]

        print(f"🔄 Processing post_id={post_id}, file={filename}", flush=True)

        resize_image(filename)

        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            print("⚠️ Post not found in database", flush=True)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        post.resized_image_path = f"images/resized/{filename}"
        db.commit()
        print("✅ Database updated with resized image path", flush=True)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        db.rollback()
        print("❌ Error processing message:", e, flush=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    finally:
        db.close()


channel.basic_consume(queue="image_resize", on_message_callback=callback)
print("👂 Worker listening for messages...", flush=True)
channel.start_consuming()
