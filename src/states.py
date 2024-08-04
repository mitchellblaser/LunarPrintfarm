from enum import Enum

class PrinterState(Enum):
    READY = 0
    PRINTING = 1
    ERROR = 2