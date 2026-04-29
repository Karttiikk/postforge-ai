import subprocess
import time
import sys
import os

def run_dev():
    print("Starting PostForge AI Development Servers...")
    
    # 1. Start FastAPI Backend
    print("Starting FastAPI Backend on port 8000...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api:app", "--port", "8000", "--reload"],
        cwd=os.getcwd()
    )
    
    # Wait a bit for backend to initialize
    time.sleep(2)
    
    # 2. Start React Frontend
    print("Starting React Frontend on port 5173...")
    frontend_process = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=os.path.join(os.getcwd(), "frontend"),
        shell=True
    )
    
    print("\nBoth servers are running!")
    print("Backend: http://localhost:8000")
    print("Frontend: http://localhost:5173")
    print("\nPress Ctrl+C to stop both servers.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Servers stopped.")

if __name__ == "__main__":
    run_dev()
