import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [dramas, setDramas] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchDramas = async () => {
      try {
        const response = await fetch('/api/dramas/')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        setDramas(data)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchDramas()
  }, [])

  if (loading) {
    return <div className="container">Loading...</div>
  }

  if (error) {
    return <div className="container">Error: {error}</div>
  }

  return (
    <div className="container">
      <header>
        <h1>K-Drama World</h1>
      </header>
      <main>
        <h2>All K-Dramas</h2>
        <div className="drama-grid">
          {dramas.map((drama) => (
            <div key={drama.id} className="drama-card">
              <h3>{drama.title}</h3>
              <p>Genre: {drama.genre}</p>
              <p>Episodes: {drama.episodes}</p>
              <p>Year: {drama.release_year}</p>
              <p>Rating: {drama.rating}</p>
              <p>{drama.description}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}

export default App
