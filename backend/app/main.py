from fastapi import FastAPI

app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Cloud Security Analyst",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Sentinel AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }