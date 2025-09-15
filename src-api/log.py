import logging
from logging.handlers import TimedRotatingFileHandler
import os

if not os.path.exists("/data/logs"):
    os.makedirs("/data/logs")

logger = logging.getLogger("textboard")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    filename="/data/logs/api.log",
    when="midnight",
    interval=1,
    backupCount=7
)
handler.suffix = "%Y-%m-%d"
format = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
handler.setFormatter(format)
logger.addHandler(handler)