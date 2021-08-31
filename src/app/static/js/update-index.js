let info;
function initialUpdate() {
    fetch("/api/servers").then(r=> r.json().then(j=> servers = j['servers']));
}

function doUpdate() {
    var printer_count = servers.length;
    var printing_count = 0;

    fetch("/api/info").then(r=> r.json().then(j=> info = j));

    for (var i=0; i<servers.length; i++) {

        if (info != undefined) {
            var status = info[servers[i]]['result']['status'];
    
            if (status['print_stats']['filename'] != "") {
                printing_count++;
                document.getElementById(servers[i] + "_Percentage").innerText = "Progress: " + status['display_status']['progress'].toFixed(2) + "%";
                document.getElementById(servers[i] + "_FileName").innerText = "Printing: " + status['print_stats']['filename'];
            } else {
                document.getElementById(servers[i] + "_Percentage").innerText = "Progress: None";
                document.getElementById(servers[i] + "_FileName").innerText = "Printing: None";
            }
        }
    }
    
    if (info != undefined) {
        document.getElementById("utilization_title").innerText = "Printer Usage (" + printing_count + "/" + printer_count + " Busy)";
        document.getElementById("utilization_bar").value = printing_count;
        document.getElementById("utilization_bar").max = printer_count;
    }
}

initialUpdate();
var periodicUpdate = setInterval(doUpdate, 5000);