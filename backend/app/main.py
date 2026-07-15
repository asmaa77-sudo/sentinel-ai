from fastapi import FastAPI

app = FastAPI(
    title="Sentinel AI",
    description="AI-powered cybersecurity assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Sentinel AI 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "running",
        "service": "Sentinel AI Backend"
    }