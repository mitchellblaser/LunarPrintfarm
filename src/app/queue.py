from logging import setLoggerClass
from app import serverapi

class printQueueObject:
    def __init__(self):
        self.name = ""
        self.estimate_mins = -1
        self.estimate_str = ""
        return

# calculate_print_time(string filepath)
# Returns slicer estimated print time in seconds.
def calculate_print_time(filepath):
    file = open(filepath, "r")
    for line in file:
        if line[:6] == ";TIME:":
            return int(line[6:])

# add_file_to_queue(string filepath)
# With a provided filepath, and requirements provided from the GUI, and the slicer time estimate taken into consideration,
# this function will assign a gcode file to a printer to print as efficiently as possible.
def add_file_to_queue(filepath):
    # Calculate the existing stack's time estimates
    server_times = {}
    for server in serverapi.servers:
        server_times[server] = 0
        for file in serverapi.queue[server]:
            if file == serverapi.queue[server][0]:
                # Get current print elapsed time and subtract from slicer estimate
                current_percentage = serverapi.info()[server]['result']['status']['display_status']['progress']
                server_times[server] = server_times[server] + calculate_print_time(file)*current_percentage
            else:
                # Get times for the rest of the files in the queue
                server_times[server] = server_times[server] + calculate_print_time(file)
        
    last_time = -1
    selected_candidate = ""
    for server in serverapi.servers:
        if last_time == -1:
            last_time = server_times[server]
            selected_candidate = server
        else:
            if last_time > server_times[server]:
                last_time = server_times[server]
                selected_candidate = server

    # If queue is empty, send straight away
    if serverapi.queue[selected_candidate] == []:
        serverapi.queue[selected_candidate].append(filepath)
        serverapi.print_file(serverapi.queue[selected_candidate][0], selected_candidate)
    else:
        serverapi.queue[selected_candidate].append(filepath)
    return

# on_print_completion(string server)
# Call this function once the print has finished to remove it from the stack and start the next print
def on_print_completion(server):
    serverapi.queue[server].pop(0) # Pop the filepath from the stack
    ## Upload the next file in the queue for the printer
    if serverapi.queue[server] != []:
        # If there is another file in the queue
        serverapi.print_file(serverapi.queue[server][0], server)
    return