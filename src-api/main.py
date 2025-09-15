from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

from db.db import init_db
from db.models import addMessage, fetchMessages,Message
from log import logger

app = FastAPI()
init_db()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error on {request.url.path}: {exc.errors()} | Body: {exc.body}")
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "detail": exc.errors(),
            "body": exc.body
        }),
    )

@app.get("/health")
def health():
    return {"message":"service is healthy"}

@app.get("/messages")
def getMessages():
    try:
        logger.info("Message has been fetched")
        return JSONResponse(status_code=200, content={"data": fetchMessages()})
    except Exception as e:
        logger.error("Unable to fetch data: %s", e)
        return JSONResponse(status_code=500, content={"status":"error", "message":str(e)})

@app.post("/message/send")
def sendMessage(msg: Message):
    try:
        addMessage(msg)
        logger.info("Message content has been sent by %s successfully", msg.name)
        return JSONResponse(status_code=200, content={"status":"success"})
    except Exception as e:
        logger.error("Unable to send message content: %s", e)
        return JSONResponse(status_code=500, content={"status":"error", "message":str(e)})