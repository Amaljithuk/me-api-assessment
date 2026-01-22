from sqlalchemy import Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.orm import relationship
from .database import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    resume_link = Column(String)
    github_link = Column(String)
    linkedin_link = Column(String)
    portfolio_link = Column(String)

    # Relationships
    education = relationship("Education", back_populates="profile")
    skills = relationship("Skill", back_populates="profile")
    projects = relationship("Project", back_populates="profile")
    work = relationship("WorkExperience", back_populates="profile")

class Education(Base):
    __tablename__ = "education"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    school = Column(String)
    degree = Column(String)
    year = Column(String)
    
    profile = relationship("Profile", back_populates="education")

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    name = Column(String)
    category = Column(String) # e.g. "Frontend", "Backend"

    profile = relationship("Profile", back_populates="skills")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    title = Column(String)
    description = Column(Text)
    repo_link = Column(String)
    demo_link = Column(String)
    tech_stack = Column(String) # Simple string for now, or use JSON/ARRAY if using Postgres specific types

    profile = relationship("Profile", back_populates="projects")

class WorkExperience(Base):
    __tablename__ = "work_experience"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    company = Column(String)
    role = Column(String)
    start_date = Column(String) # Using string for simplicity, can be Date
    end_date = Column(String)
    description = Column(Text)

    profile = relationship("Profile", back_populates="work")