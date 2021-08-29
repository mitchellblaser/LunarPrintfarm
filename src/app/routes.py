from flask import render_template
from app import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    print(request.info())
    return render_template("index.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")