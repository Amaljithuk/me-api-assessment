import requests

API_URL = "http://127.0.0.1:8000/profile"

# Your Real Data
data = {
    "name": "Amaljith",
    "email": "amaljith@example.com",  # Replace with real email if you want
    "resume_link": "https://linkedin.com/in/yourprofile",
    "github_link": "https://github.com/yourusername",
    "linkedin_link": "https://linkedin.com/in/yourprofile",
    "portfolio_link": "https://yourportfolio.com",
    
    "education": [
        {
            "school": "CUSAT",
            "degree": "Master of Computer Applications (MCA)",
            "year": "2025"
        }
    ],
    
    "skills": [
        {"name": "Python", "category": "Backend"},
        {"name": "FastAPI", "category": "Backend"},
        {"name": "React", "category": "Frontend"},
        {"name": "Docker", "category": "DevOps"},
        {"name": "OpenCV", "category": "AI/ML"},
        {"name": "Supabase", "category": "Database"}
    ],
    
    "projects": [
        {
            "title": "Chodyamedham (Persona Puzzle)",
            "description": "A daily guessing game web app testing logical reasoning.",
            "tech_stack": "React, Supabase, Netlify",
            "repo_link": "https://github.com/yourusername/chodyamedham",
            "demo_link": "https://chodyamedham.netlify.app"
        },
        {
            "title": "Topic Simplifier",
            "description": "Web app that simplifies complex topics using AI agents.",
            "tech_stack": "React, FastAPI, Docker, CrewAI",
            "repo_link": "https://github.com/yourusername/topic-simplifier"
        },
        {
            "title": "Snake AR",
            "description": "AI-powered snake game controlled via computer vision (hand gestures).",
            "tech_stack": "Python, OpenCV, MediaPipe",
            "repo_link": "https://github.com/yourusername/snake-ar"
        }
    ],
    
    "work": [
        {
            "company": "Decathlon (Example)", 
            "role": "Omni Sports Advisor",
            "start_date": "2025-12-01",
            "end_date": "Present",
            "description": "Assisting customers and managing sports inventory."
        }
    ]
}

print("Seeding data...")
response = requests.post(API_URL, json=data)

if response.status_code == 200:
    print("✅ Success! Database seeded with your profile.")
    print(response.json())
else:
    print("❌ Failed:", response.text)