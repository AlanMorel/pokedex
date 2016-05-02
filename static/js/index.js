function showSuggestions(str) {
    var suggestions = document.querySelector(".suggestions");

    if (!str || str.length < 1) {
        suggestions.style.visibility = "hidden";
        return;
    }

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200 && request.responseText.length > 0) {
            suggestions.innerHTML = request.responseText;
            suggestions.style.visibility = "visible";
        } else {
            suggestions.style.visibility = "hidden";
        }
    };

    request.open("GET", "/api?q=" + str, true);
    request.send();
    suggestions.style.visibility = "visible";
}