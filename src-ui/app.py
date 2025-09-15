from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get("http://nginx/api/messages")
        messages = response.json()["data"]
    except Exception as e:
        messages = [{"name": "system", "content": f"Error: {e}"}]
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def sendMessage():
    name = request.form.get("name")
    content = request.form.get("content")
    if name and content:
        try:
            requests.post(f"http://nginx/api/message/send", json={"name": name, "content": content})
        except Exception as e:
            print("Error sending message:", e)
    return redirect("/")

@app.route("/health", methods=["GET"])
def health():
    return {"message":"service is healthy"}