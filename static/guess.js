function guess(){
    var textfield = document.querySelector('input[name="guess"]');

    if (textfield.value.toLowerCase() === pokemon.toLowerCase()){
        document.querySelector('.sprite').className = "sprite show-pokemon"
        document.querySelector('.id').className = "id show-top";
        document.querySelector('.name').className = "name show-top";
        document.querySelector('.guess-outer').className = "hide";
    } else {
        //document.querySelector('.sprite').classList.remove("shake");
        document.querySelector('.sprite').classList.add("shake");

       // document.querySelector('.sprite').style.animation = "";
        //document.querySelector('.sprite').style.animation = "shake 0.5s cubic-bezier(.36,.07,.19,.97) both";

        //console.log(document.querySelector('.sprite').style);
        document.querySelector('.sprite').style.animationPlayState = "running";

        setTimeout(function(){
            document.querySelector('.sprite').style.animationPlayState = "paused";
         }, 1000);

        textfield.value = "";
    }
}

function giveUp(){
    alert("The pokemon is " + pokemon);
}