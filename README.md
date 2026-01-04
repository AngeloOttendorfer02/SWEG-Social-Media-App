# 🧠 Exercise Part 6: Event-Driven Machine Learning Services

This exercise extends the social media application by introducing **machine-learning–based microservices** to enhance user experience.  
Pre-trained **GPT-2 / DistilGPT-2 models** are integrated into the system to provide **sentiment analysis** and **text generation**, leveraging an **event-driven architecture** for asynchronous processing.

---

## 📘 Exercise Description

### Objective
Enhance the application by introducing **ML-powered microservices** that:

- Analyze user-generated content using **sentiment analysis**
- Generate **context-aware reply suggestions**
- Process ML tasks asynchronously using a **message queue**
- Store additional ML metadata in the database
- Integrate seamlessly into the existing microservice architecture

This approach improves scalability, responsiveness, and user engagement while demonstrating real-world ML system design.

---

## ⚙️ Steps to Complete

### 1. Event-Driven ML Processing
- [x] Submit text-analysis tasks to a **message queue** after post creation  
- [x] Perform **sentiment analysis** asynchronously using a pre-trained GPT-2 model  
- [x] Compute and store a **confidence score** for the sentiment prediction  
- [x] Generate **reply suggestions** using a GPT-based language model  

Sentiment analysis is handled asynchronously via RabbitMQ, ensuring non-blocking API responses.

---

### 2. Microservice Architecture
- [x] Implement ML inference as a **dedicated GPT-2 worker service**
- [x] Separate ML logic from the main backend service
- [x] Integrate the ML worker into the existing **Docker Compose** setup
- [x] Ensure services communicate exclusively via a **message queue**

---

### 3. API, Database, and Frontend Updates
- [x] Extend the database schema to store:
  - Sentiment label  
  - Sentiment confidence score  
- [x] Adapt REST API endpoints to expose ML-enriched post data  
- [x] Add a **sentiment badge** to the frontend UI  
- [x] Enable **on-demand reply suggestion generation** from the frontend  
- [x] Display AI-generated suggestions directly in the WebApp  

---

### 4. Container Orchestration
- [x] Add ML worker service to container orchestration
- [x] Ensure reproducible environments for:
  - Backend
  - Frontend
  - GPT-2 worker
  - Message broker (RabbitMQ)

---

## 🧠 ML Models Used

- **DistilGPT-2**
  - Faster inference
  - Lower memory footprint
  - Suitable for real-time applications
- Hugging Face `transformers` library

---

## 👥 Time Required ~6–8 hours
