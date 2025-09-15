from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return {"message":"service is healthy"}