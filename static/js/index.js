function showHint(str) {
    if (str.length < 1) {
        document.querySelector(".tooltiptext").style.visibility = "hidden";
    } else {
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState == 4 && request.status == 200 && request.responseText.length > 0) {
                document.querySelector(".tooltiptext").style.visibility = "visible";
                document.querySelector(".tooltiptext").innerHTML = "Suggestions: " + request.responseText;
            } else {
                document.querySelector(".tooltiptext").style.visibility = "hidden";
                return;
            }
        };
        request.open("GET", "/api?q=" + str, true);
        request.send();
    }
}
