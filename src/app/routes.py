from flask import render_template
from flask import request
from app import serverapi
from app import lunar_api_calls
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", servers=serverapi.servers)

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/queue')
def queue():
    return render_template("queue.html", printqueue=[{"name": "Test Print", "estimate_str": "10h6m"}])