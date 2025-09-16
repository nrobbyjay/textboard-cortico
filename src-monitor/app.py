from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/data").percent

    return {
        "cpu_usage": cpu,
        "memory_usage": mem,
        "disk_usage": disk
    }

@app.route("/health", methods=["GET"])
def health():
    return {"message":"service is healthy"}