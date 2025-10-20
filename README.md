# 🧠 Learning FastAPI — Todo App Project

## 🚀 Overview
This is a simple **FastAPI Todo Application** built as part of my learning journey to understand:
- REST API design (GET, POST, PUT, DELETE)
- Data validation with **Pydantic models**
- Path & Query parameters
- CRUD operations on an in-memory list (acting as a database)
- Handling validation errors (422, 404)
- API documentation via **Swagger UI**

---

## 🧩 Project Structure

Learning-FastApi/
│
├── main.py # Main FastAPI app
├── venv/ # Virtual environment (ignored in .gitignore)
├── .gitignore # Ignore virtualenv and cache files
└── README.md # This file


## ⚙️ Setup Instructions

### 1️⃣ Create & Activate Virtual Environment
```
python -m venv venv
.\venv\Scripts\activate       # (Windows)
# or
source venv/bin/activate      # (Mac/Linux)
```

### 2️⃣ Install Dependencies
```
pip install fastapi uvicorn
````


### 3️⃣ Run the App
uvicorn main:app --reload

Visit:
🌐 Docs (Swagger UI): http://127.0.0.1:8000/docs
📄 Redoc UI: http://127.0.0.1:8000/redoc



🧠 Learning Highlights
🟢 FastAPI Concepts

@app.get, @app.post, @app.put, @app.delete for route creation

Path parameters → /todos/{todo_id}

Query parameters → /todos?first_n=3

Automatic validation via Pydantic

🟢 Pydantic Models
class TodoBase(BaseModel):
    name: str
    description: str
    priority: Priority


Field(..., min_length=3) → required field

Field(None) → optional field

Custom enum Priority(IntEnum) for priority levels

🟢 Error Handling

Used HTTPException for clean responses:

raise HTTPException(status_code=404, detail="Todo not found")

🟢 Common Fixes You Learned
Issue	Cause	Solution
422 Unprocessable Entity	Missing body fields	Use correct Pydantic model (TodoBaseCreate)
500 Internal Server Error	Function name shadowing variable	Rename one of them
404 Not Found	Wrong path param	Check ID exists in list
🧩 Example Todo Object
{
  "id": 1,
  "name": "Buy groceries",
  "description": "Get fruits and vegetables",
  "priority": 2
}

🔄 Git Workflow Summary
Step	Command
Initialize repo	git init
Stage files	git add .
Commit	git commit -m "Initial FastAPI project commit"
Add remote	git remote add origin <repo-url>
Push	git push -u origin main

💬 Future Plans / Next Learning Goals

⏩ Integrate a real database (SQLite / PostgreSQL with SQLAlchemy)

🧰 Add authentication (JWT)

🧾 Write unit tests using pytest

🌐 Deploy on Render / Railway / AWS EC2

✨ Personal Notes

This project helped me deeply understand FastAPI’s async design, Pydantic validation, and RESTful patterns.
I also practiced debugging errors like 422 Unprocessable Entity and ResponseValidationError.
Keeping this repo will help me quickly refresh all FastAPI fundamentals before any interview or future project.
