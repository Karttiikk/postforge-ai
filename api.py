from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from post_generator import generate_post, get_prompt
from few_shot import FewShotPosts

app = FastAPI(title="PostForge AI API", version="1.0.0")

# Allow React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Shared FewShotPosts instance
fs = FewShotPosts()


class GenerateRequest(BaseModel):
    topic: str
    length: str       # "Short" | "Medium" | "Long"
    language: str     # "English" | "Hinglish"
    tone: str = "Professional"
    use_emoji: str = "On"  # "On" | "Off" | "Minimal"


@app.get("/api/tags")
def get_tags():
    tags = fs.get_tags()
    return {"tags": sorted(tags)}


@app.post("/api/generate")
def generate(req: GenerateRequest):
    valid_lengths = ["Short", "Medium", "Long"]
    valid_languages = ["English", "Hinglish"]

    if req.length not in valid_lengths:
        raise HTTPException(status_code=400, detail=f"length must be one of {valid_lengths}")
    if req.language not in valid_languages:
        raise HTTPException(status_code=400, detail=f"language must be one of {valid_languages}")

    try:
        post = generate_post(
            length=req.length,
            language=req.language,
            tag=req.topic,
            tone=req.tone,
            use_emoji=req.use_emoji,
        )
        return {"post": post}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
def health():
    return {"status": "ok"}
