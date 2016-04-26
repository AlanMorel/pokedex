function showHint(str) {
    if (str.length < 1) {
        document.querySelector(".tooltiptext").style.visibility = "hidden";
        return;
    } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200 && xmlhttp.responseText.length > 0) {
                document.querySelector(".tooltiptext").style.visibility = "visible";
                document.querySelector(".tooltiptext").innerHTML = "Suggestions: " + xmlhttp.responseText;
            } else {
                document.querySelector(".tooltiptext").style.visibility = "hidden";
                return;
            }
        };
        xmlhttp.open("GET", "/hint?pokemon=" + str, true);
        xmlhttp.send();
    }
}
