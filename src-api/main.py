from fastapi import FastAPI

from db.db import init_db

app = FastAPI()
init_db()


@app.get("/")
def root():
    return {"message": "API is active"}


@app.get("/health")
def health():
    return {"message":"service is healthy"}