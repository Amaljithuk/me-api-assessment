import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [profile, setProfile] = useState(null)
  const [projects, setProjects] = useState([])
  const [search, setSearch] = useState("")

  // 1. Fetch Profile on Load
  useEffect(() => {
    axios.get('https://me-api-assessment.vercel.app/profile')
      .then(res => {
        if (res.data && res.data.length > 0) {
          setProfile(res.data[0]) // Get the first profile
          setProjects(res.data[0].projects) // Initial projects list
        }
      })
      .catch(err => console.error("Error fetching data:", err))
  }, [])

  // 2. Handle Search
  const handleSearch = (e) => {
    const query = e.target.value
    setSearch(query)

    if (query === "") {
      // If search is empty, show all original projects
      if (profile) setProjects(profile.projects)
      return
    }

    // Call the search endpoint
    axios.get(`https://me-api-assessment.vercel.app/search?q=${query}`)
      .then(res => {
        setProjects(res.data.projects)
      })
      .catch(err => console.error("Search error:", err))
  }

  if (!profile) return <div className="container">Loading... (Is Backend Running?)</div>

  return (
    <div className="container">
      {/* Header Section */}
      <header className="card">
        <h1>{profile.name}</h1>
        <p>{profile.education[0]?.degree} @ {profile.education[0]?.school}</p>
        <div style={{ marginTop: '10px' }}>
          <a href={profile.github_link} target="_blank">GitHub</a> | 
          <a href={profile.linkedin_link} target="_blank" style={{ marginLeft: '10px' }}>LinkedIn</a> | 
          <a href={profile.resume_link} target="_blank" style={{ marginLeft: '10px' }}>Resume</a>
        </div>
      </header>

      {/* Skills Section */}
      <section className="card">
        <h2>Skills</h2>
        <div>
          {profile.skills.map(skill => (
            <span key={skill.id} className="tag">{skill.name}</span>
          ))}
        </div>
      </section>

      {/* Projects & Search */}
      <section>
        <h2>Projects</h2>
        <input 
          type="text" 
          className="search-box" 
          placeholder="Search projects by skill or title..." 
          value={search}
          onChange={handleSearch}
        />

        {projects.length === 0 ? <p>No projects found.</p> : projects.map(proj => (
          <div key={proj.id} className="card">
            <h3>{proj.title}</h3>
            <p>{proj.description}</p>
            <p><small><strong>Stack:</strong> {proj.tech_stack}</small></p>
            <div>
              {proj.repo_link && <a href={proj.repo_link} target="_blank">View Code</a>}
              {proj.demo_link && <a href={proj.demo_link} target="_blank" style={{ marginLeft: '15px' }}>Live Demo</a>}
            </div>
          </div>
        ))}
      </section>
    </div>
  )
}

export default App