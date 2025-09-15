import time, sqlite3
from pydantic import BaseModel
from datetime import datetime

from .db import get_connection

class Message(BaseModel):
    name: str
    content: str

def addMessage(msg: Message, retries=5, delay=0.5):
    for _ in range(retries):
        try:
            with get_connection() as conn:
                conn.execute("INSERT INTO messages (name, content, timestamp) VALUES (?,?,?)", (msg.name, msg.content, datetime.now().strftime("%Y-%m-%d %H:%M:%S")) )
            return
        except sqlite3.OperationalError:
            time.sleep(delay)
    raise Exception("Unable to write to database; Database is locked!")

def fetchMessages():
    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM messages ORDER BY id DESC")
            rows = [dict(row) for row in cursor.fetchall()]
            return rows
    except Exception as e:
        return e