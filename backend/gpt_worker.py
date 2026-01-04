import json
import pika
import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Post

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

tokenizer.pad_token = tokenizer.eos_token

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="sentiment_analysis", durable=True)

def analyze_sentiment(text: str):
    prompt = (
        "Classify the sentiment of the following text as Positive, Neutral, or Negative.\n\n"
        f"Text: \"{text}\"\n"
        "Sentiment:"
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=5,
            pad_token_id=tokenizer.eos_token_id,
            return_dict_in_generate=True,
            output_scores=True
        )

    decoded = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True).lower()

    if "positive" in decoded:
        sentiment = "positive"
    elif "negative" in decoded:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    scores = outputs.scores[-1]
    probs = torch.softmax(scores, dim=-1)
    confidence = torch.max(probs).item()

    return sentiment, confidence

def generate_reply(text: str) -> str:
    prompt = (
        "You are a helpful social media assistant. Write a short, friendly, and relevant reply to the following post. "
        "Keep it under 50 words, positive, and engaging. Do not add extra text.\n\n"
        f"Post: {text}\n"
        "Reply:"
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    if "Reply:" in decoded:
        reply = decoded.split("Reply:")[-1].strip()
    else:
        reply = decoded.strip()

    # Post-process: limit to first sentence or reasonable length
    reply = reply.split('.')[0] + '.' if '.' in reply else reply
    if len(reply) > 100:
        reply = reply[:100] + '...'

    return reply.strip()

def callback(ch, method, properties, body):
    data = json.loads(body)

    post_id = data["post_id"]
    text = data["text"]

    sentiment, confidence = analyze_sentiment(text)
    suggested_reply = generate_reply(text)

    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()

    if post:
        post.sentiment = sentiment
        post.sentiment_score = confidence
        post.suggested_reply = suggested_reply
        db.commit()

    db.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="sentiment_analysis", on_message_callback=callback)

print("GPT-2 worker started (sentiment + text generation)")
channel.start_consuming()
