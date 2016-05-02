function guess(){

    var textfield = document.querySelector('input[name="guess"]');

    if (textfield.value.toLowerCase() === pokemon.toLowerCase()){
        showPokemon();
    } else {
        textfield.value = "";

        var sprite = document.querySelector('.sprite');

        sprite.style.animationPlayState = "running";
        setTimeout(function(){
            sprite.style.animationPlayState = "paused";
         }, 1000);
    }
}

function giveUp(){
    showPokemon();
}

function showPokemon(){
    var sprite = document.querySelector('.sprite');

    sprite.className = "sprite show-pokemon"
    sprite.style.animationPlayState = "running";
    document.querySelector('.description').innerHTML = normalDescription;
    document.querySelector('.id').className = "id show-top";
    document.querySelector('.name').className = "name show-top";
    document.querySelector('.guess-outer').className = "hide";
}