import requests
import json

servers = ["http://127.0.0.1:7125"] ## This will need to be set from the gui - need initial setup window and settings page.
queue = {}
for server in servers:
    queue[server] = []

def info():
    type = "GET" # "GET"/"POST"
    path = "/printer/objects/query?toolhead=position&display_status=progress&print_stats=filename"
    return make_request(type, path)

def print_file(filepath, server):
    type = "POST"
    path = "/server/files/upload"
    requests.post(server + path, files={"file": open(filepath, 'rb')}, data={"path": "lunar", "print": "true"})
    print("Sending file for printing: " + filepath)
    print("to server: " + server + ".")
    return

def make_request(type, path):
    # returns {'server': {key:value}}
    retval = {}

    for server in servers:
        if type == "GET":
            response = requests.get(server + path)
        elif type == "POST":
            response = requests.post(server + path)
        retval[server] = json.loads(response.text)
    
    return retval