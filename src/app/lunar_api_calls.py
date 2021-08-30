from app import app
from app import serverapi

@app.route('/api/servers')
def getServers():
    return {"servers": serverapi.servers}

@app.route('/api/info')
def getInfo():
    return serverapi.info()