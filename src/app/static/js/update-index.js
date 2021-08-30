function initialUpdate() {
    fetch("/api/servers").then(r=> r.json().then(j=> servers = j['servers']));
}

function doUpdate() {
    fetch("/api/info").then(r=> r.json().then(j=> info = j));

    for (var i=0; i<servers.length; i++) {

        var status = info[servers[i]]['result']['status'];

        document.getElementById(servers[i] + "_Percentage").innerText = "Progress: " + status['display_status']['progress'].toFixed(2) + "%";
        document.getElementById(servers[i] + "_FileName").innerText = "Printing: " + status['print_stats']['filename'];

    }

}

initialUpdate();
var periodicUpdate = setInterval(doUpdate, 5000);