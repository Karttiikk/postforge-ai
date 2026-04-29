# ✍️ PostForge AI

**PostForge AI** is a professional-grade LinkedIn content generation platform. It empowers influencers and thought leaders to create high-impact posts that sound exactly like them, powered by **Few-Shot Learning** and the latest **Llama 3.3** LLM.

![PostForge UI Preview](C:\Users\91902\.gemini\antigravity\brain\ee0c51d0-3ebe-462f-92fe-f9857bdb820f\postforge_ui_full_page_1777443128008.png)

## 🚀 Key Features

- **Personalized Voice**: Uses your past posts to mimic your unique writing style, hook patterns, and formatting.
- **Tone Control**: Choose from various tones like Professional, Casual, Inspirational, or Story-driven.
- **Emoji Management**: Toggle between full emojis, minimal usage, or clean text-only posts.
- **Bilingual Support**: Seamlessly generate content in English or **Hinglish**.
- **Content Optimizer**: Real-time LinkedIn character counting and "scroll-friendly" formatting.
- **Premium UI**: A sleek, high-performance dark-mode interface built with React.

## 🛠️ Tech Stack

- **Frontend**: React (Vite), Vanilla CSS (Premium Glassmorphism Design).
- **Backend**: FastAPI (Python), Uvicorn.
- **AI/LLM**: LangChain, Groq API (Llama 3.3-70b-versatile).
- **Data**: Pandas, JSON-based storage.

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/PostForge-AI.git
cd PostForge-AI
```

### 2. Setup Backend
```bash
# Install Python dependencies
pip install -r requirements.txt

# Create a .env file and add your Groq API Key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

### 3. Setup Frontend
```bash
cd frontend
npm install
cd ..
```

## 🏃‍♂️ Running the App

You can launch both the backend and frontend simultaneously using the provided orchestration script:

```bash
python run_dev.py
```

- **Frontend**: [http://localhost:5173](http://localhost:5173)
- **Backend API**: [http://localhost:8000](http://localhost:8000)

## 🏗️ Project Structure

- `api.py`: FastAPI backend server.
- `post_generator.py`: Core AI prompt engineering logic.
- `few_shot.py`: Logic for retrieving relevant examples from history.
- `llm_helper.py`: LLM initialization and Groq integration.
- `data/`: Contains raw and processed LinkedIn posts.
- `frontend/`: The React source code.

## 📄 License

This project is licensed under the MIT License.

---
Built with ❤️ by **PostForge AI Team**
