from fastapi import FastAPI
from backend.app.api.documents import router as documents_router

app = FastAPI()

app.include_router(documents_router)

title="Adaptive AI Tutor API"

@app.get("/")
def root():
    return {"message": "Adaptive AI Tutor API is running!"}