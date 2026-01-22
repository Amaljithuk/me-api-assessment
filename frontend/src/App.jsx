import { useState, useEffect } from 'react'
import axios from 'axios'
import { FaGithub, FaLinkedin, FaFileAlt, FaExternalLinkAlt, FaCode } from 'react-icons/fa' // Import Icons
import './App.css'

function App() {
  const [profile, setProfile] = useState(null)
  const [projects, setProjects] = useState([])
  const [search, setSearch] = useState("")

  // Use YOUR Vercel/Render URL here (not localhost)
  const API_URL = "https://me-api-assessment.vercel.app" 

  useEffect(() => {
    axios.get(`${API_URL}/profile`)
      .then(res => {
        if (res.data && res.data.length > 0) {
          setProfile(res.data[0])
          setProjects(res.data[0].projects)
        }
      })
      .catch(err => console.error(err))
  }, [])

  const handleSearch = (e) => {
    const query = e.target.value
    setSearch(query)
    if (query === "") {
      if (profile) setProjects(profile.projects)
      return
    }
    axios.get(`${API_URL}/search?q=${query}`)
      .then(res => setProjects(res.data.projects))
      .catch(err => console.error(err))
  }

  if (!profile) return <div className="container" style={{textAlign:'center', marginTop: '50px'}}>Loading Profile...</div>

  return (
    <div className="container">
      
      {/* 1. Hero Section */}
      <header className="hero">
        <h1>{profile.name}</h1>
        <p style={{fontSize: '1.2rem', color: '#94a3b8'}}>
          {profile.education[0]?.degree} • {profile.education[0]?.school}
        </p>
        
        <div className="social-links">
          {profile.github_link && (
            <a href={profile.github_link} target="_blank">
              <FaGithub /> GitHub
            </a>
          )}
          {profile.linkedin_link && (
            <a href={profile.linkedin_link} target="_blank">
              <FaLinkedin /> LinkedIn
            </a>
          )}
          {profile.resume_link && (
            <a href={profile.resume_link} target="_blank">
              <FaFileAlt /> Resume
            </a>
          )}
        </div>
      </header>

      {/* 2. Skills Section */}
      <section>
        <h2>Technical Skills</h2>
        <div className="skills-grid">
          {profile.skills.map(skill => (
            <span key={skill.id} className="tag">{skill.name}</span>
          ))}
        </div>
      </section>

      {/* 3. Projects Section */}
      <section>
        <h2>Projects Showcase</h2>
        <div className="search-wrapper">
          <input 
            type="text" 
            className="search-box" 
            placeholder="🔍  Search by skill (e.g., 'React') or project name..." 
            value={search}
            onChange={handleSearch}
          />
        </div>

        <div className="projects-grid">
          {projects.length === 0 ? <p>No projects match your search.</p> : projects.map(proj => (
            <div key={proj.id} className="card">
              <div>
                <h3>{proj.title}</h3>
                <p>{proj.description}</p>
                <div style={{marginTop: '10px'}}>
                   <small style={{color: '#6366f1', fontWeight: 'bold'}}>STACK</small> <br/>
                   <span style={{color: '#cbd5e1', fontSize: '0.9rem'}}>{proj.tech_stack}</span>
                </div>
              </div>
              
              <div className="card-footer">
                {proj.repo_link && (
                  <a href={proj.repo_link} target="_blank">
                    <FaCode /> Code
                  </a>
                )}
                {proj.demo_link && (
                  <a href={proj.demo_link} target="_blank">
                    <FaExternalLinkAlt /> Live Demo
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      <footer style={{textAlign: 'center', marginTop: '60px', color: '#475569', fontSize: '0.9rem'}}>
        <p>Built with FastAPI & React • Hosted on Vercel</p>
      </footer>
    </div>
  )
}

export default App