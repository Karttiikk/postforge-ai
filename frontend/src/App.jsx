import { useState } from 'react'
import './index.css'
import Header from './components/Header'
import PostGenerator from './components/PostGenerator'
import PostCard from './components/PostCard'
import { generatePost } from './api'

export default function App() {
  const [result, setResult]   = useState(null)
  const [meta, setMeta]       = useState(null)
  const [regenLoading, setRegenLoading] = useState(false)

  function handleResult(post, postMeta) {
    setResult(post)
    setMeta(postMeta)
  }

  async function handleRegenerate() {
    if (!meta) return
    setRegenLoading(true)
    try {
      const post = await generatePost({
        topic: meta.topic,
        length: meta.length,
        language: meta.language,
        tone: meta.tone,
        use_emoji: meta.emoji,
      })
      setResult(post)
    } catch (e) {
      console.error(e)
    } finally {
      setRegenLoading(false)
    }
  }

  return (
    <div className="app-wrapper">
      <div className="app-container">
        <Header />

        {/* Hero */}
        <div className="hero">
          <div className="hero-eyebrow">AI-Powered Content</div>
          <h1>
            Write LinkedIn posts<br />
            <span className="gradient">in your voice.</span>
          </h1>
          <p>
            Feed your past posts. Pick a topic. Get content that sounds
            exactly like <em>you</em> — powered by few-shot AI.
          </p>
        </div>

        {/* Generator form */}
        <PostGenerator onResult={handleResult} />

        {/* Generated output */}
        {result && (
          <PostCard
            post={result}
            meta={meta}
            onRegenerate={handleRegenerate}
            loading={regenLoading}
          />
        )}

        <footer className="footer">
          PostForge AI — Built with LangChain × Groq × React
        </footer>
      </div>
    </div>
  )
}
