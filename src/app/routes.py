from flask import render_template
from flask import request
from app import serverapi
from app import app

@app.route('/')
@app.route('/index')
def index():
    print(serverapi.info())
    return render_template("index.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/queue')
def queue():
    return render_template("queue.html")