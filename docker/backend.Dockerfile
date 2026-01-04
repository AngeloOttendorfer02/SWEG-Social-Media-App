FROM python:3.11-slim

WORKDIR /backend

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn pika pillow sqlalchemy python-multipart psycopg2-binary passlib[pbkdf2_sha256] python-jose[cryptography]

COPY backend/ ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
