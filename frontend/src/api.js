const BASE = '/api'

export async function fetchTags() {
  const res = await fetch(`${BASE}/tags`)
  if (!res.ok) throw new Error('Failed to fetch tags')
  const data = await res.json()
  return data.tags
}

export async function generatePost({ topic, length, language, tone, use_emoji }) {
  const res = await fetch(`${BASE}/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic, length, language, tone, use_emoji }),
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Unknown error' }))
    throw new Error(err.detail || 'Failed to generate post')
  }
  const data = await res.json()
  return data.post
}
