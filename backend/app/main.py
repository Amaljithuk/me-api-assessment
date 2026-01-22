from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import models, schemas, database
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

# Create the App
app = FastAPI(title="Me-API Playground")

# Enable CORS (Allows your React frontend to talk to this backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace * with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- 1. Health Check (Requirement 1.c) ---
@app.get("/health")
def health_check():
    return {"status": "ok", "code": 200}

# --- 2. Create/Seed Profile (Requirement 1.a) ---
@app.post("/profile", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    # Create main profile
    db_profile = models.Profile(
        name=profile.name,
        email=profile.email,
        resume_link=profile.resume_link,
        github_link=profile.github_link,
        linkedin_link=profile.linkedin_link,
        portfolio_link=profile.portfolio_link
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    # Add related items (Education, Skills, etc.)
    for edu in profile.education:
        db.add(models.Education(**edu.dict(), profile_id=db_profile.id))
    for sk in profile.skills:
        db.add(models.Skill(**sk.dict(), profile_id=db_profile.id))
    for proj in profile.projects:
        db.add(models.Project(**proj.dict(), profile_id=db_profile.id))
    for wk in profile.work:
        db.add(models.WorkExperience(**wk.dict(), profile_id=db_profile.id))
    
    db.commit()
    db.refresh(db_profile)
    return db_profile

# --- 3. Get Profile (Requirement 1.a) ---
@app.get("/profile", response_model=List[schemas.Profile])
def get_profile(db: Session = Depends(get_db)):
    # Returns a list, but usually you only have 1 profile (you)
    return db.query(models.Profile).all()

# --- 4. Get Projects with Filtering (Requirement 1.b) ---
@app.get("/projects")
def get_projects(skill: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Project)
    
    if skill:
        # Simple filter: checks if the skill string is inside the tech_stack string
        query = query.filter(models.Project.tech_stack.ilike(f"%{skill}%"))
        
    return query.all()

# --- 5. Search Endpoint (Requirement 1.b) ---

# --- 5. Search Endpoint (Updated) ---
@app.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    # Now searches Title, Description, AND Tech Stack
    projects = db.query(models.Project).filter(
        (models.Project.title.ilike(f"%{q}%")) | 
        (models.Project.description.ilike(f"%{q}%")) |
        (models.Project.tech_stack.ilike(f"%{q}%"))  # <--- Added this line
    ).all()
    
    skills = db.query(models.Skill).filter(models.Skill.name.ilike(f"%{q}%")).all()
    
    return {"projects": projects, "skills": skills}