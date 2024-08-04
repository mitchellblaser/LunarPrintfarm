from printer import Printer, PrinterType
from states import PrinterState
import config
import printqueue

from flask import Flask, render_template, redirect

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