function showSuggestions(str) {
    var suggestions = document.querySelector(".suggestions");

    suggestions.style.visibility = "hidden";

    if (str.length < 1) {
        return;
    }

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200 && request.responseText.length > 0) {
            suggestions.style.visibility = "visible";
            suggestions.innerHTML = "Suggestions: " + request.responseText;
        }
    };

    request.open("GET", "/api?q=" + str, true);
    request.send();
}