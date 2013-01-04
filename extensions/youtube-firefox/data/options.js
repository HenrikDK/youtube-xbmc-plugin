var xbmc_host = "";
var xbmc_path = "";
var xbmc_autplay = false;
// Saves options to localStorage.
function save_options() {
  var settings = [ document.getElementById("xbmc_youtube_path").value, document.getElementById("xbmc_youtube_host").value, document.getElementById("xbmc_autoplay").checked];
  // Update status to let user know options were saved.
  var status = document.getElementById("status");
  status.innerHTML = "Saved.";
  setTimeout(function() {status.innerHTML = "";}, 1500);

  console.log("Sending postMessage : " + JSON.stringify({ "type": "save_settings", "details": settings}));
  self.postMessage({ "type": "save_settings", "details": settings});
  console.log("Sent postMessage : " + JSON.stringify({ "type": "save_settings", "details": settings}));
}

// Restores select box state to saved value from localStorage.
function restore_options() {
    if (xbmc_host) {
		document.getElementById("xbmc_youtube_host").value = xbmc_host;
    } else {
                document.getElementById("xbmc_youtube_host").value = "username:password@localhost:8080";
    }
    if (xbmc_path) {
		document.getElementById("xbmc_youtube_path").value = xbmc_path;
    } else {
                document.getElementById("xbmc_youtube_path").value = "plugin.video.youtube";
    }
    if (xbmc_autoplay) {
		document.getElementById("xbmc_autoplay").checked = xbmc_autoplay;
    } else {
                document.getElementById("xbmc_autoplay").checked = false;
    }
}

self.on("message", function(message) {
    console.log("GOT DATA: " + JSON.stringify(message));
    xbmc_path = message[0];
    xbmc_host = message[2];
    xbmc_autoplay = message[3];
    restore_options();
});

self.postMessage({ "type": "load_settings"});
document.getElementById("save_button").onclick = save_options;
