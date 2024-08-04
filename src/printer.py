from enum import Enum

import octoprint
import klipper

class PrinterType(Enum):
    OCTO = 0
    KLIPPER = 1

class Printer:
    def __init__(self, id: int, name: str, type: PrinterType, ipaddr: str, port: int, apikey: str, tags: list):
        self.type = type
        
        if self.type == PrinterType.OCTO:
            self.pr = octoprint.PrinterOctoPrint(id, name, ipaddr, port, apikey, tags)
        if self.type == PrinterType.KLIPPER:
            self.pr = klipper.PrinterKlipper(id, name, ipaddr, port, apikey, tags)
        

    type = PrinterType.OCTO
    
    pr = None