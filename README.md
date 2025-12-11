# 🧩 Exercise Part 1: Automation

This project is the **first step in developing a simple social media application**.  
The goal of this exercise is to design a small Python program that stores and retrieves social media posts from a database and to automate testing using GitHub Actions.

---

## 📘 Exercise Description

### Objective
Develop a Python application that can:
- Store **social media posts** in a database containing:
  - 🖼️ Image  
  - 💬 Text (comment)  
  - 👤 User  
- Retrieve the **latest post** from the database.


---

## ⚙️ Steps to Complete
 

### 1. Develop Python Application
- [ ] Define the post information (image, text, user).  
- [ ] Store multiple posts in a **SQLite database**.  
- [ ] Implement functionality to **retrieve the latest post**.

### 2. Test the Application
- [ ] Write unit tests to verify database storage and retrieval logic.  
- [ ] Ensure the program runs correctly and returns the expected data.

### 3. Configure GitHub Actions
- [ ] Create a **GitHub Actions workflow** that:
  - Automatically runs tests on pull requests.  
  - Ensures all tests pass before merging.  

### 4. Final Steps
- [ ] Commit all developed code and workflow configurations.  
- [ ] Push the final version to GitHub.

---

## 👥 Contribution

| Task Area | Angelo Ottendorfer | Martin Ferschl |
|------------|------------------------------|--------------------------------|
| **1. Python Application** | Implement `database.py` (SQLite setup, add/retrieve posts) | Support by testing functions manually, react setup |
| **3. Testing** | Provide testable database functions | Create `tests/test_app.py` using `pytest` |
| **4. GitHub Actions** | Review pipeline configuration | Create `.github/workflows/ci.yml` and ensure CI runs only on pull requests |
| **5. Final Steps** | Commit app code | Commit tests + CI config and verify all tests pass |
| **Branch** | `feature/backend` | `react` |


# 🧩 Exercise Part 2: REST API

This project is the **next step in developing the simple social media application**.  
The goal of this exercise is to create a REST API to expose the functionality developed in Part 1 and integrate it with a **React web frontend**.

---

## 📘 Exercise Description

### Objective
Develop a REST API and a web application that can:  
- **Send, retrieve, and search social media posts** via API endpoints.  
- Expose the functionality of the Python application from Part 1.  
- Provide a **React frontend** to interact with the API.

---

## ⚙️ Steps to Complete

### 1. Develop REST API
- [ ] Implement API endpoints to:
  - Submit a new post  
  - Retrieve posts  
  - Search posts by user or content
- [ ] Provide an **FastAPI specification** for your REST API.  

### 2. Expand Testing
- [ ] Extend the testing framework to include API tests (e.g., using `pytest` + `requests`).  
- [ ] Ensure all API endpoints work as expected.  

### 3. Create Web Application
- [ ] Develop a **React frontend** that can:
  - Submit a post  
  - List and display all posts  
  - Search and display posts by user  

### 4. Git & GitHub Workflow
- [ ] Commit code frequently.  
- [ ] Track feature requests in GitHub issues.  
- [ ] Use **feature branches** and **pull requests** to integrate changes.

---

## 👥 Contribution

| Task Area | Martin Ferschl |
|------------|------------------------------|
| **1. REST API** | Implement all endpoints for submitting, retrieving, and searching posts |
| **2. OpenAPI Spec** | Create OpenAPI/Swagger documentation for the API |
| **3. Testing** | Expand testing framework to cover all API functionality |
| **4. React Frontend** | Develop web frontend to submit, list, and search posts |
| **5. Git & GitHub** | Commit frequently, track features, manage feature branches & pull requests |
| **Branch** | `feature/react` |


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
|------------|------------------------------|------------------------------|
| **1. Docker Container** | Create Dockerfile and configure container to run REST API | - |
| **2. GitHub Actions** | - | Implement CI workflow to build and push Docker container |
| **Branch** | `feature/docker` | `feature/docker-ci` |


# 🧩 Exercise Part 4: Container Orchestration

This project focuses on **orchestrating the social media application** using Docker Compose.  
The goal is to **separate the application logic from the data**, persist data across releases, and allow environment-specific configuration.

---

## 📘 Exercise Description

### Objective
Develop a Docker Compose setup that:

- Separates containers for the **REST API**, **database**, and any other required infrastructure  
- Persists data during container re-deployment  
- Supports environment-specific configurations using a `.env` file  

This allows the application to be **easily deployed and updated** without losing data.

---

## ⚙️ Steps to Complete

### 1. Container Orchestration
- [ ] Create a **Docker Compose file** that defines services for:
  - Backend REST API  
  - Frontend web application  
  - Database (SQLite persisted via Docker volume)
- [ ] Configure volumes to **persist data** across container restarts.  
- [ ] Ensure services can communicate through the Docker network.  

### 2. Environment Configuration
- [ ] Create a `.env` file to define environment-specific variables:
  - Backend and frontend ports  
  - Database URL  
  - Other configuration options
- [ ] Ensure backend reads database configuration from environment variables.

---

## 👥 Contribution

| Task Area | Angelo Ottendorfer | Martin Ferschl |
|------------|------------------------------|------------------------------|
| **1. Docker Compose Orchestration** | Configure backend, frontend, and volumes for data persistence | Adapted files for postgres addition |
| **2. Environment Configuration** | Setup `.env` file and configure backend to use environment variables | Added postgres as seperate container for data storage |
| **3. Testing** | Test container orchestration and persistence | Tested orchestration with now 3 containers, persistent data |
| **Branch** | `feature-testing` | 'feature-postgres' |
| **Time Required** | 1h | ~1h |

