import { useState } from 'react'

const LINKEDIN_MAX = 3000

export default function PostCard({ post, meta, onRegenerate, loading }) {
  const [copied, setCopied] = useState(false)

  const charCount = post.length
  const charClass = charCount > LINKEDIN_MAX ? 'over' : charCount > LINKEDIN_MAX * 0.85 ? 'warn' : 'ok'

  function handleCopy() {
    navigator.clipboard.writeText(post).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    })
  }

  return (
    <div className="card output-card">
      {/* Header row */}
      <div className="output-header">
        <div className="output-label">
          <span className="dot" />
          Generated Post
        </div>
        <div className="output-actions">
          <button
            className={`action-btn${copied ? ' copied' : ''}`}
            onClick={handleCopy}
            id="copy-post-btn"
          >
            {copied ? '✓ Copied!' : '⎘ Copy'}
          </button>
          <button
            className="action-btn"
            onClick={onRegenerate}
            disabled={loading}
            id="regenerate-btn"
          >
            {loading ? <span className="spinner" /> : '↻ Regenerate'}
          </button>
        </div>
      </div>

      {/* Post body */}
      <div className="post-text">{post}</div>

      {/* Meta chips */}
      <div className="post-meta">
        <span className="meta-chip">📌 {meta.topic}</span>
        <span className="meta-chip">📏 {meta.length}</span>
        <span className="meta-chip">🌐 {meta.language}</span>
        <span className="meta-chip">🎭 {meta.tone}</span>
        <span className={`char-count ${charClass}`}>
          {charCount.toLocaleString()} / {LINKEDIN_MAX.toLocaleString()} chars
        </span>
      </div>
    </div>
  )
}
