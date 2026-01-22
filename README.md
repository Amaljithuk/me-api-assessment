# Me-API Playground

A full-stack "Playground" application that exposes my professional profile, skills, and projects via a REST API. Built for the **Backend Assessment (Track A)**.

## 🏗 Architecture

* **Database:** PostgreSQL (Hosted on Supabase / Local Docker)
* **Backend:** FastAPI (Python) with SQLAlchemy & Pydantic
* **Frontend:** React (Vite) + Plain CSS
* **Containerization:** Docker support available

## 🚀 Setup Instructions

### Prerequisites
* Python 3.10+
* Node.js & npm
* PostgreSQL

### 1. Backend Setup
```bash
cd backend
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment
# Create a .env file and add your DB URL:
# DATABASE_URL=postgresql://user:pass@localhost:5432/me_api_db

# Initialize DB & Seed Data
python seed.py

# Run Server
uvicorn app.main:app --reload
2. Frontend Setup
Bash

cd frontend
npm install
npm run dev

🗄 Database Schema

The database consists of 5 relational tables:

    Profile: Main user details (Name, Email, Links).

    Education: Linked to Profile (One-to-Many).

    Skills: Categorized skills (One-to-Many).

    Projects: Portfolio items with tech stack & links (One-to-Many).

    WorkExperience: Professional history.

📡 API Usage & Sample Requests

Base URL: http://localhost:8000 (Local)
Get Profile (GET)
Bash

curl -X 'GET' \
  'http://localhost:8000/profile' \
  -H 'accept: application/json'

Search Projects (GET)

Filters by Title, Description, or Skill (Tech Stack).
Bash

curl -X 'GET' \
  'http://localhost:8000/search?q=python' \
  -H 'accept: application/json'

Interactive Documentation (Swagger UI)

Visit /docs (e.g., http://localhost:8000/docs) for the full interactive API documentation.
📄 Resume

[LINK TO YOUR GOOGLE DRIVE/LINKEDIN RESUME PDF]
⚠️ Known Limitations

    Search is currently simple text matching (ilike); no fuzzy search implemented yet.

    Frontend styling is minimal as per requirements.