from app.database import engine, Base
from app.models import Profile, Education, Skill, Project, WorkExperience

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")