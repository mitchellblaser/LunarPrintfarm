from printer import Printer, PrinterType
from states import PrinterState
import config

from flask import Flask, render_template

app = Flask(__name__)

printers = []

for entry in config.printers:
    printers.append(Printer(entry["name"], entry["type"], entry["ipaddr"], entry["port"], entry["apikey"]).pr)

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