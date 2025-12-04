# 🧩 Exercise Part 3: Docker / Container Creation

This project focuses on **containerizing the social media application** to make it easy to deploy and compatible with other REST API definitions.  
The goal is to package the REST API as a **Docker container** and automate container workflows with **GitHub Actions**.

---

## 📘 Exercise Description

### Objective
Develop a Docker container for the REST API and integrate GitHub Actions to automate the build and deployment process.  
The application should be easy to deploy and run in any environment.

---

## ⚙️ Steps to Complete

### 1. Docker Containerization
- [ ] Create a **Dockerfile** for the REST API including:
  - All necessary libraries and dependencies  
  - Configuration for executing the API from Docker
- [ ] Ensure the container can be **built and run locally** using Docker commands.

### 2. Automate with GitHub Actions
- [ ] Create a **GitHub Actions workflow** that:
  - Automatically builds the Docker container on push or pull request  
  - Pushes the container to a container registry (e.g., Docker Hub or GitHub Container Registry)  
- [ ] Verify that the workflow runs correctly and the container is available in the registry.

---

## 👥 Contribution

| Task Area | Angelo Ottendorfer | Martin Ferschl |
<<<<<<< HEAD
|------------|------------------------------|------------------------------|
| **1. Docker Container** | Create Dockerfile and configure container to run REST API | - |
| **2. GitHub Actions** | - | Implement CI workflow to build and push Docker container |
| **Branch** | `feature/docker` | `feature/docker-ci` |
=======
|------------|------------------------------|--------------------------------|
| **1. Python Application** | Implement `database.py` (SQLite setup, add/retrieve posts) | Support by testing functions manually |
| **3. Testing** | Provide testable database functions | Create `tests/test_app.py` using `pytest` |
| **4. GitHub Actions** | Review pipeline configuration | Create `.github/workflows/ci.yml` and ensure CI runs only on pull requests |
| **5. Final Steps** | Commit app code | Commit tests + CI config and verify all tests pass |
| **Branch** | `feature/backend` | `feature/tests-ci` |
| **Time Required** | 0.5h - 1h | 0.5h - 1h |



>>>>>>> feature-testing
