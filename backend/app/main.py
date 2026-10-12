from fastapi import FastAPI

from backend.app.api.documents import router as documents_router
from backend.app.api.search import router as search_router


app = FastAPI(
    title="Adaptive AI Tutor API",
    description="An AI tutor that learns from course materials and adapts to students.",
    version="0.1.0",
)

app.include_router(documents_router)
app.include_router(search_router)


@app.get("/")
def root():
    return {"message": "Adaptive AI Tutor API is running!"}