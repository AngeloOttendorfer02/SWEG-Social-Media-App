#TODO: This script is for testing the message queue ONLY. This MUST be deleted later, as it should not be necessary!!!
import pika
import json
import pytest

def test_rabbitmq_connection():
    """Test that we can connect to RabbitMQ (if available)"""
    try:
        credentials = pika.PlainCredentials("user", "password")
        parameters = pika.ConnectionParameters(
            host="rabbitmq",
            port=5672,
            credentials=credentials
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue="image_resize", durable=True)
        connection.close()
        assert True
    except Exception as e:
        pytest.skip(f"RabbitMQ not available: {e}")

# Original consumer code commented out for CI
# credentials = pika.PlainCredentials("user", "password")
# parameters = pika.ConnectionParameters(
#     host="rabbitmq",
#     port=5672,
#     credentials=credentials
# )

# connection = pika.BlockingConnection(parameters)
# channel = connection.channel()

# channel.queue_declare(queue="image_resize", durable=True)

# def callback(ch, method, properties, body):
#     message = json.loads(body.decode("utf-8"))
#     print("Received message:", message)

#     # acknowledge message so RabbitMQ removes it
#     ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.basic_consume(
#     queue="image_resize",
#     on_message_callback=callback
# )

# print("Waiting for messages...")
# channel.start_consuming()
