from pydantic import BaseModel
from typing import List, Optional

# --- Shared Base Models ---
class EducationBase(BaseModel):
    school: str
    degree: str
    year: str

class SkillBase(BaseModel):
    name: str
    category: str

class ProjectBase(BaseModel):
    title: str
    description: str
    repo_link: Optional[str] = None
    demo_link: Optional[str] = None
    tech_stack: Optional[str] = None # We will store as comma-separated string

class WorkExperienceBase(BaseModel):
    company: str
    role: str
    start_date: str
    end_date: str
    description: str

# --- Profile Models ---
class ProfileBase(BaseModel):
    name: str
    email: str
    resume_link: Optional[str] = None
    github_link: Optional[str] = None
    linkedin_link: Optional[str] = None
    portfolio_link: Optional[str] = None

class ProfileCreate(ProfileBase):
    education: List[EducationBase] = []
    skills: List[SkillBase] = []
    projects: List[ProjectBase] = []
    work: List[WorkExperienceBase] = []

class Profile(ProfileBase):
    id: int
    education: List[EducationBase] = []
    skills: List[SkillBase] = []
    projects: List[ProjectBase] = []
    work: List[WorkExperienceBase] = []

    class Config:
        from_attributes = True # updated for Pydantic v2 (was orm_mode)