from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is active"}


@app.get("/health")
def health():
    return {"message":"service is healthy"}