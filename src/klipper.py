import requests
import json

from states import PrinterState

class PrinterKlipper:
    def __init__(self, id: int, name: str, ipaddr: str, port: int, apikey: str, tags: list):
        self.id = id
        self.name = name
        self.ipaddr = ipaddr
        self.port = port
        self.apikey = apikey
        self.tags = tags
    
    id = 0
    name = "Unconfigured"
    ipaddr = "127.0.0.1"
    port = 5000
    apikey = ""
    tags = []
    
    def GetVersion(self):
        """Returns version string from printer.

        Returns:
            str: Plaintext Version String
        """
        return "Klipper " + requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/printer/info").json()["result"]["software_version"]
    
    
    def GetStatus(self):
        """Returns state of printer.

        Returns:
            states.PrinterState: Current state of printer.
        """
        if requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/printer").json()["state"]["flags"]["printing"] == True:
            return PrinterState.PRINTING
        if requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/printer/info").json()["result"]["state"] == ready:
            return PrinterState.READY
        return PrinterState.ERROR
    
    def GetStatusFriendly(self):
        if requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/printer").json()["state"]["flags"]["printing"] == True:
            return "Printing"
        if requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/printer/info").json()["result"]["state"] == ready:
            return "Ready"
        return "Error!"
    
    def UploadFile(self, filepath: str, select = True, print = False):
        """Opens file from local storage and uploads to target printer.

        Args:
            filepath (str): Path to sliced gcode file.
        """
        return
    
    
    def GetPrintCompletion(self):
        return 0
    
    def CancelPrint(self):
        return