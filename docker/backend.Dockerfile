FROM python:3.11-slim

WORKDIR /backend
RUN mkdir -p /backend/images

COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../backend/ ./
COPY ../backend/images ./images 

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
