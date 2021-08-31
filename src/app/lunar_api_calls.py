from app import app
from app import serverapi
from app import queue

@app.route('/api/servers')
def getServers():
    return {"servers": serverapi.servers}

@app.route('/api/info')
def getInfo():
    return serverapi.info()

@app.route('/api/upload')
def uploadFile():
    queue.add_file_to_queue("/Users/mblaser/Desktop/testfile.gcode")
    print(serverapi.servers)
    print(serverapi.queue)
    return "OK"