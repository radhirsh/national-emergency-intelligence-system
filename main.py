from fastapi import FastAPI

app = FastAPI(
    title="National Emergency Intelligence System",
    version="0.1.0",
    description="AI-driven crisis intelligence platform"
)


@app.get("/")
def root():
    return {
        "message": "National Emergency Intelligence System Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }