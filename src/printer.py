from enum import Enum

import octoprint
import klipper

class PrinterType(Enum):
    OCTO = 0
    KLIPPER = 1

class Printer:
    def __init__(self, name: str, type: PrinterType, ipaddr: str, port: int, apikey: str):
        self.type = type
        
        if self.type == PrinterType.OCTO:
            self.pr = octoprint.PrinterOctoPrint(name, ipaddr, port, apikey)
        if self.type == PrinterType.KLIPPER:
            self.pr = klipper.PrinterKlipper(name, ipaddr, port, apikey)
        

    type = PrinterType.OCTO
    
    pr = None