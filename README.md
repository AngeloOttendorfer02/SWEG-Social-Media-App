# 🧩 Exercise Part 5: Event-Driven Architecture

This exercise extends the social media application with an **event-driven architecture** to improve image loading performance.  
Instead of serving only full-size images, the application now processes images asynchronously to generate **reduced-size versions** using a dedicated microservice triggered by a **message queue**.

---

## 📘 Exercise Description

### Objective
Enhance the application by introducing an **image processing microservice** that:

- Stores both **full-size** and **reduced-size** images  
- Uses a **message queue** to trigger image resizing asynchronously  
- Separates image processing logic into an independent container  
- Updates the REST API and frontend to support optimized image delivery  

This approach improves scalability, performance, and user experience.

---

## ⚙️ Steps to Complete

### 1. Event-Driven Image Processing
- [ ] Store both **original** and **resized** versions of uploaded images  
- [ ] Submit image-processing tasks to a **message queue** after image upload  
- [ ] Implement a **separate image resize service** that:
  - Listens to the queue  
  - Processes images asynchronously  
  - Stores the resized image  

### 2. Microservice Architecture
- [ ] Provide the image resize functionality as a **dedicated container**  
- [ ] Integrate the image processing service into the existing Docker Compose setup  
- [ ] Ensure services communicate via the message queue  

### 3. API and Frontend Updates
- [ ] Extend the **REST API** to:
  - Serve full-size images  
  - Serve reduced-size images  
- [ ] Update the REST API + WebApp as needed to enable reduced-size + full-size images  

### 4. Automation with GitHub Actions
- [ ] Add **unit and integration tests** for:
  - Backend API  
  - Image processing service  
- [ ] Create GitHub Actions workflows to:
  - Automatically test all services  
  - Build and push Docker images for:
    - Backend  
    - Frontend  
    - Image processing service  

---

## 👥 Contribution

| Task Area | Angelo Ottendorfer | Martin Ferschl |
|------------|------------------------------|------------------------------|
| **1. Event-Driven Design** | - | Design message queue integration |
| **2. Image Processing Service** | Implement image resize microservice | - |
| **3. REST API & Frontend Updates** | Extend API and frontend for image handling | - |
| **4. GitHub Actions** | - | Configure CI workflows for testing and container publishing |
| **Branch** | `feature-messagequeue` | `feature-messagequeue`, `feature-testing` |
| **Time Required** | 4h |  |
