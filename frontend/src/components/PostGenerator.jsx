import { useState, useEffect } from 'react'
import Selector from './Selector'
import { fetchTags, generatePost } from '../api'

const LENGTHS   = ['Short', 'Medium', 'Long']
const LANGUAGES = ['English', 'Hinglish']
const TONES     = ['Professional', 'Casual', 'Inspirational', 'Humorous', 'Story-driven']
const EMOJIS    = ['On', 'Minimal', 'Off']

export default function PostGenerator({ onResult }) {
  const [tags, setTags]         = useState([])
  const [topic, setTopic]       = useState('')
  const [length, setLength]     = useState('Medium')
  const [language, setLanguage] = useState('English')
  const [tone, setTone]         = useState('Professional')
  const [emoji, setEmoji]       = useState('On')
  const [loading, setLoading]   = useState(false)
  const [error, setError]       = useState('')
  const [tagsLoading, setTagsLoading] = useState(true)

  useEffect(() => {
    fetchTags()
      .then(t => { setTags(t); setTopic(t[0] || '') })
      .catch(() => setError('⚠️ Could not connect to backend. Is the API server running?'))
      .finally(() => setTagsLoading(false))
  }, [])

  async function handleGenerate() {
    if (!topic) return
    setLoading(true)
    setError('')
    try {
      const post = await generatePost({ topic, length, language, tone, use_emoji: emoji })
      onResult(post, { topic, length, language, tone, emoji })
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card generator-card">
      <p className="section-label">Configure your post</p>

      {error && (
        <div className="error-box" id="error-message">
          ⚠️ {error}
        </div>
      )}

      {/* Row 1 — Topic + Length */}
      <div className="form-grid">
        <Selector
          label="Topic"
          id="select-topic"
          value={topic}
          onChange={setTopic}
          options={tagsLoading ? ['Loading…'] : tags}
        />
        <Selector
          label="Length"
          id="select-length"
          value={length}
          onChange={setLength}
          options={LENGTHS}
        />
      </div>

      {/* Row 2 — Language + Tone */}
      <div className="form-grid" style={{ marginBottom: '24px' }}>
        <Selector
          label="Language"
          id="select-language"
          value={language}
          onChange={setLanguage}
          options={LANGUAGES}
        />
        <Selector
          label="Tone"
          id="select-tone"
          value={tone}
          onChange={setTone}
          options={TONES}
        />
      </div>

      {/* Emoji toggle */}
      <div className="form-field" style={{ marginBottom: '24px' }}>
        <label>Emoji Usage</label>
        <div className="toggle-group">
          {EMOJIS.map(opt => (
            <button
              key={opt}
              id={`emoji-${opt.toLowerCase()}`}
              className={`toggle-btn${emoji === opt ? ' active' : ''}`}
              onClick={() => setEmoji(opt)}
            >
              {opt === 'On' ? '😊 On' : opt === 'Off' ? '🚫 Off' : '✨ Minimal'}
            </button>
          ))}
        </div>
      </div>

      <div className="divider" />

      <button
        id="generate-btn"
        className="generate-btn"
        onClick={handleGenerate}
        disabled={loading || tagsLoading || !topic}
      >
        {loading
          ? <><span className="spinner" /> Crafting your post…</>
          : <><span className="btn-icon">⚡</span> Generate Post</>
        }
      </button>
    </div>
  )
}
