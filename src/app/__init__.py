from printer import Printer, PrinterType
from states import PrinterState
import config
import printqueue

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

printers = []

entries = 0
for entry in config.printers:
    printers.append(Printer(entries, entry["name"], entry["type"], entry["ipaddr"], entry["port"], entry["apikey"], entry["tags"]).pr)
    entries = entries + 1

for printer in printers:
    print(printer.name + " - [" + printer.GetVersion() + "]")
    print("==========================")
    print(printer.GetStatus())
    
    # printer.UploadFile("./test.gcode", select = True, print = False)
    
    print(printer.GetPrintCompletion())
    
    print("")

def GetActivePrinters():
    active = 0
    for printer in printers:
        if printer.GetStatus() == PrinterState.PRINTING:
            active = active + 1
    return active

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", printers=printers, usage=GetActivePrinters(), max=len(printers))

@app.route('/cancel/<printer>')
def cancelprint(printer):
    printers[int(printer)].CancelPrint()
    return redirect("/")

@app.route('/job')
def job():
    return render_template("job.html", printers=printers, tags=printqueue.CollectAllTags(printers))

@app.route('/upload/<printer>')
def uploadprint(printer):
    return render_template("single.html", printer=printers[int(printer)])

@app.route('/upload/<printer>', methods=['POST'])
def print(printer):
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save("./gcode/" + uploaded_file.filename)
        printers[int(printer)].UploadFile("./gcode/" + uploaded_file.filename, select = True, print = True)
    return redirect("/")