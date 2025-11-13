# 🧩 SWEG Social Media App – Exercise Part 1: Automation

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
| **1. Python Application** | Implement `database.py` (SQLite setup, add/retrieve posts) | Support by testing functions manually |
| **3. Testing** | Provide testable database functions | Create `tests/test_app.py` using `pytest` |
| **4. GitHub Actions** | Review pipeline configuration | Create `.github/workflows/ci.yml` and ensure CI runs only on pull requests |
| **5. Final Steps** | Commit app code | Commit tests + CI config and verify all tests pass |
| **Branch** | `feature/backend` | `feature/tests-ci` |
| **Time Required** | 0.5h - 1h | 0.5h - 1h |



