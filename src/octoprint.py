import requests
import json

from states import PrinterState

class PrinterOctoPrint:
    def __init__(self, id: int, name: str, ipaddr: str, port: int, apikey: str):
        self.id = id
        self.name = name
        self.ipaddr = ipaddr
        self.port = port
        self.apikey = apikey
    
    id = 0
    name = "Unconfigured"
    ipaddr = "127.0.0.1"
    port = 5000
    apikey = ""
    
    def GetVersion(self):
        """Returns version string from printer.

        Returns:
            str: Plaintext Version String
        """
        return requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/version", headers={"X-Api-Key": self.apikey}).json()['text']
    
    
    def GetStatus(self):
        """Returns state of printer.

        Returns:
            states.PrinterState: Current state of printer.
        """
        match requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/job", headers={"X-Api-Key": self.apikey}).json()["state"]:
            case "Operational":
                return PrinterState.READY
            case "Printing":
                return PrinterState.PRINTING
        
        return PrinterState.ERROR
    
    
    def GetStatusFriendly(self):
        match requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/job", headers={"X-Api-Key": self.apikey}).json()["state"]:
            case "Operational":
                return "Ready"
            case "Printing":
                return "Printing"
        
        return "Error!"
    
    def UploadFile(self, filepath: str, select = True, print = False):
        """Opens file from local storage and uploads to target printer.

        Args:
            filepath (str): Path to sliced gcode file.
        """

        fle={'file': open(filepath, 'rb'), 'filename': 'max.gcode'}
        url='http://' + self.ipaddr + ":" + str(self.port) + '/api/files/{}'.format('local')
        payload={'select': str(select).lower(),'print': str(print).lower() }
        header={'X-Api-Key': self.apikey }
        response = requests.post(url, files=fle,data=payload,headers=header)
        return
    
    
    def GetPrintCompletion(self):
        response = requests.get("http://" + self.ipaddr + ":" + str(self.port) + "/api/job", headers={"X-Api-Key": self.apikey}).json()["progress"]["completion"]
        
        if self.GetStatus() == PrinterState.PRINTING:
            return response
        return 0
    
    def CancelPrint(self):
        requests.post("http://" + self.ipaddr + ":" + str(self.port) + "/api/job", json={"command": "cancel"}, headers={"X-Api-Key": self.apikey})
        return