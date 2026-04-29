from rag_helper import RAGHelper
import os

if os.path.exists("faiss_index.bin"):
    os.remove("faiss_index.bin")

try:
    print("Initializing RAGHelper...")
    rag = RAGHelper()
    print("RAGHelper initialized successfully!")
except Exception as e:
    import traceback
    traceback.print_exc()
