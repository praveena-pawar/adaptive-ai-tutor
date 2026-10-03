from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Adaptive AI Tutor API is running!"}