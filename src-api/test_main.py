from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sendMessage():
    body={"name":"pytest", "content":"successful!"}
    response = client.post("/message/send", json=body)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["status"] == "success"

def test_getMessages():
    response = client.get("/messages")
    assert response.status_code == 200