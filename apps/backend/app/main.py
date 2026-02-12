from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "backend",
        "status": "ok",
        "message": "Backend API is running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
