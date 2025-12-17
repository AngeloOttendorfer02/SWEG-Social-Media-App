import pika
import json

def get_channel():
    credentials = pika.PlainCredentials("user", "password")#TODO: replace with env vars!!!
    parameters = pika.ConnectionParameters(
        host="rabbitmq",
        port=5672,
        credentials=credentials
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Ensure queue exists
    channel.queue_declare(queue="image_resize", durable=True)

    return connection, channel


def send_test_message():
    connection, channel = get_channel()

    message = {
        "test": "hello rabbitmq"
    }

    channel.basic_publish(
        exchange="",
        routing_key="image_resize",
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        )
    )

    print("✅ Sent test message to queue")

    connection.close()
