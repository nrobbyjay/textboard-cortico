from fastapi import FastAPI
from fastapi.responses import JSONResponse

from db.db import init_db
from db.models import addMessage, fetchMessages,Message

app = FastAPI()
init_db()

@app.get("/")
def root():
    return {"message": "API is active"}

@app.get("/health")
def health():
    return {"message":"service is healthy"}

@app.get("/messages")
def getMessages():
    try:
        return JSONResponse(status_code=200, content={"data": fetchMessages()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":"error", "message":str(e)})

@app.post("/message/send")
def sendMessage(msg: Message):
    try:
        addMessage(msg)
        return JSONResponse(status_code=200, content={"status":"success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":"error", "message":str(e)})