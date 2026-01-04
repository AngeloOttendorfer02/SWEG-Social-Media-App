import pika
import json
import os


def get_channel():
    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_USER", "user"),
        os.getenv("RABBITMQ_PASS", "password")
    )
    parameters = pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
        port=5672,
        credentials=credentials
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="image_resize", durable=True)
    return connection, channel


def send_test_message():
    connection, channel = get_channel()
    message = {"post_id": 1, "filename": "example.png"}
    channel.basic_publish(
        exchange="",
        routing_key="image_resize",
        body=json.dumps(message).encode("utf-8"),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    print("Sent test message to queue")
    connection.close()
