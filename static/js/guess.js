function guess(){

    var textfield = document.querySelector('input[name="guess"]');
    var sprite = document.querySelector('.sprite');

    if (textfield.value.toLowerCase() === pokemon.toLowerCase()){
        sprite.className = "sprite show-pokemon"
        sprite.style.animationPlayState = "running";
        document.querySelector('.id').className = "id show-top";
        document.querySelector('.name').className = "name show-top";
        document.querySelector('.guess-outer').className = "hide";
    } else {
        textfield.value = "";
        sprite.style.animationPlayState = "running";
        setTimeout(function(){
            sprite.style.animationPlayState = "paused";
         }, 1000);
    }
}

function giveUp(){
    alert("The pokemon is " + pokemon);
}