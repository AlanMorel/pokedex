document.body.style.backgroundColor = "rgba(" + color[0] + "," + color[1] + "," + color[2] + ", 0.4)";
document.querySelector(".name").style.backgroundColor = "rgba(" + color[0] + "," + color[1] + "," + color[2] + ", 0.8)";

document.querySelector(".attack").style.width = barValues[0] + "%";
document.querySelector(".special-attack").style.width = barValues[1] + "%";
document.querySelector(".defense").style.width = barValues[2] + "%";
document.querySelector(".special-defense").style.width = barValues[3] + "%";

document.querySelector(".attack").style.backgroundColor = barColors[0];
document.querySelector(".special-attack").style.backgroundColor = barColors[1];
document.querySelector(".defense").style.backgroundColor = barColors[2];
document.querySelector(".special-defense").style.backgroundColor = barColors[3];

function playSound() {
    sound.play();
}

function toggle(){
    var moves = document.querySelector(".all-moves");
    var icon = document.querySelector(".expand-collapse");
    document.querySelector(".moves-prompt").style.display = moves.style.display;
    if(moves.style.display == "none"){
        moves.style.display = "block";
        icon.src = "/static/images/collapse.png"
    } else {
        moves.style.display = "none";
        icon.src = "/static/images/expand.png"
    }
}