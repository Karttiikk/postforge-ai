from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from post_generator import generate_post
from rag_helper import RAGHelper

app = FastAPI(title="PostForge AI API", version="1.0.0")

# Allow React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG helper (loads FAISS index and model on startup)
rag = RAGHelper()


class GenerateRequest(BaseModel):
    topic: str
    length: str       # "Short" | "Medium" | "Long"
    language: str     # "English" | "Hinglish"
    tone: str = "Professional"
    use_emoji: str = "On"  # "On" | "Off" | "Minimal"


@app.get("/api/tags")
def get_tags():
    # Extract unique tags from the loaded posts
    unique_tags = set()
    for post in rag.posts:
        unique_tags.update(post.get("tags", []))
    return {"tags": sorted(list(unique_tags))}


@app.post("/api/generate")
def generate(req: GenerateRequest):
    valid_lengths = ["Short", "Medium", "Long"]
    valid_languages = ["English", "Hinglish"]

    if req.length not in valid_lengths:
        raise HTTPException(status_code=400, detail=f"length must be one of {valid_lengths}")
    if req.language not in valid_languages:
        raise HTTPException(status_code=400, detail=f"language must be one of {valid_languages}")

    try:
        # Retrieve similar posts using RAG
        retrieved_posts = rag.retrieve_similar_posts(
            topic=req.topic,
            tone=req.tone,
            length=req.length,
            k=3
        )

        # Generate the new post
        post = generate_post(
            length=req.length,
            language=req.language,
            tag=req.topic,
            retrieved_posts=retrieved_posts,
            tone=req.tone,
            use_emoji=req.use_emoji,
        )
        return {"post": post}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
def health():
    return {"status": "ok"}
