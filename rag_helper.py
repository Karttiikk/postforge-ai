import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class RAGHelper:
    def __init__(self, data_path="data/processed_posts.json", index_path="faiss_index.bin"):
        self.data_path = data_path
        self.index_path = index_path
        self.posts = []
        self.index = None
        # Load the sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._load_posts()
        self._initialize_index()

    def _load_posts(self):
        """Loads posts from the JSON file."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        
        with open(self.data_path, "r", encoding="utf-8") as f:
            self.posts = json.load(f)

    def _initialize_index(self):
        """Loads the FAISS index if it exists, otherwise builds and saves it."""
        if not self.posts:
            return

        if os.path.exists(self.index_path):
            # Load existing index
            self.index = faiss.read_index(self.index_path)
        else:
            # Build new index
            texts = []
            for post in self.posts:
                # Combine metadata and text for a richer embedding
                tags_str = ", ".join(post.get("tags", []))
                lang = post.get("language", "")
                text = post.get("text", "")
                combined_text = f"Tags: {tags_str}. Language: {lang}. Content: {text}"
                texts.append(combined_text)

            with open("debug_rag.txt", "w", encoding="utf-8") as df:
                df.write(f"Building index for {len(texts)} posts...\n")
                for i, t in enumerate(texts):
                    df.write(f"Post {i}: {type(t)} - {repr(t)}\n")
            
            embeddings = self.model.encode(texts, show_progress_bar=True)
            embeddings = np.array(embeddings).astype("float32")
            
            # Create FAISS index (L2 distance)
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
            self.index.add(embeddings)
            
            # Save index to disk
            faiss.write_index(self.index, self.index_path)

    def retrieve_similar_posts(self, topic: str, tone: str, length: str, k: int = 3):
        """Retrieves top k semantically similar posts based on the query."""
        if self.index is None or not self.posts:
            return []

        query = f"Topic: {topic}, Tone: {tone}, Length: {length}"
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        # Search the index
        distances, indices = self.index.search(query_embedding, k)
        
        retrieved_posts = []
        for idx in indices[0]:
            if 0 <= idx < len(self.posts):
                retrieved_posts.append(self.posts[idx])
                
        return retrieved_posts
